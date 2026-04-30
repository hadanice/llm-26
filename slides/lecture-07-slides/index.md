<!-- page 0 | slides: 1, 2 -->
<div class="two-panes">
<div class="pane title-pane">
<span class="slide-badge">Slide 1</span>
<div class="title-main">Lecture 07<br>Benchmarks</div>
<div class="title-sub">
Baojian Zhou<br>
DATA130030.01 (自然语言处理)<br>
School of Data Science, Fudan University<br>
10/29/2025
</div>
<div class="title-tag">Largely adopted from Anoop Sarkar</div>
</div>
<div class="pane outline-pane">
<span class="slide-badge">Slide 2</span>
<div class="pane-title">Outline</div>
<ul class="outline-list">
<li>GLUE / SuperGLUE</li>
<li>SWAG / HellaSWAG</li>
<li>Lambada</li>
<li>Other Datasets</li>
<li>Datasets by Task Types</li>
</ul>
</div>
</div>

---

<!-- page 1 | slides: 3, 4 -->
<div class="page-header">GLUE Benchmark</div>
<div class="two-panes">
<div class="pane">
<span class="slide-badge">Slide 3</span>
<div class="pane-title">GLUE — General Language Understanding Evaluation</div>
<div class="pane-text">
<p>A collection of NLU tasks including QA, sentiment analysis, and textual entailment, together with an online platform for model evaluation, comparison, and analysis.</p>
<p style="margin-top:6px"><em>Wang et al., "GLUE: A multi-task benchmark and analysis platform for natural language understanding", 2018</em></p>
</div>
<div class="pane-img"><img src="media/image1.png" alt="GLUE overview"></div>
<div class="source-link">https://gluebenchmark.com/ · https://huggingface.co/datasets/nyu-mll/glue</div>
</div>
<div class="pane">
<span class="slide-badge">Slide 4</span>
<div class="pane-title">GLUE on HuggingFace</div>
<div class="pane-img"><img src="media/image2.png" alt="GLUE HuggingFace"></div>
<div class="source-link">https://huggingface.co/datasets/nyu-mll/glue</div>
</div>
</div>

---

<!-- page 2 | slides: 5, 6 -->
<div class="page-header">GLUE — Single-Sentence Tasks</div>
<div class="two-panes">
<div class="pane">
<span class="slide-badge">Slide 5</span>
<div class="pane-title">CoLA — Corpus of Linguistic Acceptability</div>
<div class="pane-text">
<p>English acceptability judgments drawn from books and journal articles on linguistic theory.</p>
<p>Each example is a sequence of words annotated with whether it is a grammatical English sentence. Score is in [−1, 1].</p>
</div>
<div class="pane-img"><img src="media/image3.png" alt="CoLA"></div>
<div class="source-link">https://huggingface.co/datasets/nyu-mll/glue</div>
</div>
<div class="pane">
<span class="slide-badge">Slide 6</span>
<div class="pane-title">SST-2 — Stanford Sentiment Treebank</div>
<div class="pane-text">
<p>Sentences from movie reviews with human sentiment annotations. Task: predict positive/negative sentiment at sentence level.</p>
<ul>
<li><em>"uneasy mishmash of styles and genres"</em></li>
<li><em>"it's also heavy-handed and devotes too much time to bigoted views"</em></li>
<li><em>"waydowntown boasts a huge charm factor and smacks of originality"</em></li>
<li><em>"a remarkable 179-minute meditation on the nature of revolution"</em></li>
<li><em>"starts off with a bang, but then fizzles like a wet stick of dynamite"</em></li>
</ul>
</div>
<div class="source-link">https://huggingface.co/datasets/nyu-mll/glue</div>
</div>
</div>

---

