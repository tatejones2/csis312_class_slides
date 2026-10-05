# JHTP11_11 - LECTURE 3 Updated -WK3 -FALL 2021_B (1).pptx

## Slide 1

Chapter 11Exception Handling: A Deeper Look
Java How to Program, 11/e

### Speaker notes


1

## Slide 2

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Speaker notes


78

## Slide 3

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Speaker notes


79

## Slide 4

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 5

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 6

An exception indicates a problem during a program’s execution.
Exception handling enables applications to resolve (or handle) exceptions.
In some cases, a program can continue executing as if no problem had been encountered.
The features presented in this week help you write robust faut-tolerant programs that can deal with problems and continue executing or terminate gracefully.

Further Discussion on Exception Handling
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 7

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 8

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 9

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 10

Further Discussion on Exception Handling Cont.
First, we handle an exception that occurs when a method attempts to divide an integer by zero.
We discuss when to use exception handling and show a portion of the exception-handling class hierarchy.
As you’ll see, only subclasses of Throwable can be used with exception handling.
We introduce the try statement’s finally block, which executes whether or not an exception occurs.
We then show how to use chained exceptions to add application-specific information to an exception and how to create your own exception types.

## Slide 11

Further Discussion on Exception Handling Cont.
In the below examples, first we demonstrate what happens when errors arise in an application that does not use exception handling.
Example 1 prompts the user for two integers and passes them to method quotient, which calculates the integer quotient and returns an int result.
In this example, you’ll see that exceptions are thrown (i.e., the exception occurs) by a method when it detects a problem and is unable to handle it.

## Slide 12

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 13

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 14

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 15

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 16

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 17

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 18

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 19

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 20

The first sample execution in above shows a successful division.
In the second execution, the user enters the value 0 as the denominator.
Several lines of information are displayed in response to this invalid input.
This information is known as a stack trace, which includes the name of the exception (java.lang.ArithmeticException) in a descriptive message that indicates the problem and the method-call stack (i.e., the call chain) at the time the problem occurred.
The stack trace includes the path of execution that led to the exception method by method.
This helps you debug the program.
Even if a problem has not occurred, you can see the stack trace any time by calling Thread.dumpStack().
Exception Handling : Stack Trace

## Slide 21

An uncaught exception is one for which there are no matching catch blocks.
You saw uncaught exceptions in the second and third outputs of Fig. 11.2.
Recall that when exceptions occurred in that example, the application terminated early (after displaying the exception’s stack trace).
Uncaught Exceptions

## Slide 22

If an exception occurs in a try block (such as an InputMismatchException being thrown as a result of the code at line 23 of Fig. 11.3),
The try block terminates immediately and program control transfers to the first of the following catch blocks in which the exception parameter’s type matches the thrown exception’s type.
In Fig. 11.3, the first catch block catches InputMismatchExceptions (which occur if invalid input is entered)
and the second catch block catches ArithmeticExceptions (which occur if an attempt is made to divide by zero).
After exception is handled, program control does not return to the throw point, because the try block has expired (and its local variables have been lost)
Rather, control resumes after the last catch block. This is known as the termination model of exception handling.
Termination Model of Exception Handling

## Slide 23

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 24



## Slide 25

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 26

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 27

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 28

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 29

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 30

All Java exception classes inherit directly or indirectly from class Exception, forming an inheritance hierarchy.
You can extend this hierarchy with your own exception classes.
Figure in next slide shows a small portion of the inheritance hierarchy for class Throwable (a subclass of Object), which is the superclass of class Exception.

Java Exception Hierarchy

## Slide 31

Only Throwable objects can be used with the exception-handling mechanism.
Class Throwable has two direct subclasses:
Exception and Error.
Class Exception and its subclasses—for example, Runtime-Exception (package java.lang) and IOException (package java.io)—represent exceptional situations that can occur in a Java program and that can be caught by the application.
Class Error and its subclasses represent abnormal situations that happen in the JVM.
Java Exception Hierarchy

## Slide 32

The Java exception hierarchy contains hundreds of classes.
Information about Java’s exception classes can be found throughout the Java API.
You can view Throwable’s documentation at:
http://docs.oracle.com/javase/8/docs/api/java/lang/Throwable.html
From there, you can look at this class’s subclasses to get more information about Java’s Exceptions and Errors.
Java Exception Hierarchy

## Slide 33

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 34

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 35

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 36

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 37

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 38

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 39

