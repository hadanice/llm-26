<!-- page 0 -->
<section class="title">
  <div class="title-main">Lecture 06 – (Pretrained) LLMs</div>
  <div class="title-sub">CS40008.01: NLP and LLMs</div>
  <div class="title-meta">
    <div>Baojian Zhou</div>
    <div>School of Data Science</div>
    <div>Fudan University</div>
    <div>04/16/2026</div>
  </div>
  <div style="margin-top:60px; font-size:22px; opacity:0.65;">Some slides are adopted from Jacob Devlin and Anoop Sarkar</div>
</section>

---

<!-- page 1 -->
<section class="ppt">
  <div class="ppt-title">Outline</div>
  <div class="ppt-line"></div>
  <ul class="outline-bullets med">
    <li class="active">History of pre-training</li>
    <li class="muted">Transformers as pretrained LMs</li>
    <li class="muted">Autoregressive generation</li>
    <li class="muted">Pretrained Decoders (GPT series)</li>
    <li class="muted">Datasets, Scaling laws, KV Cache, LoRA</li>
    <li class="muted">Pretrained Encoders (BERT series)</li>
  </ul>
</section>

---

<!-- page 2 -->
<section class="ppt">
  <div class="ppt-title">Brief history of pre-training</div>
  <div class="ppt-line"></div>
  <div class="twocol" style="--left:58%; margin-top:6px;">
    <div>
      <p style="font-size:36px; font-weight:800; color:var(--fudan-blue); margin:0 0 10px;">1960 to 2015</p>
      <ul style="font-size:30px; line-height:1.45; font-weight:600;">
        <li><b>Singular Value Decomposition (1960s)</b>
          <ul style="font-size:26px; margin-top:6px; line-height:1.4;">
            <li>Take matrix of word co-occurrence counts</li>
            <li>Use SVD to map truncated to initial singular values</li>
            <li>Use truncated vectors as word embeddings</li>
          </ul>
        </li>
        <li style="margin-top:14px;"><b>word2vec / GloVe (2010s)</b>
          <ul style="font-size:26px; margin-top:6px; line-height:1.4;">
            <li>Skip-gram: target word predicts each context word</li>
            <li>CBOW: context words predict target word</li>
            <li>Learning from co-occurrence counts + regression</li>
          </ul>
        </li>
      </ul>
    </div>
    <div style="border:2px solid rgba(0,0,0,0.10); border-radius:14px; padding:20px; background:#f6f7f9; text-align:center; margin-top:30px;">
      <div style="font-size:22px; font-weight:700; color:var(--fudan-blue); margin-bottom:16px;">word2vec example</div>
      <div style="font-size:32px; font-weight:900; color:var(--fudan-blue);">king</div>
      <div style="font-size:18px; opacity:0.75; margin:4px 0 12px;">[-0.5, -0.9, 1.3, …]</div>
      <div style="font-size:32px; font-weight:900; color:var(--fudan-blue);">queen</div>
      <div style="font-size:18px; opacity:0.75; margin:4px 0 16px;">[-0.7, -0.2, 1.4, …]</div>
      <div style="font-size:20px; font-weight:600; line-height:1.4;">
        <div>the <b>king</b> wore a crown</div>
        <div>the <b>queen</b> wore a crown</div>
      </div>
      <div style="margin-top:12px; font-size:18px; opacity:0.7;">Inner product → similar context<br>→ similar embedding</div>
    </div>
  </div>
</section>

---

<!-- page 3 -->
<section class="ppt">
  <div class="ppt-title">Contextual representations</div>
  <div class="ppt-line"></div>

  <!-- upper: text content -->
  <div style="font-size:30px; line-height:1.5; font-weight:600; margin-top:8px;">
    <p><b>Problem:</b> Word embeddings are applied in a <span style="color:red; font-weight:800;">context free</span> manner</p>
    <p class="fragment" style="margin-top:8px;"><b>Solution:</b> Train <span style="color:var(--fudan-blue); font-weight:800;">contextual representations</span> on text corpus</p>
    <div class="fragment" style="margin-top:10px; font-size:26px; background:rgba(0,0,0,0.05); padding:12px 16px; border-radius:10px; display:inline-block;">
      open a <b>bank</b> account → [0.9, −0.2, 1.6, …] &nbsp;|&nbsp; on the river <b>bank</b> → [−1.9, −0.4, 0.1, …]
    </div>
    <p class="fragment" style="margin-top:14px;"><b>Semi-Supervised Sequence Learning</b>, Google, 2015
      <a href="https://arxiv.org/abs/1511.01432" style="font-size:20px; font-weight:400; margin-left:8px;" target="_blank">arxiv:1511.01432</a>
    </p>
    <ul class="fragment" style="font-size:26px; margin-top:8px; line-height:1.45;">
      <li>"…reads the input sequence into a vector and predicts the input sequence again" (sequence autoencoder)</li>
      <li style="margin-top:6px;">Can be used as a <b>pretraining</b> step for a later supervised sequence learning algorithm</li>
    </ul>
  </div>

  <!-- lower: model architecture image -->
  <div class="fragment" style="margin-top:16px; text-align:center;">
    <img src="media/image3.png" style="height:200px; border-radius:10px; object-fit:contain;">
  </div>
