# JavaFX + NetBeans (Java with Ant) + Scene Builder: Complete Mac Guide

**For:** macOS Apple Silicon (M4), Apache NetBeans, **Java with Ant**, JavaFX and Gluon Scene Builder.  
**Your confirmed JDK:** Azul Zulu OpenJDK **21.0.12.1** (arm64).  
**Your previous JavaFX SDK folder:** `~/JavaFX/javafx-sdk-27` (**NOT compatible with JDK 21**).  
**Recommended pairing for these instructions:** JDK **21** + JavaFX SDK **21.x**, macOS **aarch64**. A newer standalone Scene Builder application can usually edit JavaFX 21 FXML; its bundled runtime version does not determine which JavaFX libraries your Ant application uses.

> **In one sentence:** NetBeans writes/runs Java; Scene Builder visually edits an **FXML file**; a Java **controller** handles UI events; JavaFX `FXMLLoader` loads the FXML into a `Scene` displayed in a `Stage`.

## Table of contents

1. What all the pieces do
2. Install and verify JavaFX and Scene Builder
3. Create a JavaFX project in NetBeans using Java with Ant
4. Add JavaFX dependencies and runtime arguments
5. Make and edit an FXML file with Scene Builder
6. Connect FXML, controller, and main application
7. Complete working Welcome App
8. Complete working Tip Calculator
9. Workflows for future projects
10. Troubleshooting reference
11. Checklist and reference links

---

## 1. Understand the pieces

| Component | What it does | Where you work |
|---|---|---|
| **JDK** | Compiles and executes Java source | Installed on Mac; selected in NetBeans |
| **JavaFX SDK** | Supplies `javafx.controls`, `javafx.fxml`, etc. | `~/JavaFX/javafx-sdk-21.../lib` |
| **NetBeans** | Creates, compiles, and runs Java/Ant projects | Java files and project settings |
| **Scene Builder** | Visual drag-and-drop editor that writes FXML | `.fxml` files |
| **FXML** | XML description of controls and layout | `Welcome.fxml`, `TipCalculator.fxml` |
| **Controller** | Java class with `@FXML` references and event handlers | `WelcomeController.java`, `TipCalculatorController.java` |
| **Application class** | JavaFX entry point, loads FXML and shows a window | `WelcomeApp.java`, `TipCalculatorApp.java` |

Key JavaFX concepts from **Chapter 12**: `Stage` is the top-level window, `Scene` is its content area, a layout such as `VBox` or `GridPane` arranges controls, and controls include `Label`, `TextField`, `Button`, `Slider`, and `ImageView`. The chapter introduces the Welcome GUI in §12.4 and the Tip Calculator in §12.5; those are the examples used below. The build/environment advice in this guide is additional modern setup guidance, not instructions quoted from the textbook.

### How the connection works

```text
NetBeans Java with Ant project
  src/chapter12/
    WelcomeApp.java          <-- launches JavaFX and loads FXML
    WelcomeController.java   <-- Java behavior (if needed)
    Welcome.fxml             <-- design created by Scene Builder
    duke.png                 <-- optional image resource

Scene Builder  --edits--> Welcome.fxml
WelcomeApp    --loads--> Welcome.fxml with FXMLLoader
Welcome.fxml  --refers to--> WelcomeController using fx:controller
FXML fx:id   --maps to--> @FXML fields in controller
FXML onAction --maps to--> @FXML handler methods
```

---

## 2. Install and verify JavaFX and Scene Builder

### A. Check your JDK (already completed on your Mac)

```bash
java -version
/usr/libexec/java_home -V
```

You have JDK 21 at:

```text
/Library/Java/JavaVirtualMachines/zulu-21.jdk/Contents/Home
```

You **do not** need to reinstall Java 21.

### B. Get the matching JavaFX SDK

1. Visit https://gluonhq.com/products/javafx/.
2. Download **JavaFX 21.x** → **macOS** → **aarch64** → **SDK** (not jmods).
3. Extract it and move its directory into `~/JavaFX/`.
4. Check the actual directory name (it might include a patch number):

