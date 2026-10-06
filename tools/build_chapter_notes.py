"""Build one Markdown reference per supplied chapter from existing extracts."""
from pathlib import Path
from urllib.parse import quote
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'chapters'
OUT.mkdir(exist_ok=True)
DATA = {
    8: ('Classes and Objects: A Deeper Look', [
        'Scope and access modifiers; separate class responsibilities.',
        'Constructors, overloaded constructors, the current object (`this`) and validation.',
        'Composition, enums, class members (`static`), constants (`final`) and packages.',
        'Time and account examples; precise decimal calculations with `BigDecimal`.'
    ], ['Week1 Java CODES']),
    9: ('Inheritance', [
        'Superclass and subclass relationships using `extends`.',
        'Inherited members, access control and `protected`.',
        'Superclass constructors and methods using `super`.',
        'Method overriding, `Object.toString`, and commission employee examples.'
    ], ['Week 2, 3 & 4 Java CODES-3']),
    10: ('Polymorphism and Interfaces', [
        'Superclass references and runtime selection of overridden methods.',
        'Abstract classes and methods; concrete subclasses.',
        'Interfaces and common operations across different classes.',
        'Polymorphic employee payroll and payable/invoice examples.'
    ], ['Week 2, 3 & 4 Java CODES-3']),
    11: ('Exception Handling: A Deeper Look', [
        'Exceptions, stack traces and the termination model of exception handling.',
        '`try`, `catch`, `finally`, `throw` and `throws`.',
        'Checked and unchecked exceptions, exception hierarchies and propagation.',
        'Chained and custom exceptions; handling invalid input and division errors.'
    ], ['Week1 Java CODES', 'Week 2, 3 & 4 Java CODES-3']),
    12: ('JavaFX Graphical User Interfaces: Part 1', [
        'Stages, scenes, scene graphs and JavaFX controls.',
        'Scene Builder, FXML, controller classes and event handling.',
        '`VBox` and `GridPane`; labels, images, text fields, sliders and buttons.',
        'Welcome GUI and Tip Calculator examples.'
    ], []),
    13: ('JavaFX GUI: Part 2', [
        'Layout panels, including `Pane`, `BorderPane` and `TitledPane`.',
        'Radio buttons, mouse events and shapes in the Painter example.',
        'Property binding and listeners in the Color Chooser example.',
        'JavaFX collections, `ListView` and custom cells in the Cover Viewer examples.'
    ], []),
    14: ('Strings, Characters and Regular Expressions', [
        'String construction, comparison, searching and manipulation.',
        '`StringBuilder` and character processing with `Character`.',
        'Regex character classes, quantifiers and input validation.',
        '`Pattern`, `Matcher`, replacement and splitting; string comparison examples.'
    ], ['Week 7 & 8 Java CODES']),
    15: ('Files, I/O, NIO and Serialization', [
        'Files, directories, paths and standard input/output/error streams.',
        'Reading and writing text using buffered readers/writers, `Scanner` and `Formatter`.',
        '`Path`, `Paths`, `Files` and `DirectoryStream`.',
        'Binary object serialization with `Serializable` and object streams; `transient` fields.',
        'XML serialization with JAXB and the account-record examples.'
    ], ['Week 7 & 8 Java CODES']),
}
index = ['# Chapter references', '', 'One Markdown file for each chapter supplied in this repository (8–15).', '',
         'Each file contains a topic overview, source links and the full available chapter extract.',
         'JavaFX manual text is OCR; check code and diagrams against the originals.', '']
for number, (title, topics, examples) in DATA.items():
    sources = list((ROOT / 'reference/extracted').glob(f'JHTP11_{number:02d}*.md'))
    if number == 12:
        sources += list((ROOT / 'reference/extracted').glob('Chapter 12*SCANNED*.txt'))
    if number == 13:
        sources += list((ROOT / 'reference/extracted').glob('Java FX Chap 13*SCANNED*.txt'))
    assert sources, f'Missing chapter {number}'
    filename = f'chapter-{number:02d}.md'
    index.append(f'- [Chapter {number}: {title}]({filename})')
    parts = [f'# Chapter {number}: {title}', '', '[All chapters](README.md) · [Course guide](../reference/COURSE_GUIDE.md)', '',
             '## Main concepts', '', *['- ' + topic for topic in topics], '', '## Sources', '']
    for source in sources:
        original = ROOT / (source.stem + ('.pptx' if source.suffix == '.md' else '.pdf'))
        assert original.exists()
        parts += [f'- [{original.name}](../{quote(original.name)})',
                  f'- [Searchable text: {source.name}](../reference/extracted/{quote(source.name)})']
    if examples:
        parts += ['', '## Related instructor examples', '',
                  'These documents cover several chapters; use the examples relevant to this topic.', '']
        for example in examples:
            parts += [f'- [{example}.docx](../{quote(example + ".docx")}) · [Searchable examples](../reference/extracted/{quote(example + ".txt")})']
    parts += ['', '## Reading these notes', '',
              'The material below preserves the available extracted text. Slide and PDF page numbers',
              'refer to the supplied files, not necessarily the printed textbook page numbers.',
              'Images, diagrams and image-based code require the original documents. OCR can',
              'misread identifiers and punctuation; extracted examples are not verified runnable code.']
    if number == 8:
        parts += ['', 'Tate clarified on October 5, 2026 that the professor permits AI use; that',
                  'updated permission supersedes the older statement retained in the slide extract.']
    for source in sources:
        body = source.read_text()
        if source.suffix == '.md':
            body = body.split('\n', 1)[1].lstrip()
        # Nest original slide/page headings beneath each source section.
        body = re.sub(r'(?m)^(#{2,5}) ', r'\1# ', body)
        parts += ['', f'## {"Slide text" if source.suffix == ".md" else "Manual text (OCR)"}: {source.name}', '', body.rstrip()]
    (OUT / filename).write_text('\n'.join(parts) + '\n')
(OUT / 'README.md').write_text('\n'.join(index) + '\n')
print('Built 8 chapter Markdown files and a chapter index.')
