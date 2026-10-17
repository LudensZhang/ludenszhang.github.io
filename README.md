# Haohong Zhang · Personal homepage

A Haohong Ink static academic website for [ludenszhang.github.io](https://ludenszhang.github.io/), designed for GitHub Pages. No build process, package installation or server-side code is required.

## Files and design

- `index.html` — the homepage: identity, recent work, research and MGM2, 25 publications, six projects, education, three CV links, and contact. Canonical, social, and Person metadata stay in the head.
- `assets/home/home.css` and `assets/home/home.js` — layout, type, paper filters, and citation copy. The page stays readable without JavaScript; search and citation copy need it.
- `assets/home/plate.jpg` — a still life made for the page. It is decorative, not a result or a diagram.
- `assets/home/og.jpg` — the social card, 1200 × 630.
- `assets/fonts/` — self-hosted Newsreader and IBM Plex, both SIL Open Font License. See `assets/fonts/NOTICE.txt`.
- `assets/brand/` — owner-supplied HZ monogram, vector trace, CV raster and home-screen icon.
- `assets/favicon.svg` — site icon.
- `assets/dossier/` — the previous layout. It stays in the repository and is not used by the current page.
- `.nojekyll` — serve the repository as static files.
- `scripts/version_assets.py` — refresh content-based resource URLs after edits.
- `SOURCES.md` and `docs/cv-sources.md` — content sources.

Earlier design assets remain in the repository for history and are not dependencies of the current layout. Candidate designs, browser output and local tooling are not required for deployment.

## Preview and GitHub Pages

Run `python3 -m http.server 8765` from the repository, then open `http://localhost:8765`. The page also supports ordinary static-file hosting.

GitHub Pages publishes the `main` branch's root directory at `https://ludenszhang.github.io/`. The site requires no framework runtime, backend or package installation.

## Updating content

Edit content directly in `index.html`. Keep full publication titles, authors, keywords, year, kind and source URLs accurate. Each `article.paper` has `data-search`, `data-year`, `data-kind` and `data-themes` attributes used by the filters. Its citation button carries the complete citation in `data-citation`. Keep these attributes synchronized with the visible record, and update the year and kind options when adding papers. Preserve the embedded `personal-data` JSON as the structured copy of papers and projects. The CV builder reads `article.paper` and `a.project` from this file; keep those class names and the title link's `href` as its first attribute.

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
