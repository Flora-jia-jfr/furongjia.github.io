// Furong Jia's Publications
const publications = [
  // Under Review / Preprints
  {
    title: "Counting Clues: A Lightweight Probabilistic Baseline Can Match an LLM",
    authors: "<b>Furong Jia</b>*, Yuan Pu*, Finn Guo, Monica Agrawal",
    venue: "Under Review",
    links: [],
    isPreprint: true,
    isSelected: true
  },
  {
    title: "Interpreting Dataset Shift in Clinical Notes",
    authors: "Shariar Vaez-Ghaemi*, <b>Furong Jia</b>*, Monica Agrawal",
    venue: "Under Review",
    links: [],
    isPreprint: true,
    isSelected: true
  },
  {
    title: "Batch-of-Thought: Cross-Instance Learning for Enhanced LLM Reasoning",
    authors: "Xuan Yang, <b>Furong Jia</b>, Roy Xie, Xi Xiong, Jian Li, Monica Agrawal",
    venue: "Under Review",
    links: [],
    isPreprint: true,
    isSelected: true
  },
  {
    title: "What Patients Really Ask: Exploring the Effect of False Assumptions in Patient Information Seeking",
    authors: "Raymond M Xiong, <b>Furong Jia</b>, Lionel Wong, Monica Agrawal",
    venue: "Under Review",
    links: [],
    isPreprint: true,
    isSelected: true
  },
  // 2025 Publications
  {
    title: "Diagnosing our datasets: How does my language model understand clinical text?",
    authors: "<b>Furong Jia</b>, David Sontag, Monica Agrawal",
    venue: "CHIL 2025",
    links: [
      { text: "Paper", url: "https://arxiv.org/abs/2505.15024" }
    ],
    isNew: true,
    isPreprint: false,
    isSelected: true
  },
  // 2024 Publications
  {
    title: "TEMPO: Prompt-based Generative Pre-trained Transformer for Time Series Forecasting",
    authors: "Defu Cao, <b>Furong Jia</b>, Sercan O Arik, Tomas Pfister, Yixiang Zheng, Wen Ye, Yan Liu",
    venue: "ICLR 2024",
    links: [
      { text: "Paper", url: "https://arxiv.org/abs/2310.04948" }
    ],
    isNew: false,
    isPreprint: false,
    isSelected: true
  },
  {
    title: "GPT4MTS: Prompt-based Large Language Model for Multimodal Time-series Forecasting",
    authors: "<b>Furong Jia</b>, Kevin Zheng, Yixiang Zheng, Defu Cao, Yan Liu",
    venue: "EAAI-24",
    links: [
      { text: "Paper", url: "https://ojs.aaai.org/index.php/AAAI/article/view/30383" }
    ],
    isNew: false,
    isPreprint: false,
    isSelected: true
  },
  // 2023 Publications
  {
    title: "I2I: Initializing Adapters with Improvised Knowledge",
    authors: "Tejas Srinivasan, <b>Furong Jia</b>, Mohammad Rostami, Jesse Thomason",
    venue: "CoLLAs 2023",
    links: [
      { text: "Paper", url: "https://arxiv.org/abs/2304.02168" }
    ],
    isNew: false,
    isPreprint: false,
    isSelected: true
  }
];

// Helper functions to filter publications
const getPreprints = () => publications.filter(pub => pub.isPreprint);
const getSelectedPreprints = () => publications.filter(pub => pub.isPreprint && pub.isSelected);
const getPublications = () => publications.filter(pub => !pub.isPreprint);
const getSelectedPublications = () => publications.filter(pub => !pub.isPreprint && pub.isSelected);
const getAllPublications = () => publications.filter(pub => !pub.isPreprint);

// Legacy variables for backward compatibility
const preprints = getSelectedPreprints();
const selectedPublications = getSelectedPublications();
const fullPublications = getAllPublications();

