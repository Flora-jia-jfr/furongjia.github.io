// Template Publications Data - Replace with your own publications
const publications = [
  // Preprints Examples
  {
    title: "Your Preprint Title Here",
    authors: "<b>Your Name</b>, Co-Author One, Co-Author Two",
    venue: "ArXiv:YYYY",
    links: [
      { text: "Paper", url: "https://arxiv.org/abs/YYYY.XXXXX" },
      { text: "Code", url: "https://github.com/yourusername/yourproject" }
    ],
    isPreprint: true,
    isSelected: true
  },
  // Publications Examples
  {
    title: "Your Publication Title Here",
    authors: "<b>Your Name</b>, Co-Author One, Co-Author Two",
    venue: "Conference Name YYYY",
    links: [
      { text: "Paper", url: "https://arxiv.org/abs/YYYY.XXXXX" },
      { text: "Code", url: "https://github.com/yourusername/yourproject" }
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

// Template Projects Data - Replace with your own projects
const projects = [
  {
    title: "Your Project Name",
    description: "Description of your project with <a href='#'>links</a> if needed. (<a href='https://github.com/yourusername/yourproject'>Project Homepage</a>)",
    badges: [
      { url: "https://github.com/yourusername/yourproject/releases", img: "https://img.shields.io/badge/Version-1.0-blue" },
      { url: "https://github.com/yourusername/yourproject/blob/main/LICENSE.md", img: "https://img.shields.io/badge/License-MIT-blue" },
      { url: "https://github.com/yourusername/yourproject/stargazers", img: "https://img.shields.io/github/stars/yourusername/yourproject" },
      { url: "https://github.com/yourusername/yourproject/network/members", img: "https://img.shields.io/github/forks/yourusername/yourproject" }
    ],
    isSelected: true,
    demoPath: "photos/project-demo/your-project.png"
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
