# Course reference

## How to use these materials

Start with the assignment prompt and rubric, identify its concepts in the map below,
then read the matching extracted text and original slides or manual pages. Original
files remain at the repository root. Searchable copies are in `reference/extracted/`.
The map describes material supplied as of October 5, 2026, not a complete syllabus.

## Topic map

| Material | Concepts and examples | Slides |
| --- | --- | ---: |
| JHTP11_08 | Classes and objects; scope; access control; constructors and `this`; composition; `static`, `final`, enums, packages and `BigDecimal`; preliminary exception examples | 179 |
| JHTP11_09 | Inheritance; superclass/subclass relationships; `extends`, `super`, protected members, overriding, `Object` and `toString`; employee examples | 101 |
| JHTP11_10 | Polymorphism; dynamic method dispatch; abstract classes and methods; interfaces; employee payroll and payable/invoice examples | 204 |
| JHTP11_11 | Exception handling; stack traces; `try`, `catch`, `finally`, `throw`, `throws`; checked/unchecked exceptions; chained and custom exceptions | 84 |
| JHTP11_12 | JavaFX GUI introduction; Scene Builder; FXML; stages, scenes and scene graphs; controls, events and controllers | 61 |
| JHTP11_14 | Strings, characters, `StringBuilder`, comparison and manipulation; regular expressions, `Pattern`, `Matcher`, validation and replacement | 176 |
| JHTP11_15 | Files and directories; streams; `java.io` and NIO; `Scanner`, `Formatter`; object serialization and XML/JAXB | 98 |
| Chapter 12 JavaFX manual PDF | JavaFX basics; VBox/GridPane, labels, images, text fields, sliders, buttons; Welcome GUI and Tip Calculator | 19 PDF pages |
| Chapter 13 JavaFX manual PDF | Layout panels; radio buttons, mouse events, shapes, property bindings/listeners; Painter, Color Chooser and Cover Viewer/ListView cell factories | 22 PDF pages |
| Week1 Java CODES | Scope, multiple classes, exceptions, constructors, `Time1`/`Time2` and constructor overloading | Document |
| Week 2, 3 & 4 Java CODES | Inheritance and `toString`; employee classes; polymorphism, abstract classes/interfaces and exception examples | Document |
| Week 7 & 8 Java CODES | String comparison; regex replacement with `Pattern`/`Matcher`; file information, text records and XML/JAXB examples | Document |

## JavaFX assignment approach

Tate expects JavaFX for most assignments. The Chapter 12 slides introduce visual
layout using Scene Builder, FXML and controller code. Read the relevant manual
example before deciding whether an assignment calls for that workflow or a GUI
created directly in Java.

For a GUI assignment, map the rubric to controls and layout, identify which actions
need event handlers, and keep the underlying object model and calculations clear.
When FXML is required, check controller linkage, `fx:id` values, handler names and
resource paths against the instructor's examples. Handle invalid input using the
exception and validation techniques taught in Chapters 11 and 14.

No specific JDK, JavaFX version, IDE or build system has been established by Tate.
Verify the actual assignment environment before adding dependencies or setup
instructions; historical installation steps are not proof of current requirements.

## Reading the instructor's code

The example documents contain multiple unrelated programs and use a mixture of paragraphs and multiline code blocks. They are reference documents, not one compilable
Java project. Match missing examples to the slide decks rather than inventing code
and labeling it as instructor-provided. Preserve the source wording; explain and
correct errors separately when adapting examples.

Extracted slide text retains slide numbers and editable text, including speaker
notes when present. Code stored in images, diagrams and visual arrangement are not
captured by the Office extraction. PDF OCR is automatically recognized text and can
misread punctuation, identifiers and indentation. Always inspect the original page
before relying on a code listing.

## Course expectations recorded in the slides

The opening deck describes CSIS 312 as a continuation of CSIS 212 and tells students
to review Chapters 1–11. This repository only contains the files listed above; it
does not establish that every chapter or example from either course is present.

On October 5, 2026, Tate reported that the professor permits AI use, despite
the older prohibition in Chapter 8, slide 3. This updated instructor permission
supersedes the slide for assignment help. Use the course examples and JavaFX
approach when helping, and follow each assignment's prompt and rubric.

## Persistent context

`AGENTS.md` records how a coding assistant should use this repository. It allows
future sessions with repository access to recover the course context and JavaFX
preference. It does not give an assistant permanent memory across unrelated chats.
