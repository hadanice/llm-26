# transformer.py

import math
import time
import random
from types import SimpleNamespace
from typing import List

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch import optim
import matplotlib.pyplot as plt

from utils import *


# -----------------------------------------------------------------------------
# Reused MLP (kept exactly as provided in the template).
# Pure nn.Linear + GELU -> fully compliant with the "no off-the-shelf
# self-attention" rule.  We will plug this into our hand-written TransformerLayer
# via a lightweight config object (SimpleNamespace(n_embd=d_model)).
# -----------------------------------------------------------------------------
class MLP(nn.Module):

    def __init__(self, config):
        super().__init__()
        self.c_fc    = nn.Linear(config.n_embd, 4 * config.n_embd)
        self.gelu    = nn.GELU(approximate='tanh')
        self.c_proj  = nn.Linear(4 * config.n_embd, config.n_embd)
        self.c_proj.NANOGPT_SCALE_INIT = 1

    def forward(self, x):
        x = self.c_fc(x)
        x = self.gelu(x)
        x = self.c_proj(x)
        return x


# Wraps an example: stores the raw input string (input), the indexed form of the string (input_indexed),
# a tensorized version of that (input_tensor), the raw outputs (output; a numpy array) and a tensorized version
# of it (output_tensor).
# Per the task definition, the outputs are 0, 1, or 2 based on whether the character occurs 0, 1, or 2 or more
# times previously in the input sequence (not counting the current occurrence).
class LetterCountingExample(object):
    def __init__(self, input: str, output: np.array, vocab_index: Indexer):
        self.input = input
        self.input_indexed = np.array([vocab_index.index_of(ci) for ci in input])
        self.input_tensor = torch.LongTensor(self.input_indexed)
        self.output = output
        self.output_tensor = torch.LongTensor(self.output)


# Should contain your overall Transformer implementation. You will want to use Transformer layer to implement
# a single layer of the Transformer; this Module will take the raw words as input and do all of the steps necessary
# to return distributions over the labels (0, 1, or 2).
class Transformer(nn.Module):
    def __init__(self, vocab_size, num_positions, d_model, d_internal, num_classes, num_layers, causal: bool = True):
        """
        :param vocab_size: vocabulary size of the embedding layer
        :param num_positions: max sequence length that will be fed to the model; should be 20
        :param d_model: see TransformerLayer
        :param d_internal: see TransformerLayer
        :param num_classes: number of classes predicted at the output layer; should be 3
        :param num_layers: number of TransformerLayers to use; can be whatever you want
        :param causal: if True, each position only attends to previous positions (BEFORE task).
                        If False, each position attends to all positions (BEFOREAFTER task).
        """
        super().__init__()
        self.vocab_size = vocab_size
        self.num_positions = num_positions
        self.d_model = d_model
        self.num_classes = num_classes
        self.causal = causal

        self.tok_emb = nn.Embedding(vocab_size, d_model)
        self.pos_enc = PositionalEncoding(d_model, num_positions=num_positions, batched=False)

        self.layers = nn.ModuleList([
            TransformerLayer(d_model, d_internal, causal=causal)
            for _ in range(num_layers)
        ])

        self.ln_f = nn.LayerNorm(d_model)
        self.head = nn.Linear(d_model, num_classes)

    def forward(self, indices):
        """

        :param indices: LongTensor of shape [seq_len] (non-batched, required by decode())
                        OR [batch, seq_len] (used internally for faster training)
        :return: A tuple of the softmax log probabilities and a list of attention maps.
                Shapes follow the input: [seq_len, num_classes] / [seq_len, seq_len] for 1D input,
                or [batch, seq_len, num_classes] / [batch, seq_len, seq_len] for 2D input.
        """
        if indices.dim() not in (1, 2):
            raise ValueError("forward() expects a 1D or 2D LongTensor; got shape %s" % str(indices.shape))

        x = self.tok_emb(indices)
        x = self.pos_enc(x)

        attn_maps = []
        for layer in self.layers:
            x, attn = layer(x)
            attn_maps.append(attn)

        x = self.ln_f(x)
        logits = self.head(x)
        log_probs = torch.log_softmax(logits, dim=-1)
        return log_probs, attn_maps


