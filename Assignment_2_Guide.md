# Assignment 2 RPN Calculator Guide

Use this guide to complete the supplied CSIS 312 Java calculator project. It maps the assignment requirements to the starter code, explains the calculation logic, and gives you a checklist for testing your work.

## 1. Assignment requirements

The two supplied Word documents contain the same assignment text:

- Use the supplied starter project.
- Complete an RPN calculator that performs integer addition, subtraction, multiplication, and division.
- Handle the buttons on the UI; keyboard input is not required.
- Support compound calculations, including `9 9 8 7 + - /`.
- ENTER pushes the entered number onto the stack.
- DROP discards the top stack value.
- Include full descriptive comments.
- Follow the standard course rubric. That rubric, a deadline, and submission packaging instructions are not included in these files; check your course materials for them.

The remaining sections explain implementation choices and starter-code behavior. Error recovery recommendations below are useful safeguards, but the assignment text does not specify their exact wording or behavior.

## 2. Know which files to use

| File | Purpose | Work needed |
| --- | --- | --- |
| `src/RPNCalculator/RPNModel.java` | Stores operands and performs arithmetic | Complete `enter`, `multiply`, and `subtract`; correct `divide` |
| `src/RPNCalculator/CalculatorController.java` | Handles buttons, input, display, and error messages | Complete handlers for 0, 3, 7, +, and /; review input and error handling |
| `src/RPNCalculator/Calculator.java` | Launches the JavaFX application | Starter explicitly says no changes needed |
| `src/RPNCalculator/CalculatorView.fxml` | Defines the existing UI and button connections | Keep the provided UI and handler names |
| `src/RPNCalculator/lu.png` | Image referenced by the FXML | Keep alongside the FXML |
| `src/stack/MyStack.java` | Provided generic stack | No changes required; capacity is **8 values** |
| `src/stack/LinkedList.java` | Storage used by `MyStack` | No changes required |
| `Assignment 2.iml` | IntelliJ module configuration | Identifies `src` as the source folder; inherits the project JDK |

Keep the package names `RPNCalculator` and `stack`. Use the supplied `MyStack<Integer>` rather than replacing the project with another calculator or stack implementation.

## 3. Understand RPN before coding

RPN puts the operator after its operands. To calculate `1 + 1`, press:

```text
1 ENTER 1 ENTER +
```

Each ENTER pushes a number. An arithmetic operation removes the top two numbers and pushes one result, so a successful operation reduces the stack size by one.

**Operand order matters.** The first value popped is the right operand; the second is the left operand:

```text
right = pop()
left  = pop()
result = left operator right
push(result)
```

For `8 ENTER 2 ENTER -`, calculate `8 - 2`, giving `6`. For `8 ENTER 2 ENTER /`, calculate `8 / 2`, giving `4`.

Use integer arithmetic: `7 / 2` gives `3`. Negative integer division truncates toward zero, so `-7 / 2` gives `-3`.

### Trace the required compound calculation

In this table the stack is written from bottom to top, with the top at the right. This notation explains the logical stack; it does not describe the exact display layout.

| Action | Stack afterward |
| --- | --- |
| `9 ENTER` | `[9]` |
| `9 ENTER` | `[9, 9]` |
| `8 ENTER` | `[9, 9, 8]` |
| `7 ENTER` | `[9, 9, 8, 7]` |
| `+` | `[9, 9, 15]` |
| `-` | `[9, -6]` |
| `/` | `[-1]` |

The calculation is `9 / (9 - (8 + 7))`, which produces `-1` using integer division. Spaces in the assignment example separate operands; on the UI, use ENTER to separate numbers.

## 4. Complete the model first

Work in `RPNModel.java`. Keep arithmetic in this class and UI messages in the controller.

### `enter(int val)`

- Push `val` onto the existing stack.
- Return the boolean returned by `stack.push(val)`.
- Do not always return `true`: the ninth stored value must be rejected because the capacity is eight.

### `multiply()`

- If fewer than two operands exist, return `false` without changing the stack.
- Pop the two operands, multiply them, and push the result.
- Return success.

Use the supplied `add()` method as a pattern for the size check and result push.

### `subtract()`

- Check for at least two operands before popping anything.
- Pop the right operand first and the left operand second.
- Push `left - right` and return success.

### Correct `divide()`

The supplied method currently evaluates `stack.pop() / stack.pop()`. That reverses standard RPN operand order and can remove values before a division error occurs.

- Return `false` if fewer than two operands exist.
- Treat the top value as the divisor.
- Check for zero before removing values. The provided `stack.get(stack.size() - 1)` lets you inspect the top without popping it; `divide()` already declares `throws Exception`.
- If the divisor is zero, throw an exception with a clear message for the controller to display.
- Otherwise, pop right and left, then push `left / right`.

Recommended behavior: preserve both operands when division by zero fails so the user can correct the input.

### Review the existing methods

- `add()` already checks the operand count and pushes the sum.
- `drop()` already returns `false` on an empty stack and removes a value otherwise. Its unbraced `else` is visually misleading, although its current control flow works; braces would make the intent clearer if you edit it.
- `getValues()` is explicitly marked as requiring no modification. It formats the stack for the display.

## 5. Complete the controller

Work in `CalculatorController.java`. `currentVal` is the number being typed as a string; `rpn` holds the entered stack values.

### Digit handlers

Complete:

- `buttonZeroClick`
- `buttonThreeClick`
- `buttonSevenClick`

Follow an existing handler such as `buttonFourClick`: append the appropriate digit to `currentVal`, then call `updateDisplay()`. Append rather than replace so that pressing `1`, then `2`, creates `12`.

