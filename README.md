# Haohong Zhang · Personal homepage

An Apple-inspired static academic website for [ludenszhang.github.io](https://ludenszhang.github.io/), designed for GitHub Pages. No build process, package installation or server-side code is required.

## Files

- `index.html` — profile, research, selected publications, publication archive and project links.
- `assets/site.css` — system sans-serif typography, centered hero, translucent navigation, rounded panels, responsive layouts, automatic dark mode, reduced-motion support and print styles.
- `assets/site.js` — optional active navigation and avatar fallback. All content, navigation and the publication archive work without JavaScript.
- `assets/favicon.svg` — site icon.
- `assets/projects/*.jpg` — six generated glass project icons, based on the repository functions documented in `SOURCES.md`. Generation prompts and processing details: `docs/project-icon-prompts.md`. The earlier SVG studies are retained but not loaded.
- `.nojekyll` — serve the repository as static files.
- `scripts/version_assets.py` — update resource URL versions after CSS, JavaScript or icon changes.
- `SOURCES.md` — sources and scope of the September 2026 content update.

The page uses local system fonts. The GitHub avatar is optional and falls back to an initials mark if unavailable. Existing `assets/html2canvas.min.js` and `assets/liquidGL.js` have been preserved but are no longer loaded.

## Preview

Run `python3 -m http.server 8765` from the repository, then open `http://localhost:8765`. Opening `index.html` directly also works.

## GitHub Pages

Push the changes to the repository's publishing branch. In **Settings → Pages**, choose **Deploy from a branch**, select that branch, and use **/ (root)**. The website is served at `https://ludenszhang.github.io/`; no GitHub Actions workflow is needed for this setup. If Pages already publishes this branch and root directory, no settings changes are needed.

## Updating content

Edit content directly in `index.html`. Keep journal articles, preprints and conference abstracts clearly distinguished. Update the footer date when revising content. New publication entries can follow the existing `article.paper` markup. Use DOI links when verified; other preserved entries link to an exact-title Scholar search.

The September 2026 redesign preserves all 20 entries and all six projects from the previous homepage, adds two verified 2026 preprints, and updates MGM2's repository link. It does not maintain a live citation counter.

## Asset caching

CSS, JavaScript, favicon and project-icon links include a SHA-256 content version. This keeps newly deployed HTML from reusing a previous asset from the browser cache. After editing any of those files, run `python3 scripts/version_assets.py` and commit the updated `index.html` together with the changed assets. Verify before publishing with `python3 scripts/version_assets.py --check`. The script is idempotent, has no external dependencies, and does not run in the browser. The website still needs no build step to serve.


## CV PDFs

The hero's **View CV** link opens the general two-page English CV. About also links to academic and research/engineering variants. All three use the site's charcoal, gray and blue palette, contain selectable text and clickable links, and work as ordinary PDFs on GitHub Pages.

- `assets/cv/Haohong-Zhang-CV.pdf` — general research profile.
- `assets/cv/Haohong-Zhang-CV-Academic.pdf` — publications and education first.
- `assets/cv/Haohong-Zhang-CV-Research-Engineer.pdf` — technical skills and engineering projects first.
- `scripts/build_cv.py` — reproducible PDF builder; requires ReportLab.
- `docs/cv-sources.md` — evidence for additional honors, conference activity and technical skills.

After content edits, run `python3 scripts/build_cv.py`, render and review all PDF pages, then run `python3 scripts/version_assets.py`. The version script updates all occurrences of each asset, including both general-CV links.
