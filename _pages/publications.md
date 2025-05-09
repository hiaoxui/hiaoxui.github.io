---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---



<style>
  /* ==== switch toggle ===== */
  .switch {
    --track-w: 2.4rem;   /* overall size – edit just these two lines */
    --track-h: 1.3rem;

    position: relative;
    display: inline-flex;
    align-items: center;
    font-size: 0.95rem;
    gap: 0.55rem;
    cursor: pointer;
    user-select: none;
  }

  /* hide the native checkbox but keep it accessible */
  .switch input {
    position: absolute;
    opacity: 0;
    width: 0;
    height: 0;
  }

  /* track */
  .switch .track {
    width: var(--track-w);
    height: var(--track-h);
    background: #c4c6c9;
    border-radius: var(--track-h);
    transition: background 0.2s ease;
  }

  /* thumb */
  .switch .thumb {
    position: absolute;
    top: 0.1rem;
    left: 0.1rem;
    width: calc(var(--track-h) - 0.2rem);
    height: calc(var(--track-h) - 0.2rem);
    background: #fff;
    border-radius: 50%;
    box-shadow: 0 0 2px rgba(0,0,0,.25);
    transition: transform 0.2s ease;
  }

  /* when checked → move thumb + change track color */
  .switch input:checked + .track {
    background: #007acc;            /* pick any accent color */
  }
  .switch input:checked + .track .thumb {
    transform: translateX(calc(var(--track-w) - var(--track-h)));
  }
</style>

<label class="switch">
  <input type="checkbox" id="onlySelected" checked>
  <span class="track"><span class="thumb"></span></span>
  Selected&nbsp;publications
</label>



