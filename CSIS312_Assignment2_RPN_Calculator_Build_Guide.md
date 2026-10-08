# CSIS 312 — Assignment 2: RPN Calculator
## Step-by-step build guide for NetBeans (Java with Ant) + JavaFX Scene Builder on macOS

> **Start here:** Your assignment **requires you to use the instructor's starter project**. This is a guide to finish that project, **not** instructions to submit a new replacement project. I have the one-page assignment instructions and screenshot, but **not the starter project files or the full rubric**. Therefore, class names, FXML filenames, `fx:id` values, and existing handler methods in your starter may differ from the examples below. Preserve the starter's structure and adapt the examples to it.

## 1. What the assignment specifically requires

According to the supplied **CSIS 312 Assignment 2 RPN Calculator** sheet:

- Make a calculator that performs **integer** addition, subtraction, multiplication, and division.
- Use **Reverse Polish Notation (RPN)**, with a **stack** to store operands and intermediate results.
- **Use the supplied starter project**.
- Process **UI button clicks only**; keyboard input is **not required**.
- Support **compound expressions**, such as `9 9 8 7 + - /`.
- `ENTER` **pushes** the number being entered onto the stack.
- `DROP` **removes** the top value from the stack.
- The sheet's example for adding two ones is **`1 ENTER 1 ENTER +`**.
- Include **full descriptive comments** in your code.
- Follow any additional **standard rubric** requirements given separately (not included in the uploaded sheet).

### Screenshot layout to preserve

The assignment image shows a tall stack-display area, a Liberty logo, a `DROP` button to the left below the display, a small status `Label` near the bottom, and this 4-column button layout:

```text
                [  stack display  ]
 [DROP]
 [ 7 ]  [ 8 ]  [ 9 ]  [ X ]
 [ 4 ]  [ 5 ]  [ 6 ]  [ - ]
 [ 1 ]  [ 2 ]  [ 3 ]  [ + ]
 [ 0 ]  [    ENTER   ] [ / ]
 [status label]
```

**Do not rebuild the visual interface if the starter already includes it.** The screenshot is a visual target, not evidence of specific FXML control types or field names. Use the logo asset provided in the starter (if any); do not substitute an arbitrary external logo.

## 2. Check your environment (once)

You previously installed **JDK 21 (Zulu, arm64)** and successfully opened an FXML document in **Gluon Scene Builder**. For running a JavaFX 21 program, you also need the matching **JavaFX 21 SDK**, which is distinct from JDK 21 and Scene Builder. You previously had JavaFX 27 in `~/JavaFX/`; do **not** point your JDK 21 project to JavaFX 27.

In Terminal:

```bash
java -version
/usr/libexec/java_home -V
ls ~/JavaFX/
```

Look for a folder like `javafx-sdk-21` or `javafx-sdk-21.0.x`. If it is missing, download **JavaFX 21 SDK — macOS aarch64** at <https://gluonhq.com/products/javafx/> and extract it under `~/JavaFX/`. Keep the exact folder name handy.

Scene Builder: <https://gluonhq.com/products/scene-builder/>.

**Note:** Scene Builder can run on its own runtime, even if its JavaFX version differs from the SDK used to compile your NetBeans project. What matters for building/running the project is matching the JavaFX SDK to the JDK.

## 3. Open the **existing** starter project in NetBeans

1. Download and unzip the starter project supplied by your instructor, if necessary.
2. In NetBeans, choose **File → Open Project** and navigate to the project directory containing `build.xml` and `nbproject/`.
3. Choose **Open Project**. Do **not** choose New Project when the assignment already gives one.
4. Expand **Source Packages** and take note of the package name, Java classes, and `.fxml` files.
5. Also look for images, CSS files, and library references under the project.
6. Make a backup copy of the untouched starter before editing.

### Which files do what?

| File or component | Purpose |
|---|---|
| `build.xml`, `nbproject/` | NetBeans **Ant** project configuration — keep these. |
| Java class extending `Application` | Starts JavaFX, loads FXML, shows the window. |
| `.fxml` file | Layout and controls edited visually with Scene Builder. |
| Controller `.java` file | Handles buttons, stack logic, display updates. |
| Assets (e.g. logo) | Images used by FXML; preserve their project-relative paths. |

