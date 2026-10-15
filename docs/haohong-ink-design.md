# Haohong Ink redesign

Updated 16 September 2026. The user requested a fresh reading of their revised
`haohong-ink` skill and a coordinated redesign of the English website and CVs.
The current skill defines visual preferences, leaving layout and imagery choices
to the content. No biographical facts were copied from its reference artwork.

## Design

- Warm ivory `#FBF8F2`, navy `#001F44`, blue `#314E93`, gray-blue `#5A6B7A`,
  thin rules `#CBD4DD`, small yellow/gold accents.
- Georgia headings and Helvetica Neue/Arial body text. The website uses local
  fonts; the PDFs embed Georgia and Arial when available.
- Asymmetric editorial hero, compact profile, horizontal latest-paper strip.
- Desktop About groups the heading with education beside the biography and CV
  links. Mobile follows a single-column reading order.
- Numbered publication rows retain full citations and concise keyword lists.
  The native archive disclosure uses two centered CSS bars for its plus icon.
- Each repository has one linked surface and one visible repository cue.
- Three two-page CVs retain their factual record and different reading priorities.
  Their ivory pages, serif headings, fine rules and small gold accents match the site.

## Artwork provenance

`research-network.jpg` was generated with the built-in image generation tool for
this redesign, then exported as a 1000 × 667 JPEG. It is decorative, with empty
alternative text; it does not assert an experimental result or model architecture.

Generation prompt:

> Create a refined editorial scientific decorative illustration for an English academic personal website. Landscape 3:2 composition. Completely uniform warm ivory background #FBF8F2. Airy abstract sweeping crescent of sparse networks, fine curved navy and research-blue lines (#001F44, #314E93), small separated circular nodes, only four tiny warm gold #E9BA35 accent nodes. Linework delicate yet clear, like precision pen on ivory paper, flat 2D editorial illustration, no 3D or glass, no glow, no shadows, no texture. The crescent sweeps from lower-left to upper-right with wide empty spaces within and around it; center slightly right. A subtle biological-community feeling from the organic geometry, but NOT an experimental figure or model architecture. No text, no numbers, no logos, no watermark, no border, no axis, no legend. At actual website size about 440x300 the lines should remain visible, highly restrained academic identity visual.

The six line icons use coordinated 64 px canvases and blue strokes with small gold
accents. MGM2, MGM and DeepMicroCancer adapt the skill's compute, community and
cell illustrations. MicroVQVAE shows ordered discrete tokens; EXPERT-lightning
shows source nodes converging on a sample; ASD-cancer shows two modalities joining
before subtype separation. These are conceptual identifiers, not scientific figures.
Earlier glass artwork remains archived in `assets/projects/`.

## Verification

- Desktop (1440 px) and mobile (390 px) browser inspection: hero, About,
  publications and repository layout; no horizontal page overflow.
- All six project icons load; publication keywords use the intended flex layout.
- Native disclosure opens and closes using Enter; visible keyboard focus retained.
- All six PDF pages rendered and visually inspected for clipping and overflow.
- Local asset references use content hashes, including PDFs and new artwork.
- No external font service, build system or backend required for GitHub Pages.

## Structural redesign — 13 October 2026

A full rebuild of the homepage structure and stylesheet in the same Haohong Ink palette:

- **Hero:** editorial cover with an oversized Georgia name, a “New · MGM2 v2” announcement, and an inline-SVG network (nodes on three orbits around a gold core). It replaces the JPEG, which showed a darker rectangle under `mix-blend-mode:multiply`. Below the hero, a masthead strip lists profile, group, focus and record.
- **Rhythm:** numbered section labels (01–05), ink top rules on every list and grid, hairlines inside. Research uses a tinted band, and MGM2 is the page's single deep-navy band with an ivory line schematic and Georgia figures.
- **Research:** a 2×2 grid; each direction has a line icon and tags naming related work.
- **Publications:** five selected entries with large numerals and a gold hover rule; the remaining 20 are in a disclosure with optional filters.
- **Code:** a shared-border 3×2 grid. **Footer:** a large serif sign-off and a ruled link list.
- **Motion:** stroke draw-in for the hero, a dashed flow in the schematic, below-the-fold reveals and a header reading-progress line. All of it is disabled under `prefers-reduced-motion`; content never depends on JavaScript.
- Verified at 1440 px and 375 px: no horizontal page overflow. On phones the schematic scrolls inside its card.

