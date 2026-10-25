# Haohong Zhang · Dispatch

A static academic personal website for [ludenszhang.github.io](https://ludenszhang.github.io/), using the selected Dispatch / 朱印 design: paper, ink, vermilion, a condensed personal masthead and editorial columns. GitHub Pages serves the `main` branch root. No server-side runtime or package installation is needed to browse the site.

## Layout and assets

- `index.html`: personal profile, recent research, themes and MGM2, 25 papers, six repositories, education, three CV editions and contact. Canonical, social, Person metadata and the existing Cloudflare analytics configuration are retained.
- `assets/dispatch/dispatch.css`, `tokens.css`, `base.css`: the selected responsive design.
- `assets/dispatch/interactions.js`: publication search, year/type/theme filters, citation copy and navigation state. Original native disclosures keep the full record readable without JavaScript.
- `assets/dispatch/fonts.css` and `fonts/`: locally hosted Six Caps, Bevan and Archivo Narrow. WOFF2 is used on the web; static TrueType instances are embedded in the PDFs. See the SIL Open Font License files and NOTICE.
- `assets/dispatch/hz-mark.png`: the new selected HZ monogram; its conceptual identity provenance is recorded in `image-provenance.json`.
- `assets/data/personal.json`: a portable copy of the publication/project record. The `personal-data` script in the page is the CV builder's input; keep both in sync.
- `assets/cv/`: three two-page, searchable, linked PDFs in the same visual system.
- `SOURCES.md` and `docs/cv-sources.md`: factual sources and CV editorial scope.

Earlier design assets remain in the repository for history but are not loaded by the selected homepage. Unselected local candidates and browser inspection outputs are not deployment dependencies.

## Preview

From the repository root:

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Open `http://127.0.0.1:8765/`. All production resources use relative links and work on GitHub Pages.

## Update content

Edit the semantic HTML and its embedded `personal-data` JSON together. Preserve complete scientific titles, author strings, publication types, source links and the `data-year`, `data-kind`, `data-themes`, `data-search` filter attributes. Keep citation button text and the portable JSON synchronized. Paper author records and older papers expand natively; search and clipboard copy need JavaScript.

After changing HTML or assets:

```sh
python3 scripts/version_assets.py
python3 scripts/version_assets.py --check
```

This hashes all directly referenced CSS, script, image and PDF resources so the page does not reuse stale files after deployment. Check desktop and mobile layouts and exercise changed interactions before publishing.

## CV editions

- General CV: profile, education, skills and research software first.
- Academic CV: education and selected peer-reviewed publications first.
- Research & engineering CV: technical skills and source-backed engineering projects first.

All three retain two A4 pages with selectable text, clickable links and embedded fonts. Rebuild with `python3 scripts/build_cv.py` in an environment with `reportlab` and `pypdf`. No network is needed to rebuild: all font files are bundled. The builder reads the embedded factual record and uses only the additional details documented in `docs/cv-sources.md`. It checks page overflow and verifies author/editor metadata as Haohong Zhang. Render and inspect all six pages after edits, then refresh asset hashes.

## Analytics

The existing Cloudflare Web Analytics beacon is preserved. Its site token is a public identifier. Blocking extensions or network restrictions can prevent analytics requests; dashboard access remains with the owner's account.