The starter might use different names or even build some UI directly in Java. **Inspect before changing anything.**

## 4. Make sure NetBeans can compile and run JavaFX

*Do this only if the starter doesn't already work and doesn't already include its own JavaFX configuration.*

1. NetBeans: **Tools → Java Platforms**. Add or select the installed JDK 21, such as `/Library/Java/JavaVirtualMachines/zulu-21.jdk/Contents/Home`.
2. **Tools → Libraries → New Library**. Name it `JavaFX21`, type **Class Libraries**.
3. Under **Classpath**, add all JavaFX 21 `.jar` files from `~/JavaFX/<YOUR_JAVAFX_21_SDK_FOLDER>/lib/` (not `.dylib` files).
4. Right-click your starter project → **Properties → Libraries**. Set **Java Platform** to JDK 21 and add the `JavaFX21` library to the compile classpath. The exact NetBeans section can vary by version.
5. Under **Properties → Run**, add the following **VM Options**, replacing the folder name with the **real** one:

```text
--module-path "/Users/tatejones/JavaFX/javafx-sdk-21.0.x/lib" --add-modules javafx.controls,javafx.fxml
```

6. Set the **Main Class** to the *existing* JavaFX `Application` subclass, not the controller.
7. Run the starter once and record any errors **before** editing logic.

**If the supplied starter already uses a custom `build.xml`, `module-info.java`, or additional JavaFX libraries, do not indiscriminately add a second configuration.** Use its provided build instructions first.

## 5. Open the starter's FXML in Scene Builder

1. Find the existing `.fxml` file in NetBeans.
2. Try **Open With → Scene Builder** if available. Otherwise open Scene Builder, choose **File → Open**, and select the same actual file inside the starter project's `src` tree.
3. In Scene Builder, locate the **Library** (controls), **Hierarchy** (tree), and **Inspector** (Properties/Code/Layout) panels.
4. Verify the preview resembles the assignment screenshot: stack display; digits 0–9; `X`, `-`, `+`, `/`; `ENTER`; `DROP`.
5. **Save using Command + S**. The FXML file and NetBeans project should now reference the same file.

### If parts are missing

Use the Scene Builder **Library** to add them. A `GridPane` works well for the numeric/operator keypad, while `VBox`, `BorderPane`, and `AnchorPane` can hold the full UI. The starter might already specify a different parent container: preserve it when possible.

Prefer a **read-only** `TextArea` (multi-line) or `ListView<Integer>` for the visible stack, depending on what the starter uses. A `Label` works for a small current-entry/status area. The assignment image does not mandate a particular stack display control.

### Name the controls (Code → fx:id)

**First check whether the starter already assigned names.** Otherwise, example IDs are:

| Control | Example `fx:id` | Purpose |
|---|---|---|
| Stack display (`TextArea`) | `stackDisplay` | Shows contents of stack. |
| Current entry/status (`Label`) | `statusLabel` | Shows pending number or errors. |
| Digit buttons | Optional shared handler; individual IDs not required | Enter digits. |
| Operators and `ENTER`/`DROP` | Optional shared handler or per-button handlers | Operations. |

In Scene Builder, select a control → **Inspector → Code → fx:id**. A value like `stackDisplay` must match the Java controller field *exactly*, including uppercase/lowercase.

## 6. Understand RPN before coding

Unlike a regular infix calculator (`1 + 1`), an RPN calculator **pushes numbers, then executes operators**:

```text
1  ENTER   → stack [1]
1  ENTER   → stack [1, 1]
+          → pop 1 and 1; push 2 → stack [2]
```

Use a `Deque<Integer>` with `ArrayDeque<>` as a stack. In the code below, **the top is the first item** of the deque. Useful methods:

- `push(value)` — add to top
- `pop()` — remove and return top
- `peek()` — inspect top without removing
- `size()` — count stack entries
- `isEmpty()` — test whether stack is empty

