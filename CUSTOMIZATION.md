# Customization Guide

This guide helps you customize the template to match your preferences and needs.

## Visual Customization

### Color Scheme

Edit `config.js` to change the color scheme:

```javascript
const CONFIG = {
  colors: {
    primary: '#0065C0',      // Main links and headings
    secondary: '#f09228',    // Hover effects and accents
    text: '#000000',         // Main text color
    background: '#FFFFFF',   // Page background
    border: '#bbb',          // Borders and dividers
    accent: '#B31B1B'        // Special highlights
  }
};
```

### Popular Color Schemes

**Academic Blue** (Default):
```javascript
primary: '#0065C0', secondary: '#f09228'
```

**Professional Green**:
```javascript
primary: '#2E8B57', secondary: '#FF6B35'
```

**Modern Purple**:
```javascript
primary: '#6A4C93', secondary: '#F72585'
```

**Classic Red**:
```javascript
primary: '#B31B1B', secondary: '#FFD700'
```

### Typography

Modify font settings in `config.js`:

```javascript
typography: {
  fontFamily: "'Lato', Verdana, Helvetica, sans-serif",
  baseFontSize: '16px',
  lineHeight: 1.7,
  headingFontSize: '22px',
  nameFontSize: '32px'
}
```

## Layout Customization

### Section Order

To reorder sections on the homepage, move the corresponding HTML blocks in `index.html`:

```html
<!-- Move these sections around as desired -->
<div class="section-spacing"><!-- Preprints --></div>
<div class="section-spacing"><!-- Publications --></div>
<div class="section-spacing"><!-- Projects --></div>
<div class="section-spacing"><!-- Research Experience --></div>
```

### Hiding Sections

To hide a section, add `style="display: none;"` to the section div:

```html
<div class="section-spacing" style="display: none;">
  <!-- This section will be hidden -->
</div>
```

### Adding Custom Sections

1. Add HTML structure:
```html
<div class="section-spacing">
  <table style="width:100%;border:0px;border-spacing:0px;border-collapse:separate;">
    <tbody>
      <tr>
        <td style="padding:20px;width:100%;vertical-align:middle">
          <heading id="custom-section">Custom Section</heading>
          <ul id="custom-list">
            <!-- Content will be inserted here -->
          </ul>
        </td>
      </tr>
    </tbody>
  </table>
</div>
```

2. Add data to `data.js`:
```javascript
const customData = [
  "Custom item 1",
  "Custom item 2"
];
```

3. Add population function to `main.js`:
```javascript
function populateCustomSection() {
  const list = document.getElementById('custom-list');
  if (!list) return;
  
  customData.forEach(item => {
    const li = document.createElement('li');
    li.innerHTML = `<p>${item}</p>`;
    list.appendChild(li);
  });
}
```

## Feature Customization

### Navigation Menu

To modify the navigation menu, edit each HTML file:

```html
<nav class="nav-buttons">
  <a href="index.html" class="nav-button">Home</a>
  <a href="publications.html" class="nav-button">Publications</a>
  <a href="projects.html" class="nav-button">Projects</a>
  <!-- Add, remove, or modify navigation items -->
  <a href="custom-page.html" class="nav-button">Custom Page</a>
</nav>
```

### Sidebar Outline

Update the sidebar navigation in `index.html`:

```html
<ul id="outline-list">
  <li><a href="#preprints">Preprints</a></li>
  <li><a href="#selected-publications">Publications</a></li>
  <!-- Add links to your custom sections -->
  <li><a href="#custom-section">Custom Section</a></li>
</ul>
```

### Footer

Customize the footer in each HTML file:

```html
<div class="footer-section">
  <table>
    <tr>
      <td><!-- Left content --></td>
      <td>© 2025 Your Name. Custom footer text.</td>
      <td><!-- Right content --></td>
    </tr>
  </table>
</div>
```

## Content Customization

### Publication Display

Customize how publications are displayed by modifying the `populatePublications` function in `main.js`:

```javascript
function populatePublications(publications, listId) {
  // Modify this function to change publication formatting
  // Add custom badges, styling, or information
}
```

### Project Badges

Add custom badges to your projects in `data.js`:

```javascript
badges: [
  { url: "github-url", img: "https://img.shields.io/github/stars/user/repo" },
  { url: "demo-url", img: "https://img.shields.io/badge/Demo-Live-green" },
  { url: "paper-url", img: "https://img.shields.io/badge/Paper-PDF-red" }
]
```

### Social Media Links

Update social media links in the structured data and contact section:

```html
<p style="text-align:center">
  <a href="mailto:your.email@domain.com">Email</a> /
  <a href="https://github.com/yourusername">GitHub</a> /
  <a href="https://linkedin.com/in/yourprofile">LinkedIn</a> /
  <a href="https://twitter.com/yourusername">Twitter</a> /
  <a href="https://orcid.org/0000-0000-0000-0000">ORCID</a>
</p>
```

## Advanced Customization

### Adding Google Analytics

Add this to the `<head>` section of all HTML files:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_TRACKING_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_TRACKING_ID');
</script>
```

### Custom CSS

Add custom styles to a new file `custom.css`:

```css
/* Custom styles */
.my-custom-class {
  /* Your custom styles */
}

/* Override existing styles */
.papertitle {
  font-size: 18px; /* Larger paper titles */
}
```

Then include it in your HTML:

```html
<link rel="stylesheet" type="text/css" href="custom.css">
```

### Blog Integration

To integrate with a blog system:

1. Replace `blogs.html` with your blog platform's generated page
2. Or modify the existing blogs page to load from your blog API
3. Update navigation links accordingly

## Content Management Tips

### Regular Updates

Create a maintenance schedule:
- **Monthly**: Update publications and projects
- **Quarterly**: Review and update bio/research interests
- **Annually**: Update CV, photos, and major sections

### Version Control

Consider using Git to track changes:

```bash
git init
git add .
git commit -m "Initial template setup"
git remote add origin your-repo-url
git push -u origin main
```

### Backup Strategy

- Keep backups of your customized files
- Store images in multiple locations
- Export your data.js content regularly

## Testing Your Customizations

### Local Testing

1. Open HTML files in your browser
2. Test all navigation links
3. Verify responsive design (resize browser window)
4. Test dark mode toggle
5. Check all external links

### Browser Compatibility

Test in multiple browsers:
- Chrome/Chromium
- Firefox
- Safari
- Edge

### Mobile Testing

Test on actual mobile devices or use browser developer tools to simulate:
- Phone portrait/landscape
- Tablet portrait/landscape
- Different screen sizes

## Common Customization Questions

**Q: How do I change the profile photo shape from circle to square?**
A: Modify the CSS for `.profile-photo` and remove `border-radius: 50%;`

**Q: Can I add more pages?**
A: Yes! Create new HTML files following the same structure and add them to navigation.

**Q: How do I change the visitor map?**
A: Replace the ClustrMaps URL in the `initializeLazyVisitorMap` function in `main.js`.

**Q: Can I use a different font?**
A: Yes! Update the font imports in CSS and modify the `fontFamily` in `config.js`.

---

Need more help? Check the main README.md or review the code comments for additional guidance!