```bash
ls ~/JavaFX/
ls ~/JavaFX/javafx-sdk-21*/lib/javafx.controls.jar
ls ~/JavaFX/javafx-sdk-21*/lib/javafx.fxml.jar
```

For the rest of the guide **replace** `/Users/tatejones/JavaFX/javafx-sdk-21/lib` with the exact directory on your Mac if it includes a version suffix like `-21.0.9`.

**Important:** You previously downloaded `javafx-sdk-27`. Do not use its JARs or VM module path when running against JDK 21; keep it elsewhere or ignore it.

### C. Install and open Scene Builder

- Download from https://gluonhq.com/products/scene-builder/ (macOS Apple Silicon), **or** use Homebrew:

```bash
brew install --cask scenebuilder
```

Open **Scene Builder** from Applications. On newer versions, the welcome screen has an **Empty** template. Pick it to create a new layout. Scene Builder is its own app; it can work even without being integrated into NetBeans.

---

## 3. Create a NetBeans JavaFX project (Java with Ant)

1. Open NetBeans → **File → New Project**.
2. Select **Java with Ant → Java Application**. **Do not** choose a legacy **JavaFX Application** template that asks for a JDK with bundled JavaFX.
3. Name the project, e.g. `Chapter12JavaFX`.
4. Uncheck **Create Main Class** if offered; otherwise you may delete or ignore its generated class.
5. Finish.
6. Right-click the project → **Properties → Libraries** and choose the **JDK 21** Java Platform. If it is not listed, use **Tools → Java Platforms → Add Platform**, then select:

```text
/Library/Java/JavaVirtualMachines/zulu-21.jdk/Contents/Home
```

7. In **Source Packages**, create the package `chapter12` (right-click → New → Java Package).
8. The examples below assume Java and FXML files reside **in that same `chapter12` package**.

> **Path rule:** `WelcomeApp.class.getResource("Welcome.fxml")` finds `Welcome.fxml` in the **same package** as `WelcomeApp`. If the file is elsewhere, adjust the resource path. The exact FXML placement and runtime classpath are critical in Ant projects.

---

## 4. Configure JavaFX compilation and runtime in an Ant project

JavaFX needs **both** compile-time libraries and runtime module arguments.

### A. Create a global JavaFX library

1. In NetBeans choose **Tools → Libraries**.
2. **New Library** → name `JavaFX21` → **Class Libraries**.
3. On **Classpath**, select **Add JAR/Folder**.
4. Navigate into your JavaFX 21 SDK `lib/` folder.
5. Select the `.jar` files (e.g. `javafx.base.jar`, `javafx.controls.jar`, `javafx.fxml.jar`, `javafx.graphics.jar`, etc.). **Do not select `.dylib` files or `src.zip`.**
6. Save the library.

### B. Add it to your project

1. Right-click your project → **Properties → Libraries**.
2. Under **Compile**, add the `JavaFX21` library to the **Classpath** (not as a Java Platform).
3. If NetBeans has a **Run Classpath** section, confirm the libraries are included there as well.
4. Under **Build → Compiling**, if a **Compile on Save** checkbox causes outdated/odd launch behavior, turn it off.

### C. Set the JVM runtime options

Project → **Properties → Run** → **VM Options**:

```text
--module-path "/Users/tatejones/JavaFX/javafx-sdk-21/lib" --add-modules javafx.controls,javafx.fxml
```

Use your real SDK folder name, not the example if yours ends in `.x`. There must be **a space** between `--module-path` and its value. The two arguments belong to the **VM**, not **Application Arguments**.

If **Run → VM Options** is absent, consult the project's Ant run configuration / `nbproject/project.properties` or your NetBeans version's platform run settings. Avoid modifying Ant-generated files until you have identified how that version passes JVM arguments.

### D. Confirm before writing the whole app

Create and run this `HelloFX.java` in package `chapter12`:

```java
package chapter12;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;

public class HelloFX extends Application {
    @Override
    public void start(Stage stage) {
        stage.setScene(new Scene(
                new StackPane(new Label("JavaFX works!")), 400, 250));
        stage.setTitle("JavaFX Test");
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
```

