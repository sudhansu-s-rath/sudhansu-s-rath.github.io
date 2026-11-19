# Sudhansu Sekhar Rath — Personal Website

Personal academic website, hosted on GitHub Pages: [sudhansu-s-rath.github.io](https://sudhansu-s-rath.github.io)

## Pages
- **Home** (`index.html`): introduction, education, experience, skills
- **Research** (`research.html`): research projects
- **Teaching** (`teaching.html`): teaching and mentorship
- **Publications** (`publications.html`): publications, presentations, CV download
- **Contact** (`contact.html`): affiliations and profiles
- **Data note** (`heat-resilience-phoenix.html`): rooftop albedo and heat resilience, Phoenix–Tempe

## Technology
- Plain HTML + one stylesheet (`css/modern.css`); no framework
- Icons: Font Awesome 6 (CDN) with the v4 compatibility layer, so `fa fa-...` class names work
- Hosting: GitHub Pages (static files; folders starting with `_` are not published)

## Maintaining the site
**Shared header, navigation, and footer** live in `_partials/` (`head.html`, `nav.html`, `footer.html`).
Edit them once, then copy them into every page:
```bash
python3 _tools/sync_layout.py
```
Each page keeps its own `<title>` and description, which also feed the link-preview (Open Graph) tags.

**Publications, talks, and the CV PDF** are generated from the CV project (`../CV`, see its README):
```bash
cd ../CV
./build.sh --public && cp out/CV_public.pdf ../PersonalPage/files/CV_Sudhansu_Rath.pdf
python tools/web_publications.py ../PersonalPage/publications.html   # in geo_env
```
Only the regions between `<!-- BEGIN AUTO:... -->` / `<!-- BEGIN SHARED:... -->` markers are rewritten;
everything else is edited by hand.

**Preview locally:** open `index.html` in a browser, or run `python3 -m http.server` here and visit
http://localhost:8000.

## Contact
- **Email**: sudhansu@asu.edu
- **Google Scholar**: https://scholar.google.com/citations?user=o4jIZJAAAAAJ&hl=en
- **ORCID**: https://orcid.org/0000-0003-4529-3719

## License
MIT License (see [LICENSE](LICENSE)).
