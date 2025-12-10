# Pre-Publication Checklist

## Before pushing to GitHub, update these placeholders:

### research.html
- [ ] Line ~40: Update Phoenix project details with your actual work
- [ ] Line ~65: Add specific WRF configuration details
- [ ] Line ~95: Add your agro-climatic project details
- [ ] Line ~110: Update research interests list

### teaching.html
- [ ] Line ~42: Add specific course names at Galgotias University
- [ ] Line ~66: Add NIT Rourkela course names
- [ ] Line ~84: Update student supervision numbers
- [ ] Line ~96: Add actual workshop titles/dates

### publications.html
**MOST IMPORTANT - Add your real publications!**
- [ ] Line ~51: Replace example publication with real one
- [ ] Line ~60: Add more journal articles
- [ ] Line ~70: Add conference papers
- [ ] Line ~86: Update PhD thesis year (if completed)
- [ ] Line ~122: Add your actual Google Scholar/ResearchGate links

### contact.html
- [ ] Line ~45: Add your phone number
- [ ] Line ~53: Add ASU email/affiliation (if applicable)
- [ ] Line ~63: Add actual LinkedIn URL
- [ ] Line ~64: Verify GitHub username
- [ ] Line ~65-67: Add actual Google Scholar/ResearchGate/ORCID links
- [ ] Line ~83: Update office hours

### index.md (Homepage)
- [ ] Line ~102: Update PhD duration if completed: "2015 - present" → "2015 - 2024"
- [ ] Line ~136: Update career profile text to current work
- [ ] Line ~147: Update research experience dates
- [ ] Line ~75-88: Add new technical skills (Python, xarray, WRF v4.7, HPC, etc.)
- [ ] Update photo in images/ folder if needed

## Quick Commands

### 1. Preview locally
```bash
cd /data/mgeorge7/sudhansu_WORK/PersonalPage
python -m http.server 8000
# Open: http://localhost:8000
```

### 2. Check what will be committed
```bash
git status
git diff index.md
```

### 3. Publish to GitHub
```bash
git add *.html index.md UPDATE_GUIDE.md CHECKLIST.md
git commit -m "Add research, teaching, publications, and contact pages"
git push origin main
```

### 4. Verify live
Wait 1-2 minutes, then visit:
https://sudhansu-s-rath.github.io/

## File Sizes (Should stay under 100KB each)
```bash
ls -lh *.html index.md
```

Current:
- research.html: 7.8KB ✅
- teaching.html: 7.5KB ✅
- publications.html: 7.9KB ✅
- contact.html: 6.1KB ✅
- index.md: ~11KB ✅

Total new content: ~29KB (excellent!)

## Common Mistakes to Avoid
- [ ] Don't add large PDFs (link to external sources instead)
- [ ] Don't use absolute paths (use relative: `research.html` not `/research.html`)
- [ ] Don't forget to update copyright year
- [ ] Don't leave placeholder text like "[Add content here]"
- [ ] Test all links before publishing

## After Publishing
- [ ] Test all navigation links
- [ ] Verify pages load correctly
- [ ] Check mobile responsiveness
- [ ] Update LinkedIn/CV with new website sections
