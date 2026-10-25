#!/usr/bin/env python3
"""Build three linked, two-page CVs from homepage content and verified additions.

Requires reportlab and pypdf. Run from any directory. No network access.
Research provenance: docs/cv-sources.md. Add new personal details here only when
confirmed by the owner or supported by the recorded public sources.
"""
from pathlib import Path
from html import escape, unescape
import re
import json
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'assets/cv'
OUT.mkdir(parents=True, exist_ok=True)
source = (ROOT / 'index.html').read_text()
W, H = A4
M = 45
CW = W - 2 * M
INK, MUTED, BLUE, SURFACE, LINE, GOLD = '#191612', '#544b40', '#b6321e', '#eee5ca', '#b6ab95', '#b6321e'
LOGO = ImageReader(str(ROOT / 'assets/dispatch/hz-mark.png'))
LOGO_RATIO = LOGO.getSize()[1] / LOGO.getSize()[0]
FONT, BOLD, HEADING, DISPLAY = 'DispatchText', 'DispatchBold', 'DispatchHeading', 'DispatchDisplay'
font_dir = ROOT / 'assets/dispatch/fonts'
for name, file in [(FONT,'archivonarrow-400.ttf'),(BOLD,'archivonarrow-600.ttf'),(HEADING,'bevan-400.ttf'),(DISPLAY,'sixcaps-400.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(font_dir / file)))
pdfmetrics.registerFontFamily(FONT, normal=FONT, bold=BOLD, italic=FONT, boldItalic=BOLD)

def clean(text):
    return re.sub(r'\s+', ' ', text.replace('↗', '').replace('\u2060', '').replace('—', '-').replace('–', '-').replace('’', "'")).strip()

def link(text, url):
    return f'<a href="{escape(url, quote=True)}" color="{BLUE}">{escape(text)}</a>'

def text(fragment):
    return clean(unescape(re.sub(r'<[^>]+>', '', fragment)))

data = json.loads(re.search(r'<script[^>]*id="personal-data"[^>]*>(.*?)</script>', source, re.S)[1])
papers = [dict(title=clean(p['title']),url=p['url'],citation=clean(p['authors']),year=str(p['year']),keywords=' / '.join(p['keywords'])) for p in data['papers']]

def by_doi(*dois):
    return [next(p for p in papers if doi in p['url']) for doi in dois]
selected = by_doi('10.1002/advs.202513333', '10.1002/ggn2.70046', '10.1038/s41467-026-77510-3', '10.1128/msystems.01395-24', '10.1093/bib/bbac629')
preprints = by_doi('10.64898/2026.07.20.739063', '10.64898/2026.07.21.739769')
projects = [dict(name=p['name'],description=clean(p['description']),url=p['url']) for p in data['projects']]

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
        self.c.setCreator('Haohong Zhang')
        self.c.setProducer('Haohong Zhang')
        self.c.setSubject('Bioinformatics, microbiome foundation models and AI for biology')
        self.label, self.page, self.y, self.sections = label, 0, 0, 0

    def para(self, text, size=10.5, leading=14.2, color=INK, bold=False, gap=5, x=M, width=CW, heading=False):
        style = ParagraphStyle('cv', fontName=HEADING if heading else (BOLD if bold else FONT), fontSize=size, leading=leading, textColor=HexColor(color))
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
        self.c.setFillColor(HexColor(SURFACE))
        self.c.rect(0, 0, W, H, fill=1, stroke=0)
        self.y = 36
        logo_w = 78 if first else 42
        self.c.drawImage(LOGO, W-M-logo_w, H-self.y-logo_w*LOGO_RATIO, logo_w, logo_w*LOGO_RATIO, mask='auto')
        if first:
            self.para(escape(self.label.upper()), size=10.5, leading=15, heading=True, gap=4, width=CW-94)
            style = ParagraphStyle('name',fontName=DISPLAY,fontSize=68,leading=69,textColor=HexColor(INK))
            name = Paragraph('HAOHONG ZHANG',style)
            _, nh = name.wrap(CW-94,H);name.drawOn(self.c,M,H-self.y-nh);self.y += nh+8
            self.para('Bioinformatics  /  Foundation models  /  AI for biology', 11.5, 15, BLUE, gap=6)
            self.para('Ph.D. student, Huazhong University of Science and Technology, Wuhan, China', 10, 13, MUTED, gap=4)
            self.para(link('haohongzh@gmail.com', 'mailto:haohongzh@gmail.com') + ' &nbsp; / &nbsp; ' + link('ludenszhang.github.io', 'https://ludenszhang.github.io/') + ' &nbsp; / &nbsp; ' + link('GitHub', 'https://github.com/LudensZhang') + ' &nbsp; / &nbsp; ' + link('Scholar', 'https://scholar.google.com/citations?user=e12kCmAAAAAJ&hl=en') + ' &nbsp; / &nbsp; ' + link('ORCID 0000-0001-6267-4244', 'https://orcid.org/0000-0001-6267-4244'), 9.5, 13, gap=12)
        else:
            style = ParagraphStyle('running-name',fontName=DISPLAY,fontSize=36,leading=39,textColor=HexColor(INK))
            name = Paragraph('HAOHONG ZHANG',style);_, nh=name.wrap(CW-60,H);name.drawOn(self.c,M,H-self.y-nh);self.y+=nh+3
            self.para(self.label,10,14,MUTED,gap=10)
        self.c.setStrokeColor(HexColor(INK)); self.c.setLineWidth(2)
        self.c.line(M, H-self.y, W-M, H-self.y)
        self.y += 7

    def section(self, text):
        self.sections += 1
        self.y += 12
        self.para(escape(text.upper()), 11.2, 16, INK, heading=True, gap=5)
        self.c.setStrokeColor(HexColor(BLUE)); self.c.setLineWidth(.7)
        self.c.line(M, H-self.y, W-M, H-self.y)
        self.y += 9

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
            doi = link('doi:' + p['url'].removeprefix('https://doi.org/'), p['url'])
            self.para(citation + f" ({p['year']}). &nbsp;" + doi, 9, 12.3, MUTED, gap=3)
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
        c.drawString(M, 25, f'Haohong Zhang / {self.label} / Updated 25 October 2026')
        c.drawRightString(W-M, 25, f'{self.page} / 2')

    def finish(self):
        self.footer(); self.c.save()
        # Final metadata and annotation attribution are checked after export.
        from pypdf import PdfReader, PdfWriter
        from pypdf.generic import NameObject, TextStringObject, DecodedStreamObject
        from xml.sax.saxutils import escape as xe
        reader=PdfReader(self.path);writer=PdfWriter();writer.clone_document_from_reader(reader)
        who='Haohong Zhang';date="D:20261025120000+08'00'"
        writer.add_metadata({'/Author':who,'/Creator':who,'/Producer':who,'/LastModifiedBy':who,'/Editor':who,'/CreationDate':date,'/ModDate':date})
        xml=f'''<?xpacket begin="\ufeff"?><x:xmpmeta xmlns:x="adobe:ns:meta/"><rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"><rdf:Description rdf:about="" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:xmp="http://ns.adobe.com/xap/1.0/" xmlns:pdf="http://ns.adobe.com/pdf/1.3/" xmlns:cv="https://ludenszhang.github.io/ns/cv/"><dc:creator><rdf:Seq><rdf:li>{who}</rdf:li></rdf:Seq></dc:creator><dc:title><rdf:Alt><rdf:li xml:lang="x-default">{xe('Haohong Zhang | '+self.label)}</rdf:li></rdf:Alt></dc:title><xmp:CreatorTool>{who}</xmp:CreatorTool><xmp:ModifyDate>2026-10-25T12:00:00+08:00</xmp:ModifyDate><pdf:Producer>{who}</pdf:Producer><cv:LastModifiedBy>{who}</cv:LastModifiedBy></rdf:Description></rdf:RDF></x:xmpmeta><?xpacket end="w"?>'''
        stream=DecodedStreamObject();stream.set_data(xml.encode('utf-8'));stream[NameObject('/Type')]=NameObject('/Metadata');stream[NameObject('/Subtype')]=NameObject('/XML');writer._root_object[NameObject('/Metadata')]=writer._add_object(stream)
        for page in writer.pages:
            for ref in page.get('/Annots',[]):
                annot=ref.get_object()
                if '/T' in annot or annot.get('/Subtype')!='/Link':annot[NameObject('/T')]=TextStringObject(who)
        with open(self.path,'wb') as out:writer.write(out)
        final=PdfReader(self.path)
        assert len(final.pages)==2
        assert all(final.metadata.get(k)==who for k in ['/Author','/Creator','/Producer','/LastModifiedBy','/Editor'])
        assert final.xmp_metadata.dc_creator==[who]
        assert not re.search(r'reportlab|anonymous|python-docx',str(final.metadata),re.I)
        print(self.path)

general = CV('', 'Curriculum vitae')
general.new_page(first=True); general.summary(); general.education(); general.skills(); general.project_list()
general.new_page(); general.publications(selected, 'Selected peer-reviewed publications'); general.publications(preprints, 'Preprints'); general.conference(); general.honors(); general.finish()

academic = CV('-Academic', 'Academic CV')
academic.new_page(first=True); academic.education(); academic.publications(selected, 'Selected peer-reviewed publications'); academic.honors()
academic.new_page(); academic.publications(preprints, 'Preprints'); academic.conference(); academic.project_list(); academic.skills(); academic.finish()

industry = CV('-Research-Engineer', 'Research & engineering CV')
industry.new_page(first=True); industry.summary(industry=True); industry.skills(); industry.project_list(personal, 'Selected engineering projects'); industry.education()
industry.new_page(); industry.publications(selected[:3], 'Selected peer-reviewed research'); industry.publications(preprints, 'Preprints'); industry.conference(); industry.honors()
industry.section('Further research'); industry.para('Research software includes MGM2, MGM, MicroVQVAE, DeepMicroCancer and ASD-cancer. '+link('Explore projects and full bibliography', 'https://ludenszhang.github.io/'), 10, 14); industry.finish()