<!-- page 3 | slides: 7, 8 -->
<div class="page-header">GLUE — Similarity &amp; Paraphrase Tasks</div>
<div class="two-panes">
<div class="pane">
<span class="slide-badge">Slide 7</span>
<div class="pane-title">MRPC — Microsoft Research Paraphrase Corpus</div>
<div class="pane-text">
<p>Sentence pairs with human annotations of semantic equivalence. Classes are imbalanced (68% positive).</p>
</div>
<div class="pane-img"><img src="media/image4.png" alt="MRPC"></div>
<div class="source-link">https://huggingface.co/datasets/nyu-mll/glue</div>
</div>
<div class="pane">
<span class="slide-badge">Slide 8</span>
<div class="pane-title">STS-B — Semantic Textual Similarity Benchmark</div>
<div class="pane-text">
<p>Sentence pairs from various sources, human-annotated with similarity scores from 1 to 5.</p>
<p>Task: predict [1, 5]. Report Pearson and Spearman correlation coefficients.</p>
</div>
<div class="pane-img"><img src="media/image5.png" alt="STS-B"></div>
</div>
</div>

---

<!-- page 4 | slides: 9, 10 -->
<div class="page-header">GLUE — Similarity &amp; Inference Tasks</div>
<div class="two-panes">
<div class="pane">
<span class="slide-badge">Slide 9</span>
<div class="pane-title">QQP — Quora Question Pairs</div>
<div class="pane-text">
<p>Question pairs from Quora. Classes are imbalanced (63% negative) so accuracy and F1 score are both reported.</p>
</div>
<div class="pane-img"><img src="media/image6.png" alt="QQP"></div>
</div>
<div class="pane">
<span class="slide-badge">Slide 10</span>
<div class="pane-title">MNLI — Multi-Genre Natural Language Inference</div>
<div class="pane-text">
<p>Crowd-sourced sentence pairs with entailment annotations: entailment (0), contradiction (2), neutral (1).</p>
<p>Task: predict these three labels.</p>
</div>
<div class="pane-img"><img src="media/image7.png" alt="MNLI"></div>
</div>
</div>

---

<!-- page 5 | slides: 11, 12 -->
<div class="page-header">GLUE — Inference Tasks</div>
<div class="two-panes">
<div class="pane">
<span class="slide-badge">Slide 11</span>
<div class="pane-title">QNLI — Stanford Question Answering Dataset</div>
<div class="pane-text">
<p>Converted to sentence-pair classification: form a pair between each question and each sentence in the context, filter pairs with low lexical overlap.</p>
<p>Task: predict yes (0) or no (1) — does the context sentence contain the answer?</p>
</div>
<div class="pane-img"><img src="media/image8.png" alt="QNLI"></div>
</div>
<div class="pane">
<span class="slide-badge">Slide 12</span>
<div class="pane-title">RTE — Recognizing Textual Entailment</div>
<div class="pane-text">
<p>Task: predict entailment (0) or not-entailment (1) between pairs of sentences.</p>
</div>
<div class="pane-img"><img src="media/image9.png" alt="RTE"></div>
</div>
</div>

---

<!-- page 6 | slides: 13, 14 -->
<div class="page-header">GLUE — Inference Tasks &amp; Performance</div>
<div class="two-panes">
<div class="pane">
<span class="slide-badge">Slide 13</span>
<div class="pane-title">WNLI — Winograd Schema Challenge</div>
<div class="pane-text">
<p>Reading comprehension task: identify the referent of a pronoun using entailment between two sentences (one with the pronoun reference made explicit).</p>
<p>Predict 1 (entailment) or 0 (not entailment). Designed to fool simple statistical techniques. Test set is imbalanced (65% not-entailment); dev set is adversarial.</p>
</div>
<div class="pane-img"><img src="media/image10.png" alt="WNLI"></div>
</div>
<div class="pane perf-pane">
<span class="slide-badge">Slide 14</span>
<div class="pane-title">GLUE Benchmark Performance</div>
<div class="pane-img"><img src="media/image11.png" alt="GLUE performance chart"></div>
</div>
</div>

---

<!-- page 7 | slides: 15, 16 -->
<div class="page-header">SuperGLUE</div>
<div class="two-panes">
<div class="pane">
<span class="slide-badge">Slide 15</span>
<div class="pane-title">SuperGLUE — A More Rigorous NLU Test</div>
<div class="pane-text">
<p>GLUE was too easy for LLMs after July 2019. SuperGLUE is a harder benchmark with more challenging tasks.</p>
</div>
<div class="pane-img"><img src="media/image12.png" alt="SuperGLUE overview"></div>
<div class="source-link">https://super.gluebenchmark.com/ · https://huggingface.co/datasets/aps/super_glue</div>
</div>
<div class="pane">
<span class="slide-badge">Slide 16</span>
<div class="pane-title">SuperGLUE 1. BoolQ — Boolean Questions</div>
<div class="pane-text">
<p>QA task with yes/no answers. Kinds of reasoning required:</p>
</div>
<div class="pane-img"><img src="media/image14.png" alt="BoolQ"></div>
<div class="source-link">https://huggingface.co/datasets/aps/super_glue</div>
</div>
</div>