### Critical operand order

When you press an operator:

```java
int right = stack.pop();  // most recently pushed value
int left  = stack.pop();  // value immediately below it
```

Calculate **`left - right`** or **`left / right`**, **not** the reverse. Addition/multiplication may conceal this bug because operand order does not matter for them.

### Compound expression from assignment

For the assignment's `9 9 8 7 + - /`, enter the digits as individual operands with `ENTER` after each:

| Button(s) | Stack from bottom to top |
|---|---|
| `9 ENTER` | `[9]` |
| `9 ENTER` | `[9, 9]` |
| `8 ENTER` | `[9, 9, 8]` |
| `7 ENTER` | `[9, 9, 8, 7]` |
| `+` | `[9, 9, 15]` |
| `-` | `[9, -6]` (9 − 15) |
| `/` | `[-1]` (9 ÷ −6, Java integer division truncates toward zero) |

An expression as printed with spaces does **not** automatically mean the user types spaces into the app. Your assignment requires only button processing.

## 7. Implement calculator behavior in the **existing controller**

**Adapt, don't blindly replace.** If the starter has a controller, keep its class name, package, existing `@FXML` fields, handlers, and initialization until you understand what each does. The following is a complete **reference controller core** showing the intended logic. It assumes the FXML has a `TextArea` with `fx:id="stackDisplay"`, a `Label` with `fx:id="statusLabel"`, and separate event handlers. If the starter has different controls, change the declarations and UI update method.

```java
package YOUR_EXISTING_PACKAGE; // Replace with the starter's real package!

import java.util.ArrayDeque;
import java.util.Deque;
import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.control.TextArea;

/**
 * Controller for the RPN calculator.
 * Accepts digits and commands from UI buttons, stores integer operands
 * on a stack, and displays the current stack after each action.
 */
public class CalculatorController { // Use your EXISTING controller name!

    /** Stores calculator operands; the deque's first item is the stack top. */
    private final Deque<Integer> stack = new ArrayDeque<>();

    /** Digits of the number currently being entered, before ENTER is pressed. */
    private final StringBuilder currentEntry = new StringBuilder();

    @FXML private TextArea stackDisplay;
    @FXML private Label statusLabel;

    /** Initializes the display after the FXML controls have been injected. */
    @FXML
    private void initialize() {
        stackDisplay.setEditable(false);
        refreshDisplay();
    }

    /** Appends one digit to the number currently being typed. */
    private void appendDigit(String digit) {
        currentEntry.append(digit);
        statusLabel.setText("Entry: " + currentEntry);
    }

    /** Pushes the entered integer onto the stack. */
    @FXML
    private void enter() {
        if (currentEntry.length() == 0) {
            statusLabel.setText("Enter a number first.");
            return;
        }
        try {
            int value = Integer.parseInt(currentEntry.toString());
            stack.push(value);
            currentEntry.setLength(0);
            refreshDisplay();
        } catch (NumberFormatException ex) {
            // Handles a number too large to fit in a 32-bit Java int.
            statusLabel.setText("Invalid integer or too many digits.");
        }
    }

    /** Removes the top value; does nothing if the stack is empty. */
    @FXML
    private void drop() {
        if (stack.isEmpty()) {
            statusLabel.setText("Stack is empty.");
            return;
        }
        stack.pop();
        refreshDisplay();
    }

    /**
     * Applies an operator to the top two stack items.
     * The first popped value is the right-hand operand.
     */
    private void applyOperator(String operator) {
        if (stack.size() < 2) {
            statusLabel.setText("Need two numbers.");
            return;
        }

        int right = stack.pop();
        int left = stack.pop();

        // Check division by zero before attempting integer division.
        if ("/".equals(operator) && right == 0) {
            stack.push(left);   // Restore original stack in proper order.
            stack.push(right);
            statusLabel.setText("Cannot divide by zero.");
            return;
        }

        int result;
        switch (operator) {
            case "+": result = left + right; break;
            case "-": result = left - right; break;
            case "X": result = left * right; break;
            case "/": result = left / right; break; // Integer division.
            default:
                stack.push(left);
                stack.push(right);
                statusLabel.setText("Unknown operator.");
                return;
        }

        stack.push(result);
        refreshDisplay();
    }

    /** Renders the stack and clears any prior error/status message. */
    private void refreshDisplay() {
        StringBuilder output = new StringBuilder("TOP\n");
        for (int value : stack) {
            output.append(value).append('\n');
        }
        stackDisplay.setText(output.toString());
        statusLabel.setText("Entry: " + currentEntry);
    }

    // The next section explains how to wire digit/operator buttons.
}
```

