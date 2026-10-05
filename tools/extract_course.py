"""Extract editable text; retain originals for images, diagrams and formatting."""
from pathlib import Path
import re
import zipfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'reference' / 'extracted'
OUT.mkdir(parents=True, exist_ok=True)
for source in sorted(ROOT.iterdir()):
    if source.suffix not in ('.pptx', '.docx'):
        continue
    with zipfile.ZipFile(source) as archive:
        if source.suffix == '.pptx':
            ns = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}
            names = sorted((n for n in archive.namelist() if re.fullmatch(r'ppt/slides/slide\d+.xml', n)),
                           key=lambda n: int(re.search(r'(\d+)\.xml', n).group(1)))
            sections = ['# ' + source.name]
            for index, name in enumerate(names, 1):
                xml = ET.fromstring(archive.read(name))
                paragraphs = [''.join(t.text or '' for t in p.findall('.//a:t', ns))
                              for p in xml.findall('.//a:p', ns)]
                sections.append(f'## Slide {index}\n\n' + '\n'.join(paragraphs))
                notes = f'ppt/notesSlides/notesSlide{index}.xml'
                if notes in archive.namelist():
                    xml = ET.fromstring(archive.read(notes))
                    text = [''.join(t.text or '' for t in p.findall('.//a:t', ns))
                            for p in xml.findall('.//a:p', ns)]
                    sections.append('### Speaker notes\n\n' + '\n'.join(text))
            (OUT / (source.stem + '.md')).write_text('\n\n'.join(sections), encoding='utf-8')
        else:
            ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
            xml = ET.fromstring(archive.read('word/document.xml'))
            paragraphs = []
            for p in xml.findall('.//w:p', ns):
                pieces = []
                for element in p.iter():
                    if element.tag == '{' + ns['w'] + '}t': pieces.append(element.text or '')
                    elif element.tag == '{' + ns['w'] + '}tab': pieces.append('\t')
                    elif element.tag in ('{' + ns['w'] + '}br', '{' + ns['w'] + '}cr'): pieces.append('\n')
                paragraphs.append(''.join(pieces))
            (OUT / (source.stem + '.txt')).write_text('\n'.join(paragraphs), encoding='utf-8')
    print(source.name)

# Normalize source whitespace in searchable copies only.
for target in OUT.iterdir():
    if target.suffix in (".md", ".txt"):
        target.write_text("\n".join(line.expandtabs(4).rstrip() for line in target.read_text().splitlines()).rstrip() + "\n", encoding="utf-8")