</section>

---

<!-- page 4 -->
<section class="ppt">
  <div class="ppt-title">Contextual representations: ELMo</div>
  <div class="ppt-line"></div>
  <div style="display:flex; gap:32px; align-items:flex-start; margin-top:10px;">
    <!-- left 40% -->
    <div style="flex:0 0 40%; font-size:28px; line-height:1.5; font-weight:600;">
      <p><b>ELMo: Deep Contextual Word Embeddings</b></p>
      <p style="font-size:22px; margin-top:6px;">AI2 & University of Washington, 2017</p>
      <p style="margin-top:12px;"><a href="https://arxiv.org/pdf/1802.05365" target="_blank" style="font-size:20px;">arxiv:1802.05365</a></p>
      <p style="margin-top:6px;"><a href="https://allenai.org/allennlp/software/elmo" target="_blank" style="font-size:20px;">allenai.org/allennlp/software/elmo</a></p>
    </div>
    <!-- right 60% -->
    <div style="flex:0 0 60%;">
      <p style="font-size:28px; font-weight:600; line-height:1.5;">Word vectors are learned functions of the internal states of a <b>deep bidirectional language model (biLM)</b>, which is pretrained on a large text corpus.</p>
      <img src="media/image6.png" style="width:100%; border-radius:10px; margin-top:14px;">
    </div>
  </div>
</section>

---

<!-- page 5 -->
<section class="ppt">
  <div class="ppt-title">Outline</div>
  <div class="ppt-line"></div>
  <ul class="outline-bullets med">
    <li class="muted">History of pre-training</li>
    <li class="active">Transformers as pretrained LMs</li>
    <li class="muted">Autoregressive generation</li>
    <li class="muted">Pretrained Decoders (GPT series)</li>
    <li class="muted">Datasets, Scaling laws, KV Cache, LoRA</li>
    <li class="muted">Pretrained Encoders (BERT series)</li>
  </ul>
</section>

---

<!-- page 6 -->
<section class="ppt">
  <div class="ppt-title">Transformers as LMs</div>
  <div class="ppt-line"></div>
  <div style="font-size:30px; line-height:1.5; font-weight:600; margin-top:8px;">
    <p>Given a training corpus of plain text we'll train the model <b>autoregressively</b> to predict the next token in a sequence, using cross-entropy loss.</p>
    <p class="fragment" style="margin-top:10px;"><b>Teacher forcing:</b> We always give the model the correct history sequence to predict the next word (rather than feeding the model its best guess from the previous time step).</p>
  </div>
  <div class="fragment" style="margin-top:16px; text-align:center;">
    <p style="font-size:26px; font-weight:650; margin-bottom:10px;">Training a transformer as a language model</p>
    <img src="media/image7.png" style="width:62%; border-radius:10px;">
  </div>
</section>

---

<!-- page 7 -->
<section class="ppt">
  <div class="ppt-title">Where we were: pretrained word embeddings</div>
  <div class="ppt-line"></div>
  <div class="twocol" style="--left:55%; margin-top:10px;">
    <div style="font-size:30px; line-height:1.5; font-weight:600;">
      <p><b>Before 2017</b></p>
      <ul style="font-size:28px; margin-top:10px;">
        <li>Start with pretrained word embeddings (no context!)</li>
        <li>Learn how to incorporate context in an LSTM or Transformer while training on the task.</li>
      </ul>
      <p style="margin-top:18px; font-size:28px;"><b>Some issues:</b></p>
      <ul style="font-size:26px; margin-top:8px;">
        <li>The training data we have for our downstream task must be sufficient to teach all contextual aspects of language</li>
        <li>Most of the parameters in our network are <span style="color:red;">randomly initialized!</span></li>
      </ul>
    </div>
    <div class="fig">
      <img src="media/image8.png" style="width:100%; border-radius:10px;">
    </div>
  </div>
