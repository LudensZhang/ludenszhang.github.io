---
author: Haohong Zhang
last_modified_by: Haohong Zhang
updated: 2026-10-25
---

# CV sources and editorial scope

Content verified 10 September 2026; visual design updated 25 October 2026. Three English versions share the same factual record:
general CV, academic CV, and research/engineering CV. Each is two A4 pages.

## Sources

- Existing owner-maintained homepage and `SOURCES.md`: education dates, degree names, advisor, affiliation, contact information, selected papers and lab projects. No expected Ph.D. completion date was inferred.
- [HUST News](https://news.hust.edu.cn/info/1002/47567.htm): indexed university article explicitly identifies Zhang Haohong as an undergraduate in Dengfeng Program Class 1901 and links him to the life-trajectory paper. English program wording is a translation; no major beyond the owner's stated Bachelor of Science was inferred.
- [HUST College of Life Science and Technology notice](https://life.hust.edu.cn/life/info/1057/14815.htm), 17 May 2023: lists 张皓鸿 among the 2023 Outstanding Graduate awardees. The public notice is the award evidence.
- [Cold Spring Harbor Asia 2026 AI and Biology program](https://www.csh-asia.org/upload/aaibioprogram2026.pdf): poster-session entry 41, PDF page 9, lists “A discrete token language of prokaryotic genomes learned by MicroVQVAE”, Haohong Zhang and Kang Ning, HUST affiliation. Conference dates: 20-24 April 2026. This is a poster entry, not an invited oral talk.
- [nt_gtdb training](https://github.com/LudensZhang/nt_gtdb) and [repository](https://github.com/LudensZhang/nt_gtdb): inspected `mlm_finetune.py` and `create_datasets.py` through GitHub's contents API; evidence for PyTorch, Hugging Face Transformers/Datasets, masked-language-model fine-tuning, learning-rate scheduling, tokenization, Biopython FASTA processing, genome-level train/validation/test dataset preparation and pandas.
- [EXPERT-lightning](https://github.com/LudensZhang/EXPERT-lightning): source tracking and PyTorch Lightning implementation; inspected `setup.py`, which names Hui Chong and Haohong Zhang as authors and defines a package and CLI entry point. Package authorship is not represented as sole ownership.
- [BGC](https://github.com/LudensZhang/BGC): inspected `src/dVAE/Trainer.py`; evidence for PyTorch discrete VAE training, reconstruction/regularization losses, validation, early stopping and TensorBoard. No unsupported link between this code and a specific paper is asserted.
- [BriskyPCoA](https://github.com/LudensZhang/BriskyPCoA): inspected `BriskyPCoA.py`; evidence for NumPy, pandas, SciPy, scikit-learn, scikit-bio, plotnine, PCA/PCoA and CLI development.

Skills summarize visible code use, not measured proficiency. Forked courses or repositories were excluded as standalone skill evidence. No employment history, internships, visiting positions, patents, grant income, citation metrics, review service or additional honors were inferred. Lab software is described by function without inventing individual contribution percentages or leadership titles. Journal articles and preprints are separated; the publication list is explicitly selected, with links to Scholar and the website for the full record.

## Rebuild and publish

Run `python3 scripts/build_cv.py` in an environment with `reportlab` and `pypdf`. The script reads the embedded `personal-data` publication/project JSON from `index.html`, embeds the selected Dispatch fonts bundled in `assets/dispatch/fonts/`, writes three linked PDFs under `assets/cv/`, checks page overflow and verifies final metadata. No network or platform-specific fonts are required. Then run `python3 scripts/version_assets.py` to refresh PDF references. Render and verify all six pages after substantive edits.

## October 2026 update

- Selected peer-reviewed publications now include the *Advanced Genetics* review (doi:10.1002/ggn2.70046) and mHolmes in *Nature Communications* (doi:10.1038/s41467-026-77510-3). Sources are recorded in `SOURCES.md`.
- The MGM2 preprint uses its v2 title and author list. The project description follows the website.
- The 2024 *iScience* paper was dropped from the CV's selected list to keep two pages. It remains on the website.
- Visual update to match the website: the HZ logo in the header, a gold period after the name, an ink masthead rule, numbered section heads with a gold accent, and DOI links inline with each citation.

## Dispatch selection, 25 October 2026

The user selected candidate A (Dispatch / 朱印). The three CVs now share its buff paper, black ink, vermilion links and new HZ mark, Six Caps nameplate, Bevan section heads and Archivo Narrow text. All existing substantive CV content and the distinction between journal articles and preprints are retained. The source of paper/project facts is the embedded owner-maintained JSON, which is independent of the rendered HTML layout.

The four TrueType files are static PDF instances of the same OFL-licensed families used in the browser; Archivo Narrow 400 and 600 are instantiated at their actual weights. All author, creator, producer, editor and last-modified identity fields are Haohong Zhang, including XMP creator metadata. Link annotations remain interactive. No substantive comments or revisions are removed as a metadata-cleanup shortcut. Final files are reopened and verified by the builder.