## Logo and icon consistency — 13 October 2026

- The owner-supplied HZ logo was traced to SVG with sub-pixel contours and simplification (3 shapes plus the gold square). It is used in the navigation, favicon, touch icon and CV headers.
- Icon audit: all project icons use a 1.7 stroke on a 64 grid, and research icons use 1.3 on a 48 grid. Both render at about 1.5 px at their display sizes of 56 px. Removed fixed `width`/`height` attributes from three icons.
- Project cards no longer switch to a white background on hover, which had exposed the MGM2 icon's ivory node fills. Hover now shows a gold top rule instead.
- Research icon I: removed the stand that read as a lamp and replaced it with three input nodes. Icon III: the gene arrows now point the same way with gaps, reading as a gene cluster above a peptide chain.

## Abstract identity refinement — 15 October 2026

At the owner's request, use abstract research/project marks. The earlier literal microbe/stack/magnifier candidates were superseded. Scope is limited to six project icons and the four small icons in section 02. All CSS, JavaScript, animated hero, animated MGM2 schematic, layout, publications, CVs, links and interactions remain from Claude commit `dacd116`.

Official repository READMEs were retrieved again through the GitHub API on 15 October. Marks are conceptual identities derived from the following functions, not literal architecture diagrams or scientific evidence:

| Project | Verified concept | Abstract identity | Source |
| --- | --- | --- | --- |
| MGM2 | Microbial identity and abundance combined into a community state | Two complementary bands forming one shared core | [Repository](https://github.com/HUST-NingKang-Lab/MGM2) |
| MGM | Abundance-ranked genus tokens and causal language-model pretraining | Ordered segments continuing toward a gold next element | [Repository](https://github.com/HUST-NingKang-Lab/MGM) |
| MicroVQVAE | Context-aware protein embeddings quantized into discrete genome tokens | A continuous arc transitioning into separated square segments | [Repository](https://github.com/HUST-NingKang-Lab/MicroVQVAE) |
| EXPERT-lightning | Ontology-aware transfer learning to quantify microbial source contributions | Different arc lengths forming a source-signature ring | [Repository](https://github.com/LudensZhang/EXPERT-lightning) |
| DeepMicroCancer | Random-forest classifiers and transfer learning for cancer-type prediction | An interlocking branching ensemble with one highlighted branch | [Repository](https://github.com/HUST-NingKang-Lab/DeepMicroCancer) |
| ASD-cancer | Autoencoder-derived latent features and survival subtype separation | A compressed ribbon opening into distinct lower lobes | [Repository](https://github.com/HUST-NingKang-Lab/ASD-cancer) |

Section 02 uses a shared core for foundation models, phase progression for community dynamics, a folded sequence with a discovered element for functional discovery, and paired forms linked across a shared bridge for cross-cohort learning. This matches the owner's preference for project-style abstract symbols rather than explanatory miniatures.

Generated with the built-in Codex image tool, one request per mark, on transparent 1280 × 1280 PNG canvases. The local gpt-image CLI/API key was unavailable; no CLI model override was made. Final WebP assets preserve alpha at 256 × 256 (cwebp quality 90, alpha quality 100), totaling 81,412 bytes. Ten displayed icon boxes retain the original 56 × 56 px size. Style uses Haohong Ink blue and one small gold accent; no third-party mark was used as an image reference.

### Prompts

**mgm2** — `assets/ink/icons/mgm2.webp`

Use case: logo-brand. Create a single elegant ABSTRACT RESEARCH BRAND MARK on a square transparent canvas. It will render at 56px on an ivory academic website. It must look like an original modern research-project identity, not a clip-art pictogram or a model architecture diagram. Use an extremely economical single coherent geometric silhouette, generous negative space, smooth precise ribbon-like contours, uniform monoline about 26px on a 1024px canvas, centered within 12% safe margins. Matte flat muted blue #314E93 only, with ONE short gold #E9BA35 accent segment. No pale shaded fill, no gradients, textures, shadows, glass, 3D, tile or enclosing box, lettering, numbers, arrows, text, cartoon bacteria, double-helix stock symbols, brain, microscope, magnifier or chip. Visually sophisticated, calm, optically balanced and memorable. Conceptual brief: MGM2 integrates microbial identity and abundance into one contextual community state. The abstract mark is TWO complementary curved bands, one smoothly continuous and one gently stepped, interweaving into one open circular core with a gold shared junction. Use a compact harmonious interlocking-loop motif, one clear negative-space center; suggests two information types forming a shared community representation. No individual organisms, node-network or petals.

**mgm** — `assets/ink/icons/mgm.webp`

Use case: logo-brand. Create a single elegant ABSTRACT RESEARCH BRAND MARK on a square transparent canvas. It will render at 56px on an ivory academic website. It must look like an original modern research-project identity, not a clip-art pictogram or a model architecture diagram. Use an extremely economical single coherent geometric silhouette, generous negative space, smooth precise ribbon-like contours, uniform monoline about 26px on a 1024px canvas, centered within 12% safe margins. Matte flat muted blue #314E93 only, with ONE short gold #E9BA35 accent segment. No pale shaded fill, no gradients, textures, shadows, glass, 3D, tile or enclosing box, lettering, numbers, arrows, text, cartoon bacteria, double-helix stock symbols, brain, microscope, magnifier or chip. Visually sophisticated, calm, optically balanced and memorable. Conceptual brief: MGM is causal language modeling on abundance-ranked microbial tokens. Build a distinctive compact abstract mark from THREE rounded bars of progressively decreasing lengths, arranged along one gently rising curved baseline, followed by a small fourth gold bar. The overall silhouette should feel like a forward-unfolding ordered sequence, not a bar chart or a database stack. No axes, circles, diagrams or microbes.

**microvqvae** — `assets/ink/icons/microvqvae.webp`

Use case: logo-brand. Create a single elegant ABSTRACT RESEARCH BRAND MARK on a square transparent canvas. It will render at 56px on an ivory academic website. It must look like an original modern research-project identity, not a clip-art pictogram or a model architecture diagram. Use an extremely economical single coherent geometric silhouette, generous negative space, smooth precise ribbon-like contours, uniform monoline about 26px on a 1024px canvas, centered within 12% safe margins. Matte flat muted blue #314E93 only, with ONE short gold #E9BA35 accent segment. No pale shaded fill, no gradients, textures, shadows, glass, 3D, tile or enclosing box, lettering, numbers, arrows, text, cartoon bacteria, double-helix stock symbols, brain, microscope, magnifier or chip. Visually sophisticated, calm, optically balanced and memorable. Conceptual brief: MicroVQVAE quantizes continuous context-aware protein/genome representations into discrete genome tokens. One smooth blue ribbon curves into three separated small rounded-square segments along the SAME arc; the terminal segment is gold. A continuous-to-discrete transformation expressed as a single compact broken-loop emblem, with clearly intentional equal spacing and generous negative space. No arrows, DNA helix, codebook table or chart.

**expert-lightning** — `assets/ink/icons/expert-lightning.webp`

Use case: logo-brand. Create a single elegant ABSTRACT RESEARCH BRAND MARK on a square transparent canvas. It will render at 56px on an ivory academic website. It must look like an original modern research-project identity, not a clip-art pictogram or a model architecture diagram. Use an extremely economical single coherent geometric silhouette, generous negative space, smooth precise ribbon-like contours, uniform monoline about 26px on a 1024px canvas, centered within 12% safe margins. Matte flat muted blue #314E93 only, with ONE short gold #E9BA35 accent segment. No pale shaded fill, no gradients, textures, shadows, glass, 3D, tile or enclosing box, lettering, numbers, arrows, text, cartoon bacteria, double-helix stock symbols, brain, microscope, magnifier or chip. Visually sophisticated, calm, optically balanced and memorable. Conceptual brief: EXPERT quantifies mixture-source contributions with ontology-aware transfer learning. A fingerprint-like abstract ring of THREE concentric offset arcs with clearly different arc lengths, aligned at a common radial opening; a short gold arc marks one contribution. The composition suggests identifying proportional origins within a mixture. A refined source-signature emblem, not a pie chart, Y junction, map pin or network.

**deepmicrocancer** — `assets/ink/icons/deepmicrocancer.webp`

Use case: logo-brand. Create a single elegant ABSTRACT RESEARCH BRAND MARK on a square transparent canvas. It will render at 56px on an ivory academic website. It must look like an original modern research-project identity, not a clip-art pictogram or a model architecture diagram. Use an extremely economical single coherent geometric silhouette, generous negative space, smooth precise ribbon-like contours, uniform monoline about 26px on a 1024px canvas, centered within 12% safe margins. Matte flat muted blue #314E93 only, with ONE short gold #E9BA35 accent segment. No pale shaded fill, no gradients, textures, shadows, glass, 3D, tile or enclosing box, lettering, numbers, arrows, text, cartoon bacteria, double-helix stock symbols, brain, microscope, magnifier or chip. Visually sophisticated, calm, optically balanced and memorable. Conceptual brief: DeepMicroCancer uses random forests and transfer learning for microbiome-based cancer classification. An abstract branching-ensemble identity: THREE very economical branching strokes interlock to form one compact open circular canopy, with a single gold terminal branch. The negative space should suggest multiple decisions converging to one coherent identity. No literal evergreen trees, forests, health shields, medical symbols or magnifier. It must be a clean research logo rather than a decision-tree diagram.

**asd-cancer** — `assets/ink/icons/asd-cancer.webp`

Use case: logo-brand. Create a single elegant ABSTRACT RESEARCH BRAND MARK on a square transparent canvas. It will render at 56px on an ivory academic website. It must look like an original modern research-project identity, not a clip-art pictogram or a model architecture diagram. Use an extremely economical single coherent geometric silhouette, generous negative space, smooth precise ribbon-like contours, uniform monoline about 26px on a 1024px canvas, centered within 12% safe margins. Matte flat muted blue #314E93 only, with ONE short gold #E9BA35 accent segment. No pale shaded fill, no gradients, textures, shadows, glass, 3D, tile or enclosing box, lettering, numbers, arrows, text, cartoon bacteria, double-helix stock symbols, brain, microscope, magnifier or chip. Visually sophisticated, calm, optically balanced and memorable. Conceptual brief: ASD-cancer extracts latent features with autoencoders and separates survival subtypes. A single continuous blue ribbon pinches narrowly at its center, then opens into THREE clean separated curved lobes below; one short interior arc is gold. A compact abstract compression-and-separation emblem with graceful negative space. Not an hourglass object, not a flowchart, no input icons, circles connected by lines or survival plot.

**research-foundation** — `assets/ink/icons/research-foundation.webp`

Use case: logo-brand. Create a single elegant ABSTRACT RESEARCH BRAND MARK on a square transparent canvas. It will render at 56px on an ivory academic website. It must look like an original modern research-project identity, not a clip-art pictogram or a model architecture diagram. Use an extremely economical single coherent geometric silhouette, generous negative space, smooth precise ribbon-like contours, uniform monoline about 26px on a 1024px canvas, centered within 12% safe margins. Matte flat muted blue #314E93 only, with ONE short gold #E9BA35 accent segment. No pale shaded fill, no gradients, textures, shadows, glass, 3D, tile or enclosing box, lettering, numbers, arrows, text, cartoon bacteria, double-helix stock symbols, brain, microscope, magnifier or chip. Visually sophisticated, calm, optically balanced and memorable. Conceptual brief: Research direction: reusable representations learned from diverse microbiome data support multiple downstream questions. An open central core formed by THREE gently interlocking broad arcs, unified by a small gold shared hinge. A coherent abstract foundation-and-generality emblem, radial balance, no layer stack, nodes, network or organisms. Distinct from a two-band interlock: this has three equal-weight arcs.

**research-dynamics** — `assets/ink/icons/research-dynamics.webp`

Use case: logo-brand. Create a single elegant ABSTRACT RESEARCH BRAND MARK on a square transparent canvas. It will render at 56px on an ivory academic website. It must look like an original modern research-project identity, not a clip-art pictogram or a model architecture diagram. Use an extremely economical single coherent geometric silhouette, generous negative space, smooth precise ribbon-like contours, uniform monoline about 26px on a 1024px canvas, centered within 12% safe margins. Matte flat muted blue #314E93 only, with ONE short gold #E9BA35 accent segment. No pale shaded fill, no gradients, textures, shadows, glass, 3D, tile or enclosing box, lettering, numbers, arrows, text, cartoon bacteria, double-helix stock symbols, brain, microscope, magnifier or chip. Visually sophisticated, calm, optically balanced and memorable. Conceptual brief: Research direction: microbial community states evolve over time, with context-aware forecasting and digital twins. TWO smooth offset crescent sweeps follow the same elliptical trajectory; one reaches farther forward and ends in a short gold continuation. A compact abstract phase-progression emblem, visibly suggests motion and evolving states. No chart axes, time labels, circles, clock, arrowheads or orbits around a nucleus.

**research-function** — `assets/ink/icons/research-function.webp`

Use case: logo-brand. Create a single elegant ABSTRACT RESEARCH BRAND MARK on a square transparent canvas. It will render at 56px on an ivory academic website. It must look like an original modern research-project identity, not a clip-art pictogram or a model architecture diagram. Use an extremely economical single coherent geometric silhouette, generous negative space, smooth precise ribbon-like contours, uniform monoline about 26px on a 1024px canvas, centered within 12% safe margins. Matte flat muted blue #314E93 only, with ONE short gold #E9BA35 accent segment. No pale shaded fill, no gradients, textures, shadows, glass, 3D, tile or enclosing box, lettering, numbers, arrows, text, cartoon bacteria, double-helix stock symbols, brain, microscope, magnifier or chip. Visually sophisticated, calm, optically balanced and memorable. Conceptual brief: Research direction: functional discovery from genomic context, biosynthetic gene clusters and peptides. THREE adjoining folded chevron-ribbon segments form one compact angular open curve; a single small gold diamond emerges from the open end as a discovered feature. Sophisticated abstract sequence-to-function emblem. No DNA stock symbol, molecule ball-and-stick, magnifying glass, literal sparkle/star, genome track, arrows or chart.

**research-transfer** — `assets/ink/icons/research-transfer.webp`

Use case: logo-brand. Create a single elegant ABSTRACT RESEARCH BRAND MARK on a square transparent canvas. It will render at 56px on an ivory academic website. It must look like an original modern research-project identity, not a clip-art pictogram or a model architecture diagram. Use an extremely economical single coherent geometric silhouette, generous negative space, smooth precise ribbon-like contours, uniform monoline about 26px on a 1024px canvas, centered within 12% safe margins. Matte flat muted blue #314E93 only, with ONE short gold #E9BA35 accent segment. No pale shaded fill, no gradients, textures, shadows, glass, 3D, tile or enclosing box, lettering, numbers, arrows, text, cartoon bacteria, double-helix stock symbols, brain, microscope, magnifier or chip. Visually sophisticated, calm, optically balanced and memorable. Conceptual brief: Research direction: knowledge transfers across cohorts and regions while aligning shared structure. TWO mirrored open-loop blue forms face each other with a short gold bridge at their shared center, forming a balanced horizontally interwoven abstract link. Make the common connection unmistakable without arrows. A concise cross-domain alignment mark. No people, geographic globes, maps, bacteria, charts or connected data nodes.

### Verification

CSS and JavaScript compared byte-for-byte with `dacd116`; normalizing only the ten icon tags made HTML identical to that baseline. In normal motion mode, Claude's hero runs `drift`, `draw`, `breathe`, and `pop`, and its MGM2 schematic retains `flow`. All ten WebP images decoded at 56 × 56 px. Desktop and phone screenshots were reviewed for section 02 and project cards; no horizontal overflow. Asset hash checks passed.
