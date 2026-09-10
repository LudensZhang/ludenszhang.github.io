# Content provenance — 7 September 2026

The existing homepage is the source for the educational timeline, email, X profile, research interests, six original projects and 20 original bibliography entries. This update is a targeted verification and refresh, not an exhaustive new literature search. Original unverified bibliography details were retained; they should not be read as independently audited.

## Public sources checked

- [GitHub profile](https://github.com/LudensZhang): identity, affiliation and focus on biological foundation models.
- [ORCID 0000-0001-6267-4244](https://orcid.org/0000-0001-6267-4244): identity, bachelor's education and the two July 2026 preprints.
- [MGM2 preprint](https://www.biorxiv.org/content/10.64898/2026.07.20.739063v1.full): title, author list, preprint status, model description and lab repository. DOI: 10.64898/2026.07.20.739063.
- [MGM2 repository](https://github.com/HUST-NingKang-Lab/MGM2): current source-code destination. Replaces the older personal-account project link.
- [MetaClaw preprint](https://www.biorxiv.org/content/10.64898/2026.07.21.739769v1.full): title, author list and preprint status, corroborated by ORCID. DOI: 10.64898/2026.07.21.739769.
- [MGM, PubMed](https://pubmed.ncbi.nlm.nih.gov/41580987/): Advanced Science, 2026, 13(24), e13333; DOI: 10.1002/advs.202513333.
- [ASD cancer study, PubMed](https://pubmed.ncbi.nlm.nih.gov/39565103/): mSystems, 2024; DOI: 10.1128/msystems.01395-24. Corrected the selected entry's role label to co-first author, based on the equal-contribution note.
- [Life-trajectory paper, Oxford Academic](https://academic.oup.com/bib/article/24/1/bbac629/6984796): title, venue, DOI and identity link to ORCID.
- [Pancreatic cancer paper, PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10915599/): DOI: 10.1016/j.isci.2024.109294 and equal-contribution attribution.

## Editorial decisions

- Added MGM2 and MetaClaw as **preprints**, without presenting them as peer-reviewed journal articles.
- Kept all 20 original bibliography entries, including preprint/journal versions and conference abstracts. Four works are selected; the remaining 18 entries are in the expandable archive.
- Removed the old citation, h-index and i10-index numbers because they are dated snapshots. Google Scholar remains linked directly.
- Preserved the original Ph.D. timeline and contact information; did not infer a graduation date or add unverified personal details.
- Publication titles link directly to verified DOIs where available. Remaining entries link to Scholar searches by title.

## Correction — 8 September 2026

Verified the [MicroVQVAE repository README](https://github.com/HUST-NingKang-Lab/MicroVQVAE). MicroVQVAE is a genome foundation model that combines PAIR-esm2 protein embeddings with vector-quantized representation learning to obtain discrete, context-aware genome tokens from ordered prokaryotic protein sequences. The public repository provides the inference pipeline. Corrected the previous inaccurate microbial-community generative-model description, changed the category to “Genome foundation model”, and updated the repository URL to the lab account.

## Repository icons and links — 10 September 2026

Read the public README of each project before designing the six symbols. Following visual feedback, the initial SVG studies were replaced by generated glass sculptures with coordinated lighting, rounded silhouettes and project-specific colors. No Apple logo or proprietary symbol assets are used. Full prompts and generation details are recorded in [project-icon-prompts.md](docs/project-icon-prompts.md). These icons are conceptual illustrations of the functions below, not exact architecture diagrams.

| Project / source | Symbol rationale |
| --- | --- |
| [MGM2](https://github.com/HUST-NingKang-Lab/MGM2) | Differently sized community nodes surrounding a shared representation, reflecting identity, abundance and community embeddings. |
| [MGM](https://github.com/HUST-NingKang-Lab/MGM) | Stacked token layers for large-scale microbiome pretraining and representation learning. |
| [MicroVQVAE](https://github.com/HUST-NingKang-Lab/MicroVQVAE) | Ordered discrete blocks connected along a sequence, representing context-aware genome tokens. |
| [EXPERT-lightning](https://github.com/LudensZhang/EXPERT-lightning) | Multiple source nodes converging on one sample, reflecting microbial source attribution. |
| [DeepMicroCancer](https://github.com/HUST-NingKang-Lab/DeepMicroCancer) | A magnifying lens over microbial features, representing microbiome-based cancer classification. |
| [ASD-cancer](https://github.com/HUST-NingKang-Lab/ASD-cancer) | Two input modalities meet at an encoding bottleneck and separate into subtypes, reflecting autoencoder-based multi-omics survival subtyping. |

Updated MGM, DeepMicroCancer and ASD-cancer links to the verified lab repositories. Corrected EXPERT-lightning's broad classification/prediction description to its documented core purpose: context-aware microbial source tracking with transfer learning and biome ontology. Each project remains one linked card with a single visible “View repository” cue. Icon URLs participate in content-based asset versioning.
