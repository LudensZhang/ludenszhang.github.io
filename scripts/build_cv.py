#!/usr/bin/env python3
"""Build three linked, two-page CVs from homepage content and verified additions.

Requires reportlab. Run from any directory. No network access.
Research provenance: docs/cv-sources.md. Add new personal details here only when
confirmed by the owner or supported by the recorded public sources.
"""
from pathlib import Path
from html import escape, unescape
import re
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'assets/cv'
OUT.mkdir(parents=True, exist_ok=True)
source = (ROOT / 'index.html').read_text()
W, H = A4
M = 45
CW = W - 2 * M
INK, MUTED, BLUE, SURFACE, LINE = '#1d1d1f', '#6e6e73', '#0066cc', '#f5f5f7', '#d2d2d7'
FONT, BOLD = 'Helvetica', 'Helvetica-Bold'
font_dir = Path('/System/Library/Fonts/Supplemental')
if (font_dir / 'Arial.ttf').exists():
    pdfmetrics.registerFont(TTFont('CVSans', str(font_dir / 'Arial.ttf')))
    pdfmetrics.registerFont(TTFont('CVSans-Bold', str(font_dir / 'Arial Bold.ttf')))
    pdfmetrics.registerFontFamily('CVSans', normal='CVSans', bold='CVSans-Bold', italic='CVSans', boldItalic='CVSans-Bold')
    FONT, BOLD = 'CVSans', 'CVSans-Bold'

def clean(text):
    return re.sub(r'\s+', ' ', text.replace('↗', '').replace('—', '-').replace('–', '-').replace('’', "'")).strip()

def link(text, url):
    return f'<a href="{escape(url, quote=True)}" color="{BLUE}">{escape(text)}</a>'

def text(fragment):
    return clean(unescape(re.sub(r'<[^>]+>', '', fragment)))

papers = []
for entry in re.findall(r'<article class="paper">(.*?)</article>', source, re.S):
    href, title = re.search(r'<h3><a href="([^"]+)"[^>]*>(.*?)</a></h3>', entry, re.S).groups()
    citation = re.search(r'<p class="paper-authors">(.*?)</p>', entry, re.S)[1]
    year = re.search(r'<div class="paper-kicker"><span>(.*?)</span>', entry)[1]
    keywords = re.findall(r'<li>(.*?)</li>', entry)
    papers.append(dict(title=text(title),url=unescape(href),citation=text(citation),year=year,keywords=' / '.join(map(text,keywords))))
doi_order = ['10.1002/advs.202513333', '10.1128/msystems.01395-24', '10.1016/j.isci.2024.109294', '10.1093/bib/bbac629']
selected = [next(p for p in papers if doi in p['url']) for doi in doi_order]
preprints = papers[:2]
projects = []
for href, body in re.findall(r'<a class="project" href="([^"]+)"[^>]*>(.*?)</a>', source, re.S):
    projects.append(dict(name=text(re.search(r'<h3>(.*?)</h3>',body,re.S)[1]),description=text(re.search(r'<p>(.*?)</p>',body,re.S)[1]),url=unescape(href)))
personal = [
    dict(name='Nucleotide Transformer fine-tuning', url='https://github.com/LudensZhang/nt_gtdb', description='GTDB genome preprocessing and masked-language-model fine-tuning with Hugging Face Transformers and Datasets; configurable learning-rate schedules, tokenization and evaluation.'),
    dict(name='EXPERT-lightning', url='https://github.com/LudensZhang/EXPERT-lightning', description='Transfer learning for context-aware microbial source tracking, with a Python package, command-line interface and biome ontology.'),
    dict(name='Genome representation learning', url='https://github.com/LudensZhang/BGC', description='PyTorch discrete variational autoencoder training, reconstruction and regularization objectives, validation, early stopping and TensorBoard logging.'),
    dict(name='BriskyPCoA', url='https://github.com/LudensZhang/BriskyPCoA', description='Command-line PCA and PCoA visualization of microbial abundance profiles using NumPy, pandas, SciPy, scikit-learn, scikit-bio and plotnine.'),
]