**Important design choice:** This example requires `ENTER` before an operator, matching the assignment's explicit `1 ENTER 1 ENTER +` sequence. If the instructor's starter has a documented convention for an uncommitted current entry, follow that instead.

### Handle digit buttons — choose ONE approach

**Option A: Individual handlers** (straightforward in Scene Builder): add these methods **inside your existing controller class**:

```java
@FXML private void digit0() { appendDigit("0"); }
@FXML private void digit1() { appendDigit("1"); }
@FXML private void digit2() { appendDigit("2"); }
@FXML private void digit3() { appendDigit("3"); }
@FXML private void digit4() { appendDigit("4"); }
@FXML private void digit5() { appendDigit("5"); }
@FXML private void digit6() { appendDigit("6"); }
@FXML private void digit7() { appendDigit("7"); }
@FXML private void digit8() { appendDigit("8"); }
@FXML private void digit9() { appendDigit("9"); }

@FXML private void add()      { applyOperator("+"); }
@FXML private void subtract() { applyOperator("-"); }
@FXML private void multiply() { applyOperator("X"); }
@FXML private void divide()   { applyOperator("/"); }
```

**Option B: Shared event handler** (less repetition): have all digit buttons call a method receiving an `ActionEvent`, identify the `Button` that fired it, and read its text. For example:

```java
import javafx.event.ActionEvent;
import javafx.scene.control.Button;

@FXML
private void digitPressed(ActionEvent event) {
    Button source = (Button) event.getSource();
    appendDigit(source.getText());
}
```

If you use Option B, set the **On Action** field for *all ten digit buttons* to `digitPressed` and do not also connect individual digit handlers. Adapt existing starter handlers rather than duplicating them.

### A note about errors and integer limits

The assignment only explicitly asks for integer arithmetic and button handling; it does not state an error-message design. Sensible safeguards include:

- Fewer than two stack entries when an operator is pressed: show a message, leave stack unchanged.
- Division by zero: show a message, restore stack unchanged.
- `DROP` on an empty stack: show a message instead of crashing.
- `ENTER` with no current digits: show a message or follow starter behavior.
- Integers beyond `Integer.MAX_VALUE`/`Integer.MIN_VALUE`: `Integer.parseInt` rejects them; arithmetic overflow is **not** fully handled in this sample. If the rubric requires overflow detection, use `Math.addExact`, `subtractExact`, and `multiplyExact` and catch `ArithmeticException`.

## 8. Connect the Scene Builder interface to the Java controller

This is the step where the visual design and Java code become one application.

1. In Scene Builder, select the **root** layout element in **Hierarchy**.
2. In the right-side **Inspector → Controller**, set **Controller class** to the controller's **fully qualified name**, e.g. `your.package.CalculatorController` (replace this with the actual starter package/class).
3. Select the stack display control and set **Code → fx:id** to match your `@FXML` field (`stackDisplay` in the example).
4. Select the status label and give it the `fx:id` `statusLabel` if using that example.
5. Select each button → **Inspector → Code → On Action** and choose the matching controller method:

| Button | Example `On Action` method |
|---|---|
| `0`–`9` | `digit0`–`digit9` **or** shared `digitPressed` |
| `ENTER` | `enter` |
| `DROP` | `drop` |
| `+` | `add` |
| `-` | `subtract` |
| `X` | `multiply` |
| `/` | `divide` |

