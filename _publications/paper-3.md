---
title: "TEMPO: Prompt-based Generative Pre-trained Transformer for Time Series Forecasting"
collection: publications
permalink: /publication/paper-3
excerpt: ''
date: 2023-09-29
venue: 'arxiv preprint'
submit: 'ICLR 2024'
paperurl: # 'https://arxiv.org/pdf/2310.04948.pdf'
citation: 
authors: 'Defu Cao, <strong>Furong Jia</strong>, Sercan O Arik, Tomas Pfister, Yixiang Zheng, Wen Ye, Yan Liu'
---
> Submitted to ICLR 2024

The past decade has witnessed significant advances in time series modeling with deep learning. While achieving state-of-the-art results, the best-performing architectures vary highly across applications and domains. Meanwhile, for natural language processing, the Generative Pre-trained Transformer (GPT) has demonstrated impressive performance via training one general-purpose model across various textual datasets. It is intriguing to explore whether GPT-type architectures can be effective for time series, capturing the intrinsic dynamic attributes and leading to significant accuracy improvements. In this paper, we propose a novel framework, TEMPO, that can effectively learn time series representations. We focus on utilizing two essential inductive biases of the time series task for pre-trained models: (i) decomposition of the complex interaction between trend, seasonal and residual components; and (ii) introducing the selection-based prompts to facilitate distribution adaptation in non-stationary time series. TEMPO expands the capability for dynamically modeling real-world temporal phenomena from data within diverse domains. Our experiments demonstrate the superior performance of TEMPO over state-of-the-art methods on a number of time series benchmark datasets. This performance gain is observed not only in standard supervised learning settings but also in scenarios involving previously unseen datasets as well as in scenarios with multi-modal inputs. This compelling finding highlights TEMPO's potential to constitute a foundational model-building framework.

[Download paper here](https://arxiv.org/pdf/2310.04948.pdf)