# Your implementation of the Transformer layer goes here. It should take vectors and return the same number of vectors
# of the same length, applying self-attention, the feedforward layer, etc.
class TransformerLayer(nn.Module):
    def __init__(self, d_model, d_internal, causal: bool = True):
        """
        :param d_model: The dimension of the inputs and outputs of the layer (note that the inputs and outputs
        have to be the same size for the residual connection to work)
        :param d_internal: The "internal" dimension used in the self-attention computation. Your keys and queries
        should both be of this length.
        :param causal: whether to apply a causal (upper-triangular) attention mask.
        """
        super().__init__()
        self.d_model = d_model
        self.d_internal = d_internal
        self.causal = causal

        self.W_q = nn.Linear(d_model, d_internal)
        self.W_k = nn.Linear(d_model, d_internal)
        self.W_v = nn.Linear(d_model, d_internal)
        self.W_o = nn.Linear(d_internal, d_model)

        self.ln_1 = nn.LayerNorm(d_model)
        self.ln_2 = nn.LayerNorm(d_model)

        self.mlp = MLP(SimpleNamespace(n_embd=d_model))

    def forward(self, input_vecs):
        """
        :param input_vecs: tensor of shape [seq len, d_model] OR [batch, seq len, d_model]
        :return: a tuple of two elements:
            - output tensor of the same shape as input_vecs
            - attention map: shape [seq len, seq len] if input is 2D, or [batch, seq len, seq len] if 3D
        """
        x = input_vecs
        T = x.shape[-2]

        h = self.ln_1(x)
        q = self.W_q(h)
        k = self.W_k(h)
        v = self.W_v(h)

        scores = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(self.d_internal)

        if self.causal:
            mask = torch.triu(torch.ones(T, T, device=scores.device), diagonal=1).bool()
            scores = scores.masked_fill(mask, float('-inf'))

        attn = torch.softmax(scores, dim=-1)

        ctx = torch.matmul(attn, v)
        attn_out = self.W_o(ctx)

        x = x + attn_out
        x = x + self.mlp(self.ln_2(x))

        return x, attn


# Implementation of positional encoding that you can use in your network
class PositionalEncoding(nn.Module):
    def __init__(self, d_model: int, num_positions: int=20, batched=False):
        """
        :param d_model: dimensionality of the embedding layer to your model; since the position encodings are being
        added to character encodings, these need to match (and will match the dimension of the subsequent Transformer
        layer inputs/outputs)
        :param num_positions: the number of positions that need to be encoded; the maximum sequence length this
        module will see
        :param batched: True if you are using batching, False otherwise
        """
        super().__init__()
        # Dict size
        self.emb = nn.Embedding(num_positions, d_model)
        self.batched = batched

    def forward(self, x):
        """
        :param x: If using batching, should be [batch size, seq len, embedding dim]. Otherwise, [seq len, embedding dim]
        :return: a tensor of the same size with positional embeddings added in
        """
        # Second-to-last dimension will always be sequence length
        input_size = x.shape[-2]
        indices_to_embed = torch.tensor(np.asarray(range(0, input_size))).type(torch.LongTensor)
        if self.batched:
            # Use unsqueeze to form a [1, seq len, embedding dim] tensor -- broadcasting will ensure that this
            # gets added correctly across the batch
            emb_unsq = self.emb(indices_to_embed).unsqueeze(0)
            return x + emb_unsq
        else:
            return x + self.emb(indices_to_embed)


