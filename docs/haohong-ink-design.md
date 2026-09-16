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