In project **Properties → Run**, set **Main Class** to `chapter12.HelloFX`. Click **Run Project**. A window saying **JavaFX works!** means the SDK + Ant JavaFX runtime path are configured.

---

## 5. Create and edit FXML with Scene Builder

### A. Create FXML

Either method works:

**Method 1 — from Scene Builder (often simplest)**

1. Launch Scene Builder → select **Empty**.
2. Make your layout, then **File → Save As**.
3. Save it **inside the NetBeans project's source package**, e.g. `src/chapter12/Welcome.fxml` (some generated project structures differ; inspect your project's Source Packages).
4. Back in NetBeans, refresh the project tree if needed.

**Method 2 — from NetBeans**

1. Right-click the Java package → **New → Other → Empty File** (if an FXML template isn't offered).
2. Name it `Welcome.fxml`.
3. Insert valid FXML, save it, then open the saved file with Scene Builder (**File → Open** or macOS **Open With**).

### B. Critical XML rule

**The very first bytes of the file must be `<?xml ... ?>` if you include an XML declaration. There must be NO empty line or space before it.** You already encountered this exact error:

```text
SAXParseException: lineNumber: 2; columnNumber: 6
The processing instruction target matching "[xX][mM][lL]" is not allowed.
```

**Fix:** delete every character before `<?xml` so the declaration is on **line 1**. Alternatively, omit the XML declaration entirely. Use a plain text editor, not rich-text formatting.

### C. Main Scene Builder areas

| Panel | Purpose |
|---|---|
| **Library** | Drag containers and controls onto the canvas |
| **Hierarchy** | Shows actual component nesting; useful for selecting parent containers |
| **Content / Preview area** | Visual layout you edit |
| **Inspector → Properties** | Text, prompt text, image, slider values, etc. |
| **Inspector → Layout** | Sizing, alignment, padding, spacing, row/column constraints |
| **Inspector → Code** | Set **fx:id**, `onAction`, and a root's controller class |
| **Preview → Show Preview in Window** | See the FXML layout without launching the whole Java app |

**Common containers:**

- `VBox`: stacks controls vertically (Welcome example).
- `HBox`: arranges controls horizontally.
- `GridPane`: form-like rows/columns (Tip Calculator).
- `AnchorPane`: positions children using top/left/bottom/right anchors.
- `BorderPane`: top, bottom, center, left, right regions.

### D. Find/open Scene Builder from NetBeans

Some NetBeans releases expose **NetBeans → Settings/Preferences → Java → JavaFX → Scene Builder Home**, while others do not. If not available, use the standalone Scene Builder app and open your `.fxml` directly. **No NetBeans integration plugin is required** to save an FXML file and use it in an Ant project.

---

## 6. Connect Scene Builder to Java (the three-part pattern)

### Part A — Design FXML

1. Drag in controls in Scene Builder.
2. In **Inspector → Code**, give controls used in Java unique **fx:id** values, e.g. `amountTextField`.
3. To handle button clicks, set **On Action** to a method such as `#calculateButtonPressed` (Scene Builder may show just the method name in its editable selector).
4. In the **Controller** area (typically lower-left or under Code), enter the fully-qualified controller class, e.g. `chapter12.TipCalculatorController`.
5. Save the FXML.

### Part B — Make a controller class

FXML:

```xml
<Button fx:id="calculateButton"
        text="Calculate"
        onAction="#calculateButtonPressed" />
```

Controller:

```java
package chapter12;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;

public class ExampleController {
    @FXML private Button calculateButton;

    @FXML
    private void calculateButtonPressed(ActionEvent event) {
        System.out.println("Clicked!");
    }
}
```

FXML root must specify the controller if one is used:

```xml
<VBox xmlns:fx="http://javafx.com/fxml/1"
      fx:controller="chapter12.ExampleController">
    <!-- child controls here -->
</VBox>
```

**Rules:**

- `fx:id="calculateButton"` and `@FXML private Button calculateButton;` **must match exactly**, including capitalization.
- `onAction="#calculateButtonPressed"` and the controller method name **must match exactly**.
- `fx:controller` requires the **full package name**.
- Each FXML document typically has **one** controller.
- `@FXML` allows the loader to inject private fields/call private handler methods.
- Controller code runs after FXML loading; do not expect injected fields to exist in the controller constructor. Use `initialize()` for UI initialization.

### Part C — Load FXML in a JavaFX Application

```java
package chapter12;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class ExampleApp extends Application {
    @Override
    public void start(Stage stage) throws Exception {
        Parent root = FXMLLoader.load(
                getClass().getResource("Example.fxml"));
        stage.setScene(new Scene(root));
        stage.setTitle("Example");
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
```

**Run the application class**, not the FXML file and not the controller. Under project **Properties → Run → Main Class**, select `chapter12.ExampleApp`. `FXMLLoader` loads FXML, finds its controller, injects fields, and wires up events.

---

## 7. Working Welcome App (Chapter 12, §12.4)

**Goal:** display **Welcome to JavaFX!** above an image. The textbook's design uses a `VBox`, `Label`, and `ImageView`. **No controller is needed** because this app has no interaction.

### A. Design it in Scene Builder

1. New **Empty** FXML → drag a **VBox** as the root/container (or replace existing root with VBox).
2. Set `VBox` **Pref Width = 300**, **Pref Height = 300**, **Alignment = CENTER**, **Spacing = 0**.
3. Drag in a `Label`, set **Text = Welcome to JavaFX!**, choose a larger font.
4. Drag an `ImageView` below the label. Choose your own image or the course-provided example image if available.
5. Adjust `Fit Width` / `Fit Height` and enable `Preserve Ratio`.
6. Save as `Welcome.fxml` **inside `src/chapter12/`**, with any chosen image in the same package.
7. **Preview → Show Preview in Window**.

### B. Working starter FXML without an image

Save as `src/chapter12/Welcome.fxml` (XML declaration starts on first line):

```xml
<?xml version="1.0" encoding="UTF-8"?>

<?import javafx.scene.control.Label?>
<?import javafx.scene.layout.VBox?>

<VBox xmlns:fx="http://javafx.com/fxml/1"
      alignment="CENTER"
      spacing="8.0"
      prefWidth="300.0"
      prefHeight="300.0">
    <children>
        <Label text="Welcome to JavaFX!" style="-fx-font-size: 20px;" />
    </children>
</VBox>
```

To add an image later, edit and save using Scene Builder. If the image is in the same package as the FXML, you can use FXML like:

```xml
<?import javafx.scene.image.Image?>
<?import javafx.scene.image.ImageView?>

<ImageView fitWidth="240.0" preserveRatio="true">
    <image>
        <Image url="@duke.png" />
    </image>
</ImageView>
```

Those additional imports go with other `<?import ...?>` statements, and the `ImageView` goes **inside** the VBox `<children>` section. Ensure `duke.png` really exists in the FXML's directory. You may instead pick an image via Scene Builder's image picker and inspect its saved resource path.

### C. Main application

Create `src/chapter12/WelcomeApp.java`:

```java
package chapter12;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class WelcomeApp extends Application {
    @Override
    public void start(Stage stage) throws Exception {
        Parent root = FXMLLoader.load(
                getClass().getResource("Welcome.fxml"));
        stage.setTitle("Welcome");
        stage.setScene(new Scene(root));
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
```

Set main class to **`chapter12.WelcomeApp`**, then **Run Project**. If successful, the FXML preview and the launched application display the same layout. An image path error may appear only after adding an ImageView; the image is optional for the basic runtime test but part of the textbook assignment design.

---

## 8. Working Tip Calculator (Chapter 12, §12.5)

**Goal:** enter a bill amount, choose a percentage with a `Slider`, and click **Calculate** to display the tip and total. The textbook also discusses updating the percentage label as the slider changes.

### A. Build it in Scene Builder

1. Create `TipCalculator.fxml` in the `chapter12` package.
2. Use a **GridPane** root; for a form, choose **2 columns and 4 rows**.
3. Add labels for **Amount**, **Tip %**, **Tip**, **Total**.
4. Add three text fields to the right for amount/tip/total.
5. Add a `Slider` for tip selection, set `Min = 0`, `Max = 30`, and `Value = 15`.
6. Add a **Calculate** button in a lower row, spanning columns if desired.
7. Give each Java-accessed item an **fx:id** exactly as specified below.
8. Set the root's **Controller class** to `chapter12.TipCalculatorController`.
9. Set Calculate button **On Action** to `#calculateButtonPressed`.
10. Save the FXML and verify its preview.

### B. Recommended IDs

| Control | fx:id | Other settings |
|---|---|---|
| Amount `TextField` | `amountTextField` | Prompt `Bill amount` |
| Tip percentage `Label` | `tipPercentageLabel` | Starts as `15%` |
| Tip `Slider` | `tipPercentageSlider` | Min `0`, Max `30`, Value `15` |
| Tip `TextField` | `tipTextField` | `editable=false` |
| Total `TextField` | `totalTextField` | `editable=false` |
| Calculate `Button` | optional | On Action `#calculateButtonPressed` |

### C. Complete FXML you can paste instead of dragging

`src/chapter12/TipCalculator.fxml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>

<?import javafx.scene.control.*?>
<?import javafx.scene.layout.*?>
<?import javafx.geometry.Insets?>

<GridPane xmlns:fx="http://javafx.com/fxml/1"
          fx:controller="chapter12.TipCalculatorController"
          hgap="10.0" vgap="12.0"
          prefWidth="380.0" prefHeight="250.0">
    <padding>
        <Insets top="16.0" right="16.0"
                bottom="16.0" left="16.0" />
    </padding>
    <children>
        <Label text="Amount" GridPane.rowIndex="0" GridPane.columnIndex="0" />
        <TextField fx:id="amountTextField" promptText="Bill amount"
                   GridPane.rowIndex="0" GridPane.columnIndex="1" />

        <Label fx:id="tipPercentageLabel" text="15%"
               GridPane.rowIndex="1" GridPane.columnIndex="0" />
        <Slider fx:id="tipPercentageSlider" min="0.0" max="30.0" value="15.0"
                GridPane.rowIndex="1" GridPane.columnIndex="1" />

        <Label text="Tip" GridPane.rowIndex="2" GridPane.columnIndex="0" />
        <TextField fx:id="tipTextField" editable="false"
                   GridPane.rowIndex="2" GridPane.columnIndex="1" />

        <Label text="Total" GridPane.rowIndex="3" GridPane.columnIndex="0" />
        <TextField fx:id="totalTextField" editable="false"
                   GridPane.rowIndex="3" GridPane.columnIndex="1" />

        <Button text="Calculate" onAction="#calculateButtonPressed"
                GridPane.rowIndex="4" GridPane.columnIndex="0"
                GridPane.columnSpan="2" maxWidth="Infinity" />
    </children>
</GridPane>
```

### D. Controller

`src/chapter12/TipCalculatorController.java`:

```java
package chapter12;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.text.NumberFormat;
import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.control.Slider;
import javafx.scene.control.TextField;

public class TipCalculatorController {
    @FXML private TextField amountTextField;
    @FXML private Label tipPercentageLabel;
    @FXML private Slider tipPercentageSlider;
    @FXML private TextField tipTextField;
    @FXML private TextField totalTextField;

    private final NumberFormat currency = NumberFormat.getCurrencyInstance();

    @FXML
    private void initialize() {
        tipPercentageLabel.setText(
                Math.round(tipPercentageSlider.getValue()) + "%");
        tipPercentageSlider.valueProperty().addListener((obs, oldValue, newValue) -> {
            tipPercentageLabel.setText(Math.round(newValue.doubleValue()) + "%");
        });
    }

    @FXML
    private void calculateButtonPressed() {
        try {
            // Accept decimal bill amounts such as 24.56.
            BigDecimal amount = new BigDecimal(amountTextField.getText().trim());
            if (amount.signum() < 0) {
                throw new NumberFormatException("Negative amount");
            }

            long roundedPercent = Math.round(tipPercentageSlider.getValue());
            BigDecimal tip = amount.multiply(BigDecimal.valueOf(roundedPercent))
                    .divide(BigDecimal.valueOf(100), 2, RoundingMode.HALF_UP);
            BigDecimal total = amount.add(tip);

            tipTextField.setText(currency.format(tip));
            totalTextField.setText(currency.format(total));
        } catch (NumberFormatException ex) {
            tipTextField.setText("Invalid amount");
            totalTextField.clear();
        }
    }
}
```

**Behavior note:** This example rounds the slider to a whole percentage and calculates when clicked. The textbook's design may specify slightly different percentage-display or calculation timing; follow your instructor's exact rubric when it differs.

### E. Main application

`src/chapter12/TipCalculatorApp.java`:

```java
package chapter12;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class TipCalculatorApp extends Application {
    @Override
    public void start(Stage stage) throws Exception {
        Parent root = FXMLLoader.load(
                getClass().getResource("TipCalculator.fxml"));
        stage.setTitle("Tip Calculator");
        stage.setScene(new Scene(root));
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
```

Set the project's main class to **`chapter12.TipCalculatorApp`** and click Run. Test `24.56` with a `15%` tip: expected tip **$3.68** and total **$28.24** (for US currency formatting). Slide to 20%, click Calculate, and confirm the figures update.

---

## 9. Workflow for every new JavaFX/Scene Builder project

**Reusable sequence:**

1. Create **Java with Ant → Java Application** in NetBeans.
2. Use the installed JDK 21, project library `JavaFX21`, and JavaFX 21 SDK `--module-path`/`--add-modules` options.
3. Create a Java package (e.g. `com.example.myapp`).
4. Create the FXML inside that package (Scene Builder Empty template, Save As).
5. Choose the root container: VBox / GridPane / BorderPane / AnchorPane.
6. Add controls; set layout and text in the Inspector.
7. **Only if the app needs behavior:** set `fx:id`, controller class, and action methods.
8. Write a Java controller whose package and names match the FXML exactly.
9. Write a JavaFX `Application` subclass that loads the FXML using `getResource`.
10. Set the project **Main Class** to the `Application` subclass.
11. Run, test, and repeat: edit FXML in Scene Builder → save → run again in NetBeans.

### Save changes correctly

- **Scene Builder → File → Save** modifies the `.fxml` file itself.
- **NetBeans → Run Project** compiles/loads the latest saved FXML.
- If NetBeans shows stale content: save both sides, **Clean and Build**, then **Run**.
- Avoid editing the same FXML simultaneously in both programs without saving/reopening; one editor may overwrite the other's unsaved edits.

### Multiple screens

Each screen can have its own FXML and controller. Load another screen in a click handler using `FXMLLoader`, then change the existing stage's scene or swap its root. Keep file paths relative to the class/package or use absolute classpath resources like `/com/example/myapp/Other.fxml`.

### Images and other resources

Place bundled images near the FXML or in a `resources` package included in the runtime classpath. In FXML, a relative image URL such as `@duke.png` refers to the FXML's location. Resources stored outside the project or addressed via `/Users/.../Downloads` may work on your own Mac but break when the project is submitted.

---

## 10. Troubleshooting quick reference

| Problem/error | Most likely reason | Fix |
|---|---|---|
| **`The processing instruction target matching "[xX][mM][lL]" is not allowed`** | Blank line/characters before `<?xml` | Put declaration at byte 1 on line 1, or omit it |
| **`JDK with JavaFX is required`** in New Project | Legacy JavaFX Ant template expects JavaFX inside JDK | Choose **Java with Ant → Java Application** instead |
| **`package javafx... does not exist`** | SDK JARs not on compile classpath | Add `JavaFX21` library to project Libraries/Compile |
| **`JavaFX runtime components are missing`** | Runtime options absent/wrong | Add `--module-path ... --add-modules javafx.controls,javafx.fxml` to **VM Options** |
| **`UnsupportedClassVersionError`** | Runtime Java too old for compiled class/library | Match JDK 21 with JavaFX 21 SDK; make sure NetBeans actually runs on selected platform |
| **`Module javafx.controls not found`** | Module path wrong/points to wrong directory | Point to SDK's **lib** directory, check with `ls` |
| **`Location is not set`** or NPE in `FXMLLoader` | FXML resource not found | Put FXML in same package or correct `getResource("...")` path; ensure built output contains it |
| **`LoadException: controller`** | `fx:controller` class name wrong, class missing or failing to construct | Set correct fully-qualified class name and compile controller |
| **`Error resolving onAction`** | Method name doesn't match or inaccessible | Match `#handlerName` to `@FXML` method, rebuild |
| **`... is null` when handler runs** | `fx:id` mismatch or field not injected | Check exact `fx:id` and matching `@FXML` field; do not access injected fields in constructor |
| **Image not displayed** | Bad file/resource path | Keep image with FXML, use `@filename.png`, check capitalization |
| **Scene Builder does not show in NetBeans** | No built-in integration in that version | Open FXML with standalone Scene Builder; save/reopen in NetBeans |
| **FXML previews in Scene Builder, but Run fails** | Preview verifies design, not controller/application runtime | Check JDK + SDK, Ant VM options, controller, FXML resource location |
| **Controls are cut off** | Fixed window/container size too small | Adjust Pref Width/Height, padding, GridPane constraints |
| **Wrong Main Class** | NetBeans is running an old test class | Project → Properties → Run → Main Class = the correct `...App` class |

### Check file paths in Terminal

```bash
# SDK dirs installed
ls ~/JavaFX/

# JavaFX JARs (match your real SDK directory)
ls ~/JavaFX/javafx-sdk-21*/lib/javafx.controls.jar

# Java versions macOS knows about
/usr/libexec/java_home -V
```

### If NetBeans is confusing the two SDK versions

Review all project library JAR paths and VM Options. **Do not mix** `javafx-sdk-27` with the JavaFX 21 project. Old references can remain in saved NetBeans project settings even after downloading the correct version.

---

## 11. Final project checklist

- [ ] JDK 21 selected in the NetBeans project.
- [ ] JavaFX 21 **macOS aarch64 SDK** installed.
- [ ] JavaFX JAR files added to NetBeans library/project compile classpath.
- [ ] VM Options point to the matching JavaFX SDK `lib` folder.
- [ ] Scene Builder opens a valid FXML and can Preview it.
- [ ] FXML file saved **within the NetBeans source tree**.
- [ ] XML declaration is on **line 1**, with no preceding whitespace.
- [ ] Controller name (when used) matches `fx:controller` exactly.
- [ ] FXML `fx:id` values match controller `@FXML` fields.
- [ ] FXML action name matches Java handler.
- [ ] JavaFX Application class loads the correct FXML.
- [ ] NetBeans **Main Class** points to the Application, not controller.
- [ ] **Clean and Build**, then **Run Project**, succeed.
- [ ] Project includes needed local image files, not paths into Downloads.

## Official references

- OpenJFX home/documentation: https://openjfx.io/
- OpenJFX getting started: https://openjfx.io/openjfx-docs/
- JavaFX SDK downloads: https://gluonhq.com/products/javafx/
- Scene Builder downloads: https://gluonhq.com/products/scene-builder/
- Apache NetBeans documentation: https://netbeans.apache.org/

**Course reference:** User-provided *Chapter 12 JavaFX Graphical User Interfaces: Part 1* scanned textbook excerpt (19 PDF pages). §§12.4–12.5 introduce the Welcome App, VBox/Label/ImageView design, Scene Builder layout, Tip Calculator with GridPane/Slider/TextFields/Button, FXML controllers, and event handling. The copy is an excerpt of a textbook; this guide's working code and modern JDK/Ant installation steps are independently written examples to help carry out the chapter's goals, not verbatim textbook code.