---

<!-- page 8 | slides: 17, 18 -->
<div class="page-header">SuperGLUE</div>
<div class="two-panes">
<div class="pane">
<span class="slide-badge">Slide 17</span>
<div class="pane-title">SuperGLUE 2. CB — CommitmentBank</div>
<div class="pane-text">
<p>Is the author committed to the truth of the embedded clause? Each example consists of a premise with an embedded clause; the hypothesis is the extraction of that clause.</p>
</div>
<div class="pane-img"><img src="media/image16.png" alt="CB"></div>
</div>
<div class="pane">
<span class="slide-badge">Slide 18</span>
<div class="pane-title">SuperGLUE 3. COPA — Choice of Plausible Alternatives</div>
<div class="pane-text">
<p>Causal reasoning task: choose the most plausible cause or effect for a given premise.</p>
</div>
<div class="pane-img"><img src="media/image18.png" alt="COPA"></div>
</div>
</div>

---

<!-- page 9 | slides: 19, 20 -->
<div class="page-header">SuperGLUE</div>
<div class="two-panes">
<div class="pane">
<span class="slide-badge">Slide 19</span>
<div class="pane-title">SuperGLUE 4. MultiRC — Multi-Sentence Reading Comprehension</div>
<div class="pane-text">
<p>Reading comprehension task requiring reasoning over multiple sentences in a passage to answer questions.</p>
</div>
<div class="pane-img"><img src="media/image17.png" alt="MultiRC"></div>
</div>
<div class="pane">
<span class="slide-badge">Slide 20</span>
<div class="pane-title">SuperGLUE 5. ReCoRD — Reading Comprehension with Commonsense Reasoning</div>
<div class="pane-text">
<p>Reading comprehension dataset requiring commonsense reasoning over news articles.</p>
</div>
<div class="pane-img"><img src="media/image15.png" alt="ReCoRD"></div>
</div>
</div>

---

<!-- page 10 | slides: 21, 22 -->
<div class="page-header">SuperGLUE</div>
<div class="two-panes">
<div class="pane">
<span class="slide-badge">Slide 21</span>
<div class="pane-title">SuperGLUE 6. RTE — Recognizing Textual Entailment</div>
<div class="pane-text">
<p>Combines data from RTE1, RTE3, and RTE5 shared tasks.</p>
</div>
<div class="pane-img"><img src="media/image19.png" alt="RTE SuperGLUE"></div>
</div>
<div class="pane">
<span class="slide-badge">Slide 22</span>
<div class="pane-title">SuperGLUE 7. WiC — Word-in-Context</div>
<div class="pane-text">
<p>Word sense disambiguation cast as binary classification of sentence pairs: does the target word carry the same sense in both sentences?</p>
</div>
<div class="pane-img"><img src="media/image19.png" alt="WiC"></div>
</div>
</div>

---

<!-- page 11 | slides: 23, 24 -->
<div class="page-header">SuperGLUE &amp; Section Break</div>
<div class="two-panes">
<div class="pane">
<span class="slide-badge">Slide 23</span>
<div class="pane-title">SuperGLUE 8. WSC — Winograd Schema Challenge</div>
<div class="pane-text">
<p>Coreference resolution task: each example has a sentence with a pronoun and a list of noun phrases. Task: identify which noun phrase the pronoun refers to.</p>
</div>
<div class="pane-img"><img src="media/image15.png" alt="WSC"></div>
</div>
<div class="pane outline-pane">
<span class="slide-badge">Slide 24</span>
<div class="pane-title">Outline</div>
<ul class="outline-list">
<li>GLUE / SuperGLUE</li>
<li class="active">SWAG / HellaSWAG</li>
<li>Lambada</li>
<li>Other Datasets</li>
<li>Datasets by Task Types</li>
</ul>
</div>
</div>

---