### Addition handler

Complete `buttonPlusClick` using the existing subtraction or multiplication handler as a pattern:

1. Commit any pending number using the cursor-handling logic.
2. Call `rpn.add()`.
3. Display an insufficient-operands message if it returns `false`.
4. Refresh the display on success.

### Division handler

Complete `buttonDivideClick` similarly, but catch exceptions from `rpn.divide()` so division by zero displays a useful message instead of escaping the event handler.

### Review pending input handling

The supplied `checkCursor()` automatically pushes a typed number before an operator. This makes `8 ENTER 2 /` work without a second ENTER.

However, `checkCursor()` currently returns `void`, so an operator handler can continue even when parsing fails or the stack is full. Recommended improvement:

1. Make `checkCursor()` return a boolean.
2. Return `true` when there is no pending input or when it was successfully pushed.
3. On an invalid integer or full stack, display an error and return `false`; retain `currentVal` for correction.
4. Update **all four** operator handlers to stop when it returns `false`.

This prevents an attempted operation from changing older stack values after the new operand was rejected.

### Review display and DROP behavior

- `updateDisplay()` clears the error label. When both refreshing and showing an error, refresh first and set the error afterward so it remains visible.
- The supplied DROP handler deletes the last typed character when `currentVal` is nonempty. When there is no pending input, it drops the top stack value. Preserve this useful starter behavior unless your instructor directs otherwise.
- On an empty stack, the supplied DROP handler sets an error and then calls `updateDisplay()`, immediately clearing the error. Adjust that ordering so the message stays visible.
- Consider calling `updateDisplay()` after creating `rpn` during initialization to clear the FXML's initial placeholder label.
- `buttonSign` is declared in the controller, but the FXML contains no sign button. No additional sign-button feature is specified. Subtraction can produce negative results.

## 6. Run the supplied application

1. Open the starter project in your Java IDE and confirm `src` is the source folder.
2. Use the Java and JavaFX setup prescribed by your course. The starter imports JavaFX, and the supplied module file does not declare a JavaFX library dependency.
3. Keep `CalculatorView.fxml` and `lu.png` available as resources in the `RPNCalculator` package when building or running.
4. Run `RPNCalculator.Calculator`, the JavaFX application entry point.
5. If the UI fails to load, check the first exception for missing JavaFX dependencies, missing resources, or a mismatch between FXML `onAction` names and controller methods.

## 7. Test with the actual buttons

Start each independent test with an empty stack and no pending number. Restart the application if that is easiest. `X` below means the multiplication button.

| Test | Button sequence | Expected result or behavior |
| --- | --- | --- |
| Required simple example | `1 ENTER 1 ENTER +` | `2` |
| Newly completed digits | `7 3 0 ENTER` | One stored value, `730` |
| Addition | `8 ENTER 2 ENTER +` | `10` |
| Subtraction order | `8 ENTER 2 ENTER -` | `6` |
| Negative result | `2 ENTER 8 ENTER -` | `-6` |
| Multiplication | `6 ENTER 7 ENTER X` | `42` |
| Division order | `8 ENTER 2 ENTER /` | `4` |
| Integer division | `7 ENTER 2 ENTER /` | `3` |
| Negative division | `2 ENTER 9 ENTER - 2 ENTER /` | `-3` |
| Required compound calculation | `9 ENTER 9 ENTER 8 ENTER 7 ENTER + - /` | `-1` |
| Pending operand | `8 ENTER 2 /` | `4` |
| Empty stack operation | `+` | Insufficient-operands message; no stack change |
| One operand | `5 ENTER X` | Insufficient-operands message; `5` remains |
| Division by zero | `8 ENTER 0 ENTER /` | Visible error; recommended: both operands remain |
| DROP stored value | `4 ENTER 5 ENTER DROP` | Only `4` remains |
| DROP typed digit | `1 2 DROP ENTER` | Stores `1` |
| DROP empty stack | `DROP` | Visible no-value-to-drop message |
| Empty ENTER | `ENTER` | Invalid-value message; no stack change |
| Out-of-range integer | `2 1 4 7 4 8 3 6 4 8 ENTER` | Invalid-value message; no stack change |
| Stack capacity | Push eight values, then type a ninth and press ENTER | Full-stack message; eight stored values remain |
| Operator with full stack and pending input | Push eight values, type a ninth, press `+` | Recommended: reject pending input and preserve the eight stored values |

Repeat insufficient-operands checks for subtraction and division too. Confirm you can correct input and continue after errors. Verify that the displayed values match the stack after successful operations.

## 8. Comments and submission checklist

Write descriptive comments explaining each completed method's purpose, parameters, return value, and relevant errors. Explain why subtraction and division pop the right operand first, and why validation happens before modifying the stack.

The supplied headers include attribution and an academic-integrity statement. Preserve starter attribution, add your own author information where your course requires it, and ensure statements and citations accurately reflect your work and permitted sources.

- [ ] Used the supplied project and stack classes.
- [ ] Completed model methods `enter`, `multiply`, and `subtract`.
- [ ] Corrected division operand order and handled division by zero.
- [ ] Completed controller handlers for 0, 3, 7, +, and /.
- [ ] Verified all digit buttons and all four arithmetic buttons.
- [ ] Verified ENTER, DROP, multidigit input, and stack capacity.
- [ ] Verified the required compound calculation produces `-1`.
- [ ] Checked visible error messages and recovery after errors.
- [ ] Added full descriptive comments and accurate attribution.
- [ ] Confirmed the application runs with its FXML and image resources.
- [ ] Checked the course rubric, deadline, and required submission format.
