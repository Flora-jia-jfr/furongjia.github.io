---
title: "I2I: Initializing Adapters with Improvised Knowledge"
collection: publications
permalink: /publication/paper-1
excerpt: ''
date: 2023-05-15
venue: 'CoLLAs 2023 (Second Conference on Lifelong Learning Agents)'
authors: 'Tejas Srinivasan, <strong>Furong Jia</strong>, Mohammad Rostami, Jesse Thomason'
---

Adapters present a promising solution to the catastrophic forgetting problem in continual learning. However, training independent Adapter modules for every new task misses an opportunity for cross-task knowledge transfer. We propose Improvise to Initialize (I2I), a continual learning algorithm that initializes Adapters for incoming tasks by distilling knowledge from previously-learned tasks' Adapters. We evaluate I2I on CLiMB, a multimodal continual learning benchmark, by conducting experiments on sequences of visual question answering tasks. Adapters trained with I2I consistently achieve better task accuracy than independently-trained Adapters, demonstrating that our algorithm facilitates knowledge transfer between task Adapters. I2I also results in better cross-task knowledge transfer than the state-of-the-art AdapterFusion without incurring the associated parametric cost.

[Download paper here](https://arxiv.org/pdf/2304.02168.pdf)