# Chapter 8: Classes and Objects: A Deeper Look

[All chapters](README.md) · [Course guide](../reference/COURSE_GUIDE.md)

## Main concepts

- Scope and access modifiers; separate class responsibilities.
- Constructors, overloaded constructors, the current object (`this`) and validation.
- Composition, enums, class members (`static`), constants (`final`) and packages.
- Time and account examples; precise decimal calculations with `BigDecimal`.

## Sources

- [JHTP11_08 - UPDATED -Week 1 - 2024 (1).pptx](../JHTP11_08%20-%20UPDATED%20-Week%201%20-%202024%20%281%29.pptx)
- [Searchable text: JHTP11_08 - UPDATED -Week 1 - 2024 (1).md](../reference/extracted/JHTP11_08%20-%20UPDATED%20-Week%201%20-%202024%20%281%29.md)

## Related instructor examples

These documents cover several chapters; use the examples relevant to this topic.

- [Week1 Java CODES.docx](../Week1%20Java%20CODES.docx) · [Searchable examples](../reference/extracted/Week1%20Java%20CODES.txt)

## Reading these notes

The material below preserves the available extracted text. Slide and PDF page numbers
refer to the supplied files, not necessarily the printed textbook page numbers.
Images, diagrams and image-based code require the original documents. OCR can
misread identifiers and punctuation; extracted examples are not verified runnable code.

Tate clarified on October 5, 2026 that the professor permits AI use; that
updated permission supersedes the older statement retained in the slide extract.

## Slide text: JHTP11_08 - UPDATED -Week 1 - 2024 (1).md

### Slide 1

Introduction to CSIS 312
Continuation of 212.
You are responsible for knowing all the material in CSIS 212,
So review Chapters 1-11 in our textbook to be sure you are up to speed on the previous materials for CSIS 212.
CSIS 312 will begin from the chapters where CSIS 212 stopped
Using the same textbook (i.e. CSIS 312 will cover Chapters 11 to 24).



Welcome to CSIS 312

#### Speaker notes


6

### Slide 2

Syllabus discussion (to be discussed soon)
Coursework/assignments
We will discuss all the programming concepts in the classes with examples.
The concepts to be discussed during classes are necessary/important for you to do your assignments.
Absentees tend to struggle in the assignments
Programming assignments use pair programming
Form your partnership ASAP.
Attendance: class participations are necessary in order not to struggle in the assignments


Welcome to CSIS 312

#### Speaker notes


7

### Slide 3

USE OF AI IN ASSIGNMENT IS AN ACADEMIC FRAUD

#### Speaker notes


8

### Slide 4

Importance of practicing to prepare for assignments and exams
If you missed any classes, you are responsible for covering the materials for that missed sessions by yourself to get your assignments done.
This (i.e. your absence) is not the responsibility of my office hours to bridge your own absence and write your codes/assignments for you for the missed classes.

#### Speaker notes


9

### Slide 5

 Coursework/assignment
Attendance: class participation necessary in order not to struggle in the assignment
In-Class Programming Exercise (40 points)- To evaluate your CSIS 212 knowledge as a prerequisite to CSIS 312.
Class participation folder (55 points)
Syllabus discussion
Any questions?

Welcome to CSIS 312

#### Speaker notes


10

### Slide 6

Chapter 8 Classes and Objects: A Deeper Look
Java How to Program, 11/e

#### Speaker notes


11

### Slide 7

8.1  Lecture Outline
In this module, you will look at the use of the keyword “static” with variables, methods, and classes.
See additional details of creating class declarations.
Use the throw statement to indicate that a problem has occurred.
Use static variables and methods.
you will look at how you can customize exception handling using the throw statement.
You will also learn about the use of the “this” keyword to make development of multiple constructors easier.
Use keyword this in a constructor to call another constructor in the same class.

#### Speaker notes


12

### Slide 8

8.1  Introduction
Deeper look at building classes, controlling access to members of a class and creating constructors.
Show how to throw an exception to indicate that a problem has occurred.
Composition—a capability that allows a class to have references to objects of other classes as members.
More details on enum types.
Discuss static class members and final instance variables in detail.
Show how to organize classes in packages to help manage large applications and promote reuse.

#### Speaker notes


13

### Slide 9

   Understanding program scope
A variable that is declared inside a method is only accessible from inside that method – its “scope” of accessibility is only local to the method in which it is declared.
This means that a variable of the same name can be declared in another method without conflict.
A counter variable declared in a for loop cannot be accessed outside the loop – its scope is limited to the for statement block.


#### Speaker notes


14

### Slide 10

   Understanding program scope
The static keyword that is used in method declarations ensures that the method is a “class method” – globally accessible from any other method in the class.
Similarly, a “class variable” can be declared with the static keyword to ensure it is globally accessible throughout the class.
Its declaration should be made before the main method declaration, right after the curly bracket following the class declaration.
A program may have a global class variable and local method variable of the same name.

#### Speaker notes


15

### Slide 11

   Understanding program scope