</section>

---

<!-- page 8 -->
<section class="ppt">
  <div class="ppt-title">Where we were: Modern NLP</div>
  <div class="ppt-line"></div>
  <div class="twocol" style="--left:55%; margin-top:10px;">
    <div style="font-size:30px; line-height:1.5; font-weight:600;">
      <p>All (or almost all) parameters in NLP networks are initialized via <b>pretraining</b></p>
      <ul style="font-size:28px; margin-top:10px;">
        <li class="fragment">Pretraining methods hide parts of the input from the model, and train the model to reconstruct those parts.</li>
        <li class="fragment" style="margin-top:10px;">This has been <span style="color:var(--fudan-blue);">exceptionally effective</span></li>
        <li class="fragment" style="margin-top:10px;">Representations of language → <b>parameter initializations</b> for strong NLP models</li>
        <li class="fragment" style="margin-top:10px;">Probability distributions over language that we can <b>sample from</b></li>
      </ul>
    </div>
    <div class="fig">
      <img src="media/image9.png" style="width:100%; border-radius:10px;">
    </div>
  </div>
</section>

---

<!-- page 9 -->
<section class="ppt">
  <div class="ppt-title">The Transformer Encoder-Decoder</div>
  <div class="ppt-line"></div>
  <div class="twocol" style="--left:50%; margin-top:10px;">
    <div class="fig">
      <div class="cap">Looking back at the whole model, zooming in on an <b>Encoder block</b></div>
      <img src="media/image10.png" style="width:90%; border-radius:10px;">
    </div>
    <div class="fig">
      <div class="cap">Looking back at the whole model, zooming in on a <b>Decoder block</b></div>
      <img src="media/image11.png" style="width:110%; border-radius:10px;">
    </div>
  </div>
</section>

---

<!-- page 10 -->
<section class="ppt">
  <div class="ppt-title">The Pretraining / Finetuning Paradigm</div>
  <div class="ppt-line"></div>
  <p style="font-size:30px; font-weight:650; margin:10px 0 18px;">Pretraining improves NLP tasks by serving as parameter initialization</p>
  <img src="media/image12.png" style="width:88%; border-radius:10px; display:block; margin:0 auto;">
  <div style="display:flex; gap:60px; margin-top:18px; font-size:28px; font-weight:700;">
    <div><b>Step 1:</b> Pretrain (on language modeling) — lots of text; learn general things!</div>
    <div><b>Step 2:</b> Finetune (on your task) — not many labels; adapt to the task!</div>
  </div>
</section>

---

<!-- page 11 -->
<section class="ppt">
  <div class="ppt-title">Why it works: SGD and pretrain/finetune</div>
  <div class="ppt-line"></div>
  <div style="display:flex; gap:32px; align-items:flex-start; margin-top:10px;">
    <!-- left: SGD explanation -->
    <div style="flex:0 0 52%; font-size:26px; line-height:1.5; font-weight:600;">
      <p>Consider, provides parameters \(\hat\theta_{\text{PT}}\) by approximating:</p>
      $$\min_\theta \mathcal{L}_{\text{PT}}(\theta)$$
      <p class="fragment">(The pretraining loss.)</p>
      <p class="fragment" style="margin-top:10px;">Then, finetuning approximates \(\min_\theta \mathcal{L}_{\text{FT}}(\theta)\), starting at \(\hat\theta_{\text{PT}}\).</p>
      <p class="fragment" style="margin-top:10px;">SGD sticks (relatively) close to \(\hat\theta_{\text{PT}}\) during finetuning, so local minima nearby tend to <b>generalize well</b>!</p>
    </div>
    <!-- right: three pretraining types -->
    <div style="flex:0 0 44%;">
      <p style="font-size:22px; font-weight:700; color:var(--fudan-blue); margin:0 0 12px;">Three pretraining architectures</p>
      <div style="display:flex; flex-direction:column; gap:14px;">
        <div style="border:2px solid var(--fudan-blue); border-radius:12px; padding:14px 16px; text-align:center;">
          <div style="font-size:28px; font-weight:900; color:var(--fudan-blue);">Decoders</div>
          <div style="font-size:20px; margin-top:4px; font-weight:600;">GPT series</div>
        </div>
        <div style="border:2px solid var(--fudan-blue); border-radius:12px; padding:14px 16px; text-align:center;">
          <div style="font-size:28px; font-weight:900; color:var(--fudan-blue);">Encoders</div>
          <div style="font-size:20px; margin-top:4px; font-weight:600;">BERT</div>
        </div>
        <div style="border:2px solid var(--fudan-blue); border-radius:12px; padding:14px 16px; text-align:center;">
          <div style="font-size:28px; font-weight:900; color:var(--fudan-blue);">Encoder-Decoders</div>
          <div style="font-size:20px; margin-top:4px; font-weight:600;">T5</div>
        </div>
      </div>
    </div>
  </div>
