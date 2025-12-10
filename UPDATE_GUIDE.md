# Website Update Guide

## Overview
Your personal website has been updated with 4 new pages:
- research.html (7.8KB)
- teaching.html (7.5KB)  
- publications.html (7.9KB)
- contact.html (6.1KB)

Total size: ~29KB (very lightweight for GitHub Pages!)

## Current Structure
```
PersonalPage/
├── index.md              # Homepage (updated navigation)
├── research.html         # NEW: Research projects
├── teaching.html         # NEW: Teaching experience
├── publications.html     # NEW: Publications list
├── contact.html          # NEW: Contact information
├── css/                  # Stylesheets (unchanged)
├── js/                   # Scripts (unchanged)
├── images/               # Photos (unchanged)
└── README.md            # This file
```

## Before Publishing - CUSTOMIZE THESE:

### 1. research.html
- [ ] Update Phoenix/ASU project details
- [ ] Add actual project descriptions
- [ ] Update research interests

### 2. teaching.html
- [ ] Add specific course names you taught
- [ ] Update student supervision numbers
- [ ] Add workshop details

### 3. publications.html
**IMPORTANT:** Add your actual publications!
- [ ] Journal articles (with DOIs)
- [ ] Conference papers
- [ ] Update thesis year
- [ ] Add Google Scholar/ResearchGate links

### 4. contact.html
- [ ] Add your phone number
- [ ] Update ASU email (if applicable)
- [ ] Add LinkedIn/GitHub URLs
- [ ] Update office hours

### 5. index.md (Homepage)
- [ ] Update PhD status: "2015 - present" → "2015 - 2024" (if completed)
- [ ] Update current position/affiliation
- [ ] Add new skills: Python, xarray, WRF v4.7, etc.
- [ ] Update career profile text

## How to Test Locally

### Option 1: Simple HTTP Server
```bash
cd /data/mgeorge7/sudhansu_WORK/PersonalPage
python -m http.server 8000
# Open browser: http://localhost:8000
```

### Option 2: Direct File Opening
```bash
# Open any HTML file in your browser
firefox research.html  # or
google-chrome teaching.html
```

## Publishing to GitHub Pages

### Step 1: Check Git Status
```bash
cd /data/mgeorge7/sudhansu_WORK/PersonalPage
git status
```

### Step 2: Stage New Files
```bash
git add research.html teaching.html publications.html contact.html
git add index.md  # Updated navigation
```

### Step 3: Commit Changes
```bash
git commit -m "Add research, teaching, publications, and contact pages

- Created 4 new lightweight pages (~29KB total)
- Updated homepage navigation
- Updated copyright to 2025
- All pages mobile-friendly and GitHub Pages compatible"
```

### Step 4: Push to GitHub
```bash
git push origin main
# Or if your branch is 'master':
# git push origin master
```

### Step 5: Wait & Verify
- Wait 1-2 minutes for GitHub Pages to rebuild
- Visit: https://sudhansu-s-rath.github.io/
- Test all new pages

## GitHub Pages Settings

If pages don't show up:
1. Go to: https://github.com/sudhansu-s-rath/sudhansu-s-rath.github.io/settings/pages
2. Ensure Source is set to: `main` branch (or `master`)
3. Check that GitHub Pages is enabled

## File Size Guidelines (GitHub Pages)

✅ **Your Current Status:**
- Individual files: 6-8KB each (✅ Excellent!)
- Total repo: 5.8MB (✅ Well under 1GB limit)
- No large images or PDFs

**Keep these limits:**
- Individual files: < 100KB recommended
- Total repository: < 1GB (GitHub Pages limit)
- Individual images: < 200KB (optimize if needed)

## Tips for Staying Lightweight

1. **Images:**
   ```bash
   # Optimize images before adding
   convert profile.jpg -quality 85 -resize 500x500 profile_optimized.jpg
   ```

2. **PDFs:**
   - DON'T add large PDFs to repo
   - Link to external sources (Google Drive, ResearchGate, etc.)

3. **Publications:**
   - Link to DOI or journal websites
   - Use Google Scholar for PDF access

## Common Tasks

### Update Homepage Info
Edit: `index.md` (lines 95-260)
- Education section: Lines 95-116
- Career profile: Lines 133-139
- Research experience: Lines 143-158
- Work experience: Lines 180-210

### Add New Publication
Edit: `publications.html`
Copy the template:
```html
<div class="pub-item">
    <h4>[Paper Title]</h4>
    <p class="pub-meta"><strong>Authors:</strong> [Names]</p>
    <p class="pub-meta"><strong>Journal:</strong> [Name] | <strong>Year:</strong> [Year]</p>
    <p>Abstract: [Text]</p>
    <p><a href="[DOI]" target="_blank"><i class="fa fa-external-link"></i> View Publication</a></p>
</div>
```

### Add New Research Project
Edit: `research.html`
Copy the template:
```html
<div class="research-item">
    <h3>[Project Title]</h3>
    <p><strong>Duration:</strong> [Years] | <strong>Role:</strong> [Position]</p>
    <p><strong>Overview:</strong> [Description]</p>
    <p><strong>Tools & Methods:</strong> [List]</p>
</div>
```

## Troubleshooting

### Pages not loading?
- Check file permissions: `chmod 644 *.html`
- Verify file names (case-sensitive!)
- Check GitHub Pages build status

### Links broken?
- Use relative paths: `research.html` not `/research.html`
- For homepage: `index.md` or `./`

### Styling issues?
- Clear browser cache (Ctrl+F5)
- Check CSS file paths in HTML
- Verify Bootstrap/FontAwesome CDN links

## Next Steps

1. ✅ Pages created and navigation updated
2. ⏳ Customize content (see checklist above)
3. ⏳ Test locally
4. ⏳ Commit and push to GitHub
5. ⏳ Verify live website

## Need Help?

- GitHub Pages Docs: https://docs.github.com/en/pages
- HTML/CSS Reference: https://www.w3schools.com
- Your repo: https://github.com/sudhansu-s-rath/sudhansu-s-rath.github.io

---
Last Updated: December 10, 2025