6. Save (`Command + S`). Return to NetBeans and inspect the FXML for `fx:controller`, `fx:id`, and `onAction` attributes.

FXML event handlers usually appear like this:

```xml
<Button text="ENTER" onAction="#enter" />
<Button text="+" onAction="#add" />
```

**Very common mistake:** An `fx:id` is **not** an event handler. `fx:id="enterButton"` names a control; `onAction="#enter"` calls a controller method when clicked.

### If NetBeans or Scene Builder says it cannot find the controller

- Check the controller package declaration and class name.
- Check the FXML root's `fx:controller` string matches **exactly**.
- Check that handler methods exist with compatible signatures and are accessible to the FXML loader (usually marked `@FXML`).
- Check for duplicated controllers (e.g., an `fx:controller` in FXML **and** `loader.setController(...)` in Java). Use the existing starter's controller-loading approach rather than both.
- Scene Builder may not show compiled project classes, even though NetBeans can load them when the application runs. The **runtime test in NetBeans** is what counts.

## 9. Confirm the Java application loads the right FXML

Your starter's JavaFX main application should launch the **existing** FXML file. A typical (illustrative) JavaFX class looks like:

```java
package YOUR_EXISTING_PACKAGE;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class CalculatorApp extends Application {
    @Override
    public void start(Stage stage) throws Exception {
        Parent root = FXMLLoader.load(
            getClass().getResource("Calculator.fxml")
        );
        stage.setScene(new Scene(root));
        stage.setTitle("RPN Calculator");
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
```

**Do not copy the filename `Calculator.fxml` unless that is what your starter actually uses.** If the FXML is in another resource folder, use the correct resource path. Preserve any existing CSS/image setup and stage sizing.

## 10. Test the calculator systematically

Open NetBeans → **Run Project**. For each test below, click UI buttons only. **Write down the result**, especially if it differs from expectations.

| Test | Buttons to press | Expected stack bottom → top |
|---|---|---|
| Add | `1 ENTER 1 ENTER +` | `[2]` |
| Subtract (order) | `9 ENTER 4 ENTER -` | `[5]` |
| Divide (order) | `8 ENTER 2 ENTER /` | `[4]` |
| Multiply | `3 ENTER 7 ENTER X` | `[21]` |
| Multiple digits | `1 2 ENTER 3 ENTER +` | `[15]` |
| Integer division | `7 ENTER 2 ENTER /` | `[3]` |
| DROP | `5 ENTER 8 ENTER DROP` | `[5]` |
| Empty DROP | Start fresh, press `DROP` | No crash; stack unchanged |
| Not enough operands | Start fresh, press `+` | No crash; stack unchanged |
| Divide by zero | `8 ENTER 0 ENTER /` | No crash; original stack intact |
| Compound example | `9 ENTER 9 ENTER 8 ENTER 7 ENTER + - /` | `[-1]` |
| Reuse result | `2 ENTER 3 ENTER + 4 ENTER X` | `[20]` |

**For tests starting fresh**, restart the app or empty the stack with `DROP` until it is empty. A `CLEAR` button is **not required** by the assignment screenshot.

### Stack display order

Your stack control might show top-to-bottom rather than bottom-to-top. That is fine as long as the top is clearly represented and operator results are correct. The table uses bottom-to-top notation for explanation.

## 11. Troubleshooting on macOS / NetBeans / Scene Builder