</section>

---

<!-- page 12 -->
<section class="ppt">
  <div class="ppt-title">Outline</div>
  <div class="ppt-line"></div>
  <ul class="outline-bullets med">
    <li class="muted">History of pre-training</li>
    <li class="muted">Transformers as pretrained LMs</li>
    <li class="active">Autoregressive generation</li>
    <li class="muted">Pretrained Decoders (GPT series)</li>
    <li class="muted">Datasets, Scaling laws, KV Cache, LoRA</li>
    <li class="muted">Pretrained Encoders (BERT series)</li>
  </ul>
</section>

---

<!-- page 13 -->
<section class="ppt">
  <div class="ppt-title">LMs generation: Autoregressive generation</div>
  <div class="ppt-line"></div>
  <div style="font-size:30px; line-height:1.5; font-weight:600; margin-top:10px;">
    <p><b>Autoregressive generation</b> (or <b>causal LM generation</b>):</p>
    <ol style="margin-top:14px;">
      <li class="fragment">Sample a word from the softmax distribution using the beginning-of-sentence marker <code>&lt;s&gt;</code> as the first input.</li>
      <li class="fragment" style="margin-top:10px;">Use the word embedding for that first word as the input at the next time step, then sample the next word in the same fashion.</li>
      <li class="fragment" style="margin-top:10px;">Continue generating until the end-of-sentence marker <code>&lt;/s&gt;</code> is sampled or a fixed length limit is reached.</li>
    </ol>
    <div class="fragment" style="margin-top:20px; padding:14px; background:rgba(31,78,154,0.07); border-radius:12px; font-size:28px;">
      $$p_\theta(w_1, \ldots, w_n) = \prod_{t=1}^n p_\theta(w_t \mid w_1, \ldots, w_{t-1})$$
    </div>
  </div>
</section>

---

<!-- page 14 -->
<section class="ppt">
  <div class="ppt-title">LMs generation: greedy</div>
  <div class="ppt-line"></div>
  <div class="twocol" style="--left:55%; margin-top:10px;">
    <div style="font-size:28px; line-height:1.5; font-weight:600;">
      <p>Vocabulary: <code>{ &lt;s&gt;, &lt;/s&gt;, Hello, world, ., I, am, a, model, , }</code></p>
      <p style="margin-top:10px;">Initialize with <code>&lt;s&gt;</code>, sample from softmax distribution:</p>
      <ul style="font-size:24px; margin-top:8px;">
        <li>Hello (0.2), world (0.1), . (0.05)</li>
        <li>I (0.4), am (0.05), a (0.05)</li>
        <li>model (0.05), , (0.05), &lt;/s&gt; (0.05)</li>
      </ul>
      <p class="fragment" style="margin-top:14px;">We draw a sample and get <b>I</b>: <code>&lt;s&gt; I</code></p>
      <p class="fragment" style="margin-top:10px;">Continue until <code>&lt;/s&gt;</code> is sampled…</p>
    </div>
    <div class="fig">
      <img src="media/image910.png" style="width:100%; border-radius:10px;">
    </div>
  </div>
</section>

---

<!-- page 15 -->
<section class="ppt">
  <div class="ppt-title">LMs generation: greedy search</div>
  <div class="ppt-line"></div>
  <div class="twocol" style="--left:55%; margin-top:10px;">
    <div style="font-size:30px; line-height:1.5; font-weight:600;">
      <p><b>Greedy decoding:</b> At time \(t\), the output is chosen by computing a softmax over the set of possible outputs and then choosing the <span style="color:var(--fudan-blue);">highest probability token</span>.</p>
      <p class="fragment" style="margin-top:14px;">Greedy decoding is <b>locally optimal</b> — a choice that seems best based on the current information.</p>
    </div>
    <div class="fig">
      <img src="media/image120.png" style="width:100%; border-radius:10px;">
    </div>
  </div>
</section>

---