The local method variable takes precedence unless the global class variable is explicitly addressed by the class name prefix using dot notation, or if a local variable of that name has not been declared.
Use local method variables wherever possible to avoid conflicts – global class variables are typically only used for constants.

#### Speaker notes


16

### Slide 12

   Understanding program scope: EXAMPLE 1

#### Speaker notes


17

### Slide 13

   Understanding program scope

#### Speaker notes


18

### Slide 14

   Understanding program scope: EXAMPLE 1
// EXAMPLE 1

class Scope
{
    final static String txt = "This is a global variable of the Scope class";

    public static void main ( String[] args )
    {
        String txt = "This is a local variable in the main method";
        System.out.println( txt );
        sub();

        System.out.println( Scope.txt );
    }
    public static void sub( )

    {

String txt = "This is a local variable in the sub method";

        System.out.println( txt );
    }
}

#### Speaker notes


19

### Slide 15

   Private & Public Access modifier for Method
Classes simplify programming, because the client can use only a class’s public methods.
Clients generally care about what the class does but not how the class does it.
Methods declared with access modifier private can be called only by other methods of the class in which the private methods are declared.
Such methods are commonly referred to as utility methods or helper methods because they’re typically used to support the operation of the class’s other methods.

#### Speaker notes


20

### Slide 16

   Forming multiple classes
In the same way that a program may have multiple methods, larger programs may consist of several classes –
Each class provides specific functionality.
This modular format is generally preferable to writing the entire program in a single class as it makes debugging easier and provides better flexibility.
The public keyword that appears in declarations is an “access modifier” that determines how visible an item will be to other classes.

#### Speaker notes


22

### Slide 17

   Forming multiple classes
The public keyword can be used in the class declaration to explicitly ensure that class will be visible to any other class.
If it is omitted, the default access control level allows access from other local classes.
The public keyword must always be used with the program’s main method, however, so that method will be visible to the compiler.
The compiler will automatically find classes in adjacent external .java files – and create compiled .class files for each one.


#### Speaker notes


23

### Slide 18

   Creating multiple classes in NetBeans

#### Speaker notes


24

### Slide 19

   EXERCISE: Forming multiple classes: EXAMPLE 2

#### Speaker notes


27

### Slide 20

 REVISION: Forming multiple classes: EXAMPLE 2
// EXAMPLE 2
//Class 1
class Multi
{
    public static void main ( String[] args )
    {
        String msg = "This is a local variable in the Multi class";
        System.out.println( msg );
    System.out.println( Data.txt );
    Data.greeting();
        Draw.line();    } }
// Class 2
class Data
{
    public final static String txt = "This is a global variable of the Data class";
    public static void greeting()
    {
        System.out.print( "This is a global method " );
        System.out.println( "of the Data class" );
    }
// Class 3
class Draw
{
    static void line()
    {
        System.out.println("___________________________________________");
    } }

#### Speaker notes


28

### Slide 21

Class Activities
Following the examples above, create two extra classes and call them whatever name you want.
Create at least one method in each of the two new classes.
Invoke/call the two new classes from the Multi class.


#### Speaker notes


29

### Slide 22

   Forming multiple classes

#### Speaker notes


30

### Slide 23

   Catching exceptions: Example 3

#### Speaker notes


31

### Slide 24

   Extending an existing class
A class can inherit the features of another class by using the extends keyword in the class declaration to specify the name of the class from which it should inherit.
For example, the declaration class Extra extends Base inherits from the Base class.
The inheriting class is described as the “sub” class, and the class from which it inherits is described as the “super” class.
In the example declaration above, the Base class is the super class and the Extra class is the sub class.

#### Speaker notes


32

### Slide 25

INHERITANCE IN JAVA- Example
class A {
   int a = 9;
    }
class B extends A {
   int b = 4;
    }
public class Demo {
   public static void main(String args[]) {
      B obj = new B();
      System.out.println("Value of a is: " + obj.a);
      System.out.println("Value of b is: " + obj.b);
            }
}


#### Speaker notes


35

### Slide 26

Class Activities
Following the examples above, create two extra classes for Class C and Class D.
Class C should extend Class A
Class D should extend Class B.
Create objects for each new class as shown in the given example.


#### Speaker notes


36

### Slide 27

   Extending an existing class
Methods and variables created in a super class can generally be treated as if they existed in the sub class provided they have not been declared with the private keyword, which denies access from outside the original class.
A method in a sub class will override a method of the same name that exists in its super class unless their arguments differ.
The method in the super class may be explicitly addressed using its class name and dot notation.
For example, SuperClass.run().
It should be noted that a try catch statement in a method within a super class does not catch exceptions that occur in a sub class
– the calling statement must be enclosed within its own try catch statement to catch those exceptions.

#### Speaker notes


37

### Slide 28

   Extending an existing class: Example 4

#### Speaker notes


38

### Slide 29

   Extending an existing class

#### Speaker notes


39

### Slide 30

  Creating an object class
Real-world objects are all around us, and they each have attributes and behaviors that we can describe:
 Attributes describe the features that an object has.
 Behaviors describe actions that an object can perform.
For example, a car might be described with attributes of “red” and “coupe”, along with an “accelerates” behavior.
These features could be represented in Java programming with a Car class containing variable properties of color and bodyType, along with an accelerate() method.

#### Speaker notes


40

### Slide 31