| Symptom | Likely cause | Fix |
|---|---|---|
| `The processing instruction target matching "[xX][mM][lL]" is not allowed` | `<?xml ... ?>` is not at the very beginning of the FXML file. You encountered this earlier. | Make `<?xml version="1.0" encoding="UTF-8"?>` the **first content of line 1**; remove preceding blank lines and duplicate XML declarations. |
| Scene Builder opens but FXML fails | Invalid XML, unresolved import/image, missing custom component | Click **Show Details**, read **first meaningful cause**, fix the specific line/resource. |
| `package javafx... does not exist` | JavaFX SDK JARs not on compile classpath | Add the JavaFX 21 `.jar` libraries to NetBeans project compile classpath. |
| `JavaFX runtime components are missing` or module not found | VM module path wrong | Verify actual SDK folder and **Run → VM Options**. |
| `UnsupportedClassVersionError` | A newer JavaFX/JDK binary is being run with an older JDK | Check JDK 21 + JavaFX **21** used by the project; Scene Builder's own runtime is separate. |
| `Location is not set` / FXML not found | Wrong resource path | Match `getResource(...)` to the FXML file's actual location in project output. |
| `LoadException` at `onAction` | Misspelled or mismatched handler | Check `onAction="#method"`, Java method name, signature, and `@FXML`. |
| `NullPointerException` at `stackDisplay.setText(...)` | FXML injection failed | Make `fx:id` and `@FXML` field match, confirm correct controller. |
| Image/logo missing | Wrong resource URL | Use starter-provided asset and a valid project resource path. |
| Button works in preview but not at runtime | Preview is for **layout**, not the running Java controller | Run the actual Ant project from NetBeans. |
| Arithmetic seems reversed | `left` / `right` popped in wrong order | Compute `left - right`, `left / right`. |

## 12. Comments and documentation checklist

Because the sheet explicitly says **"full descriptive comments are required"**, include meaningful explanations rather than one vague comment at the top.

- Class-level comment: purpose and RPN behavior.
- Stack field comment: what the stack holds and which end is "top".
- Current-entry buffer comment: how digit presses form multi-digit integers.
- Comments for `ENTER`, `DROP`, and each category of operations.
- Explanation of operand order (especially subtraction/division).
- Explanation of refresh/display method and error cases.
- Existing starter code: retain or improve relevant explanatory comments.

Use Javadoc (`/** ... */`) for classes/methods when appropriate, and brief inline comments for non-obvious logic. Avoid commenting obvious statements such as `i++`.

## 13. Submission checklist

- [ ] I modified the **instructor-provided starter** rather than starting from scratch.
- [ ] The interface resembles the assignment screenshot and preserves starter assets.
- [ ] All digit buttons work with mouse clicks.
- [ ] Multi-digit integers can be entered.
- [ ] `ENTER` pushes a completed number.
- [ ] `DROP` removes one top stack value.
- [ ] `+`, `-`, `X`, `/` all produce correct integer results.
- [ ] Subtraction and division use the correct operand order.
- [ ] `1 ENTER 1 ENTER +` gives `2`.
- [ ] The assignment's compound `9 9 8 7 + - /` works (with `ENTER` to push each operand).
- [ ] Intermediate results remain available for further compound calculations.
- [ ] Invalid operations do not crash the application.
- [ ] FXML and controller are connected correctly.
- [ ] The entire project **builds and runs through NetBeans / Java with Ant**.
- [ ] Full descriptive comments are included.
- [ ] I reviewed the separate **standard rubric**, if supplied.
- [ ] I am submitting the instructor-requested project files/archive format (not just an FXML screenshot).

## 14. The fastest practical order to complete it

1. **Open starter project**, make backup, and run it once.
2. **Inspect existing FXML/controller** and write down actual class/file/ID names.
3. Open FXML in **Scene Builder** and verify/fix layout and control IDs.
4. Implement **stack + digit entry + ENTER + DROP**.
5. Implement **operators** with correct pop order and push result.
6. Connect each **On Action** in Scene Builder to its handler.
7. Run from NetBeans, test simple operations, then the **compound** sequence.
8. Add descriptive comments and review the supplied rubric.
9. Save, rebuild, and submit the original starter project in the required format.

---

### What I still need to give you exact file-by-file edits

Upload the **instructor's starter project** (preferably a `.zip`) and, if separate, the grading rubric. Then the generic placeholders in this guide can be replaced by your project's **real class names, existing event handlers, FXML control IDs, and file paths**, without accidentally undoing required starter code.

**Source:** Your uploaded *CSIS 312 Assignment 2 RPN Calculator* instruction sheet (one page, including UI screenshot). All example code, suggested safeguards, and workflow details above are instructional additions; they are not presented as requirements that the handout explicitly states.