<!-- page 16 -->
<section class="ppt">
  <div class="ppt-title">LMs generation: test greedy search on GPT-2</div>
  <div class="ppt-line"></div>
  <div class="twocol" style="--left:55%; margin-top:10px;">
    <div style="font-size:28px; line-height:1.5; font-weight:600;">
      <p>Generate word sequences using GPT-2 on the context:</p>
      <p style="font-family:monospace; font-size:26px; background:rgba(0,0,0,0.06); padding:8px 12px; border-radius:8px; margin:10px 0;">"I enjoy walking with my cute dog"</p>
      <p class="fragment" style="margin-top:14px;"><b>Greedy search gives:</b> <span style="font-style:italic;">"I enjoy walking with my cute dog, but I'm not sure if I'll ever be able to walk with my dog. I'm not sure if I'll ever be able to walk with my dog. I'm not sure if I'll…"</span></p>
      <p class="fragment" style="margin-top:14px; color:red; font-weight:700;">The model quickly starts repeating itself!</p>
    </div>
    <div class="fig">
      <img src="media/image13.png" style="width:100%; border-radius:10px;">
      <img src="media/image14.png" style="width:100%; border-radius:10px; margin-top:8px;">
    </div>
  </div>
</section>

---

<!-- page 17 -->
<section class="ppt">
  <div class="ppt-title">LMs generation: greedy search (search tree)</div>
  <div class="ppt-line"></div>
  <div class="twocol" style="--left:55%; margin-top:10px;">
    <div style="font-size:28px; line-height:1.5; font-weight:600;">
      <p>A search tree for generating a target string. Greedy search would choose <b>"yes yes"</b>, instead of the most probable sequence <b>"ok ok"</b>.</p>
      <p class="fragment" style="margin-top:14px;">Recall that HMM model computes the likelihood using dynamic programming. Can we apply dynamic programming to find the optimal sequence?</p>
      <p class="fragment" style="margin-top:14px; color:red;">Unfortunately, dynamic programming is not applicable to generation problems with <b>long-distance dependencies</b>.</p>
    </div>
    <div class="fig">
      <img src="media/image91.png" style="width:100%; border-radius:10px;">
      <img src="media/image15.png" style="width:100%; border-radius:10px; margin-top:8px;">
    </div>
  </div>
</section>

---

<!-- page 18 -->
<section class="ppt">
  <div class="ppt-title">LMs generation: beam search</div>
  <div class="ppt-line"></div>
  <div class="twocol" style="--left:55%; margin-top:10px;">
    <div style="font-size:28px; line-height:1.5; font-weight:600;">
      <p>Reduces the risk of missing hidden high probability word sequences by keeping the most likely <b>#beams</b> hypotheses at each step.</p>
      <ul style="margin-top:12px;">
        <li>Instead of choosing <em>only</em> the best token, keep <b>k</b> possible tokens at each step</li>
        <li><b>k</b> is called the <span style="color:var(--fudan-blue);">beam width</span></li>
        <li>Beam search will always find an output sequence with higher probability than greedy search, but is not guaranteed to find the globally optimal sequence</li>
      </ul>
    </div>
    <div class="fig">
      <img src="media/image16.png" style="width:100%; border-radius:10px;">
    </div>
  </div>
</section>

---

<!-- page 19 -->
<section class="ppt">
  <div class="ppt-title">LMs generation: beam search</div>
  <div class="ppt-line"></div>
  <p style="font-size:28px; font-weight:700; margin-bottom:14px;">The completed hypotheses may have different lengths</p>
  <div class="twocol" style="--left:50%;">
    <div class="fig"><img src="media/image17.png" style="width:100%; border-radius:10px;"></div>
    <div class="fig"><img src="media/image19.png" style="width:100%; border-radius:10px;"></div>
  </div>
</section>

---

<!-- page 20 -->
<section class="ppt">
  <div class="ppt-title">LMs generation: beam search on GPT-2</div>
  <div class="ppt-line"></div>
  <div class="twocol" style="--left:55%; margin-top:10px;">
    <div style="font-size:28px; line-height:1.5; font-weight:600;">
      <p><b>Output:</b></p>
      <p style="font-style:italic; font-size:26px; margin-top:8px;">"I enjoy walking with my cute dog, but I'm not sure if I'll ever be able to walk with him again. I'm not sure if I'll ever be able to walk with him again. I'm not sure if I'll…"</p>
      <p class="fragment" style="margin-top:14px;">While the result is arguably more fluent, the output still includes <span style="color:red; font-weight:700;">repetitions of the same word sequences</span>.</p>
      <p class="fragment" style="margin-top:10px; font-weight:800;">How to fix?</p>
    </div>
    <div class="fig">
      <img src="media/image18.png" style="width:100%; border-radius:10px;">
      <img src="media/image20.png" style="width:100%; border-radius:10px; margin-top:8px;">
    </div>
  </div>