  Creating an object class
Java is said to be an Object Oriented Programming (OOP) language because it makes extensive use of object attributes and behaviors to perform program tasks.
Objects are created in Java by defining a class as a template from which different copies, or “instances”, can be made.
Each instance of the class can be customized by assigning attribute values and behaviors to describe that object.
The Car class is created as a class template in the steps described below – with the default attributes and behavior outlined above.
An instance of the Car class is created in the steps described on page later, inheriting the same default attributes and behavior.

#### Speaker notes


41

### Slide 32

  Creating an object class : Example 5
The static keyword declares class variables and class methods – in this case, as members of the Car class.

#### Speaker notes


42

### Slide 33

7.4  Account Class: Initializing Objects with Constructors
Each class you declare can optionally provide a constructor with parameters that can be used to initialize an object of a class when the object is created.
Java requires a constructor call for every object that’s created.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


43

### Slide 34

7.4  Account Class: Initializing Objects with Constructors
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


44

### Slide 35

  Producing an object instance
Each class has a built-in “constructor” method that can be used to create a new instance of that class.
The constructor method has the same name as the class, and is invoked with the new keyword.
Each instance of a class inherits the object’s attributes and behaviors.
The principle of inheritance is used throughout Java so that programs can use ready-made properties.
To be more flexible, object class templates can be defined in a file other than that containing the program. This means they can be readily used by multiple programs.

#### Speaker notes


45

### Slide 36

  Producing an object instance : Example 6

#### Speaker notes


46

### Slide 37

  Producing an object instance
A virtual class is created for the new Porsche object that replicates the original Car class.
Both these objects contain static “class variables” and a “class method”, which are addressed using the class name and dot notation – as these members are globally accessible, this is not considered good programming practice.
Whilst this example demonstrates how instances of an object inherit properties of the original class,
It is improved in the next example below that uses non-static members to create “instance variables” and an “instance method”, which cannot be addressed from outside that class – as these members are not globally accessible,
this is considered good programming practice.

#### Speaker notes


47

### Slide 38

   Catching exceptions
A program may encounter a runtime problem that causes an “exception” error, which halts its execution.
Often, this will be created by unexpected user input.
A well-written program should, therefore, attempt to anticipate all possible ways the user might cause exceptions at runtime.
Code where exceptions might arise can be identified and enclosed within a try catch statement block.
This allows the program to handle exceptions without halting execution and looks like this:

#### Speaker notes


48

### Slide 39

   Catching exceptions
The parentheses following the catch keyword specify the class of exception to be caught and assign it to the variable “e”.
The top-level Exception class catches all exceptions.
Responses can be provided for specific exceptions, however, using multiple catch statements to identify different lower-level exception classes.

#### Speaker notes


49

### Slide 40

   Catching exceptions
The most common exceptions are the NumberFormatException, which arises when the program encounters a value that is not of the expected numeric type,
and the ArrayIndexOutOfBoundsException, which arises when the program attempts to address an array element number that is outside the index size.
It is helpful to create a separate response for each of these exceptions to readily notify the user about the nature of the problem.
Optionally, a try catch statement block can be extended with a finally statement block, containing code that will always be executed – irrespective of whether the program has encountered exceptions.
The e.getMessage() method returns further information about some captured exceptions.

#### Speaker notes


54

### Slide 41

Throwing Exceptions
The throw keyword in Java is used to explicitly throw an exception from a method or any block of code.
The throw keyword is mainly used to throw custom exceptions.

Syntax:
throw Instance

Example:
throw new ArithmeticException("/ by zero");
The Throwable class is the superclass of all errors and exceptions in the Java language.
Only objects that are instances of this class (or one of its subclasses) are thrown by the Java Virtual Machine or can be thrown by the Java throw statement.

#### Speaker notes


55

### Slide 42

