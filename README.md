# Haohong Zhang · Personal homepage

A Haohong Ink static academic website for [ludenszhang.github.io](https://ludenszhang.github.io/), designed for GitHub Pages. No build process, package installation or server-side code is required.

## Files and design

- `index.html` — the selected personal research dossier: identity, About with education and CV, research interests, MGM2 v2, 25 publications, six open-source projects and contact details. Retains canonical, social and structured Person metadata.
- `assets/dossier/base.css` — shared type, colors, controls, native details, focus and reduced-motion styles.
- `assets/dossier/personal.css` — biography, research, paper and project components.
- `assets/dossier/dossier.css` — the selected responsive layout. Warm ivory, navy, blue and small yellow/gold accents; Georgia and Helvetica Neue. Shared spacing scale and a 1480px maximum reading canvas. The HZ logo keeps its natural aspect ratio.
- `assets/dossier/reading.js` — progressive scroll entrances, keyword/year filtering and citation copying, with a manual-copy fallback when clipboard access is unavailable.
- `assets/dossier/interactions.js` — optional interaction enhancements, including opening one project file at a time.
- `assets/dossier/sequence-mark.webp` — one small conceptual illustration, not a model architecture or experimental result. Original generation record: `assets/dossier/image-provenance.json`.
- `assets/brand/` — owner-supplied HZ monogram, vector trace, CV raster and home-screen icon.
- `assets/favicon.svg` — HZ site icon.
- `.nojekyll` — serve the repository as static files.
- `scripts/version_assets.py` — refresh content-based resource URLs after edits.
- `SOURCES.md` and `docs/cv-sources.md` — content sources.

The site uses local system fonts. Earlier design assets remain in the repository for history and are not dependencies of the current layout. Candidate designs, browser output and local tooling are not required for deployment.

## Preview and GitHub Pages

Run `python3 -m http.server 8765` from the repository, then open `http://localhost:8765`. The page also supports ordinary static-file hosting.

GitHub Pages publishes the `main` branch's root directory at `https://ludenszhang.github.io/`. The site requires no framework runtime, backend or package installation.

## Updating content

Edit content directly in `index.html`. Keep full publication titles, authors, keywords, year, kind and source URLs accurate. Each `article.paper-record` has `data-search` and `data-year` attributes used by the search and year filters. Its citation button carries the complete citation in `data-citation`. Keep these attributes synchronized with the visible record, and update year-group counts, year options and the initial paper count when adding papers. Preserve the embedded `personal-data` JSON as the structured copy of papers and projects.

All paper records are present in the HTML. Year groups, authors, project details, source links and CV links work without JavaScript. Search and automatic citation copying require JavaScript. Content stays visible when script loading fails or reduced motion is requested.

After content or asset edits, run:

```sh
python3 scripts/version_assets.py
python3 scripts/version_assets.py --check
```

Commit `index.html` with changed assets so the new HTML references matching content hashes. Preview desktop and mobile layouts and exercise any changed interaction before publishing.

## CV PDFs

The homepage's **View CV** link jumps to the three editions in About. Each opens an ordinary PDF with selectable text and clickable links:

- `assets/cv/Haohong-Zhang-CV.pdf` — general research profile.
- `assets/cv/Haohong-Zhang-CV-Academic.pdf` — publications and education first.
- `assets/cv/Haohong-Zhang-CV-Research-Engineer.pdf` — technical skills and engineering projects first.

The PDFs use the site's ivory, navy and blue palette. `scripts/build_cv.py` rebuilds them with ReportLab; see `docs/cv-sources.md` for sources. After changing PDF content, render and review every page, then refresh asset versions.

## Web analytics

The homepage retains the existing Cloudflare Web Analytics beacon and site configuration. Traffic is available in Cloudflare's Web Analytics dashboard; the HTML snippet's site token is a public identifier, not an API credential. Ad blockers or network restrictions can prevent visits from being recorded. Dashboard access still requires the owner's Cloudflare account.