<!-- page 12 | slides: 25, 26 -->
<div class="page-header">SWAG</div>
<div class="two-panes">
<div class="pane">
<span class="slide-badge">Slide 25</span>
<div class="pane-title">SWAG — Situations With Adversarial Generations</div>
<div class="pane-text">
<p>Large-scale adversarial dataset for grounded commonsense inference. 113k multiple-choice questions about grounded situations.</p>
<ul>
<li>Given: <em>"she opened the hood of the car"</em></li>
<li>Humans reason: <em>"then, she examined the engine"</em></li>
<li>Built using Adversarial Filtering to identify meaning-based answers rather than vocabulary-overlap answers</li>
</ul>
</div>
<div class="pane-img"><img src="media/image20.png" alt="SWAG"></div>
<div class="source-link">https://huggingface.co/datasets/allenai/swag</div>
</div>
<div class="pane">
<span class="slide-badge">Slide 26</span>
<div class="pane-title">SWAG Dataset Construction</div>
<div class="pane-text">
<p>113k multiple-choice questions (73k train / 20k val / 20k test), derived from pairs of consecutive video captions from ActivityNet Captions and LSMDC.</p>
<p>Each question has one human-verified gold ending and 3 distractors.</p>
<p><strong>BERT fine-tuned on SWAG → 86% accuracy. DeBERTa-large → 94.12%.</strong></p>
</div>
<div class="pane-img"><img src="media/image21.png" alt="SWAG construction"></div>
<div class="source-link">https://rowanzellers.com/swag/</div>
</div>
</div>

---

<!-- page 13 | slides: 27, 28 -->
<div class="page-header">SWAG &amp; HellaSWAG</div>
<div class="two-panes">
<div class="pane">
<span class="slide-badge">Slide 27</span>
<div class="pane-title">SWAG — Examples</div>
<div class="pane-text">
<p>Answering <em>"An old man rides …"</em> requires knowledge about bumper cars — they are tiny, don't drive on roads, and don't work in parking lots.</p>
<p>Answering <em>"He pours the raw egg …"</em> requires intuitive physical reasoning about what happens next in making an omelet.</p>
</div>
<div class="pane-img"><img src="media/image22.png" alt="SWAG examples"></div>
</div>
<div class="pane">
<span class="slide-badge">Slide 28</span>
<div class="pane-title">HellaSWAG — Can a Machine Really Finish Your Sentence?</div>
<div class="pane-text">
<p>Pick the best ending to the context.</p>
<p><em>"How to catch dragonflies. Use a long-handled aerial net with a wide opening. Select an aerial net that is 18 inches (46 cm) in diameter or larger. Look for one with a nice long handle. …"</em></p>
</div>
<div class="pane-img"><img src="media/image26.png" alt="HellaSWAG"></div>
<div class="source-link">https://rowanzellers.com/hellaswag/</div>
</div>
</div>

---

<!-- page 14 | slides: 29, 30 -->
<div class="page-header">HellaSWAG</div>
<div class="two-panes">
<div class="pane">
<span class="slide-badge">Slide 29</span>
<div class="pane-title">HellaSWAG — Examples</div>
<div class="pane-img"><img src="media/image27.png" alt="HellaSWAG examples"></div>
<div class="source-link">https://huggingface.co/datasets/Rowan/hellaswag</div>
</div>
<div class="pane perf-pane">
<span class="slide-badge">Slide 30</span>
<div class="pane-title">HellaSWAG — Model Performance</div>
<div class="pane-text">
<p><strong>GPT-3:</strong> 85.5% accuracy (10-shot learning)</p>
<p><strong>GPT-4:</strong> 95.3% accuracy (10-shot learning)</p>
</div>
<div class="pane-img"><img src="media/image30.png" alt="HellaSWAG accuracy"></div>
<div class="source-link">https://huggingface.co/datasets/Rowan/hellaswag</div>
</div>
</div>

---

