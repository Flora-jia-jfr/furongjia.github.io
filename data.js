// Example Publications Data - Replace with your own publications
const publications = [
  // Preprints Examples
  {
    title: "LEDOM: An Open and Fundamental Reverse Language Model",
    authors: "<b>Xunjian Yin</b>, Sitao Cheng, Yuxi Xie, Xinyu Hu, Li Lin, Xinyi Wang, Liangming Pan, William Yang Wang, Xiaojun Wan",
    venue: "ArXiv:2507",
    links: [
      { text: "Paper", url: "https://arxiv.org/abs/2507.01335" },
      { text: "Model", url: "https://huggingface.co/Corning/Reverse-Model-7B-348B" }
    ],
    isPreprint: true,
    isSelected: true
  },
  // Publications Examples
  {
    title: "Gödel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement",
    authors: "<b>Xunjian Yin</b>, Xinyi Wang, Liangming Pan, Xiaojun Wan, William Yang Wang",
    venue: "ACL 2025",
    links: [
      { text: "Paper", url: "https://arxiv.org/abs/2410.04444" },
      { text: "Code", url: "https://github.com/Arvid-pku/Godel_Agent" }
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

// Example Projects Data - Replace with your own projects
const projects = [
  {
    title: "Gödel Agent",
    description: "A self-referential agent framework for recursive self-improvement implemented with Monkey Patching. (<a href='https://github.com/Arvid-pku/Godel_Agent'>Project Homepage</a>)",
    badges: [
      { url: "https://github.com/Arvid-pku/Godel_Agent/releases", img: "https://img.shields.io/badge/Version-1.0-blue" },
      { url: "https://github.com/Arvid-pku/Godel_Agent/blob/main/LICENSE.md", img: "https://img.shields.io/badge/License-MIT-blue" },
      { url: "https://github.com/Arvid-pku/Godel_Agent/stargazers", img: "https://img.shields.io/github/stars/Arvid-pku/Godel_Agent" },
      { url: "https://github.com/Arvid-pku/Godel_Agent/network/members", img: "https://img.shields.io/github/forks/Arvid-pku/Godel_Agent" },
      { url: "https://github.com/Arvid-pku/Godel_Agent/issues", img: "https://img.shields.io/github/issues/Arvid-pku/Godel_Agent" },
      { url: "https://github.com/Arvid-pku/Godel_Agent/pulls", img: "https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" },
      { url: "https://arxiv.org/abs/2410.04444", img: "https://img.shields.io/badge/Doc-Paper-red" }
    ],
    isSelected: true,
    demoPath: "photos/project-demo/godel-agent.png"
  }
];

// Helper functions to filter projects
const getSelectedProjects = () => projects.filter(project => project.isSelected);
const getAllProjects = () => projects;

// Template Research Experience Data - Replace with your own experience
const researchExperience = [
  {
    period: "Month YYYY - Month YYYY",
    institution: "Your Institution Name",
    mentor: "Prof. Mentor Name",
    description: "Brief description of your research work and achievements."
  }
];

// Template Teaching Data - Replace with your own teaching experience
const teaching = [
  "Teaching Assistant, Institution, Course Name, Semester YYYY, with Prof. Name"
];

// Template Academic Services Data - Replace with your own services
const academicServices = [
  "Reviewer: Conference1 YYYY, Conference2 YYYY",
  "Volunteer: Conference YYYY volunteer"
];

// Template Talks Data - Replace with your own talks
const talks = [
  {
    title: "Your Talk Title",
    venue: "Venue Name",
    date: "Mon DD, YYYY",
    attachments: [
      { text: "Slides", url: "files/your-talk/slides.pdf", type: "pdf" }
    ]
  }
];

// Template Honors Data - Replace with your own honors and awards
const honors = [
  "Your Award Name, Institution, Date",
  "Another Award Name, Institution, Date"
];