</section>

---

<!-- page 21 -->
<section class="ppt">
  <div class="ppt-title">LMs generation: beam search — n-gram penalties</div>
  <div class="ppt-line"></div>
  <div class="twocol" style="--left:55%; margin-top:10px;">
    <div style="font-size:28px; line-height:1.5; font-weight:600;">
      <p>Quick fix: introduce <b>n-gram penalties</b> (Paulus et al. 2017, Klein et al. 2017)</p>
      <p style="margin-top:12px;">Makes sure that no n-gram appears twice by manually setting the probability of next words that could create an already seen n-gram to 0.</p>
      <p class="fragment" style="margin-top:14px;"><b>Output:</b> <span style="font-style:italic; font-size:24px;">"I enjoy walking with my cute dog, but I'm not sure if I'll ever be able to walk with him again. I've been thinking about this for a while now, and I think it's time for me to take a break…"</span></p>
    </div>
    <div class="fig">
      <img src="media/image21.png" style="width:100%; border-radius:10px;">
      <img src="media/image22.png" style="width:100%; border-radius:10px; margin-top:8px;">
    </div>
  </div>
</section>

---

<!-- page 22 -->
<section class="ppt">
  <div class="ppt-title">LMs generation: beam search — multiple outputs</div>
  <div class="ppt-line"></div>
  <img src="media/image23.png" style="width:90%; border-radius:10px; display:block; margin:10px auto;">
</section>

---

<!-- page 23 -->
<section class="ppt">
  <div class="ppt-title">LMs generation: beam search — quick recap</div>
  <div class="ppt-line"></div>
  <ul style="font-size:30px; line-height:1.5; font-weight:600; margin-top:10px;">
    <li class="fragment">Beam search works very well in tasks where the length of the desired generation is more or less predictable — as in MT or summarization.</li>
    <li class="fragment" style="margin-top:14px;">But not the case for open-ended generation where the desired output length can vary greatly (e.g., dialog and story generation).</li>
    <li class="fragment" style="margin-top:14px;">Beam search heavily suffers from <b>repetitive generation</b>. This is especially hard to control with n-gram penalties.</li>
    <li class="fragment" style="margin-top:14px;"><b>Does high probability mean good quality?</b></li>
  </ul>
</section>

---

<!-- page 24 -->
<section class="ppt">
  <div class="ppt-title">LMs generation: beam search — high probability ≠ high quality</div>
  <div class="ppt-line"></div>
  <div class="twocol" style="--left:55%; margin-top:10px;">
    <div style="font-size:30px; line-height:1.5; font-weight:600;">
      <p>High quality human language does <b>not</b> follow a distribution of high probability next words.</p>
      <p style="margin-top:14px;">As humans, we want generated text to <span style="color:var(--fudan-blue);">surprise us</span> and not to be boring/predictable.</p>
    </div>
    <div class="fig">
      <img src="media/image24.png" style="width:100%; border-radius:10px;">
    </div>
  </div>
</section>

---

<!-- page 25 -->
<section class="ppt">
  <div class="ppt-title">LMs generation: top-k sampling</div>
  <div class="ppt-line"></div>
  <div style="font-size:28px; line-height:1.5; font-weight:600; margin-top:10px;">
    <p>A simple, but very powerful sampling scheme — <b>Top-k sampling</b>.</p>
    <p style="margin-top:12px;">The most likely next words are filtered and the probability mass is redistributed among only those <b>k</b> next words.</p>
    <p class="fragment" style="margin-top:14px;">Having set k=6, it eliminates the rather weird candidates ("not", "the", "small", "told") in the second sampling step.</p>
  </div>
  <div style="display:flex; gap:20px; margin-top:16px;">
    <img src="media/image25.png" style="width:48%; border-radius:10px;">
    <img src="media/image26.png" style="width:48%; border-radius:10px;">
  </div>
</section>

---

<!-- page 26 -->
<section class="ppt">
  <div class="ppt-title">LMs generation: top-k sampling — output</div>
  <div class="ppt-line"></div>
  <div class="twocol" style="--left:55%; margin-top:10px;">
    <div style="font-size:28px; line-height:1.5; font-weight:600;">
      <p><b>Output:</b></p>
      <p style="font-style:italic; margin-top:10px; font-size:26px;">"I enjoy walking with my cute dog. It's so good to have an environment where your dog is available to share with you and we'll be taking care of you. We hope you'll find this story interesting! I am from…"</p>
      <p class="fragment" style="margin-top:14px; color:var(--fudan-blue); font-weight:700;">The text is arguably quite human-sounding!</p>
    </div>
    <div class="fig">
      <img src="media/image27.png" style="width:100%; border-radius:10px;">
    </div>
  </div>