<!-- page 15 | slides: 31, 32 -->
<div class="page-header">HellaSWAG &amp; Section Break</div>
<div class="two-panes">
<div class="pane">
<span class="slide-badge">Slide 31</span>
<div class="pane-title">HellaSWAG — Overview Chart</div>
<div class="pane-img"><img src="media/image31.png" alt="HellaSWAG chart"></div>
<div class="source-link">https://huggingface.co/datasets/Rowan/hellaswag</div>
</div>
<div class="pane outline-pane">
<span class="slide-badge">Slide 32</span>
<div class="pane-title">Outline</div>
<ul class="outline-list">
<li>GLUE / SuperGLUE</li>
<li>SWAG / HellaSWAG</li>
<li class="active">Other Datasets</li>
<li>Datasets by Task Types</li>
</ul>
</div>
</div>

---

<!-- page 16 | slides: 33, 34 -->
<div class="page-header">Other Datasets</div>
<div class="two-panes">
<div class="pane">
<span class="slide-badge">Slide 33</span>
<div class="pane-title">Other Datasets — Overview</div>
<ul class="dataset-list">
<li><strong>MMLU</strong> Multiple choice in 57 subjects (professional &amp; academic)</li>
<li><strong>ARC</strong> AI2 Reasoning Challenge — grade school multiple-choice science</li>
<li><strong>WinoGrande</strong> Bigger Winograd Schema Challenge</li>
<li><strong>DROP</strong> Reading comprehension &amp; arithmetic</li>
<li><strong>GSM-8K</strong> Grade school math word problems</li>
<li><strong>BLiMP</strong> Benchmark of minimal linguistic pairs (new CoLA)</li>
<li><strong>HumanEval</strong> Evaluating LLMs trained on code</li>
</ul>
</div>
<div class="pane">
<span class="slide-badge">Slide 34</span>
<div class="pane-title">Lambada Dataset</div>
<div class="pane-text">
<p>Tests the ability of LMs to predict the final word of a passage based on broad context.</p>
</div>
<div class="pane-img"><img src="media/image32.png" alt="Lambada"></div>
<div class="source-link">https://huggingface.co/datasets/cimec/lambada · https://zenodo.org/records/2630551</div>
</div>
</div>

---

<!-- page 17 | slides: 35, 36 -->
<div class="page-header">Other Datasets — MMLU</div>
<div class="two-panes">
<div class="pane">
<span class="slide-badge">Slide 35</span>
<div class="pane-title">MMLU — Measuring Massive Multitask Language Understanding</div>
<div class="pane-text">
<p>Multiple-choice questions in 57 subjects spanning professional and academic domains.</p>
</div>
<div class="pane-img"><img src="media/image34.png" alt="MMLU subjects"></div>
</div>
<div class="pane">
<span class="slide-badge">Slide 36</span>
<div class="pane-title">MMLU — Results</div>
<div class="pane-img"><img src="media/image39.png" alt="MMLU results"></div>
</div>
</div>

---

<!-- page 18 | slides: 37, 38 -->
<div class="page-header">Other Datasets — ARC &amp; WinoGrande</div>
<div class="two-panes">
<div class="pane">
<span class="slide-badge">Slide 37</span>
<div class="pane-title">ARC — AI2 Reasoning Challenge</div>
<div class="pane-text">
<p>Grade school multiple-choice science quiz. Partitioned into Easy and Challenge sets.</p>
</div>
<div class="pane-img"><img src="media/image41.png" alt="ARC"></div>
<div class="source-link">https://huggingface.co/datasets/allenai/ai2_arc</div>
</div>
<div class="pane">
<span class="slide-badge">Slide 38</span>
<div class="pane-title">WinoGrande — Commonsense Pronoun Resolution</div>
<div class="pane-text">
<p>A larger and harder version of the Winograd Schema Challenge, with 44k problems.</p>
</div>
<div class="pane-img"><img src="media/image42.png" alt="WinoGrande"></div>
<div class="source-link">https://huggingface.co/datasets/allenai/winogrande</div>
</div>
</div>

---

<!-- page 19 | slides: 39, 40 -->
<div class="page-header">Other Datasets — DROP &amp; GSM-8K</div>
<div class="two-panes">
<div class="pane">
<span class="slide-badge">Slide 39</span>
<div class="pane-title">DROP — Discrete Reasoning Over Paragraphs</div>
<div class="pane-text">
<p>Reading comprehension requiring arithmetic and discrete reasoning over passage content. Reference model: BiDAF.</p>
</div>
<div class="pane-img"><img src="media/image43.png" alt="DROP"></div>
<div class="source-link">https://huggingface.co/datasets/ucinlp/drop</div>
</div>
<div class="pane">
<span class="slide-badge">Slide 40</span>
<div class="pane-title">GSM-8K — Grade School Math Word Problems</div>
<div class="pane-text">
<p>8,500 grade school math word problems requiring multi-step reasoning.</p>
</div>
<div class="pane-img"><img src="media/image44.png" alt="GSM-8K"></div>
<div class="source-link">https://huggingface.co/datasets/openai/gsm8k</div>
</div>
</div>

