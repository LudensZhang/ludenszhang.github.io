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


## Local visual refinements — 15 October 2026

Preserved the 13 October layout, palette, logo, research and project icons, publication data, CV files and analytics configuration. Replaced only the hero and MGM2 conceptual artwork using Codex's built-in image-generation tool. The local gpt-image CLI/API key was not configured, so no CLI call or explicit model override was made.

- `assets/ink/community-network.webp`: a fine-line community constellation on warm ivory. A CSS radial mask blends the raster edges into the page. Decorative, empty alt text.
- `assets/ink/mgm2-concept.webp`: three existing input modalities converge through a conceptual Transformer into a community representation. Explanatory labels and applications remain selectable HTML rather than raster lettering. Retains the conceptual-diagram caption; adds no performance or architecture claims.
- Both originals were generated as 1536 × 1024 PNGs. Final WebP derivatives are 1440 × 960, encoded with cwebp quality 86, totaling 137,206 bytes. A transparency-edit candidate was discarded because it introduced unwanted glow.
- Removed the phone-only 580 px schematic width. Real HTML labels fit at 320 px. Navigation now follows the section at a stable reading line on scroll and resize, correcting stale active links after jumps and viewport changes.

Prompt craft: adapted the coordinated identity approach from the gpt-image brand gallery No. 60 (@LexnLin, source https://x.com/LexnLin/status/2046952493213429886) and structured conceptual-diagram grammar from its research-figure gallery, with the owner's Haohong Ink tokens. No reference artwork or logo was copied.

### Final prompts

**hero**

Landscape 3:2 editorial scientific illustration, designed as a decorative artwork beside a large serif heading on a personal academic website. A single elegant abstract microbial community representation: a coherent softly tilted elliptical constellation made of roughly 60 tiny hollow navy nodes connected by fine precise flowing network lines, with a denser organized central core and 5 restrained gold nodes. Suggest biological diversity and learned community representations with nuanced rhythm and curvature. No literal planet, no satellite, no orbital atom symbol. Restrained scientific engraved linework, sophisticated print editorial craftsmanship, crisp contours, extremely subtle pale blue depth; no photorealism, no glass, no chunky 3D shapes. Background absolutely flat warm ivory #FBF8F2, not a rectangle with a visible border; all four edges must remain empty pure #FBF8F2 so the illustration integrates seamlessly with this page. Line palette ink navy #001F44, accent blue #314E93, a very small number of gold #E9BA35 highlights. Center the complete network silhouette within generous 12 percent margins, horizontal composition; no cropped lines. No letters, labels, title, watermark, frame, gradients or shadows.

**mgm2**

Landscape 3:2 scientific concept illustration for an academic homepage, polished editorial fine-line schematic on a completely flat solid dark navy #001F44 canvas, edges also exactly #001F44. Not a poster, no headline. Warm ivory #FBF8F2 and muted blue #9DB3D4 fine strokes, very sparse gold #FFD74B highlights. The diagram has three vertically aligned input symbols on the left: a short DNA strand, a clean relative-abundance bar motif, and three text-like sample-context lines. These THREE inputs flow through three uncluttered thin curves into ONE central softly rounded transformer stack of four layers, then into one compact community network representation on the right. Place a small cluster of nodes with varied radii as the representation. A single gold center node. The stack, inputs and community are horizontally balanced. Clear direction of flow with minimal arrowheads, no crisscrossing connectors. Precise restrained journal infographic aesthetic matching navy/ivory serif editorial website. Large shapes legible at 400 CSS pixels. CRITICAL: no text or lettering at all; all accessible explanatory labels will be placed as real HTML by the website. Do not add results, numerical measurements, new scientific claims, output task icons, decorative planets or additional modules. Keep all geometry within 10 percent outer margins. No gradients, shadows, textures, frames, logos, medical crosses, neon or 3D glass.

### Verification

Playwright checks at 320, 390, 768, 1080 and 1440 px: no page or figure overflow; correct MGM2 active state. All five navigation anchors selected their intended section. Archive journal filtering returned only journals; resetting showed all 20 archive entries. Desktop and mobile screenshots were reviewed. JavaScript syntax and content-based asset versions passed. Local console warnings came from the pre-existing Cloudflare analytics CORS behavior on localhost.

## Motion restoration - 15 October 2026

The generated raster replacements had removed the original animated network and schematic paths. Retained the new artwork and restored motion with lightweight decorative SVG overlays: gentle whole-network drift, moving signal traces, breathing gold nodes, three input streams, sequential model-layer pulses and a community-state pulse. Overlay view boxes match the image coordinates; overlays are hidden from assistive technology, ignore pointer events and introduce no layout space. CSS respects `prefers-reduced-motion`; IntersectionObserver pauses decorative loops outside the viewport.

Verification in normal motion mode compared the network transform and trace offset at different animation times, and confirmed running MGM2 flow. Offscreen pause and reduced-motion behavior passed (zero running decorative animations with reduced motion). Layout checks passed at 320, 390, 768 and 1440 px. Reviewed desktop and mobile screenshots. Existing reading-progress, scroll reveals and hover effects remain active.