# This is a skeleton for train_classifier: you can implement this however you want
def train_classifier(args, train, dev):
    import os

    causal = (args.task == "BEFORE")
    os.makedirs("plots", exist_ok=True)

    torch.manual_seed(0)
    np.random.seed(0)
    random.seed(0)

    vocab_size = 27
    num_positions = 20
    d_model = 64
    d_internal = 64
    num_classes = 3
    num_layers = 2

    model = Transformer(
        vocab_size=vocab_size,
        num_positions=num_positions,
        d_model=d_model,
        d_internal=d_internal,
        num_classes=num_classes,
        num_layers=num_layers,
        causal=causal,
    )
    print("Model architecture:")
    print(model)
    print("Task: %s  |  causal=%s" % (args.task, causal))

    optimizer = optim.Adam(model.parameters(), lr=1e-3)
    loss_fcn = nn.NLLLoss()

    train_inputs = torch.stack([ex.input_tensor for ex in train], dim=0)
    train_labels = torch.stack([ex.output_tensor for ex in train], dim=0)

    batch_size = 64
    num_epochs = 10
    for t in range(num_epochs):
        model.train()
        epoch_start = time.time()
        loss_this_epoch = 0.0
        num_batches = 0

        torch.manual_seed(t)
        perm = torch.randperm(len(train))

        for start in range(0, len(train), batch_size):
            idx = perm[start:start + batch_size]
            x_batch = train_inputs[idx]
            y_batch = train_labels[idx]

            log_probs, _ = model.forward(x_batch)
            B, T, C = log_probs.shape
            loss = loss_fcn(log_probs.reshape(B * T, C), y_batch.reshape(B * T))

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            loss_this_epoch += loss.item()
            num_batches += 1

        avg_loss = loss_this_epoch / max(num_batches, 1)

        model.eval()
        with torch.no_grad():
            num_correct = 0
            num_total = 0
            dev_subset = dev[:200]
            for ex in dev_subset:
                log_probs, _ = model.forward(ex.input_tensor)
                preds = log_probs.argmax(dim=-1).numpy()
                num_correct += int((preds == ex.output).sum())
                num_total += len(preds)
            dev_acc = num_correct / num_total

        print("Epoch %2d | train_loss=%.4f | dev_acc(200 exs)=%.4f | time=%.1fs"
              % (t + 1, avg_loss, dev_acc, time.time() - epoch_start), flush=True)

    model.eval()
    return model


####################################
# DO NOT MODIFY IN YOUR SUBMISSION #
####################################
def decode(model: Transformer, dev_examples: List[LetterCountingExample], do_print=False, do_plot_attn=False):
    """
    Decodes the given dataset, does plotting and printing of examples, and prints the final accuracy.
    :param model: your Transformer that returns log probabilities at each position in the input
    :param dev_examples: the list of LetterCountingExample
    :param do_print: True if you want to print the input/gold/predictions for the examples, false otherwise
    :param do_plot_attn: True if you want to write out plots for each example, false otherwise
    :return:
    """
    num_correct = 0
    num_total = 0
    if len(dev_examples) > 100:
        print("Decoding on a large number of examples (%i); not printing or plotting" % len(dev_examples))
        do_print = False
        do_plot_attn = False
    for i in range(0, len(dev_examples)):
        ex = dev_examples[i]
        (log_probs, attn_maps) = model.forward(ex.input_tensor)
        predictions = np.argmax(log_probs.detach().numpy(), axis=1)
        if do_print:
            print("INPUT %i: %s" % (i, ex.input))
            print("GOLD %i: %s" % (i, repr(ex.output.astype(dtype=int))))
            print("PRED %i: %s" % (i, repr(predictions)))
        if do_plot_attn:
            for j in range(0, len(attn_maps)):
                attn_map = attn_maps[j]
                fig, ax = plt.subplots()
                im = ax.imshow(attn_map.detach().numpy(), cmap='hot', interpolation='nearest')
                ax.set_xticks(np.arange(len(ex.input)), labels=ex.input)
                ax.set_yticks(np.arange(len(ex.input)), labels=ex.input)
                ax.xaxis.tick_top()
                # plt.show()
                plt.savefig("plots/%i_attns%i.png" % (i, j))
        acc = sum([predictions[i] == ex.output[i] for i in range(0, len(predictions))])
        num_correct += acc
        num_total += len(predictions)
    print("Accuracy: %i / %i = %f" % (num_correct, num_total, float(num_correct) / num_total))