// Furong Jia's Research Projects
const projects = [
  {
    title: "Diagnosing our datasets: How does my language model understand clinical text?",
    description: "Developed a novel diagnostic framework to analyze how language models learn clinical information from pretraining data.",
    image: "photos/project-demo/diagnosing-datasets.pdf", // Add your image here
    paperLink: "https://arxiv.org/abs/2505.15024",
    githubLink: "https://github.com/Flora-jia-jfr/diagnosing_our_datasets", // Add GitHub link if available
    isSelected: true,
    layout: "wide" // wide images display vertically: title, image, description
  },
  {
    title: "Counting Clues: A Lightweight Probabilistic Baseline Can Match an LLM",
    description: "Demonstrated that simple probabilistic models can achieve competitive performance with large language models in diagnostic reasoning tasks.",
    image: "photos/project-demo/counting-clues.png", // Add your image here
    paperLink: "", // Add paper link when available
    githubLink: "", // Add GitHub link if available
    isSelected: true,
    layout: "wide" // wide images display vertically: title, image, description
  },
  {
    title: "Interpreting Dataset Shift in Clinical Notes",
    description: "Investigated temporal and distributional shifts in clinical notes datasets and their effects on clinical NLP systems.",
    image: "photos/project-demo/dataset-shift.png", // Add your image here
    paperLink: "", // Add paper link when available
    githubLink: "", // Add GitHub link if available
    isSelected: true,
    layout: "wide" // wide images display vertically: title, image, description
  },
  {
    title: "GPT4MTS: Prompt-based Large Language Model for Multimodal Time-series Forecasting",
    description: "Created a novel framework that combines numerical time series data with textual context using large language models for improved forecasting accuracy.",
    image: "photos/project-demo/gpt4mts.png", // Add your image here
    paperLink: "https://ojs.aaai.org/index.php/AAAI/article/view/30383",
    githubLink: "https://github.com/Flora-jia-jfr/GPT4MTS-Prompt-based-Large-Language-Model-for-Multimodal-Time-series-Forecasting", // Add GitHub link if available
    isSelected: true,
    layout: "side-by-side" // square/compact images display horizontally: image on left, text on right
  }
];

// Helper functions to filter projects
const getSelectedProjects = () => projects.filter(project => project.isSelected);
const getAllProjects = () => projects;

// Furong Jia's Research Experience
const researchExperience = [
  {
    period: "Aug 2024 - Present",
    institution: "DukeNLP, Duke University",
    mentor: "Prof. Monica Agrawal",
    description: "- Diagnosing our datasets: How does my language model understand clinical text?<br>- Counting Clues: A Lightweight Probabilistic Baseline Can Match an LLM<br>- Interpreting Dataset Shift in Clinical Notes"
  },
  {
    period: "May 2023 - June 2024",
    institution: "Melady Lab, University of Southern California",
    mentor: "Prof. Yan Liu",
    description: "- TEMPO: Prompt-based Generative Pre-trained Transformer for Time Series Forecasting<br>- GPT4MTS: Prompt-based Large Language Model for Multimodal Time-series Forecasting"
  },
  {
    period: "Aug 2022 - Present",
    institution: "GLAMOR Lab, University of Southern California",
    mentor: "Prof. Jesse Thomason",
    description: "- I2I: Initializing Adapters with Improvised Knowledge"
  }
];

// Furong Jia's Teaching Experience
const teaching = [
  "Teaching Assistant, Duke University, Applied Machine Learning (CS 290), Spring 2025",
  "Teaching Assistant, University of Southern California, Algorithms and Theory of Computing (CSCI 270), Spring 2022",
  "Course Producer, University of Southern California, Web Publishing and Front-end Development (ITP 104), Fall 2021 - Spring 2024"
];

// Furong Jia's Academic Services
const academicServices = [
  "Reviewer: ACL ARR 2024 (June, October), ACL ARR 2025 (February, May)",
  "Reviewer: NeurIPS 2025",
  "Reviewer: ML4H 2025"
];

// Furong Jia's Talks - Add your talks here
const talks = [
  // {
  //   title: "Your Talk Title",
  //   venue: "Venue Name",
  //   date: "Mon DD, YYYY",
  //   attachments: [
  //     {text:"Slides", url:"files/your-talk/slides.pdf", type: "pdf"}
  //   ]
  // }
];


// Furong Jia's Honors and Awards
const honors = [
  "Albert Dorman Future Leader Award, University of Southern California, 2024",
  "Student Recognition Awards, University of Southern California, 2024",
  "Provost's Research Fellowship, University of Southern California, Fall 2023",
  "CURVE Research Fellowship, University of Southern California, Fall 2022 & Spring 2023",
  "Academic Achievement Award Scholarship, University of Southern California, 2021",
  "ABC Innovation Prize, University of Southern California, 2021",
  "W.V.T. Rusch Engineering Honors Program",
  "Viterbi Grand Challenges Scholar"
];