- [Dynamic and Biphasic Regulation of Cell Migration by Ras](https://www.biorxiv.org/content/10.1101/2025.02.13.638204v1). Yiyan Lin, Eleana Parajón, Qinling Yuan, Siyu Ye, **Guanghui Qin**, Yu Deng, Jane Borleis, Ariel Koyfman, Pablo A Iglesias, Konstantinos Konstantopoulos, Douglas N Robinson, and Peter N Devreotes. In *bioRxiv*, 2025. <span>[<a href="https://www.biorxiv.org/content/10.1101/2025.02.13.638204v1">paper</a>] [<a href="javascript:toggleDiv('0bib')">bibtex</a>]</span>
{: .publication .selected}







<div id="0bib" style="display: none" class="bib">
    @misc{linDynamicBiphasicRegulation2025,<br>
&nbsp;&nbsp;title&nbsp;=&nbsp;{Dynamic&nbsp;and&nbsp;Biphasic&nbsp;Regulation&nbsp;of&nbsp;Cell&nbsp;Migration&nbsp;by&nbsp;Ras},<br>
&nbsp;&nbsp;author&nbsp;=&nbsp;{Lin,&nbsp;Yiyan&nbsp;and&nbsp;Parajón,&nbsp;Eleana&nbsp;and&nbsp;Yuan,&nbsp;Qinling&nbsp;and&nbsp;Ye,&nbsp;Siyu&nbsp;and&nbsp;Qin,&nbsp;Guanghui&nbsp;and&nbsp;Deng,&nbsp;Yu&nbsp;and&nbsp;Borleis,&nbsp;Jane&nbsp;and&nbsp;Koyfman,&nbsp;Ariel&nbsp;and&nbsp;Iglesias,&nbsp;Pablo&nbsp;A&nbsp;and&nbsp;Konstantopoulos,&nbsp;Konstantinos&nbsp;and&nbsp;Robinson,&nbsp;Douglas&nbsp;N&nbsp;and&nbsp;Devreotes,&nbsp;Peter&nbsp;N},<br>
&nbsp;&nbsp;date&nbsp;=&nbsp;{2025},<br>
&nbsp;&nbsp;url&nbsp;=&nbsp;{https://www.biorxiv.org/content/10.1101/2025.02.13.638204v1},<br>
}<br>

    </div>



- [Med-RLVR: Emerging Medical Reasoning from a 3B base model via reinforcement Learning](https://arxiv.org/pdf/2502.19655). Sheng Zhang\*, Qianchu Liu\*, **Guanghui Qin**\*, Tristan Naumann, and Hoifung Poon. In *arXiv*, 2025. <span>[<a href="https://arxiv.org/pdf/2502.19655">paper</a>] [<a href="javascript:toggleDiv('1bib')">bibtex</a>]</span>
{: .publication data-selected="false"}







<div id="1bib" style="display: none" class="bib">
    @misc{zhang2025medrlvremergingmedicalreasoning,<br>
&nbsp;&nbsp;&nbsp;&nbsp;title={Med-RLVR:&nbsp;Emerging&nbsp;Medical&nbsp;Reasoning&nbsp;from&nbsp;a&nbsp;3B&nbsp;base&nbsp;model&nbsp;via&nbsp;reinforcement&nbsp;Learning},<br>
&nbsp;&nbsp;&nbsp;&nbsp;author={Sheng&nbsp;Zhang&nbsp;and&nbsp;Qianchu&nbsp;Liu&nbsp;and&nbsp;Guanghui&nbsp;Qin&nbsp;and&nbsp;Tristan&nbsp;Naumann&nbsp;and&nbsp;Hoifung&nbsp;Poon},<br>
&nbsp;&nbsp;&nbsp;&nbsp;year={2025},<br>
&nbsp;&nbsp;&nbsp;&nbsp;eprint={2502.19655},<br>
&nbsp;&nbsp;&nbsp;&nbsp;archivePrefix={arXiv},<br>
&nbsp;&nbsp;&nbsp;&nbsp;primaryClass={cs.CL},<br>
&nbsp;&nbsp;&nbsp;&nbsp;url={https://arxiv.org/abs/2502.19655},<br>
}<br>

    </div>



- [X-Reasoner: Towards Generalizable Reasoning Across Modalities and Domains](https://arxiv.org/pdf/2505.03981). Qianchu Liu\*, Sheng Zhang\*, **Guanghui Qin**\*, Timothy Ossowski, Yu Gu, Ying Jin, Sid Kiblawi, Sam Preston, Mu Wei, Paul Vozila, Tristan Naumann, and Hoifung Poon. In *arXiv*, 2025. <span>[<a href="https://arxiv.org/pdf/2505.03981">paper</a>] [<a href="javascript:toggleDiv('2bib')">bibtex</a>]</span>
{: .publication data-selected="false"}







<div id="2bib" style="display: none" class="bib">
    @misc{xreasoner25,<br>
&nbsp;&nbsp;year&nbsp;=&nbsp;{2025},<br>
&nbsp;&nbsp;url&nbsp;=&nbsp;{http://arxiv.org/abs/2505.03981},<br>
&nbsp;&nbsp;author&nbsp;=&nbsp;{Liu,&nbsp;Qianchu&nbsp;and&nbsp;Zhang,&nbsp;Sheng&nbsp;and&nbsp;Qin,&nbsp;Guanghui&nbsp;and&nbsp;Ossowski,&nbsp;Timothy&nbsp;and&nbsp;Gu,&nbsp;Yu&nbsp;and&nbsp;Jin,&nbsp;Ying&nbsp;and&nbsp;Kiblawi,&nbsp;Sid&nbsp;and&nbsp;Preston,&nbsp;Sam&nbsp;and&nbsp;Wei,&nbsp;Mu&nbsp;and&nbsp;Vozila,&nbsp;Paul&nbsp;and&nbsp;Naumann,&nbsp;Tristan&nbsp;and&nbsp;Poon,&nbsp;Hoifung},<br>
&nbsp;&nbsp;title&nbsp;=&nbsp;{X-{{Reasoner}}:&nbsp;{{Towards&nbsp;Generalizable&nbsp;Reasoning&nbsp;Across&nbsp;Modalities}}&nbsp;and&nbsp;{{Domains}}}<br>
}<br>
<br>

    </div>



- [CLERC: A Dataset for Legal Case Retrieval and Retrieval-Augmented Analysis Generation](https://aclanthology.org/2025.findings-naacl.441/). Abe Bohan Hou, Orion Weller, **Guanghui Qin**, Eugene Yang, Dawn Lawrie, Nils Holzenberger, Andrew Blair-Stanek, and Benjamin Van Durme. In *Annual Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics (NAACL, findings)*, 2025. <span>[<a href="https://aclanthology.org/2025.findings-naacl.441/">paper</a>] [<a href="https://huggingface.co/datasets/jhu-clsp/CLERC">data</a>] [<a href="javascript:toggleDiv('3bib')">bibtex</a>]</span>
{: .publication data-selected="false"}







<div id="3bib" style="display: none" class="bib">
    @inproceedings{hou-etal-2025-clerc,<br>
&nbsp;&nbsp;title&nbsp;=&nbsp;"{CLERC}:&nbsp;A&nbsp;Dataset&nbsp;for&nbsp;{U}.&nbsp;{S}.&nbsp;Legal&nbsp;Case&nbsp;Retrieval&nbsp;and&nbsp;Retrieval-Augmented&nbsp;Analysis&nbsp;Generation",<br>
&nbsp;&nbsp;author&nbsp;=&nbsp;"Hou,&nbsp;Abe&nbsp;Bohan&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Weller,&nbsp;Orion&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Qin,&nbsp;Guanghui&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Yang,&nbsp;Eugene&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Lawrie,&nbsp;Dawn&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Holzenberger,&nbsp;Nils&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Blair-Stanek,&nbsp;Andrew&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Van&nbsp;Durme,&nbsp;Benjamin",<br>
&nbsp;&nbsp;booktitle&nbsp;=&nbsp;"Findings&nbsp;of&nbsp;the&nbsp;Association&nbsp;for&nbsp;Computational&nbsp;Linguistics:&nbsp;NAACL&nbsp;2025",<br>
&nbsp;&nbsp;year&nbsp;=&nbsp;"2025",<br>
&nbsp;&nbsp;url&nbsp;=&nbsp;"https://aclanthology.org/2025.findings-naacl.441/",<br>
&nbsp;&nbsp;pages&nbsp;=&nbsp;"7898--7913",<br>
}<br>

    </div>



- [Researchy Questions: A Dataset of Multi-Perspective, Decompositional Questions for LLM Web Agents](https://doi.org/10.48550/arXiv.2402.17896). Corby Rosset, Ho-Lam Chung, **Guanghui Qin**, Ehtan C Chau, Zhuo Feng, Ahmed Hassan Awadallah, Jennifer Neville, and Nikhil Rao. In *SIGIR*, 2025. <span>[<a href="https://doi.org/10.48550/arXiv.2402.17896">paper</a>] [<a href="https://huggingface.co/datasets/corbyrosset/researchy_questions">data</a>] [<a href="javascript:toggleDiv('4bib')">bibtex</a>]</span>
{: .publication data-selected="false"}







<div id="4bib" style="display: none" class="bib">
    @inproceedings{rosset2025researchy,<br>
&nbsp;&nbsp;&nbsp;&nbsp;title={Researchy&nbsp;Questions:&nbsp;A&nbsp;Dataset&nbsp;of&nbsp;Multi-Perspective,&nbsp;Decompositional&nbsp;Questions&nbsp;for&nbsp;LLM&nbsp;Web&nbsp;Agents},&nbsp;<br>
&nbsp;&nbsp;&nbsp;&nbsp;author={Corby&nbsp;Rosset&nbsp;and&nbsp;Ho-Lam&nbsp;Chung&nbsp;and&nbsp;Guanghui&nbsp;Qin&nbsp;and&nbsp;Ethan&nbsp;C.&nbsp;Chau&nbsp;and&nbsp;Zhuo&nbsp;Feng&nbsp;and&nbsp;Ahmed&nbsp;Awadallah&nbsp;and&nbsp;Jennifer&nbsp;Neville&nbsp;and&nbsp;Nikhil&nbsp;Rao},<br>
&nbsp;&nbsp;&nbsp;&nbsp;year={2025},<br>
&nbsp;&nbsp;&nbsp;&nbsp;booktitle={SIGIR},<br>
&nbsp;&nbsp;&nbsp;&nbsp;url="https://doi.org/10.48550/arXiv.2402.17896"<br>
}<br>

    </div>



- [KV-Distill: Nearly Lossless Learnable Context Compression for LLMs](https://arxiv.org/pdf/2503.10337). Vivek Chari, **Guanghui Qin**, and Benjamin Van Durme. In *arXiv: 2503.10337*, 2025. <span>[<a href="https://arxiv.org/pdf/2503.10337">paper</a>] [<a href="javascript:toggleDiv('5bib')">bibtex</a>]</span>
{: .publication data-selected="false"}







<div id="5bib" style="display: none" class="bib">
    @misc{chari2025kvdistillnearlylosslesslearnable,<br>
&nbsp;&nbsp;&nbsp;&nbsp;title={KV-Distill:&nbsp;Nearly&nbsp;Lossless&nbsp;Learnable&nbsp;Context&nbsp;Compression&nbsp;for&nbsp;LLMs},<br>
&nbsp;&nbsp;&nbsp;&nbsp;author={Vivek&nbsp;Chari&nbsp;and&nbsp;Guanghui&nbsp;Qin&nbsp;and&nbsp;Benjamin&nbsp;Van&nbsp;Durme},<br>
&nbsp;&nbsp;&nbsp;&nbsp;year={2025},<br>
&nbsp;&nbsp;&nbsp;&nbsp;eprint={2503.10337},<br>
&nbsp;&nbsp;&nbsp;&nbsp;archivePrefix={arXiv},<br>
&nbsp;&nbsp;&nbsp;&nbsp;primaryClass={cs.CL},<br>
&nbsp;&nbsp;&nbsp;&nbsp;url={https://arxiv.org/abs/2503.10337},<br>
}<br>
<br>

    </div>



- [Dodo: Dynamic Contextual Compression for Decoder-only LMs](https://aclanthology.org/2024.acl-long.536/). **Guanghui Qin**, Corby Rosset, Ethan C Chau, Nikhil Rao, and Benjamin Van Durme. In *Annual Meeting of the Association for Computational Linguistics (ACL, oral)*, 2024. <span>[<a href="https://aclanthology.org/2024.acl-long.536/">paper</a>] [<a href="https://twitter.com/hiaoxui/status/1711858430510502369">twitter</a>] [<a href="javascript:toggleDiv('6bib')">bibtex</a>]</span>
{: .publication .selected}







<div id="6bib" style="display: none" class="bib">
    @inproceedings{qin-etal-2024-dodo,<br>
&nbsp;&nbsp;title&nbsp;=&nbsp;"Dodo:&nbsp;Dynamic&nbsp;Contextual&nbsp;Compression&nbsp;for&nbsp;Decoder-only&nbsp;{LM}s",<br>
&nbsp;&nbsp;author&nbsp;=&nbsp;"Qin,&nbsp;Guanghui&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Rosset,&nbsp;Corby&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Chau,&nbsp;Ethan&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Rao,&nbsp;Nikhil&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Van&nbsp;Durme,&nbsp;Benjamin",<br>
&nbsp;&nbsp;booktitle&nbsp;=&nbsp;"Proceedings&nbsp;of&nbsp;the&nbsp;62nd&nbsp;Annual&nbsp;Meeting&nbsp;of&nbsp;the&nbsp;Association&nbsp;for&nbsp;Computational&nbsp;Linguistics&nbsp;(Volume&nbsp;1:&nbsp;Long&nbsp;Papers)",<br>
&nbsp;&nbsp;year&nbsp;=&nbsp;"2024",<br>
&nbsp;&nbsp;url&nbsp;=&nbsp;"https://aclanthology.org/2024.acl-long.536",<br>
&nbsp;&nbsp;pages&nbsp;=&nbsp;"9961--9975",<br>
}<br>

    </div>



- [Ras suppression potentiates rear actomyosin contractility-driven cell polarization and migration](https://www.nature.com/articles/s41556-024-01453-4). Yiyan Lin, Dhiman Sankar Pal, Parijat Banerjee, Tatsat Banerjee, **Guanghui Qin**, Yu Deng, Jane Borleis, Pablo A Iglesias, and Peter N Devreotes. In *Nature Cell Biology*, 2024. <span>[<a href="https://www.nature.com/articles/s41556-024-01453-4">paper</a>] [<a href="https://www.biorxiv.org/content/10.1101/2023.08.30.555648">biorxiv</a>] [<a href="javascript:toggleDiv('7bib')">bibtex</a>]</span>
{: .publication .selected}







<div id="7bib" style="display: none" class="bib">
    @article&nbsp;{lin2024ras,<br>
&nbsp;&nbsp;author&nbsp;=&nbsp;{Lin,&nbsp;Yiyan&nbsp;and&nbsp;Pal,&nbsp;Dhiman&nbsp;Sankar&nbsp;and&nbsp;Banerjee,&nbsp;Parijat&nbsp;and&nbsp;Banerjee,&nbsp;Tatsat&nbsp;and&nbsp;Qin,&nbsp;Guanghui&nbsp;and&nbsp;Deng,&nbsp;Yu&nbsp;and&nbsp;Borleis,&nbsp;Jane&nbsp;and&nbsp;Iglesias,&nbsp;Pablo&nbsp;A.&nbsp;and&nbsp;Devreotes,&nbsp;Peter&nbsp;N.},<br>
&nbsp;&nbsp;title&nbsp;=&nbsp;{Ras&nbsp;suppression&nbsp;potentiates&nbsp;rear&nbsp;actomyosin&nbsp;contractility-driven&nbsp;cell&nbsp;polarization&nbsp;and&nbsp;migration},<br>
&nbsp;&nbsp;year&nbsp;=&nbsp;{2024},<br>
&nbsp;&nbsp;URL&nbsp;=&nbsp;{https://www.nature.com/articles/s41556-024-01453-4},<br>
&nbsp;&nbsp;issue&nbsp;=&nbsp;{7},<br>
&nbsp;&nbsp;volumn&nbsp;=&nbsp;{26},<br>
&nbsp;&nbsp;pages&nbsp;=&nbsp;{1062--1076},<br>
&nbsp;&nbsp;journal&nbsp;=&nbsp;{Nature&nbsp;Cell&nbsp;Biology}<br>
}<br>

    </div>



- [Towards Efficient Long-Context Natural Language Processing](https://jscholarship.library.jhu.edu/items/68c24613-c500-4255-a15c-39d3dabbcee1). **Guanghui Qin**. In *Johns Hopkins University Library (thesis)*, 2024. <span>[<a href="https://jscholarship.library.jhu.edu/items/68c24613-c500-4255-a15c-39d3dabbcee1">paper</a>] [<a href="javascript:toggleDiv('8bib')">bibtex</a>]</span>
{: .publication data-selected="false"}







<div id="8bib" style="display: none" class="bib">
    @thesis{thesis24,<br>
&nbsp;&nbsp;year&nbsp;=&nbsp;{2024},<br>
&nbsp;&nbsp;url&nbsp;=&nbsp;{https://jscholarship.library.jhu.edu/items/68c24613-c500-4255-a15c-39d3dabbcee1},<br>
&nbsp;&nbsp;author&nbsp;=&nbsp;{Qin,&nbsp;Guanghui},<br>
&nbsp;&nbsp;type&nbsp;=&nbsp;{phdthesis},<br>
&nbsp;&nbsp;title&nbsp;=&nbsp;{Towards&nbsp;{{Efficient&nbsp;Long-Context&nbsp;Natural&nbsp;Language&nbsp;Processing}}},<br>
&nbsp;&nbsp;institution&nbsp;=&nbsp;{Johns&nbsp;Hopkins&nbsp;University}<br>
}<br>

    </div>



- [Streaming Sequence Transduction through Dynamic Compression](https://doi.org/10.48550/arXiv.2402.01172). Weiting Tan, Yunmo Chen, Tongfei Chen, **Guanghui Qin**, Haoran Xu, Heidi C Zhang, Benjamin Van Durme, and Philipp Koehn. In *arXiv: 2402.01172*, 2024. <span>[<a href="https://doi.org/10.48550/arXiv.2402.01172">paper</a>] [<a href="javascript:toggleDiv('9bib')">bibtex</a>]</span>
{: .publication data-selected="false"}







<div id="9bib" style="display: none" class="bib">
    @misc{tan2024streaming,<br>
&nbsp;&nbsp;&nbsp;&nbsp;title={Streaming&nbsp;Sequence&nbsp;Transduction&nbsp;through&nbsp;Dynamic&nbsp;Compression},&nbsp;<br>
&nbsp;&nbsp;&nbsp;&nbsp;author={Weiting&nbsp;Tan&nbsp;and&nbsp;Yunmo&nbsp;Chen&nbsp;and&nbsp;Tongfei&nbsp;Chen&nbsp;and&nbsp;Guanghui&nbsp;Qin&nbsp;and&nbsp;Haoran&nbsp;Xu&nbsp;and&nbsp;Heidi&nbsp;C.&nbsp;Zhang&nbsp;and&nbsp;Benjamin&nbsp;Van&nbsp;Durme&nbsp;and&nbsp;Philipp&nbsp;Koehn},<br>
&nbsp;&nbsp;&nbsp;&nbsp;year={2024},<br>
&nbsp;&nbsp;&nbsp;&nbsp;eprint={2402.01172},<br>
&nbsp;&nbsp;&nbsp;&nbsp;archivePrefix={arXiv},<br>
&nbsp;&nbsp;&nbsp;&nbsp;primaryClass={cs.CL}<br>
}<br>

    </div>



- [Nugget: Neural Agglomerative Embeddings of Text](https://proceedings.mlr.press/v202/qin23a/qin23a.pdf). **Guanghui Qin** and Benjamin Van Durme. In *International Conference on Machine Learning (ICML)*, 2023. <span>[<a href="https://proceedings.mlr.press/v202/qin23a/qin23a.pdf">paper</a>] [<a href="https://github.com/hiaoxui/nugget-data">data</a>] [<a href="/files/23papers/nugget_poster.pdf">poster</a>] [<a href="/files/23papers/nugget_slides.pptx">slides</a>] [<a href="https://twitter.com/hiaoxui/status/1711858430510502369">twitter</a>] [<a href="javascript:toggleDiv('10bib')">bibtex</a>]</span>
{: .publication .selected}







<div id="10bib" style="display: none" class="bib">
    @InProceedings{pmlr-v202-qin23a,<br>
&nbsp;&nbsp;title&nbsp;=&nbsp;{Nugget:&nbsp;Neural&nbsp;Agglomerative&nbsp;Embeddings&nbsp;of&nbsp;Text},<br>
&nbsp;&nbsp;author&nbsp;=&nbsp;{Qin,&nbsp;Guanghui&nbsp;and&nbsp;Van&nbsp;Durme,&nbsp;Benjamin},<br>
&nbsp;&nbsp;booktitle&nbsp;=&nbsp;{Proceedings&nbsp;of&nbsp;the&nbsp;40th&nbsp;International&nbsp;Conference&nbsp;on&nbsp;Machine&nbsp;Learning},<br>
&nbsp;&nbsp;pages&nbsp;=&nbsp;{28337--28350},<br>
&nbsp;&nbsp;year&nbsp;=&nbsp;{2023},<br>
&nbsp;&nbsp;editor&nbsp;=&nbsp;{Krause,&nbsp;Andreas&nbsp;and&nbsp;Brunskill,&nbsp;Emma&nbsp;and&nbsp;Cho,&nbsp;Kyunghyun&nbsp;and&nbsp;Engelhardt,&nbsp;Barbara&nbsp;and&nbsp;Sabato,&nbsp;Sivan&nbsp;and&nbsp;Scarlett,&nbsp;Jonathan},<br>
&nbsp;&nbsp;volume&nbsp;=&nbsp;{202},<br>
&nbsp;&nbsp;series&nbsp;=&nbsp;{Proceedings&nbsp;of&nbsp;Machine&nbsp;Learning&nbsp;Research},<br>
&nbsp;&nbsp;publisher&nbsp;=&nbsp;{PMLR},<br>
&nbsp;&nbsp;url&nbsp;=&nbsp;{https://proceedings.mlr.press/v202/qin23a.html},<br>
}<br>

    </div>



- [The NLP Task Effectiveness of Long-Range Transformers](https://aclanthology.org/2023.eacl-main.273.pdf). **Guanghui Qin**, Yukun Feng, and Benjamin Van Durme. In *Annual Conference of the European Chapter of the Association for Computational Linguistics (EACL, oral)*, 2023. <span>[<a href="https://aclanthology.org/2023.eacl-main.273.pdf">paper</a>] [<a href="https://github.com/hiaoxui/long-range-transformers">code</a>] [<a href="/files/23papers/lrt_slides.pptx">slides</a>] [<a href="/files/23papers/lrt_poster.pdf">poster</a>] [<a href="https://aclanthology.org/2023.eacl-main.273.mp4">video</a>] [<a href="javascript:toggleDiv('11bib')">bibtex</a>]</span>
{: .publication .selected}







<div id="11bib" style="display: none" class="bib">
    @inproceedings{qin-etal-2023-nlp,<br>
&nbsp;&nbsp;title&nbsp;=&nbsp;"The&nbsp;{NLP}&nbsp;Task&nbsp;Effectiveness&nbsp;of&nbsp;Long-Range&nbsp;Transformers",<br>
&nbsp;&nbsp;author&nbsp;=&nbsp;"Qin,&nbsp;Guanghui&nbsp;&nbsp;and&nbsp;Feng,&nbsp;Yukun&nbsp;&nbsp;and&nbsp;Van&nbsp;Durme,&nbsp;Benjamin",<br>
&nbsp;&nbsp;booktitle&nbsp;=&nbsp;"Proceedings&nbsp;of&nbsp;the&nbsp;17th&nbsp;Conference&nbsp;of&nbsp;the&nbsp;European&nbsp;Chapter&nbsp;of&nbsp;the&nbsp;Association&nbsp;for&nbsp;Computational&nbsp;Linguistics",<br>
&nbsp;&nbsp;year&nbsp;=&nbsp;"2023",<br>
&nbsp;&nbsp;address&nbsp;=&nbsp;"Dubrovnik,&nbsp;Croatia",<br>
&nbsp;&nbsp;publisher&nbsp;=&nbsp;"Association&nbsp;for&nbsp;Computational&nbsp;Linguistics",<br>
&nbsp;&nbsp;url&nbsp;=&nbsp;"https://aclanthology.org/2023.eacl-main.273",<br>
&nbsp;&nbsp;doi&nbsp;=&nbsp;"10.18653/v1/2023.eacl-main.273",<br>
&nbsp;&nbsp;pages&nbsp;=&nbsp;"3774--3790",<br>
}<br>

    </div>



- [Learning How to Ask: Querying LMs with Mixtures of Soft Prompts](https://dx.doi.org/10.18653/v1/2021.naacl-main.410). **Guanghui Qin** and Jason Eisner. In *Annual Conference of the North American Chapter of the Association for Computational Linguistics (NAACL, short)*, 2021. <span style="color:red">**Best Short Paper**</span>.<span>[<a href="https://dx.doi.org/10.18653/v1/2021.naacl-main.410">paper</a>] [<a href="/files/21papers/prompt_poster.pdf">poster</a>] [<a href="/files/21papers/prompt_slides.pptx">slides</a>] [<a href="https://github.com/hiaoxui/soft-prompts">code</a>] [<a href="https://twitter.com/adveisner/status/1402681187018084354?lang=en">twitter</a>] [<a href="javascript:toggleDiv('12bib')">bibtex</a>]</span>
{: .publication .selected}







<div id="12bib" style="display: none" class="bib">
    @inproceedings{qin-eisner-2021-learning,<br>
&nbsp;&nbsp;title&nbsp;=&nbsp;"Learning&nbsp;How&nbsp;to&nbsp;Ask:&nbsp;Querying&nbsp;{LM}s&nbsp;with&nbsp;Mixtures&nbsp;of&nbsp;Soft&nbsp;Prompts",<br>
&nbsp;&nbsp;author&nbsp;=&nbsp;"Qin,&nbsp;Guanghui&nbsp;and&nbsp;Eisner,&nbsp;Jason",<br>
&nbsp;&nbsp;booktitle&nbsp;=&nbsp;"Proceedings&nbsp;of&nbsp;the&nbsp;2021&nbsp;Conference&nbsp;of&nbsp;the&nbsp;North&nbsp;American&nbsp;Chapter&nbsp;of&nbsp;the&nbsp;Association&nbsp;for&nbsp;Computational&nbsp;Linguistics:&nbsp;Human&nbsp;Language&nbsp;Technologies",<br>
&nbsp;&nbsp;year&nbsp;=&nbsp;"2021",<br>
&nbsp;&nbsp;address&nbsp;=&nbsp;"Online",<br>
&nbsp;&nbsp;publisher&nbsp;=&nbsp;"Association&nbsp;for&nbsp;Computational&nbsp;Linguistics",<br>
&nbsp;&nbsp;url&nbsp;=&nbsp;"https://dx.doi.org/10.18653/v1/2021.naacl-main.410",<br>
&nbsp;&nbsp;doi&nbsp;=&nbsp;"10.18653/v1/2021.naacl-main.410",<br>
&nbsp;&nbsp;pages&nbsp;=&nbsp;"5203--5212",<br>
}<br>

    </div>



- [LOME: Large Ontology Multilingual Extraction](https://dx.doi.org/10.18653/v1/2021.eacl-demos.19). Patrick Xia\*, **Guanghui Qin**\*, Siddharth Vashishtha, Yunmo Chen, Tongfei Chen, Chandler May, Craig Harman, Kyle Rawlins, Aaron Steven White, and Benjamin Van Durme. In *Annual Conference of the European Chapter of the Association for Computational Linguistics (EACL, demo)*, 2021. <span>[<a href="https://dx.doi.org/10.18653/v1/2021.eacl-demos.19">paper</a>] [<a href="https://nlp.jhu.edu/demos/lome/">demo</a>] [<a href="https://github.com/hiaoxui/span-finder">code</a>] [<a href="https://hub.docker.com/r/hltcoe/lome">docker</a>] [<a href="https://www.youtube.com/watch?v=o4KsGdnV6BE&list=LL&index=13">video</a>] [<a href="javascript:toggleDiv('13bib')">bibtex</a>]</span>
{: .publication .selected}







<div id="13bib" style="display: none" class="bib">
    @inproceedings{xia-etal-2021-lome,<br>
&nbsp;&nbsp;title&nbsp;=&nbsp;"{LOME}:&nbsp;Large&nbsp;Ontology&nbsp;Multilingual&nbsp;Extraction",<br>
&nbsp;&nbsp;author&nbsp;=&nbsp;"Xia,&nbsp;Patrick&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Qin,&nbsp;Guanghui&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Vashishtha,&nbsp;Siddharth&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Chen,&nbsp;Yunmo&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Chen,&nbsp;Tongfei&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;May,&nbsp;Chandler&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Harman,&nbsp;Craig&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Rawlins,&nbsp;Kyle&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;White,&nbsp;Aaron&nbsp;Steven&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Van&nbsp;Durme,&nbsp;Benjamin",<br>
&nbsp;&nbsp;booktitle&nbsp;=&nbsp;"Proceedings&nbsp;of&nbsp;the&nbsp;16th&nbsp;Conference&nbsp;of&nbsp;the&nbsp;European&nbsp;Chapter&nbsp;of&nbsp;the&nbsp;Association&nbsp;for&nbsp;Computational&nbsp;Linguistics:&nbsp;System&nbsp;Demonstrations",<br>
&nbsp;&nbsp;month&nbsp;=&nbsp;apr,<br>
&nbsp;&nbsp;year&nbsp;=&nbsp;"2021",<br>
&nbsp;&nbsp;address&nbsp;=&nbsp;"Online",<br>
&nbsp;&nbsp;publisher&nbsp;=&nbsp;"Association&nbsp;for&nbsp;Computational&nbsp;Linguistics",<br>
&nbsp;&nbsp;url&nbsp;=&nbsp;"https://dx.doi.org/10.18653/v1/2021.eacl-demos.19",<br>
&nbsp;&nbsp;doi&nbsp;=&nbsp;"10.18653/v1/2021.eacl-demos.19",<br>
&nbsp;&nbsp;pages&nbsp;=&nbsp;"149--159",<br>
}<br>

    </div>



- [Iterative Paraphrastic Augmentation with Discriminative Span Alignment](https://doi.org/10.1162/tacl_a_00380). Ryan Culkin, J Edward Hu, Elias Stengel-Eskin, **Guanghui Qin**, and Benjamin Van Durme. In *Transactions of the Association for Computational Linguistics (TACL)*, 2021. <span>[<a href="https://doi.org/10.1162/tacl_a_00380">paper</a>] [<a href="javascript:toggleDiv('14bib')">bibtex</a>]</span>
{: .publication data-selected="false"}







<div id="14bib" style="display: none" class="bib">
    @article{10.1162/tacl_a_00380,<br>
&nbsp;&nbsp;author&nbsp;=&nbsp;{Culkin,&nbsp;Ryan&nbsp;and&nbsp;Hu,&nbsp;J.&nbsp;Edward&nbsp;and&nbsp;Stengel-Eskin,&nbsp;Elias&nbsp;and&nbsp;Qin,&nbsp;Guanghui&nbsp;and&nbsp;Durme,&nbsp;Benjamin&nbsp;Van},<br>
&nbsp;&nbsp;title&nbsp;=&nbsp;"{Iterative&nbsp;Paraphrastic&nbsp;Augmentation&nbsp;with&nbsp;Discriminative&nbsp;Span&nbsp;Alignment}",<br>
&nbsp;&nbsp;journal&nbsp;=&nbsp;{Transactions&nbsp;of&nbsp;the&nbsp;Association&nbsp;for&nbsp;Computational&nbsp;Linguistics},<br>
&nbsp;&nbsp;volume&nbsp;=&nbsp;{9},<br>
&nbsp;&nbsp;pages&nbsp;=&nbsp;{494-509},<br>
&nbsp;&nbsp;year&nbsp;=&nbsp;{2021},<br>
&nbsp;&nbsp;month&nbsp;=&nbsp;{05},<br>
&nbsp;&nbsp;issn&nbsp;=&nbsp;{2307-387X},<br>
&nbsp;&nbsp;doi&nbsp;=&nbsp;{10.1162/tacl_a_00380},<br>
&nbsp;&nbsp;url&nbsp;=&nbsp;{https://doi.org/10.1162/tacl\_a\_00380},<br>
&nbsp;&nbsp;eprint&nbsp;=&nbsp;{https://direct.mit.edu/tacl/article-pdf/doi/10.1162/tacl\_a\_00380/1924197/tacl\_a\_00380.pdf},<br>
}<br>

    </div>



- [Everything Is All It Takes: A Multipronged Strategy for Zero-Shot Cross-Lingual Information Extraction](https://dx.doi.org/10.18653/v1/2021.emnlp-main.149). Mahsa Yarmohammadi, Shijie Wu, Marc Marone, Haoran Xu, Seth Ebner, **Guanghui Qin**, Yunmo Chen, Jialiang Guo, Craig Harman, Kenon Murray, Aaron Steven White, Mark Dredze, and Benjamin Van Durme. In *Conference on Empirical Methods in Natural Language Processing (EMNLP, oral)*, 2021. <span>[<a href="https://dx.doi.org/10.18653/v1/2021.emnlp-main.149">paper</a>] [<a href="https://aclanthology.org/2021.emnlp-main.149.mp4">video</a>] [<a href="https://github.com/shijie-wu/crosslingual-nlp">code</a>] [<a href="javascript:toggleDiv('15bib')">bibtex</a>]</span>
{: .publication data-selected="false"}







<div id="15bib" style="display: none" class="bib">
    @inproceedings{yarmohammadi-etal-2021-everything,<br>
&nbsp;&nbsp;title&nbsp;=&nbsp;"Everything&nbsp;Is&nbsp;All&nbsp;It&nbsp;Takes:&nbsp;A&nbsp;Multipronged&nbsp;Strategy&nbsp;for&nbsp;Zero-Shot&nbsp;Cross-Lingual&nbsp;Information&nbsp;Extraction",<br>
&nbsp;&nbsp;author&nbsp;=&nbsp;"Yarmohammadi,&nbsp;Mahsa&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Wu,&nbsp;Shijie&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Marone,&nbsp;Marc&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Xu,&nbsp;Haoran&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Ebner,&nbsp;Seth&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Qin,&nbsp;Guanghui&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Chen,&nbsp;Yunmo&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Guo,&nbsp;Jialiang&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Harman,&nbsp;Craig&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Murray,&nbsp;Kenton&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;White,&nbsp;Aaron&nbsp;Steven&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Dredze,&nbsp;Mark&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Van&nbsp;Durme,&nbsp;Benjamin",<br>
&nbsp;&nbsp;booktitle&nbsp;=&nbsp;"Proceedings&nbsp;of&nbsp;the&nbsp;2021&nbsp;Conference&nbsp;on&nbsp;Empirical&nbsp;Methods&nbsp;in&nbsp;Natural&nbsp;Language&nbsp;Processing",<br>
&nbsp;&nbsp;month&nbsp;=&nbsp;nov,<br>
&nbsp;&nbsp;year&nbsp;=&nbsp;"2021",<br>
&nbsp;&nbsp;address&nbsp;=&nbsp;"Online&nbsp;and&nbsp;Punta&nbsp;Cana,&nbsp;Dominican&nbsp;Republic",<br>
&nbsp;&nbsp;publisher&nbsp;=&nbsp;"Association&nbsp;for&nbsp;Computational&nbsp;Linguistics",<br>
&nbsp;&nbsp;url&nbsp;=&nbsp;"https://dx.doi.org/10.18653/v1/2021.emnlp-main.149",<br>
&nbsp;&nbsp;doi&nbsp;=&nbsp;"10.18653/v1/2021.emnlp-main.149",<br>
&nbsp;&nbsp;pages&nbsp;=&nbsp;"1950--1967",<br>
}<br>

    </div>



- [Neural Datalog through Time: Informed Temporal Modeling via Logical Specification](https://proceedings.mlr.press/v119/mei20a/mei20a.pdf). Hongyuan Mei, **Guanghui Qin**, Minjie Xu, and Jason Eisner. In *International Conference on Machine Learning (ICML, oral)*, 2020. <span>[<a href="https://proceedings.mlr.press/v119/mei20a/mei20a.pdf">paper</a>] [<a href="https://www.bloomberg.com/company/stories/icml-2020-bloomberg-ph-d-fellow-combines-datalog-and-neural-networks-to-model-dynamic-databases/">blog</a>] [<a href="/files/20papers/datalog_slides.pptx">slides</a>] [<a href="https://github.com/hongyuanmei/neural-datalog-through-time">code</a>] [<a href="https://www.cs.jhu.edu/~hmei/papers/mei+qin+xu+eisner.icml20.mp4">video</a>] [<a href="https://fortune.com/2020/09/08/disco-bell-bottoms-big-hair-and-cutting-edge-a-i/">press</a>] [<a href="javascript:toggleDiv('16bib')">bibtex</a>]</span>
{: .publication .selected}







<div id="16bib" style="display: none" class="bib">
    @InProceedings{pmlr-v119-mei20a,<br>
&nbsp;&nbsp;title&nbsp;=&nbsp;{Neural&nbsp;Datalog&nbsp;Through&nbsp;Time:&nbsp;Informed&nbsp;Temporal&nbsp;Modeling&nbsp;via&nbsp;Logical&nbsp;Specification},<br>
&nbsp;&nbsp;author&nbsp;=&nbsp;{Mei,&nbsp;Hongyuan&nbsp;and&nbsp;Qin,&nbsp;Guanghui&nbsp;and&nbsp;Xu,&nbsp;Minjie&nbsp;and&nbsp;Eisner,&nbsp;Jason},<br>
&nbsp;&nbsp;booktitle&nbsp;=&nbsp;{Proceedings&nbsp;of&nbsp;the&nbsp;37th&nbsp;International&nbsp;Conference&nbsp;on&nbsp;Machine&nbsp;Learning},<br>
&nbsp;&nbsp;pages&nbsp;=&nbsp;{6808--6819},<br>
&nbsp;&nbsp;year&nbsp;=&nbsp;{2020},<br>
&nbsp;&nbsp;editor&nbsp;=&nbsp;{III,&nbsp;Hal&nbsp;Daumé&nbsp;and&nbsp;Singh,&nbsp;Aarti},<br>
&nbsp;&nbsp;volume&nbsp;=&nbsp;{119},<br>
&nbsp;&nbsp;series&nbsp;=&nbsp;{Proceedings&nbsp;of&nbsp;Machine&nbsp;Learning&nbsp;Research},<br>
&nbsp;&nbsp;month&nbsp;=&nbsp;{13--18&nbsp;Jul},<br>
&nbsp;&nbsp;publisher&nbsp;=&nbsp;{PMLR},<br>
&nbsp;&nbsp;pdf&nbsp;=&nbsp;{https://proceedings.mlr.press/v119/mei20a/mei20a.pdf},<br>
&nbsp;&nbsp;url&nbsp;=&nbsp;{https://proceedings.mlr.press/v119/mei20a.html},<br>
}<br>

    </div>



- [CopyNext: Explicit Span Copying and Alignment in Sequence to Sequence Models](https://aclanthology.org/2020.spnlp-1.2.pdf). Abhinav Singh, Patrick Xia, **Guanghui Qin**, Mahsa Yarmohammadi, and Benjamin Van Durme. In *Fourth Workshop on Structured Prediction for NLP*, 2020. <span>[<a href="https://aclanthology.org/2020.spnlp-1.2.pdf">paper</a>] [<a href="https://slideslive.com/38940142/copynext-explicit-span-copying-and-alignment-in-sequence-to-sequence-model">video</a>] [<a href="https://github.com/abhinonymous/copynext">code</a>] [<a href="javascript:toggleDiv('17bib')">bibtex</a>]</span>
{: .publication data-selected="false"}







<div id="17bib" style="display: none" class="bib">
    @inproceedings{singh-etal-2020-copynext,<br>
&nbsp;&nbsp;title&nbsp;=&nbsp;"{C}opy{N}ext:&nbsp;Explicit&nbsp;Span&nbsp;Copying&nbsp;and&nbsp;Alignment&nbsp;in&nbsp;Sequence&nbsp;to&nbsp;Sequence&nbsp;Models",<br>
&nbsp;&nbsp;author&nbsp;=&nbsp;"Singh,&nbsp;Abhinav&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Xia,&nbsp;Patrick&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Qin,&nbsp;Guanghui&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Yarmohammadi,&nbsp;Mahsa&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Van&nbsp;Durme,&nbsp;Benjamin",<br>
&nbsp;&nbsp;booktitle&nbsp;=&nbsp;"Proceedings&nbsp;of&nbsp;the&nbsp;Fourth&nbsp;Workshop&nbsp;on&nbsp;Structured&nbsp;Prediction&nbsp;for&nbsp;NLP",<br>
&nbsp;&nbsp;month&nbsp;=&nbsp;nov,<br>
&nbsp;&nbsp;year&nbsp;=&nbsp;"2020",<br>
&nbsp;&nbsp;address&nbsp;=&nbsp;"Online",<br>
&nbsp;&nbsp;publisher&nbsp;=&nbsp;"Association&nbsp;for&nbsp;Computational&nbsp;Linguistics",<br>
&nbsp;&nbsp;url&nbsp;=&nbsp;"https://aclanthology.org/2020.spnlp-1.2.pdf",<br>
&nbsp;&nbsp;doi&nbsp;=&nbsp;"10.18653/v1/2020.spnlp-1.2",<br>
&nbsp;&nbsp;pages&nbsp;=&nbsp;"11--16",<br>
}<br>

    </div>



- [Imputing Missing Events in Continuous-Time Event Streams](https://proceedings.mlr.press/v97/mei19a/mei19a.pdf). Hongyuan Mei, **Guanghui Qin**, and Jason Eisner. In *International Conference on Machine Learning (ICML, oral)*, 2019. <span>[<a href="https://proceedings.mlr.press/v97/mei19a/mei19a.pdf">paper</a>] [<a href="https://github.com/hongyuanmei/neural-hawkes-particle-smoothing">code</a>] [<a href="/files/19papers/smoothing_poster.pdf">poster</a>] [<a href="/files/19papers/smoothing_slides.pdf">slides</a>] [<a href="javascript:toggleDiv('18bib')">bibtex</a>]</span>
{: .publication .selected}







<div id="18bib" style="display: none" class="bib">
    @InProceedings{pmlr-v97-mei19a,<br>
&nbsp;&nbsp;title&nbsp;=&nbsp;{Imputing&nbsp;Missing&nbsp;Events&nbsp;in&nbsp;Continuous-Time&nbsp;Event&nbsp;Streams},<br>
&nbsp;&nbsp;author&nbsp;=&nbsp;{Mei,&nbsp;Hongyuan&nbsp;and&nbsp;Qin,&nbsp;Guanghui&nbsp;and&nbsp;Eisner,&nbsp;Jason},<br>
&nbsp;&nbsp;booktitle&nbsp;=&nbsp;{Proceedings&nbsp;of&nbsp;the&nbsp;36th&nbsp;International&nbsp;Conference&nbsp;on&nbsp;Machine&nbsp;Learning},<br>
&nbsp;&nbsp;pages&nbsp;=&nbsp;{4475--4485},<br>
&nbsp;&nbsp;year&nbsp;=&nbsp;{2019},<br>
&nbsp;&nbsp;editor&nbsp;=&nbsp;{Chaudhuri,&nbsp;Kamalika&nbsp;and&nbsp;Salakhutdinov,&nbsp;Ruslan},<br>
&nbsp;&nbsp;volume&nbsp;=&nbsp;{97},<br>
&nbsp;&nbsp;series&nbsp;=&nbsp;{Proceedings&nbsp;of&nbsp;Machine&nbsp;Learning&nbsp;Research},<br>
&nbsp;&nbsp;publisher&nbsp;=&nbsp;{PMLR},<br>
&nbsp;&nbsp;url&nbsp;=&nbsp;{https://proceedings.mlr.press/v97/mei19a.html},<br>
}<br>

    </div>



- [Learning Latent Semantic Annotations for Grounding Natural Language to Structured Data](https://dx.doi.org/10.18653/v1/D18-1411). **Guanghui Qin**, Jin-Ge Yao, Xuening Wang, Jinpeng Wang, and Chin-Yew Lin. In *Conference on Empirical Methods in Natural Language Processing (EMNLP, oral)*, 2018. <span>[<a href="https://dx.doi.org/10.18653/v1/D18-1411">paper</a>] [<a href="https://github.com/hiaoxui/D2T-Grounding">code</a>] [<a href="/files/18papers/d2t_slides.pptx">slides</a>] [<a href="https://vimeo.com/306117499">video</a>] [<a href="javascript:toggleDiv('19bib')">bibtex</a>]</span>
{: .publication .selected}







<div id="19bib" style="display: none" class="bib">
    @inproceedings{qin-etal-2018-learning,<br>
&nbsp;&nbsp;title&nbsp;=&nbsp;"Learning&nbsp;Latent&nbsp;Semantic&nbsp;Annotations&nbsp;for&nbsp;Grounding&nbsp;Natural&nbsp;Language&nbsp;to&nbsp;Structured&nbsp;Data",<br>
&nbsp;&nbsp;author&nbsp;=&nbsp;"Qin,&nbsp;Guanghui&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Yao,&nbsp;Jin-Ge&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Wang,&nbsp;Xuening&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Wang,&nbsp;Jinpeng&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Lin,&nbsp;Chin-Yew",<br>
&nbsp;&nbsp;booktitle&nbsp;=&nbsp;"Proceedings&nbsp;of&nbsp;the&nbsp;2018&nbsp;Conference&nbsp;on&nbsp;Empirical&nbsp;Methods&nbsp;in&nbsp;Natural&nbsp;Language&nbsp;Processing",<br>
&nbsp;&nbsp;month&nbsp;=&nbsp;oct&nbsp;#&nbsp;"-"&nbsp;#&nbsp;nov,<br>
&nbsp;&nbsp;year&nbsp;=&nbsp;"2018",<br>
&nbsp;&nbsp;address&nbsp;=&nbsp;"Brussels,&nbsp;Belgium",<br>
&nbsp;&nbsp;publisher&nbsp;=&nbsp;"Association&nbsp;for&nbsp;Computational&nbsp;Linguistics",<br>
&nbsp;&nbsp;url&nbsp;=&nbsp;"https://dx.doi.org/10.18653/v1/D18-1411",<br>
&nbsp;&nbsp;doi&nbsp;=&nbsp;"10.18653/v1/D18-1411",<br>
&nbsp;&nbsp;pages&nbsp;=&nbsp;"3761--3771",<br>
}<br>

    </div>



- [Data2Text Studio: Automated Text Generation from Structured Data](https://dx.doi.org/10.18653/v1/D18-2003). Longxu Dou, **Guanghui Qin**, Jinpeng Wang, Jin-Ge Yao, and Chin-Yew Lin. In *Conference on Empirical Methods in Natural Language Processing (EMNLP, demo)*, 2018. <span>[<a href="https://dx.doi.org/10.18653/v1/D18-2003">paper</a>] [<a href="javascript:toggleDiv('20bib')">bibtex</a>]</span>
{: .publication data-selected="false"}







<div id="20bib" style="display: none" class="bib">
    @inproceedings{dou-etal-2018-data2text,<br>
&nbsp;&nbsp;title&nbsp;=&nbsp;"{D}ata2{T}ext&nbsp;Studio:&nbsp;Automated&nbsp;Text&nbsp;Generation&nbsp;from&nbsp;Structured&nbsp;Data",<br>
&nbsp;&nbsp;author&nbsp;=&nbsp;"Dou,&nbsp;Longxu&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Qin,&nbsp;Guanghui&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Wang,&nbsp;Jinpeng&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Yao,&nbsp;Jin-Ge&nbsp;&nbsp;and<br>
&nbsp;&nbsp;&nbsp;&nbsp;Lin,&nbsp;Chin-Yew",<br>
&nbsp;&nbsp;booktitle&nbsp;=&nbsp;"Proceedings&nbsp;of&nbsp;the&nbsp;2018&nbsp;Conference&nbsp;on&nbsp;Empirical&nbsp;Methods&nbsp;in&nbsp;Natural&nbsp;Language&nbsp;Processing:&nbsp;System&nbsp;Demonstrations",<br>
&nbsp;&nbsp;month&nbsp;=&nbsp;nov,<br>
&nbsp;&nbsp;year&nbsp;=&nbsp;"2018",<br>
&nbsp;&nbsp;address&nbsp;=&nbsp;"Brussels,&nbsp;Belgium",<br>
&nbsp;&nbsp;publisher&nbsp;=&nbsp;"Association&nbsp;for&nbsp;Computational&nbsp;Linguistics",<br>
&nbsp;&nbsp;url&nbsp;=&nbsp;"https://dx.doi.org/10.18653/v1/D18-2003",<br>
&nbsp;&nbsp;doi&nbsp;=&nbsp;"10.18653/v1/D18-2003",<br>
&nbsp;&nbsp;pages&nbsp;=&nbsp;"13--18",<br>
}<br>

    </div>