If multiple catch blocks match a particular exception type, only the first matching catch block executes when an exception of that type occurs.
It’s a compilation error to catch the exact same type in two different catch blocks associated with a particular try block.
However, there can be several catch blocks that match an exception—i.e., several catch blocks whose types are the same as the exception type or a superclass of that type.
For example, we could follow a catch block for type ArithmeticException with a catch block for type Exception—both would match ArithmeticExceptions, but only the first matching catch block would execute.
Only the First Matching catch Executes

## Slide 40

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 41

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 42

Programs that obtain certain resources must return them to the system to avoid so-called resource leaks.
In programming languages such as C and C++, the most common resource leak is a memory leak.
Java performs automatic garbage collection of memory no longer used by programs, thus avoiding most memory leaks.
However, other types of resource leaks can occur.
For example, files, database connections and network connections that are not closed properly after they’re no longer needed might not be available for use in other programs.
The finally Block

## Slide 43

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 44

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 45

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 46

The optional finally block (sometimes referred to as the finally clause) consists of the finally keyword, followed by code enclosed in curly braces.
If it’s present, it’s placed after the last catch block.
If there are no catch blocks, the finally block is required and immediately follows the try block.
The finally Block

## Slide 47

Because a finally block always executes, it typically contains resource-release code.
Suppose a resource is allocated in a try block.
If no exception occurs, the catch blocks are skipped and control proceeds to the finally block, which frees the resource.
Control then proceeds to the first statement after the finally block.
If an exception occurs in the try block, the try block terminates.
If the program catches the exception in one of the corresponding catch blocks, it processes the exception,
then the finally block releases the resource and
control proceeds to the first statement after the finally block.
If program doesn’t catch the exception, the finally block still releases the resource.
Demonstrating the finally Block

## Slide 48

Example below demonstrates that the finally block executes even if an exception is not thrown in the corresponding try block.
The program contains static methods main (lines 5–14), throwException (lines 17–35) and doesNotThrowException (lines 38–50).
Methods throwException and doesNotThrowException are declared static, so main can call them directly without instantiating a UsingExceptions object.
System.out and System.err are streams—sequences of bytes.
While System.out (i.e standard output stream) displays a program’s output, System.err (i.e. standard error stream) displays a program’s errors.
Using two different streams enables easy separation of error messages from output.
For example, data output from System.err could be sent to a log file, while data output from System.out can be displayed on the screen.
Releasing Resources in a finally Block

## Slide 49

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 50

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 51

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 52

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 53

// Fig. 11.5: UsingExceptions.java
// try...catch...finally exception handling mechanism.

public class UsingExceptions {
   public static void main(String[] args) {
      try {
         throwException();
      }
      catch (Exception exception) { // exception thrown by throwException
         System.err.println("Exception handled in main");
      }

      doesNotThrowException();
   }

   // demonstrate try...catch...finally
   public static void throwException() throws Exception {
      try { // throw an exception and immediately catch it
         System.out.println("Method throwException");
         throw new Exception(); // generate exception
      }
      catch (Exception exception) { // catch exception thrown in try
         System.err.println(
            "Exception handled in method throwException");
         throw exception; // rethrow for further processing

         // code here would not be reached; would cause compilation errors

      }
      finally { // executes regardless of what occurs in try...catch
         System.err.println("Finally executed in throwException");
      }

      // code here would not be reached; would cause compilation errors
   }

   // demonstrate finally when no exception occurs
   public static void doesNotThrowException() {
      try { // try block does not throw an exception
         System.out.println("Method doesNotThrowException");
      }
      catch (Exception exception) { // does not execute
         System.err.println(exception);
      }
      finally { // executes regardless of what occurs in try...catch
         System.err.println("Finally executed in doesNotThrowException");
      }

      System.out.println("End of method doesNotThrowException");
   }
}


## Slide 54

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 55

  Encapsulation and Information Hiding
Classes (and their objects) encapsulate, i.e., encase, their attributes and methods.
Objects may communicate with one another, but they’re normally not allowed to know how other objects are implemented—implementation details can be hidden within the objects themselves.
Information hiding, as we’ll see, is crucial to good software engineering.
©1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 56

 Inheritance
A new class of objects can be created conveniently by inheritance—the new class (called the subclass) starts with the characteristics of an existing class (called the superclass), possibly customizing them and adding unique characteristics of its own.
In our car analogy, an object of class “convertible” certainly is an object of the more general class “automobile,” but more specifically, the roof can be raised or lowered.
©1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 57

  Interfaces