   Catching exceptions: Example 3
// Example 3
class Exceptions
{
    public static void main( String[] args )
    {
        try
        {
            int num = Integer.parseInt(args[0]);
            System.out.println( "You entered: "+num );
        }
        catch(ArrayIndexOutOfBoundsException e)
        {
        System.out.println( "Integer argument required.");
        }
        catch( NumberFormatException e )
        {
        System.out.println( "Argument is wrong format.");
        }
        finally
        {
        System.out.println( "Program ends." );
        }   } }

#### Speaker notes


56

### Slide 43

Throwing Exceptions

#### Speaker notes


57

### Slide 44

Throwing Exceptions
For example Exception is a sub-class of Throwable and user defined exceptions typically extend Exception class.
The flow of execution of the program stops immediately after the throw statement is executed and the nearest enclosing try block is checked to see if it has a catch statement that matches the type of exception.
If it finds a match, controlled is transferred to that statement otherwise next enclosing try block is checked and so on.
If no matching catch is found then the default exception handler will halt the program.

#### Speaker notes


58

### Slide 45

Throwing Exceptions  Example 8
All methods use the throw statement to throw an exception.
The throw statement requires a single argument: a throwable object.
Throwable objects are instances of any subclass of the Throwable class.
Here's an example of a throw statement:
Example 8

#### Speaker notes


60

### Slide 46

Throwing Exceptions
If some code within a method throws a checked exception, then the method must either handle the exception or it must specify the exception using throws keyword.
For example, consider the following Java program  (EXAMPLE 7A and 7B) that opens file at location “import.txt” and prints the first three lines of it.
Without exception handling throw statement, the program doesn’t compile, because the
function main() uses FileReader() and FileReader() throws a checked exception FileNotFoundException.
It also uses readLine() and close() methods, and these methods also throw checked exception IOException

#### Speaker notes


61

### Slide 47

Throwing Exceptions
(EXAMPLE 7A and 7B)

#### Speaker notes


73

### Slide 48

8.2  Time Class Case Study
Example 8.1 further demonstrates exception and classes.
Class Time1 represents the time of day.
private int instance variables hour, minute and second represent the time in universal-time format (24-hour clock format in which hours are in the range 0–23, and minutes and seconds are each in the range 0–59).
public methods setTime, toUniversalString and toString.
Called the public services or the public interface that the class provides to its clients.

#### Speaker notes


74

### Slide 49



#### Speaker notes


78

### Slide 50

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


81

### Slide 51

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


82

### Slide 52

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


83

### Slide 53

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


95

### Slide 54

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


96

### Slide 55

8.2  Time Class Case Study (Cont.)
Class Time1 does not declare a constructor, so the compiler supplies a default constructor.
Each instance variable implicitly receives the default int value.
Instance variables also can be initialized when they are declared in the class body, using the same initialization syntax as with a local variable.

#### Speaker notes


97

### Slide 56

8.2  Time Class Case Study (Cont.)
Method setTime and Throwing Exceptions
Method setTime declares three int parameters and uses them to set the time.
Lines 13–14 test each argument to determine whether the value is outside the proper range.

#### Speaker notes


98

### Slide 57

8.2  Time Class Case Study (Cont.)
Method setTime and Throwing Exceptions (cont.)
For incorrect values, setTime throws an exception of type IllegalArgumentException
Notifies the client code that an invalid argument was passed to the method.
Can use try...catch to catch exceptions and attempt to recover from them.
The class instance creation expression in the throw statement creates a new object of type IllegalArgumentException. In this case, we call the constructor that allows us to specify a custom error message.
After the exception object is created, the throw statement immediately terminates method setTime and the exception is returned to the calling method that attempted to set the time.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


101

### Slide 58

8.2  Time Class Case Study (Cont.)
Software Engineering of the Time1 Class Declaration
The instance variables hour, minute and second are each declared private.
The actual data representation used within the class is of no concern to the class’s clients.
Reasonable for Time1 to represent the time internally as the number of seconds since midnight or the number of minutes and seconds since midnight.
Clients could use the same public methods and get the same results without being aware of this.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


102

### Slide 59



#### Speaker notes


104

### Slide 60

8.2  Time Class Case Study (Cont.)
Java SE 8—Date/Time API
Rather than building your own date and time classes, you’ll typically reuse the ones provided by the Java API.
Java SE 8 introduces a new Date/Time API—defined by the classes in the package java.time—applications built with Java SE 8 should use the Date/Time API’s capabilities, rather than those in earlier Java versions.
fixes various issues with the older classes and provides more robust, easier-to-use capabilities for manipulating dates, times, time zones, calendars and more.
Learn more about the Date/Time API’s classes at:
download.java.net/jdk8/docs/api/java/time/package-summary.html

#### Speaker notes


107

### Slide 61

8.3  Controlling Access to Members
Access modifiers public and private control access to a class’s variables and methods.
public methods present to the class’s clients a view of the services the class provides (the class’s public interface).
Clients need not be concerned with how the class accomplishes its tasks.
For this reason, the class’s private variables and private methods (i.e., its implementation details) are not accessible to its clients.
private class members are not accessible outside the class.

#### Speaker notes


113

### Slide 62



#### Speaker notes


114

### Slide 63

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


115

### Slide 64

REVISITING : Initializing Objects with Constructors
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


116

### Slide 65

REVISITING : Initializing Objects with Constructors
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


117

### Slide 66

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


118

### Slide 67

Further Discussion on constructors:
The AccountTest program (Example 9B) i.e. Fig 7.6  initializes two Account objects using the constructor.
// Example 10A and 10B contains a modified Account class with such a constructor.
The AccountTest program (Example 10B) initializes two Account objects using the constructor.

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


120

### Slide 68

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


121

### Slide 69

// Fig. 7.5: Account.java// Account class with a constructor that initializes the name.public class Account {   private String name; // instance variable   // constructor initializes name with parameter name   public Account(String name) { // constructor name is class name      this.name = name;   }                                               // method to set the name   public void setName(String name) {      this.name = name;    }    // method to retrieve the name   public String getName() {      return name;    }  }
// Fig. 7.6: AccountTest.java// Using the Account constructor to initialize the name instance// variable at the time each Account object is created.public class AccountTest {   public static void main(String[] args) {       // create two Account objects      Account account1 = new Account("Jane Green");      Account account2 = new Account("John Blue");
      // display initial value of name for each Account      System.out.printf("account1 name is: %s%n", account1.getName());      System.out.printf("account2 name is: %s%n", account2.getName());   } }

#### Speaker notes


125

### Slide 70

Improve the program above by adding three more variables in Account.java class (in addition to “Name” that you already have) e.g.:
SSN
 Address
Account balance
Ensure you declare them with necessary variable type and use Set and Get methods as appropriate.
Declare constructors to take care of the new variables.
In the AccountTest.java class create objects of the new Account.java that would include all the additional variables that you have just created.
Create account objects for at least 4 members of your family in AccountTest.java class .

Class Activities

#### Speaker notes


131

### Slide 71

7.4.2  Class AccountTest: Initializing Account Objects When They’re Created (Cont.)
Constructors Cannot Return Values
Constructors can specify parameters but not return types.
Default Constructor
If a class does not define constructors, the compiler provides a default constructor with no parameters, and the class’s instance variables are initialized to their default values.
There’s No Default Constructor in a Class That Declares a Constructor
If you declare a constructor for a class, the compiler will not create a default constructor for that class.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


133

### Slide 72

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


134

### Slide 73

8.4  Referring to the Current Object’s Members with the this Reference
Every object can access a reference to itself with keyword this.
When an instance method is called for a particular object, the method’s body implicitly uses keyword this to refer to the object’s instance variables and other methods.
Enables the class’s code to know which object should be manipulated.
Can also use keyword this explicitly in an instance method’s body.
Can use the this reference implicitly and explicitly.

#### Speaker notes


135

### Slide 74

8.4  Referring to the Current Object’s Members with the this Reference (Cont.)
When you compile a .java file containing more than one class, the compiler produces a separate class file with the .class extension for every compiled class.
When one source-code (.java) file contains multiple class declarations, the compiler places both class files for those classes in the same directory.
A source-code file can contain only one public class—otherwise, a compilation error occurs.
Non-public classes can be used only by other classes in the same package.

#### Speaker notes


136

### Slide 75

SimpleTime class is in next slide

#### Speaker notes


138

### Slide 76

If parameter names for the constructor that are identical to the class’s instance-variable names.
We use the this reference to refer to the instance variables.


#### Speaker notes


140

### Slide 77

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


142

### Slide 78

8.4  Referring to the Current Object’s Members with the this Reference (Cont.)
SimpleTime declares three private instance variables—hour, minute and second.
If parameter names for the constructor that are identical to the class’s instance-variable names.
We use the this reference to refer to the instance variables.


#### Speaker notes


148

### Slide 79

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


151

### Slide 80

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


152

### Slide 81

8.5  Time Class Case Study: Overloaded Constructors
Overloaded constructors enable objects of a class to be initialized in different ways.
To overload constructors, simply provide multiple constructor declarations with different signatures.
Recall that the compiler differentiates signatures by the number of parameters, the types of the parameters and the order of the parameter types in each signature.

#### Speaker notes


153

### Slide 82

8.5  Time Class Case Study: Overloaded Constructors (Cont.)
Class Time2 (Fig. 8.5) contains five overloaded constructors that provide convenient ways to initialize objects.
The compiler invokes the appropriate constructor by matching the number, types and order of the types of the arguments specified in the constructor call with the number, types and order of the types of the parameters specified in each constructor declaration.


#### Speaker notes


156

### Slide 83

8.5  Time Class Case Study: Overloaded Constructors (Cont.)
Using this as shown here is a popular way to reuse initialization code provided by another of the class’s constructors
A constructor that calls another constructor in this manner is known as a delegating constructor
Makes the class easier to maintain and modify
If we need to change how objects of class Time2 are initialized, only the constructor that the class’s other constructors call will need to be modified

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


157

### Slide 84

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


162

### Slide 85

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


165

### Slide 86

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


169

### Slide 87

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


170

### Slide 88

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


171

### Slide 89

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


172

### Slide 90

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


173

### Slide 91

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 92

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 93

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 94

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 95

8.5  Time Class Case Study: Overloaded Constructors (Cont.)
A program can declare a so-called no-argument constructor that is invoked without arguments.
Such a constructor simply initializes the object as specified in the constructor’s body.
Using this in method-call syntax as the first statement in a constructor’s body invokes another constructor of the same class.
Popular way to reuse initialization code provided by another of the class’s constructors rather than defining similar code in the no-argument constructor’s body.
Once you declare any constructors in a class, the compiler will not provide a default constructor.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 96

8.5  Time Class Case Study: Overloaded Constructors (Cont.)
Notes Regarding Class Time2’s set and get Methods and Constructors
Methods can access a class’s private data directly without calling the get methods.
However, consider changing the representation of the time from three int values (requiring 12 bytes of memory) to a single int value representing the total number of seconds that have elapsed since midnight (requiring only four bytes of memory).
If we made such a change, only the bodies of the methods that access the private data directly would need to change—in particular, the three-argument constructor, the setTime method and the individual set and get methods for the hour, minute and second.
There would be no need to modify the bodies of methods toUniversalString or toString because they do not access the data directly.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 97

8.5  Time Class Case Study: Overloaded Constructors (Cont.)
Designing the class in this manner reduces the likelihood of programming errors when altering the class’s implementation.
Similarly, each Time2 constructor could be written to include a copy of the appropriate statements from the three-argument constructor.
Doing so may be slightly more efficient, because the extra constructor calls are eliminated.
But, duplicating statements makes changing the class’s internal data representation more difficult.
Having the Time2 constructors call the constructor with three arguments requires any changes to the implementation of the three-argument constructor be made only once.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 98

8.6  Default and No-Argument Constructors
Every class must have at least one constructor.
If you do not provide any constructors in a class’s declaration, the compiler creates a default constructor that takes no arguments when it’s invoked.
The default constructor initializes the instance variables to the initial values specified in their declarations or to their default values (zero for primitive numeric types, false for boolean values and null for references).
Recall that if your class declares constructors, the compiler will not create a default constructor.
In this case, you must declare a no-argument constructor if default initialization is required.
Like a default constructor, a no-argument constructor is invoked with empty parentheses.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 99

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 100

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 101

8.7  Notes on Set and Get Methods
Set methods are also commonly called mutator methods, because they typically change an object’s state—i.e., modify the values of instance variables.
Get methods are also commonly called accessor methods or query methods.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 102

8.7  Notes on Set and Get Methods (Cont.)
It would seem that providing set and get capabilities is essentially the same as making a class’s instance variables public.
A public instance variable can be read or written by any method that has a reference to an object that contains that variable.
If an instance variable is declared private, a public get method certainly allows other methods to access it, but the get method can control how the client can access it.
A public set method can—and should—carefully scrutinize at-tempts to modify the variable’s value to ensure valid values.
Although set and get methods provide access to private data, it is restricted by the implementation of the methods.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 103

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 104

8.7  Notes on Set and Get Methods (Cont.)
Validity Checking in Set Methods
The benefits of data integrity do not follow automatically simply because instance variables are declared private—you must provide validity checking.
Predicate Methods
Another common use for accessor methods is to test whether a condition is true or false—such methods are often called predicate methods.
Example: ArrayList’s isEmpty method, which returns true if the ArrayList is empty and false otherwise.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 105

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 106

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 107

8.8  Composition
A class can have references to objects of other classes as members.
This is called composition and is sometimes referred to as a has-a relationship.
Example: An AlarmClock object needs to know the current time and the time when it’s supposed to sound its alarm, so it’s reasonable to include two references to Time objects in an AlarmClock object.

### Slide 108

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 109

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 110

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 111

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 112

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 113

8.9  enum Types
An enum is a special "class" that represents a group of constants (unchangeable variables, like final variables).
To create an enum, use the enum keyword (instead of class or interface), and separate the constants with a comma.
Note that they should be in uppercase letters:
enum Level {
  LOW,
  MEDIUM,
  HIGH
}
Level myVar = Level.MEDIUM;
You can access enum constants with the dot syntax:

### Slide 114

8.9  enum Types
The basic enum type defines a set of constants represented as unique identifiers.
Like classes, all enum types are reference types.
An enum type is declared with an enum declaration, which is a comma-separated list of enum constants
The declaration may optionally include other components of traditional classes, such as constructors, fields and methods.

### Slide 115

8.9  Enum Types (Cont.)
Each enum declaration declares an enum class with the following restrictions:
enum constants are implicitly final.
enum constants are implicitly static.
Any attempt to create an object of an enum type with operator new results in a compilation error.
enum constants can be used anywhere constants can be used, such as in the case labels of switch statements and to control enhanced for statements.

### Slide 116

8.9  Enum Types (Cont.)
enum declarations contain two parts—the enum constants and the other members of the enum type.
An enum constructor can specify any number of parameters and can be overloaded.
For every enum, the compiler generates the static method values that returns an array of the enum’s constants.
When an enum constant is converted to a String, the constant’s identifier is used as the String representation.

### Slide 117

8.9   Enum inside a Class
You can also have an enum inside a class:
public class Main {
  enum Level {
    LOW,
    MEDIUM,
    HIGH
  }