class CV:
    def __init__(self, slug, label):
        self.path = OUT / f'Haohong-Zhang-CV{slug}.pdf'
        self.c = canvas.Canvas(str(self.path), pagesize=A4, pageCompression=1, invariant=1)
        self.c.setTitle(f'Haohong Zhang | {label}')
        self.c.setAuthor('Haohong Zhang')
        self.c.setSubject('Bioinformatics, microbiome foundation models and AI for biology')
        self.label, self.page, self.y = label, 0, 0

    def para(self, text, size=10, leading=14, color=INK, bold=False, gap=5, x=M, width=CW):
        style = ParagraphStyle('cv', fontName=BOLD if bold else FONT, fontSize=size, leading=leading, textColor=HexColor(color))
        p = Paragraph(text, style)
        _, height = p.wrap(width, H)
        if self.y + height > H - 55:
            raise ValueError(f'{self.label} page {self.page} overflow: {text[:70]} at {self.y}')
        p.drawOn(self.c, x, H - self.y - height)
        self.y += height + gap

    def new_page(self, first=False):
        if self.page:
            self.footer()
            self.c.showPage()
        self.page += 1
        self.y = 42
        if first:
            self.para('Haohong Zhang', size=34, leading=39, bold=True, gap=4)
            self.para('Bioinformatics  /  Foundation models  /  AI for biology', 11, 15, BLUE, gap=10)
            self.para('Ph.D. student · Huazhong University of Science and Technology · Wuhan, China', 9, 13, MUTED, gap=4)
            self.para(link('haohongzh@gmail.com', 'mailto:haohongzh@gmail.com') + ' &nbsp; · &nbsp; ' + link('ludenszhang.github.io', 'https://ludenszhang.github.io/') + ' &nbsp; · &nbsp; ' + link('GitHub', 'https://github.com/LudensZhang') + ' &nbsp; · &nbsp; ' + link('Scholar', 'https://scholar.google.com/citations?user=e12kCmAAAAAJ&hl=en'), 9, 13, gap=3)
            self.para(link('ORCID 0000-0001-6267-4244', 'https://orcid.org/0000-0001-6267-4244'), 9, 12, gap=12)
        else:
            self.para('Haohong Zhang', 19, 23, bold=True, gap=3)
            self.para(self.label, 10, 14, MUTED, gap=12)

    def section(self, text):
        self.y += 8
        self.c.setFillColor(HexColor(BLUE))
        self.c.roundRect(M, H-self.y-13, 3, 13, 1.5, fill=1, stroke=0)
        self.para(text, 12.5, 17, bold=True, gap=10, x=M+12, width=CW-12)

    def summary(self, industry=False):
        text = ('Researcher working at the intersection of biological data and machine learning, with public code spanning transformer fine-tuning, discrete genome representations, microbial source tracking and scientific data visualization.' if industry else 'I develop foundation models and interpretable machine learning methods for microbiome research, connecting microbial communities, genome representations and multi-omics data with biological questions.')
        self.para(text, 10.5, 15, MUTED, gap=7)

    def education(self):
        self.section('Education')
        self.para('<b>2023 - Present &nbsp; Ph.D. in Bioinformatics</b> · Direct-track', 10, 14, gap=2)
        self.para("Huazhong University of Science and Technology · Advisor: Prof. Kang Ning", 9.5, 13, MUTED, gap=8)
        self.para('<b>2019 - 2023 &nbsp; Bachelor of Science</b>', 10, 14, gap=2)
        self.para('Huazhong University of Science and Technology · Dengfeng Program, Class of 1901', 9.5, 13, MUTED, gap=4)

    def skills(self):
        self.section('Technical skills')
        rows = [('Machine learning', 'Python, PyTorch, PyTorch Lightning, Hugging Face Transformers and Datasets; masked language modeling, transfer learning and autoencoders.'), ('Biological data', 'Biopython, FASTA processing, genome dataset preparation, microbiome abundance profiles and discrete sequence representations.'), ('Analysis & tooling', 'NumPy, pandas, SciPy, scikit-learn, scikit-bio, plotnine; PCA/PCoA, command-line tools, Python packaging and TensorBoard.')]
        for title, body in rows:
            self.para(f'<b>{title}.</b> {escape(body)}', 9.5, 13.3, gap=5)

    def project_list(self, entries=projects, title='Research software'):
        self.section(title)
        for p in entries:
            self.para('<b>'+escape(p['name'])+'</b> &nbsp; '+link('Repository', p['url']), 10, 13.5, gap=2)
            self.para(escape(p['description']), 9.5, 13.2, MUTED, gap=8)

    def publications(self, entries, title):
        self.section(title)
        for p in entries:
            self.para('<b>'+escape(p['title'])+'</b>', 10, 13.5, gap=3)
            citation = escape(p['citation']).replace('H Zhang', '<b>H Zhang</b>')
            self.para(citation + f" ({p['year']}).", 9, 12.3, MUTED, gap=3)
            self.para(link(p['url'].removeprefix('https://doi.org/'), p['url']), 8.8, 12, gap=3)
            self.para(escape(p['keywords']), 8.3, 11.3, MUTED, gap=10)

    def conference(self):
        self.section('Conference presentation')
        self.para('<b>A discrete token language of prokaryotic genomes learned by MicroVQVAE</b>', 10, 13.5, gap=3)
        self.para('Haohong Zhang, Kang Ning · Poster, Cold Spring Harbor Asia: AI and Biology.<br/>April 20-24, 2026 · Suzhou, China.', 9.5, 13, MUTED, gap=3)
        self.para(link('Conference program · Poster 41', 'https://www.csh-asia.org/upload/aaibioprogram2026.pdf'), 9, 12, gap=5)

    def honors(self):
        self.section('Honors')
        self.para('<b>Outstanding Graduate, 2023</b> · Huazhong University of Science and Technology', 9.5, 13, gap=3)

    def footer(self):
        c = self.c
        c.setStrokeColor(HexColor(LINE)); c.setLineWidth(.45)
        c.line(M, 39, W-M, 39)
        c.setFillColor(HexColor(MUTED)); c.setFont(FONT, 8)
        c.drawString(M, 25, f'{self.label} · Updated September 2026')
        c.drawRightString(W-M, 25, f'{self.page} / 2')

    def finish(self):
        self.footer(); self.c.save(); print(self.path)

general = CV('', 'Curriculum vitae')
general.new_page(first=True); general.summary(); general.education(); general.skills(); general.project_list()
general.new_page(); general.publications(selected, 'Selected peer-reviewed publications'); general.publications(preprints, 'Preprints'); general.conference(); general.honors(); general.finish()

academic = CV('-Academic', 'Academic CV')
academic.new_page(first=True); academic.education(); academic.publications(selected, 'Selected peer-reviewed publications'); academic.honors()
academic.new_page(); academic.publications(preprints, 'Preprints'); academic.conference(); academic.project_list(); academic.skills(); academic.finish()

industry = CV('-Research-Engineer', 'Research & engineering CV')
industry.new_page(first=True); industry.summary(industry=True); industry.skills(); industry.project_list(personal, 'Selected engineering projects'); industry.education()
industry.new_page(); industry.publications(selected[:2], 'Selected peer-reviewed research'); industry.publications(preprints, 'Preprints'); industry.conference(); industry.honors()
industry.section('Further research'); industry.para('Research software includes MGM2, MGM, MicroVQVAE, DeepMicroCancer and ASD-cancer. '+link('Explore projects and full bibliography', 'https://ludenszhang.github.io/'), 10, 14); industry.finish()