---

<!-- page 20 | slides: 41, 42 -->
<div class="page-header">Other Datasets — BLiMP &amp; HumanEval</div>
<div class="two-panes">
<div class="pane">
<span class="slide-badge">Slide 41</span>
<div class="pane-title">BLiMP — Benchmark of Linguistic Minimal Pairs</div>
<div class="pane-text">
<p>A challenge set evaluating linguistic knowledge of LMs on major grammatical phenomena in English.</p>
</div>
<div class="pane-img"><img src="media/image45.png" alt="BLiMP"></div>
</div>
<div class="pane">
<span class="slide-badge">Slide 42</span>
<div class="pane-title">HumanEval — Code Generation</div>
<div class="pane-text">
<p>Generate standalone Python functions from docstrings; evaluate correctness automatically via unit tests.</p>
<p>164 original programming problems assessing language comprehension, algorithms, and simple mathematics.</p>
</div>
<div class="pane-img"><img src="media/image46.png" alt="HumanEval"></div>
</div>
</div>

---

<!-- page 21 | slides: 43, 44 -->
<div class="page-header">Datasets by Task Type</div>
<div class="two-panes">
<div class="pane outline-pane">
<span class="slide-badge">Slide 43</span>
<div class="pane-title">Outline</div>
<ul class="outline-list">
<li>GLUE / SuperGLUE</li>
<li>SWAG / HellaSWAG</li>
<li>Lambada</li>
<li>Other Datasets</li>
<li class="active">Datasets by Task Types</li>
</ul>
</div>
<div class="pane">
<span class="slide-badge">Slide 44</span>
<div class="pane-title">Question Answering Datasets</div>
<ul class="dataset-list">
<li><strong>Natural Questions</strong> Questions from Google search; answers from Wikipedia</li>
<li><strong>WebQuestions</strong> Questions answerable using Freebase</li>
<li><strong>TriviaQA</strong> Large-scale dataset for reading comprehension and QA</li>
<li><strong>CoQA</strong> Conversational Question Answering Challenge</li>
</ul>
</div>
</div>

---

<!-- page 22 | slides: 45, 46 -->
<div class="page-header">Datasets by Task Type</div>
<div class="two-panes">
<div class="pane">
<span class="slide-badge">Slide 45</span>
<div class="pane-title">Summarization &amp; Natural Language Generation</div>
<div class="pane-text"><p><strong>Summarization</strong></p></div>
<ul class="dataset-list">
<li><strong>CNN-Daily Mail</strong> News article summarization</li>
<li><strong>BookSum</strong> Long-form book summarization</li>
<li><strong>NYT Dataset</strong> New York Times articles</li>
<li><strong>DUC Dataset</strong> Document Understanding Conference (NIST)</li>
</ul>
<div class="pane-text" style="margin-top:10px"><p><strong>Natural Language Generation</strong></p></div>
<ul class="dataset-list">
<li><strong>E2E</strong> Restaurant domain NLG from meaning representations</li>
<li><strong>WebNLG</strong> Triples to text generation</li>
<li><strong>DART</strong> Open-domain structured data to text</li>
</ul>
</div>
<div class="pane">
<span class="slide-badge">Slide 46</span>
<div class="pane-title">Translation Datasets</div>
<ul class="dataset-list">
<li><strong>FLORES-200</strong> 200-language evaluation benchmark</li>
<li><strong>WMT 2014</strong> Classic EN↔DE, EN↔FR machine translation</li>
<li><strong>OPUS-MT</strong> Large collection of open parallel corpora</li>
<li><strong>LORELEI</strong> Low-resource language evaluation</li>
</ul>
</div>
</div>

---