</section>

---

<!-- page 27 -->
<section class="ppt">
  <div class="ppt-title">LMs generation: top-k sampling — limitation</div>
  <div class="ppt-line"></div>
  <div class="twocol" style="--left:55%; margin-top:10px;">
    <div style="font-size:28px; line-height:1.5; font-weight:600;">
      <p>It does <b>not</b> dynamically adapt the number of words that are filtered from the next word probability distribution.</p>
      <p class="fragment" style="margin-top:14px;">This can be problematic as some words might be sampled from a very sharp distribution, whereas others from a much more flat distribution.</p>
      <div class="fragment" style="margin-top:18px; background:rgba(0,0,0,0.06); padding:12px; border-radius:10px; font-size:26px;">
        <p>T=1 → distribution is <b>flat</b></p>
        <p>T=2 → distribution is <b>sharp</b></p>
        <p style="margin-top:10px; font-weight:700;">How to handle this?</p>
      </div>
    </div>
    <div class="fig">
      <img src="media/image240.png" style="width:100%; border-radius:10px;">
    </div>
  </div>
</section>

---

<!-- page 28 -->
<section class="ppt">
  <div class="ppt-title">LMs generation: Top-p / nucleus sampling</div>
  <div class="ppt-line"></div>
  <div class="twocol" style="--left:55%; margin-top:10px;">
    <div style="font-size:28px; line-height:1.5; font-weight:600;">
      <p>Instead of sampling only from the most likely k words, <b>Top-p sampling</b> chooses from the smallest possible set of words whose cumulative probability exceeds the probability p.</p>
      <ul style="margin-top:12px;">
        <li>The probability mass is then redistributed among this set of words</li>
        <li>The size of the word set can <b>dynamically</b> increase and decrease according to the next word's probability distribution</li>
      </ul>
      <p style="margin-top:14px; font-size:22px; opacity:0.8;">Holtzman, et. al. ICLR, 2020.</p>
    </div>
    <div class="fig">
      <img src="media/image29.png" style="width:100%; border-radius:10px;">
      <img src="media/image30.png" style="width:100%; border-radius:10px; margin-top:8px;">
    </div>
  </div>
</section>

---

<!-- page 29 -->
<section class="ppt">
  <div class="ppt-title">LMs generation: Top-p / nucleus sampling</div>
  <div class="ppt-line"></div>
  <div class="twocol" style="--left:55%; margin-top:10px;">
    <div style="font-size:28px; line-height:1.5; font-weight:600;">
      <p>Set p=0.92. Top-p sampling picks the minimum number of words to exceed p=92%, defined as \(V^{(p)}\).</p>
      <p style="margin-top:14px;">In T=1, this included the 9 most likely words, whereas it only has to pick the top 3 words in T=3 to exceed 92%.</p>
    </div>
    <div class="fig">
      <img src="media/image28.png" style="width:100%; border-radius:10px;">
      <img src="media/image271.png" style="width:100%; border-radius:10px; margin-top:8px;">
    </div>
  </div>
</section>

---

<!-- page 30 -->
<section class="ppt">
  <div class="ppt-title">LMs generation: Top-p / nucleus sampling — output</div>
  <div class="ppt-line"></div>
  <div class="twocol" style="--left:55%; margin-top:10px;">
    <div style="font-size:28px; line-height:1.5; font-weight:600;">
      <p><b>Output:</b></p>
      <p style="font-style:italic; margin-top:10px; font-size:26px;">"I enjoy walking with my cute dog. He will never be the same. I watch him play. Guys, my dog needs a name. Especially if he is found with wings. What was that? I had a lot…"</p>
    </div>
    <div class="fig">
      <img src="media/image31.png" style="width:100%; border-radius:10px;">
    </div>
  </div>
</section>

---

<!-- page 31 -->
<section class="ppt">
  <div class="ppt-title">LMs generation: comparison of sampling methods</div>
  <div class="ppt-line"></div>
  <p style="font-size:28px; font-weight:650; margin-bottom:14px;">Maximization and top-k truncation methods lead to copious repetition (highlighted in blue), while sampling with and without temperature tends to lead to incoherence (highlighted in red). Nucleus Sampling largely avoids both issues.</p>
  <img src="media/image32.png" style="width:88%; border-radius:10px; display:block; margin:0 auto;">
