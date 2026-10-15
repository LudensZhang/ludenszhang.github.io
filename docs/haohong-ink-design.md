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

## Project icon refinement — 15 October 2026

Scope corrected at the owner's request: retain Claude's original animated hero, MGM2 SVG schematic, all layout, CSS and JavaScript from commit `dacd116`. The final HTML differs from that baseline only in the six project-icon resource URLs. Earlier large-raster replacements and added motion overlays were reverted; unused large-raster assets were removed.

Six conceptual project identifiers were generated with Codex's built-in image tool, as transparent 1280 × 1280 PNGs. The local gpt-image CLI/API key was unavailable; no CLI model override was made. Final website files are 256 × 256 WebP images with alpha preserved (cwebp quality 90, alpha quality 100). Their combined size is 82,276 bytes. Each renders at the unchanged 56 × 56 CSS size with Claude's original hover effect. No original logos or scientific results were copied; these are illustrative identifiers for existing repository descriptions.

Prompt craft follows the Haohong Ink palette and coordinated visual-weight guidance, informed by the gpt-image identity gallery and craft guide. Full prompts are below.

### mgm2

Asset: `assets/ink/icons/mgm2.webp`

Use case: logo-brand. Create ONE original, polished scientific software icon, square 1024x1024 canvas, genuine TRANSPARENT BACKGROUND. For a warm ivory/navy academic website. NOT an app tile. Style: precise two-dimensional editorial line emblem, masterfully balanced geometrical curves, exceptionally clear silhouette and ample negative space. Optimize to remain readable at only 56 pixels. Smooth rounded stroke ends and joins. Uniform outline stroke about 28 pixels on this 1024 canvas. Lines in muted navy blue #314E93, optional very pale blue interior fills, and only ONE small restrained gold #E9BA35 detail. The symbol should occupy roughly 80 percent of the canvas, centered optically, with safe margins and no cutoffs. NO text, letters, numbers, labels, signature, border, square container, gradients, shadows, glow, glass, 3D, tiny patterns or realistic textures. No generic chip pictogram. Subject: A unified microbial community representation: five elegantly differentiated rounded microbial capsules arranged around one shared open circular central hub, with sparse clean connecting curves and one gold center. A compact balanced rosette, representing integration of microbial identity and abundance. Exactly five satellites, varied size, graceful spacing.

### mgm

Asset: `assets/ink/icons/mgm.webp`

Use case: logo-brand. Create ONE original, polished scientific software icon, square 1024x1024 canvas, genuine TRANSPARENT BACKGROUND. For a warm ivory/navy academic website. NOT an app tile. Style: precise two-dimensional editorial line emblem, masterfully balanced geometrical curves, exceptionally clear silhouette and ample negative space. Optimize to remain readable at only 56 pixels. Smooth rounded stroke ends and joins. Uniform outline stroke about 28 pixels on this 1024 canvas. Lines in muted navy blue #314E93, optional very pale blue interior fills, and only ONE small restrained gold #E9BA35 detail. The symbol should occupy roughly 80 percent of the canvas, centered optically, with safe margins and no cutoffs. NO text, letters, numbers, labels, signature, border, square container, gradients, shadows, glow, glass, 3D, tiny patterns or realistic textures. No generic chip pictogram. Subject: Large-scale microbiome pretraining: three precisely aligned rounded representation layers, stacked with slight vertical offsets, connected by a simple central axis, with three large microbial token circles embedded in the top layer, only the central token gold. An architectural layered-learning emblem with clean depth implied by line geometry only.

### microvqvae

Asset: `assets/ink/icons/microvqvae.webp`

Use case: logo-brand. Create ONE original, polished scientific software icon, square 1024x1024 canvas, genuine TRANSPARENT BACKGROUND. For a warm ivory/navy academic website. NOT an app tile. Style: precise two-dimensional editorial line emblem, masterfully balanced geometrical curves, exceptionally clear silhouette and ample negative space. Optimize to remain readable at only 56 pixels. Smooth rounded stroke ends and joins. Uniform outline stroke about 28 pixels on this 1024 canvas. Lines in muted navy blue #314E93, optional very pale blue interior fills, and only ONE small restrained gold #E9BA35 detail. The symbol should occupy roughly 80 percent of the canvas, centered optically, with safe margins and no cutoffs. NO text, letters, numbers, labels, signature, border, square container, gradients, shadows, glow, glass, 3D, tiny patterns or realistic textures. No generic chip pictogram. Subject: Ordered genome tokens: one graceful S-shaped chain of six rounded rectangular protein-token modules, linked by short clean connectors with a distinct gap between modules. The last token contains a tiny gold inset. Ordered sequence and discrete tokenization, no DNA double helix, no circuit board, no random grid.