<!-- page 23 | slides: 47, 48 -->
<div class="page-header">Structured Prediction &amp; Benchmarking Issues</div>
<div class="two-panes">
<div class="pane">
<span class="slide-badge">Slide 47</span>
<div class="pane-title">Structured Prediction Datasets</div>
<ul class="dataset-list">
<li><strong>CoNLL 2000–2018</strong> Shared tasks for NER, chunking, parsing</li>
<li><strong>AIDA-CoNLL</strong> Entity linking to Wikipedia</li>
<li><strong>MedMentions</strong> Entity linking to UMLS (biomedical)</li>
<li><strong>Penn Treebank / PropBank</strong> Dependency &amp; phrase-structure parsing</li>
<li><strong>Morphophon</strong> Morphological analysis</li>
<li><strong>Wikipron</strong> Word pronunciation for 165 languages</li>
</ul>
</div>
<div class="pane">
<span class="slide-badge">Slide 48</span>
<div class="pane-title">Dynabench — Rethinking Benchmarking in NLP</div>
<div class="pane-text">
<p>Benchmark saturation over time for popular benchmarks, normalized with initial performance at −1 and human performance at 0.</p>
</div>
<div class="pane-img"><img src="media/image47.png" alt="Dynabench saturation"></div>
<div class="source-link">https://arxiv.org/pdf/2104.14337</div>
</div>
</div>

---

<!-- page 24 | slides: 49, 50 -->
<div class="page-header">Benchmarking Progress</div>
<div class="two-panes">
<div class="pane">
<span class="slide-badge">Slide 49</span>
<div class="pane-title">BIG-Bench Hard (BBH)</div>
<div class="pane-img"><img src="media/image48.png" alt="BIG-Bench Hard"></div>
<div class="source-link">https://arxiv.org/pdf/2210.09261 · https://contextual.ai/plotting-progress-in-ai/</div>
</div>
<div class="pane">
<span class="slide-badge">Slide 50</span>
<div class="pane-title">ARC Prize</div>
<div class="pane-img"><img src="media/image51.jpeg" alt="ARC Prize"></div>
<div class="source-link">https://arcprize.org/</div>
</div>
</div>

---

<!-- page 25 | slides: 51, 52 -->
<div class="page-header">Reasoning &amp; Humanity's Last Exam</div>
<div class="two-panes">
<div class="pane">
<span class="slide-badge">Slide 51</span>
<div class="pane-title">Reasoning Benchmarks</div>
<div class="pane-img"><img src="media/image52.png" alt="Reasoning"></div>
</div>
<div class="pane">
<span class="slide-badge">Slide 52</span>
<div class="pane-title">Humanity's Last Exam (HLE) — Motivation</div>
<div class="pane-text">
<p>SOTA LLMs now exceed <strong>90% on MMLU</strong>, saturating popular benchmarks and obscuring real frontier capabilities.</p>
<p>HLE is designed as the <em>final closed-ended academic benchmark</em> at the frontier of human knowledge — 2,500 expert-written questions across 100+ subjects, multi-modal, with unambiguous, verifiable answers.</p>
<ul>
<li>Multiple-choice + exact-match → automated grading</li>
<li>Resistant to simple internet lookup / DB retrieval</li>
<li>Emphasis on world-class mathematics &amp; deep reasoning</li>
</ul>
<p style="margin-top:6px"><em>Phan, Gatti, Han, Li, et al., "Humanity's Last Exam", 2025</em></p>
</div>
<div class="source-link">https://lastexam.ai · https://arxiv.org/abs/2501.14249</div>
</div>
</div>

---