</section>

---

<!-- page 32 -->
<section class="ppt">
  <div class="ppt-title">LMs generation: quick summary</div>
  <div class="ppt-line"></div>
  <div class="twocol" style="--left:55%; margin-top:10px;">
    <div>
      <ul style="font-size:28px; line-height:1.5; font-weight:600;">
        <li class="fragment">Top-k and top-p sampling seem to produce more fluent text than traditional greedy and beam search</li>
        <li class="fragment" style="margin-top:12px;">The drawback of greedy and beam search — mainly generating repetitive word sequences — are caused by <b>the model</b>, rather than the decoding method (Welleck et al. 2019)</li>
        <li class="fragment" style="margin-top:12px;">It looks as though top-k and top-p sampling also suffer from generating repetitive word sequences (Welleck et al. 2020)</li>
        <li class="fragment" style="margin-top:12px;"><a href="https://huggingface.co/blog/how-to-generate" target="_blank" style="font-size:22px;">https://huggingface.co/blog/how-to-generate</a></li>
      </ul>
    </div>
    <div class="fig">
      <img src="media/image35.png" style="width:100%; border-radius:10px;">
    </div>
  </div>
</section>

---

<!-- page 33 -->
<section class="ppt">
  <div class="ppt-title">Outline</div>
  <div class="ppt-line"></div>
  <ul class="outline-bullets med">
    <li class="muted">History of pre-training</li>
    <li class="muted">Transformers as pretrained LMs</li>
    <li class="muted">Autoregressive generation</li>
    <li class="active">Pretrained Decoders (GPT series)</li>
    <li class="muted">Datasets, Scaling laws, KV Cache, LoRA</li>
    <li class="muted">Pretrained Encoders (BERT series)</li>
  </ul>
</section>

---

<!-- page 34 -->
<section class="ppt">
  <div class="ppt-title">Three pretraining architectures</div>
  <div class="ppt-line"></div>
  <p style="font-size:28px; font-weight:650; margin:10px 0 20px;">The neural architecture influences the type of pretraining, and natural use cases.</p>
  <div style="display:flex; gap:24px; margin-top:10px;">
    <div style="flex:1; border:2px solid rgba(0,0,0,0.12); border-radius:14px; padding:18px; background:#f6f7f9;">
      <div style="font-size:30px; font-weight:900; color:var(--fudan-blue);">Decoders</div>
      <div style="font-size:24px; margin-top:8px; font-weight:600;">Language models! What we've seen so far. Nice to generate from; can't condition on future words.</div>
    </div>
    <div style="flex:1; border:2px solid rgba(0,0,0,0.12); border-radius:14px; padding:18px; background:#f6f7f9;">
      <div style="font-size:30px; font-weight:900; color:var(--fudan-blue);">Encoders</div>
      <div style="font-size:24px; margin-top:8px; font-weight:600;">Gets bidirectional context – can condition on future! But how do we pretrain them?</div>
    </div>
    <div style="flex:1; border:2px solid rgba(0,0,0,0.12); border-radius:14px; padding:18px; background:#f6f7f9;">
      <div style="font-size:30px; font-weight:900; color:var(--fudan-blue);">Encoder-Decoders</div>
      <div style="font-size:24px; margin-top:8px; font-weight:600;">Good parts of decoders and encoders? What's the best way to pretrain them?</div>
    </div>
  </div>
</section>

---

<!-- page 35 -->
<section class="ppt">
  <div class="ppt-title">Pretraining decoders</div>
  <div class="ppt-line"></div>
  <div class="twocol" style="--left:55%; margin-top:10px;">
    <div style="font-size:28px; line-height:1.5; font-weight:600;">
      <p>When using language model pretrained decoders, we can ignore that they were trained to model \(p(w_t \mid w_{1:t-1})\).</p>
      <p style="margin-top:14px;">We can finetune them by training a classifier on the last word's hidden state:</p>
      <p style="margin-top:10px;">$$y = \text{softmax}(W \cdot h_T + b)$$</p>
      <p style="margin-top:14px;">where \(W\) and \(b\) are randomly initialized and specified by the downstream task.</p>
      <p class="fragment" style="margin-top:14px;">Gradients backpropagate through the whole network.</p>
    </div>
    <div class="fig">
      <img src="media/image36.png" style="width:100%; border-radius:10px;">
      <img src="media/image37.png" style="width:100%; border-radius:10px; margin-top:8px;">
    </div>
  </div>
</section>