### expert-lightning

Asset: `assets/ink/icons/expert-lightning.webp`

Use case: logo-brand. Create ONE original, polished scientific software icon, square 1024x1024 canvas, genuine TRANSPARENT BACKGROUND. For a warm ivory/navy academic website. NOT an app tile. Style: precise two-dimensional editorial line emblem, masterfully balanced geometrical curves, exceptionally clear silhouette and ample negative space. Optimize to remain readable at only 56 pixels. Smooth rounded stroke ends and joins. Uniform outline stroke about 28 pixels on this 1024 canvas. Lines in muted navy blue #314E93, optional very pale blue interior fills, and only ONE small restrained gold #E9BA35 detail. The symbol should occupy roughly 80 percent of the canvas, centered optically, with safe margins and no cutoffs. NO text, letters, numbers, labels, signature, border, square container, gradients, shadows, glow, glass, 3D, tiny patterns or realistic textures. No generic chip pictogram. Subject: Microbial source tracking: three distinct small source rings at the upper left, upper center and upper right merge through three elegant smooth paths into one larger open sample ring below. A single small gold dot in the target ring. Balanced Y-like source attribution emblem; no lightning bolt.

### deepmicrocancer

Asset: `assets/ink/icons/deepmicrocancer.webp`

Use case: logo-brand. Create ONE original, polished scientific software icon, square 1024x1024 canvas, genuine TRANSPARENT BACKGROUND. For a warm ivory/navy academic website. NOT an app tile. Style: precise two-dimensional editorial line emblem, masterfully balanced geometrical curves, exceptionally clear silhouette and ample negative space. Optimize to remain readable at only 56 pixels. Smooth rounded stroke ends and joins. Uniform outline stroke about 28 pixels on this 1024 canvas. Lines in muted navy blue #314E93, optional very pale blue interior fills, and only ONE small restrained gold #E9BA35 detail. The symbol should occupy roughly 80 percent of the canvas, centered optically, with safe margins and no cutoffs. NO text, letters, numbers, labels, signature, border, square container, gradients, shadows, glow, glass, 3D, tiny patterns or realistic textures. No generic chip pictogram. Subject: Precise microbiome research: a perfectly proportioned magnifying glass with a short rounded handle, framing two simple rounded microbial capsules, one small and one larger, and one gold observation dot. Restrained lens geometry with generous negative space. No medical cross, no cancer ribbon, no busy cellular texture.

### asd-cancer

Asset: `assets/ink/icons/asd-cancer.webp`

Use case: logo-brand. Create ONE original, polished scientific software icon, square 1024x1024 canvas, genuine TRANSPARENT BACKGROUND. For a warm ivory/navy academic website. NOT an app tile. Style: precise two-dimensional editorial line emblem, masterfully balanced geometrical curves, exceptionally clear silhouette and ample negative space. Optimize to remain readable at only 56 pixels. Smooth rounded stroke ends and joins. Uniform outline stroke about 28 pixels on this 1024 canvas. Lines in muted navy blue #314E93, optional very pale blue interior fills, and only ONE small restrained gold #E9BA35 detail. The symbol should occupy roughly 80 percent of the canvas, centered optically, with safe margins and no cutoffs. NO text, letters, numbers, labels, signature, border, square container, gradients, shadows, glow, glass, 3D, tiny patterns or realistic textures. No generic chip pictogram. Subject: Multi-omics integration and subtyping: two compact distinct inputs at top (a simple microbial ring and three short gene-expression bars) flow into a central rounded diamond bottleneck, then branch into three clearly spaced open circles beneath. The center output is gold. Elegant symmetrical compact integration emblem, clean diagram semantics.

### Verification

Compared CSS and JavaScript byte-for-byte with `dacd116`; normalized HTML comparison confirmed only project icon URLs changed. In normal browser motion mode, the hero runs Claude's `drift`, `draw`, `breathe` and `pop` animations, and the MGM2 schematic runs its original `flow` animation. All six images decoded successfully at 56 × 56 px. Desktop (1440 px) and phone (390 px) screenshots reviewed; no page overflow. Content-hash URLs verified.