  public static void main(String[] args) {
    Level myVar = Level.MEDIUM;
    System.out.println(myVar);
  }
}
The output will be:

MEDIUM

### Slide 118

8.9     Loop Through an Enum
The enum type has a values() method, which returns an array of all enum constants.
This method is useful when you want to loop through the constants of an enum:
for (Level myVar : Level.values()) {
  System.out.println(myVar);
}
The output will be:

LOW
MEDIUM
HIGH

### Slide 119

Using the program above as your example
Create a class containing the workdays of the week as enum constants
Print Wednesday out of the constants.
Loop through the constants and print out the five days using values() method.

Class Activities

### Slide 120

8.9      Difference between Enums and Classes
An enum can, just like a class, have attributes and methods.
The only difference is that enum constants are public, static and final (unchangeable - cannot be overridden).
An enum cannot be used to create objects, and it cannot extend other classes (but it can implement interfaces).
Why And When To Use Enums?
Use enums when you have values that you know aren't going to change, like month days, days, colors, deck of cards, etc.

### Slide 121

8.14  Package Access
If no access modifier is specified for a method or variable when it’s declared in a class, the method or variable is considered to have package access.
If a program uses multiple classes from the same package, these classes can access each other’s package-access members directly through references to objects of the appropriate classes, or in the case of static members through the class name.
Package access is rarely used.

### Slide 122



### Slide 123

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 124

// Fig. 8.15: PackageDataTest.java
// Package-access members of a class are accessible by other classes
// in the same package.

public class PackageDataTest {
   public static void main(String[] args) {
      PackageData packageData = new PackageData();

      // output String representation of packageData
      System.out.printf("After instantiation:%n%s%n", packageData);

      // change package access data in packageData object
      packageData.number = 77;
      packageData.string = "Goodbye";

      // output String representation of packageData
      System.out.printf("%nAfter changing values:%n%s%n", packageData);
   }   }

// class with package access instance variables
class PackageData {
   int number = 0; // package-access instance variable
   String string = "Hello"; // package-access instance variable