<!-- page 26 | slides: 53, 54 -->
<div class="page-header">HLE — Dataset Collection</div>
<div class="two-panes">
<div class="pane">
<span class="slide-badge">Slide 53</span>
<div class="pane-title">Global Expert Effort</div>
<div class="pane-text">
<p>HLE was crowd-sourced from <strong>~1,000 subject-matter experts</strong> at <strong>500+ institutions</strong> across <strong>50 countries</strong> — mostly professors, researchers, and graduate-degree holders.</p>
<ul>
<li>Questions require graduate-level expertise or highly specific knowledge</li>
<li>Answers must be short, unambiguous, and accepted by domain experts</li>
<li>No open-ended / subjective / WMD content</li>
<li>Each question ships with a detailed solution</li>
</ul>
<p><strong>$500K prize pool</strong>: $5K for each top-50 question, $500 for each of the next 500, plus paper co-authorship.</p>
</div>
</div>
<div class="pane">
<span class="slide-badge">Slide 54</span>
<div class="pane-title">Review Process — Quality Control</div>
<div class="pane-text">
<p><strong>Stage 1 — LLM difficulty check.</strong> Questions first tested against frontier LLMs; only those the models <em>cannot</em> solve advance.</p>
<ul>
<li>70,000+ attempts logged</li>
<li>~13,000 questions passed to expert review</li>
</ul>
<p><strong>Stage 2 — Two-round expert review</strong> (graduate-degree reviewers):</p>
<ul>
<li>Round 1: 1–3 reviewers give iterative feedback</li>
<li>Round 2: organizers / expert reviewers approve final set</li>
</ul>
<p>A <strong>private held-out set</strong> is maintained alongside the public release to detect overfitting / gaming.</p>
</div>
</div>
</div>

---

<!-- page 27 | slides: 55, 56 -->
<div class="page-header">HLE Results &amp; References</div>
<div class="two-panes">
<div class="pane">
<span class="slide-badge">Slide 55</span>
<div class="pane-title">HLE — Frontier Model Results</div>
<div class="pane-text">
<p>All frontier models show <strong>low accuracy</strong> and <strong>high calibration error</strong> (hallucination):</p>
<table style="font-size:0.78em; border-collapse:collapse; margin-top:4px">
<thead><tr><th style="text-align:left;padding:2px 8px">Model</th><th style="padding:2px 8px">Acc ↑</th><th style="padding:2px 8px">Calib. err ↓</th></tr></thead>
<tbody>
<tr><td style="padding:2px 8px">GPT-4o</td><td style="text-align:center">2.7%</td><td style="text-align:center">89%</td></tr>
<tr><td style="padding:2px 8px">Grok 2</td><td style="text-align:center">3.0%</td><td style="text-align:center">87%</td></tr>
<tr><td style="padding:2px 8px">Claude 3.5 Sonnet</td><td style="text-align:center">4.1%</td><td style="text-align:center">84%</td></tr>
<tr><td style="padding:2px 8px">Gemini 1.5 Pro</td><td style="text-align:center">4.6%</td><td style="text-align:center">88%</td></tr>
<tr><td style="padding:2px 8px">Gemini 2.0 Flash Thinking</td><td style="text-align:center">6.6%</td><td style="text-align:center">82%</td></tr>
<tr><td style="padding:2px 8px">o1</td><td style="text-align:center">8.0%</td><td style="text-align:center">83%</td></tr>
<tr><td style="padding:2px 8px">DeepSeek-R1*</td><td style="text-align:center">8.5%</td><td style="text-align:center">73%</td></tr>
<tr><td style="padding:2px 8px">o3-mini (high)*</td><td style="text-align:center">13.4%</td><td style="text-align:center">80%</td></tr>
</tbody>
</table>
<p style="font-size:0.75em; margin-top:4px">* text-only subset. Reasoning models use 8K+ completion tokens on average. Authors project models may exceed <strong>50% accuracy by end of 2025</strong>.</p>
</div>
</div>
<div class="pane">
<span class="slide-badge">Slide 56</span>
<div class="pane-title">References</div>
<div class="pane-text">
<ul>
<li>[1] Slides from Anoop Sarkar</li>
<li>[2] A Survey on Evaluation of Large Language Models</li>
<li>[3] https://decanlp.com/</li>
<li>[4] GPT-4 — https://arxiv.org/pdf/2303.08774</li>
<li>[5] https://rowanzellers.com/hellaswag/</li>
<li>[6] https://rowanzellers.com/swag/</li>
<li>[7] https://allenai.org/data/arc</li>
<li>[8] https://winogrande.allenai.org/</li>
<li>[9] https://allenai.org/data/drop</li>
<li>[10] https://crfm.stanford.edu/helm/mmlu/latest/#/leaderboard</li>
<li>[11] Humanity's Last Exam — https://arxiv.org/abs/2501.14249 · https://lastexam.ai</li>
</ul>
<p style="margin-top:12px; font-weight:700; color:#7c3aed">Next topic: LLMs</p>
</div>
</div>
</div>
</div>