Interfaces are collections of related methods that typically enable you to tell objects what to do, but not how to do it.
In the car analogy, a “basic-driving-capabilities” interface consisting of a steering wheel, an accelerator pedal and a brake pedal would enable a driver to tell the car what to do.
Once you know how to use this interface for turning, accelerating and braking, you can drive many types of cars, even though manufacturers may implement these systems differently.
©1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 58

  Interfaces (Cont.)
A class implements zero or more interfaces, each of which can have one or more methods, just as a car implements separate interfaces for basic driving functions, controlling the radio, controlling the heating and air conditioning systems, and the like.
Just as car manufacturers implement capabilities differently, classes may implement an interface’s methods differently.

## Slide 59

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 60

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 61

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 62

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 63

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 64

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 65

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 66

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 67

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 68

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 69

// Fig. 11.6: UsingExceptions.java
// Stack unwinding and obtaining data from an exception object.

public class UsingExceptions {
   public static void main(String[] args) {
      try {
         method1();
      }
      catch (Exception exception) { // catch exception thrown in method1
         System.err.printf("%s%n%n", exception.getMessage());
         exception.printStackTrace();

         // obtain the stack-trace information
         StackTraceElement[] traceElements = exception.getStackTrace();

         System.out.printf("%nStack trace from getStackTrace:%n");
         System.out.println("Class\t\tFile\t\t\tLine\tMethod");

         // loop through traceElements to get exception description
         for (StackTraceElement element : traceElements) {
            System.out.printf("%s\t", element.getClassName());
            System.out.printf("%s\t", element.getFileName());
            System.out.printf("%s\t", element.getLineNumber());
            System.out.printf("%s%n", element.getMethodName());
         }
      }
   }

   // call method2; throw exceptions back to main
   public static void method1() throws Exception {
      method2();
   }

   // call method3; throw exceptions back to method1
   public static void method2() throws Exception {
      method3();
   }

   // throw Exception back to method2
   public static void method3() throws Exception {
      throw new Exception("Exception thrown in method3");
   }
}


## Slide 70

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 71

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 72

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 73

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 74

// Fig. 11.7: UsingChainedExceptions.java// Chained exceptions.public class UsingChainedExceptions {   public static void main(String[] args) {      try {         method1();       }       catch (Exception exception) { // exceptions thrown from method1         exception.printStackTrace();      }    }    // call method2; throw exceptions back to main   public static void method1() throws Exception {      try {         method2();       }       catch (Exception exception) { // exception thrown from method2         throw new Exception("Exception thrown in method1", exception);      }    }   // call method3; throw exceptions back to method1   public static void method2() throws Exception {      try {         method3();      }       catch (Exception exception) { // exception thrown from method3         throw new Exception("Exception thrown in method2", exception);      }   }    // throw Exception back to method2   public static void method3() throws Exception {      throw new Exception("Exception thrown in method3");   } }

## Slide 75

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 76

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 77

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 78

  Assertion Statement
An assertion is a statement in Java which ensures the correctness of any assumptions which have been done in the program.
When an assertion is executed, it is assumed to be true.
If the assertion is false, the JVM will throw an Assertion error.
It finds it application primarily in the testing purposes.
Assertion statements are used along with boolean expressions.
Assertions in Java can be done with the help of the assert keyword.

## Slide 79

  Assertion Statement
There are two ways in which an assert statement can be used.
First Way −

Second Way −
assert expression;
assert expression1 : expression2
import java.util.Scanner;

class Test
{
    public static void main( String args[] )
    {
        int value = 15;
        assert value >= 20 : " Underweight";
        System.out.println("value is "+value);
    } }

## Slide 80

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 81

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 82

// Fig. 11.8: AssertTest.java// Checking with assert that a value is within rangeimport java.util.Scanner;public class AssertTest {   public static void main(String[] args) {      Scanner input = new Scanner(System.in);      System.out.print("Enter a number between 0 and 10: ");      int number = input.nextInt();            // assert that the value is >= 0 and <= 10      assert (number >= 0 && number <= 10) : "bad number: " + number;            System.out.printf("You entered %d%n", number);   } }

## Slide 83

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 84

EXTRAL SLIDES FOR HARD WORKING STUDENTS
EXTRAL SLIDES FOR HARD WORKING STUDENTS