   // return PackageData object String representation
   public String toString() {
      return String.format("number: %d; string: %s", number, string);
   }  }

### Slide 125

CLASS ACTIVITIES
Change the declaration of variables in Class PackageDate to private variables and implement relevant set and get method to print out the values . i.e.:
class PackageData {
private   int number = 0;
private    String string = "Hello";


### Slide 126

EXTRAL SLIDES FOR HARD WORKING STUDENTS
EXTRAL SLIDES FOR HARD WORKING STUDENTS

### Slide 127

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 128

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 129

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 130

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 131

8.9   Enum Types (Cont.)
Use the static method range of class EnumSet (declared in package java.util) to access a range of an enum’s constants.
Method range takes two parameters—the first and the last enum constants in the range
Returns an EnumSet that contains all the constants between these two constants, inclusive.
The enhanced for statement can be used with an EnumSet just as it can with an array.
Class EnumSet provides several other static methods.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 132

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 133

8.10  Garbage Collection
Every object uses system resources, such as memory.
Need a disciplined way to give resources back to the system when they’re no longer needed; otherwise, “resource leaks” might occur.
The JVM performs automatic garbage collection to reclaim the memory occupied by objects that are no longer used.
When there are no more references to an object, the object is eligible to be collected.
Collection typically occurs when the JVM executes its garbage collector, which may not happen for a while, or even at all before a program terminates.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 134

8.10  Garbage Collection (Cont.)
So, memory leaks that are common in other languages like C and C++ (because memory is not automatically reclaimed in those languages) are less likely in Java, but some can still happen in subtle ways.
Resource leaks other than memory leaks can also occur.
An app may open a file on disk to modify its contents.
If the app does not close the file, it must terminate before any other app can use the file.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 135

8.10  Garbage Collection (Cont.)
A Note about Class Object’s finalize Method
Every class in Java has the methods of class Object (package java.lang), one of which is method finalize.
You should never use method finalize, because it can cause many problems and there’s uncertainty as to whether it will ever get called before a program terminates.
The original intent of finalize was to allow the garbage collector to perform termination housekeeping on an object just before reclaiming the object’s memory.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 136

8.10  Garbage Collection (Cont.)
Now, it’s considered better practice for any class that uses system resources—such as files on disk—to provide a method that programmers can call to release resources when they’re no longer needed in a program.
AutoClosable objects reduce the likelihood of resource leaks when you use them with the try-with-resources statement.
As its name implies, an AutoClosable object is closed automatically, once a try-with-resources statement finishes using the object.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 137

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 138

8.11  static Class Members
In certain cases, only one copy of a particular variable should be shared by all objects of a class.
A static field—called a class variable—is used in such cases.
A static variable represents classwide information—all objects of the class share the same piece of data.
The declaration of a static variable begins with the keyword static.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 139

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 140

8.11  static Class Members (Cont.)
Static variables have class scope—they can be used in all of the class’s methods.
Can access a class’s public static members through a reference to any object of the class, or by qualifying the member name with the class name and a dot (.), as in Math.random().
private static class members can be accessed by client code only through methods of the class.
static class members are available as soon as the class is loaded into memory at execution time.
To access a public static member when no objects of the class exist (and even when they do), prefix the class name and a dot (.) to the static member, as in Math.PI.
To access a private static member when no objects of the class exist, provide a public static method and call it by qualifying its name with the class name and a dot.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 141

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 142

8.11  static Class Members (Cont.)
A static method cannot access a class’s instance variables and instance methods, because a static method can be called even when no objects of the class have been instantiated.
For the same reason, the this reference cannot be used in a static method.
The this reference must refer to a specific object of the class, and when a static method is called, there might not be any objects of its class in memory.
If a static variable is not initialized, the compiler assigns it a default value—in this case 0, the default value for type int.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 143

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 144

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 145

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 146

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 147

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 148

8.11  static Class Members (Cont.)
String objects in Java are immutable—they cannot be modified after they are created.
Therefore, it’s safe to have many references to one String object.
This is not normally the case for objects of most other classes in Java.
If String objects are immutable, you might wonder why are we able to use operators + and += to concatenate String objects.
String-concatenation actually results in a new String object containing the concatenated values—the original String objects are not modified.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 149

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 150

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 151

8.11  static Class Members (Cont.)
In a typical app, the garbage collector might eventually reclaim the memory for any objects that are eligible for collection.
The JVM does not guarantee when, or even whether, the garbage collector will execute.
When the garbage collector does execute, it’s possible that no objects or only a subset of the eligible objects will be collected.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 152

8.12  static Import
A static import declaration enables you to import the static members of a class or interface so you can access them via their unqualified names in your class—that is, the class name and a dot (.) are not required when using an imported static member.
Two forms
One that imports a particular static member (which is known as single static import)
One that imports all static members of a class (which is known as static import on demand)

### Slide 153

8.12  static Import (Cont.)
The following syntax imports a particular static member:
    import static packageName.ClassName.staticMemberName;
where packageName is the package of the class, ClassName is the name of the class and staticMemberName is the name of the static field or method.
The following syntax imports all static members of a class:
    import static packageName.ClassName.*;
packageName is the package of the class and ClassName is the name of the class.
* indicates that all static members of the specified class should be available for use in the class(es) declared in the file.
static import declarations import only static class members.
Regular import statements should be used to specify the classes used in a program.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 154

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 155

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 156

8.13  final Instance Variables
The principle of least privilege is fundamental to good software engineering.
Code should be granted only the amount of privilege and access that it needs to accomplish its designated task, but no more.
Makes your programs more robust by preventing code from accidentally (or maliciously) modifying variable values and calling methods that should not be accessible.
Keyword final specifies that a variable is not modifiable (i.e., it’s a constant) and any attempt to modify it is an error.
    private final int INCREMENT;
Declares a final (constant) instance variable INCREMENT of type int.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 157

8.13  final Instance Variables (cont.)
final variables can be initialized when they are declared or by each of the class’s constructors so that each object of the class has a different value.
If a class provides multiple constructors, every one would be required to initialize each final variable.
A final variable cannot be modified by assignment after it’s initialized.
If a final variable is not initialized, a compilation error occurs.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 158

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 159

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 160

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 161

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 162

8.14  Package Access
If no access modifier is specified for a method or variable when it’s declared in a class, the method or variable is considered to have package access.
In a program uses multiple classes from the same package, these classes can access each other’s package-access members directly through references to objects of the appropriate classes, or in the case of static members through the class name.
Package access is rarely used.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 163

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 164

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 165

8.15  Using BigDecimal for Precise Monetary Calculations
In earlier chapters, we demonstrated monetary calculations using values of type double.
some double values are represented approximately.
Any application that requires precise floating-point calculations—such as those in financial applications—should instead use class BigDecimal (from package java.math).
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 166

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 167

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 168

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 169

8.15  Using BigDecimal for Precise Monetary Calculations (Cont.)
Interest Calculations Using BigDecimal
Figure 8.16 reimplements the interest calculation example of Fig. 5.6 using objects of class BigDecimal to perform the calculations.
We also introduce class NumberFormat (package java.text) for formatting numeric values as locale-specific Strings—for example, in the U.S. locale, the value 1234.56, would be formatted as "1,234.56", whereas in many European locales it would be formatted as "1.234,56".
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 170

8.15  Using BigDecimal for Precise Monetary Calculations (Cont.)
Rounding BigDecimal Values
In addition to precise calculations, BigDecimal also gives you control over how values are rounded—by default all calculations are exact and no rounding occurs.
If you do not specify how to round BigDecimal values and a given value cannot be represented exactly—such as the result of 1 divided by 3, which is 0.3333333…—an ArithmeticException occurs.
You can specify the rounding mode for BigDecimal by supplying a MathContext object (package java.math) to class BigDecimal’s constructor when you create a BigDecimal. You may also provide a MathContext to various BigDecimal methods that perform calculations.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 171

8.15  Using BigDecimal for Precise Monetary Calculations (Cont.)
Class MathContext contains several pre-configured MathContext objects that you can learn about at
http://docs.oracle.com/javase/7/docs/api/java/math/MathContext.html
By default, each pre-configured MathContext uses so called “bankers rounding” as explained for the RoundingMode constant HALF_EVEN at:
http://docs.oracle.com/javase/7/docs/api/java/math/RoundingMode.html#HALF_EVEN

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 172

8.15  Using BigDecimal for Precise Monetary Calculations (Cont.)
Scaling BigDecimal Values
A BigDecimal’s scale is the number of digits to the right of its decimal point. If you need a BigDecimal rounded to a specific digit, you can call BigDecimal method setScale.
For example, the following expression returns a BigDecimal with two digits to the right of the decimal point and using bankers rounding:
amount.setScale(2, RoundingMode.HALF_EVEN)

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 173

8.16  (Optional) GUI and Graphics Case Study: Using Objects with Graphics

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 174

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 175

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 176

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 177

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 178

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 179

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.
