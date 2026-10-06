# Chapter 9: Inheritance

[All chapters](README.md) · [Course guide](../reference/COURSE_GUIDE.md)

## Main concepts

- Superclass and subclass relationships using `extends`.
- Inherited members, access control and `protected`.
- Superclass constructors and methods using `super`.
- Method overriding, `Object.toString`, and commission employee examples.

## Sources

- [JHTP11_09 - UPDATED 312- -2022 (1).pptx](../JHTP11_09%20-%20UPDATED%20312-%20-2022%20%281%29.pptx)
- [Searchable text: JHTP11_09 - UPDATED 312- -2022 (1).md](../reference/extracted/JHTP11_09%20-%20UPDATED%20312-%20-2022%20%281%29.md)

## Related instructor examples

These documents cover several chapters; use the examples relevant to this topic.

- [Week 2, 3 & 4 Java CODES-3.docx](../Week%202%2C%203%20%26%204%20Java%20CODES-3.docx) · [Searchable examples](../reference/extracted/Week%202%2C%203%20%26%204%20Java%20CODES-3.txt)

## Reading these notes

The material below preserves the available extracted text. Slide and PDF page numbers
refer to the supplied files, not necessarily the printed textbook page numbers.
Images, diagrams and image-based code require the original documents. OCR can
misread identifiers and punctuation; extracted examples are not verified runnable code.

## Slide text: JHTP11_09 - UPDATED 312- -2022 (1).md

### Slide 1

Chapter 9Object-Oriented Programming: Inheritance
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


1

### Slide 2

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


2

### Slide 3

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


4

### Slide 4

9.1  Introduction
Inheritance
A new class is created by acquiring an existing class’s members and possibly embellishing them with new or modified capabilities.
Can save time during program development by basing new classes on existing proven and debugged high-quality software.
Increases the likelihood that a system will be implemented and maintained effectively.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


5

### Slide 5

9.1  Introduction - Inheritance
When creating a class, rather than declaring completely new members, you can designate that the new class should inherit the members of an existing class.
Existing class is the superclass
New class is the subclass
A subclass can be a superclass of future subclasses.
A subclass can add its own fields and methods.
A subclass is more specific than its superclass and represents a more specialized group of objects.
The subclass exhibits the behaviors of its superclass and can add behaviors that are specific to the subclass.
This is why inheritance is sometimes referred to as specialization.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


6

### Slide 6

9.1  Introduction – Inheritance cont.
The direct superclass is the superclass from which the subclass explicitly inherits.
An indirect superclass is any class above the direct superclass in the class hierarchy.
The Java class hierarchy begins with class Object (in package java.lang)
Every class in Java directly or indirectly extends (or “inherits from”) Object.
Java supports only single inheritance, in which each class is derived from exactly one direct superclass.


#### Speaker notes


7

### Slide 7

9.1  Introduction (Cont.)
Multiple inheritance means that a subclass can inherit from two or more superclasses.

C++ allows multiple inheritance, but Java allows only single inheritance, that is, a subclass can inherit only from one superclass.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


8

### Slide 8

9.1  Introduction (Cont.)
We had distinguished between the is-a relationship and the has-a relationship
Is-a represents inheritance
In an is-a relationship, an object of a subclass can also be treated as an object of its superclass
Has-a represents composition
In a has-a relationship, an object contains as members references to other objects

#### Speaker notes


9

### Slide 9

9.2  Superclasses and Subclasses
Figure 9.1 lists several simple examples of superclasses and subclasses
Superclasses tend to be “more general” and subclasses “more specific.”
Because every subclass object is an object of its superclass, and one superclass can have many subclasses,
the set of objects represented by a superclass is typically larger than the set of objects represented by any of its subclasses.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


13

### Slide 10

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


15

### Slide 11

Use of EXTENDS Keyword
An object can acquire the properties and behaviour of another object using Inheritance.
In Java, the extends keyword is used to indicate that a new class is derived from the base class using inheritance.
So basically, extends keyword is used to extend the functionality of the class.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


17

### Slide 12

RE-VISITING Use of EXTENDS Keyword

EXAMPLE 4
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


18

### Slide 13

  Superclasses and Subclasses (Cont.)
A superclass exists in a hierarchical relationship with its subclasses.
Next slide shows a sample university community class hierarchy
Also called an inheritance hierarchy.
Each arrow in the hierarchy represents an is-a relationship.
Follow the arrows upward in the class hierarchy
an Employee is a CommunityMember”
“a Teacher is a Faculty member.”
CommunityMember is the direct superclass of Employee, Student and Alumnus and is an indirect superclass of all the other classes in the diagram.
Starting from the bottom, you can follow the arrows and apply the is-a relationship up to the topmost superclass.

#### Speaker notes


19

### Slide 14

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


20

### Slide 15

9.2  Superclasses and Subclasses (Cont.)
Fig. 9.3 shows a Shape inheritance hierarchy.
We follow the arrows from the bottom of the diagram to the topmost superclass in this class hierarchy to identify several is-a relationships.
A Triangle is a TwoDimensionalShape and is a Shape
ASphere is a ThreeDimensionalShape and is a Shape.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


25

### Slide 16

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


28

### Slide 17

9.2  Superclasses and Subclasses (Cont.)
Not every class relationship is an inheritance relationship.
Has-a relationship
Create classes by composition of existing classes.
Example: Given the classes Employee, BirthDate and TelephoneNumber, it’s improper to say that an Employee is a BirthDate or that an Employee is a TelephoneNumber.
However, an Employee has a BirthDate, and an Employee has a TelephoneNumber.

#### Speaker notes


29

### Slide 18

9.2  Superclasses and Subclasses (Cont.)
Objects of all classes that extend a common superclass can be treated as objects of that superclass.
Commonality expressed in the members of the superclass.
Inheritance issue
A subclass can inherit methods that it does not need or should not have.
Even when a superclass method is appropriate for a subclass, that subclass often needs a customized version of the method.
The subclass can override (redefine) the superclass method with an appropriate implementation.

#### Speaker notes


30

### Slide 19

9.3  protected Members
A class’s public members are accessible wherever the program has a reference to an object of that class or one of its subclasses.
A class’s private members are accessible only within the class itself.
protected access is an intermediate level of access between public and private.
A superclass’s protected members can be accessed by members of that superclass, by members of its subclasses and by members of other classes in the same package
protected members also have package access.
All public and protected superclass members retain their original access modifier when they become members of the subclass.

#### Speaker notes

10%
31

### Slide 20

9.3  protected Members (Cont.)
A superclass’s private members are hidden from its subclasses
They can be accessed only through the public or protected methods inherited from the superclass
Subclass methods can refer to public and protected members inherited from the superclass simply by using the member names.
When a subclass method overrides an inherited superclass method, the superclass version of the method can be accessed from the subclass by preceding the superclass method name with keyword super and a dot (.) separator.

#### Speaker notes


36

### Slide 21

The use of SUPER keyword
The super keyword refers to superclass (parent) objects.
It is used to call superclass methods, and to access the superclass constructor.
The most common use of the super keyword is to eliminate the confusion between superclasses and subclasses that have methods with the same name.
To understand the super keyword, you should have a basic understanding of Inheritance and Polymorphism.

#### Speaker notes


37

### Slide 22

Example 9. The use of SUPER keyword
Example 9. The use of SUPER keyword
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


40

### Slide 23

RE-VISITING SuperClass and SubClass

EXAMPLE 5
Change the following access modifiers to “private”
protected String brand = "Ford";
Implement relevant set and get methods.

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


47

### Slide 24

Improve Time2 Class by creating additional variable e.g. month (in addition to hour, minute and second).
Implement necessary overloaded constructor to take care of the additional variable that you have just created.
Implement relevant set and get methods.
In Time2Test class, create an object that print all the four variables.
Class Activities

#### Speaker notes

$1000 + 10% of sales
49

### Slide 25

ASSIGNMENT: Reverse Polish Notation Calculator
In reverse Polish notation, the operators follow their operands; for instance, to add 3 and 4, one would write 3 4 + rather than 3 + 4.
If there are multiple operations, operators are given immediately after their second operands; so the expression written 3 − 4 + 5 in conventional notation would be written 3 4 − 5 + in reverse Polish notation: 4 is first subtracted from 3, then 5 is added to it.
An advantage of reverse Polish notation is that it removes the need for parentheses that are required by infix notation.

#### Speaker notes

Base salary  + Commision

$400   + grossSale X  commission


50

### Slide 26



#### Speaker notes

Base salary  + Commision

$400   + grossSale X  commission

56

### Slide 27

Information hiding means encapsulation in java

#### Speaker notes


57

### Slide 28

9.4  Relationship Between Superclasses and Subclasses
Inheritance hierarchy containing types of employees in a company’s payroll application
Commission employees are paid a percentage of their sales
Base-salaried commission employees receive a base salary plus a percentage of their sales.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes

Base salary  + Commision

$300   + grossSale X  commission

58

### Slide 29

9.4.1 Creating and Using a CommissionEmployee Class
RECALL THAT: The Java class hierarchy begins with class Object (in package java.lang)
Every class in Java directly or indirectly extends (or “inherits from”) Object.
Class CommissionEmployee (Fig. 9.4) extends class Object (from package java.lang).
CommissionEmployee inherits Object’s methods.
If you don’t explicitly specify which class a new class extends, the class extends Object implicitly.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


61

### Slide 30

OBJECT CLASS
Object class is present in java.lang package.
Every class in Java is directly or indirectly derived from the Object class.
If a Class does not extend any other class then it is direct child class of Object and if extends other class then it is an indirectly derived.
Therefore, the Object class methods are available to all Java classes.
Hence Object class acts as a root of inheritance hierarchy in any Java Program.

#### Speaker notes


62

### Slide 31

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.
Example 8a

#### Speaker notes


64

### Slide 32

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


67

### Slide 33

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


72

### Slide 34

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


73

### Slide 35

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


74

### Slide 36

9.4.1 Creating and Using a CommissionEmployee Class (Cont.)
Constructors are not inherited.
The first task of a subclass constructor is to call its direct superclass’s constructor explicitly or implicitly
Ensures that the instance variables inherited from the superclass are initialized properly.
If the code does not include an explicit call to the superclass constructor, Java implicitly calls the superclass’s default or no-argument constructor.
A class’s default constructor calls the superclass’s default or no-argument constructor.

#### Speaker notes


75

### Slide 37

9.4.1 Creating and Using a CommissionEmployee Class (Cont.)
toString is one of the methods that every class inherits directly or indirectly from class Object.
Returns a String representing an object.
Called implicitly whenever an object must be converted to a String representation.
Class Object’s toString method returns a String that includes the name of the object’s class.
This is primarily a placeholder that can be overridden by a subclass to specify an appropriate String representation.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


79

### Slide 38

Class Object’s toString method
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


80

### Slide 39

Class Object’s toString method
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


81

### Slide 40

9.4.1 Creating and Using a CommissionEmployee Class (Cont.)
To override a superclass method, a subclass must declare a method with the same signature as the superclass method
@Override annotation
Indicates that a method should override a superclass method with the same signature.
If it does not, a compilation error occurs.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


83

### Slide 41

If you want to represent any object as a string, toString() method comes into existence.
The toString() method returns string representation of the object.
If you print any object, java compiler internally invokes the toString() method on the object.
So, overriding the toString() method, returns the desired output, it can be the state of an object etc. depends on your implementation.
By overriding the toString() method of the Object class, we can return values of the object, so we don't need to write much code.

Understanding problem without toString() method

#### Speaker notes


91

### Slide 42

Let's see the simple code that prints reference.
EXAMPLE 6

Understanding problem without toString() method
Output:
Student@1fee6fc
Student@1eed786
As you can see in the above example, printing s1 and s2 prints the hashcode values of the objects but I want to print the values of these objects.
Since java compiler internally calls toString() method, overriding this method will return the specified values.
Let's understand it with the EXAMPLE 7


#### Speaker notes


93

### Slide 43

So, there are many ways to print object
By explicitly override toString() method in class Object
By using System.out.printf() and  specify the format that object should be printed.
By using the fommatter class which function in similar way as System.out.printf()


Understanding problem without toString() method

### Slide 44

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 45

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 46

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 47

ACTIVITY
Remove extends Object  in class CommissionEmployee.
i.e. change the class from:
public class CommissionEmployee extends Object

TO:

public class CommissionEmployee

Compile the same classes above and verify that you got same results.

### Slide 48

IMPROVE YOUR CHAPTER 7 CLASS ACTIVITIES BASED ON YOUR NEW KNOWLEDGE OF toString Method
Improve the program above by adding three more variables in Account.java class (in addition to “Name” that you already have) e.g.:
SSN
 Address
Account balance
Ensure you declare them with necessary variable type and use Set and Get methods as appropriate.
Declare constructors to take care of the new variables.
In the AccountTest.java class create objects of the new Account.java that would include all the additional variables that you have just created.
Create account objects for at least 4 members of your family in AccountTest.java class.
                NEW TASKS
Step 1: Try to print out each object using System.out.println(account1), and the separate statements to print the rest of the objects i.e. account 2, account3, etc..
Step 2:  Copy the same codes and create another class
Now, try to override the toString Method as shown in example 6 in the MS Word document and then print out the object again using System.out.println(account1), and the separate statements to print the rest of the objects account 2, account2, etc..


Class Activities

### Slide 49

9.4.2 Creating and Using a BasePlus-CommissionEmployee Class
Class BasePlusCommissionEmployee (Fig. 9.6) contains a first name, last name, social security number, gross sales amount, commission rate and base salary.
All but the base salary are in common with class CommissionEmployee.
Class BasePlusCommissionEmployee’s public services include a constructor, and methods earnings, toString and get and set for each instance variable
Most of these are in common with class CommissionEmployee.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 50

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 51

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 52

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 53

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 54

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 55

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 56

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 57

9.4.2 Creating and Using a BasePlus-CommissionEmployee Class (Cont.)
Class BasePlusCommissionEmployee does not specify “extends Object”
Implicitly extends Object.
BasePlusCommissionEmployee’s constructor invokes class Object’s default constructor implicitly.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 58

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 59

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 60

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 61

9.4.2 Creating and Using a BasePlus-CommissionEmployee Class (Cont.)
Much of BasePlusCommissionEmployee’s code is similar, or identical, to that of CommissionEmployee.
private instance variables firstName and lastName and methods setFirstName, getFirstName, setLastName and getLastName are identical.
Both classes also contain corresponding get and set methods.
The constructors are almost identical
BasePlusCommissionEmployee’s constructor also sets the baseSalary.
The toString methods are almost identical
BasePlusCommissionEmployee’s toString also outputs instance variable baseSalary
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 62

9.4.2 Creating and Using a BasePlus-CommissionEmployee Class (Cont.)
We literally copied CommissionEmployee’s code, pasted it into BasePlusCommissionEmployee, then modified the new class to include a base salary and methods that manipulate the base salary.
This “copy-and-paste” approach is often error prone and time consuming.
It spreads copies of the same code throughout a system, creating a code-maintenance problems—changes to the code would need to be made in multiple classes.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 63

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 64

9.4.3 Creating a CommissionEmployee–BasePlusCommissionEmployee Inheritance Hierarchy
Class BasePlusCommissionEmployee class extends class CommissionEmployee
A BasePlusCommissionEmployee object is a CommissionEmployee
Inheritance passes on class CommissionEmployee’s capabilities.
Class BasePlusCommissionEmployee also has instance variable baseSalary.
Subclass BasePlusCommissionEmployee inherits CommissionEmployee’s instance variables and methods
Only CommissionEmployee’s public and protected members are directly accessible in the subclass.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 65

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 66

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 67

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 68

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 69

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 70

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 71

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 72

9.4.3 Creating a CommissionEmployee–BasePlusCommissionEmployee Inheritance Hierarchy (Cont.)
Each subclass constructor must implicitly or explicitly call one of its superclass’s constructors to initialize the instance variables inherited from the superclass.
Superclass constructor call syntax—keyword super, followed by a set of parentheses containing the superclass constructor arguments.
Must be the first statement in the constructor’s body.
If the subclass constructor did not invoke the superclass’s constructor explicitly, the compiler would attempt to insert a call to the superclass’s default or no-argument constructor.
Class CommissionEmployee does not have such a constructor, so the compiler would issue an error.
You can explicitly use super() to call the superclass’s no-argument or default constructor, but this is rarely done.

### Slide 73

9.4.3 Creating a CommissionEmployee–BasePlusCommissionEmployee Inheritance Hierarchy (Cont.)
Compilation errors occur when the subclass attempts to access the superclass’s private instance variables.
These lines could have used appropriate get methods to retrieve the values of the superclass’s instance variables.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 74

9.4.4 CommissionEmployee–BasePlusCommissionEmployee Inheritance Hierarchy Using protected Instance Variables
To enable a subclass to directly access superclass instance variables, we can declare those members as protected in the superclass.
New CommissionEmployee class modified only the instance variable declarations of Fig. 9.4 as follows:
    protected final String firstName;                              protected final String lastName;                               protected final String socialSecurityNumber;                   protected double grossSales;      protected double commissionRate;
With protected instance variables, the subclass gets access to the instance variables, but classes that are not subclasses and classes that are not in the same package cannot access these variables directly.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 75

9.4.4 CommissionEmployee–BasePlus-CommissionEmployee Inheritance Hierarchy Using protected Instance Variables (Cont.)
Class BasePlusCommissionEmployee (Fig. 9.9) extends the new version of class CommissionEmployee with protected instance variables.
These variables are now protected members of BasePlusCommissionEmployee.
If another class extends this version of class BasePlusCommissionEmployee, the new subclass also can access the protected members.
The source code in Fig. 9.9 is considerably shorter than that in Fig. 9.6
Most of the functionality is now inherited from CommissionEmployee
There is now only one copy of the functionality.
Code is easier to maintain, modify and debug—the code related to a CommissionEmployee exists only in that class.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 76

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 77

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 78

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 79

9.4.4 CommissionEmployee–BasePlus-CommissionEmployee Inheritance Hierarchy Using protected Instance Variables (Cont.)
Inheriting protected instance variables enables direct access to the variables by subclasses.
In most cases, it’s better to use private instance variables to encourage proper software engineering.
Code will be easier to maintain, modify and debug.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 80

9.4.4 CommissionEmployee–BasePlus-CommissionEmployee Inheritance Hierarchy Using protected Instance Variables (Cont.)
Using protected instance variables creates several potential problems.
The subclass object can set an inherited variable’s value directly without using a set method.
A subclass object can assign an invalid value to the variable
Subclass methods are more likely to be written so that they depend on the superclass’s data implementation.
Subclasses should depend only on the superclass services and not on the superclass data implementation.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 81

9.5  Constructors in Subclasses
Instantiating a subclass object begins a chain of constructor calls
The subclass constructor, before performing its own tasks, explicitly uses super to call one of the constructors in its direct superclass or implicitly calls the superclass’s default or no-argument constructor
If the superclass is derived from another class, the superclass constructor invokes the constructor of the next class up the hierarchy, and so on.
The last constructor called in the chain is always Object’s constructor.
Original subclass constructor’s body finishes executing last.
Each superclass’s constructor manipulates the superclass instance variables that the subclass object inherits.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 82

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 83

9.6   Class Object
All classes in Java inherit directly or indirectly from class Object, so its 11 methods are inherited by all other classes.
Figure 9.12 summarizes Object’s methods.
Every array has an overridden clone method that copies the array.
If the array stores references to objects, the objects are not copied—a shallow copy is performed.

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 84

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 85

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 86

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 87

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 88

ACTIVITY
Go to class Object in Java API
Familiarize yourself with the class and its methods.
Check their implementation documentation.

### Slide 89

There’s much discussion in the software engineering community about the relative merits of composition and inheritance
Each has its own place, but inheritance is often overused and composition is more appropriate in many cases
A mix of composition and inheritance often is a reasonable design approach.
9.7   Designing with Composition vs. Inheritance
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 90

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 91

EXTRAL SLIDES FOR HARD WORKING STUDENTS
EXTRAL SLIDES FOR HARD WORKING STUDENTS

### Slide 92

Inheritance-Based Designs
Inheritance creates tight coupling among the classes in a hierarchy
Each subclass typically depends on its direct or indirect superclasses’ implementations
Changes in superclass implementation can affect the behavior of subclasses, often in subtle ways
Tightly coupled designs are more difficult to modify than those in loosely coupled, composition-based designs
Change is the rule rather than the exception—this encourages composition
9.7   Designing with Composition vs. Inheritance (cont.)
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 93

In general, use inheritance only for true is-a relationships in which you can assign a subclass object to a superclass reference
When you invoke a method via a superclass reference to a subclass object, the subclass’s corresponding method executes
This is called polymorphic behavior, which we explore in Chapter 10
9.7   Designing with Composition vs. Inheritance (cont.)
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 94

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 95

Composition-Based Designs
Composition is loosely coupled
When you compose a reference as an instance variable of a class, it’s part of the class’s implementation details that are hidden from the class’s client code
If the reference’s class type changes, you may need to make changes to the composing class’s internal details, but those changes do not affect the client code

9.7   Designing with Composition vs. Inheritance (cont.)
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 96

Composition-Based Designs
In addition, inheritance is done at compile time
Composition is more flexible—it, too, can be done at compile time, but it also can be done at execution time because non-final references to composed objects can be modified
We call this dynamic composition
This is another aspect of loose coupling—if the reference is of a superclass type, you can replace the referenced object with an object of any type that has an is-a relationship with the reference’s class type

9.7   Designing with Composition vs. Inheritance (cont.)
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 97

Composition-Based Designs
When you use a composition approach instead of inheritance, you’ll typically create a larger number of smaller classes, each focused on one responsibility
Smaller classes generally are easier to test, debug and modify
Java does not offer multiple inheritance—each class in Java may extend only one class
However, a new class may reuse the capabilities of one or more other classes by composition. As you’ll see in Chapter 10, we can get many of multiple inheritance's benefits by implementing multiple interfaces

9.7   Designing with Composition vs. Inheritance (cont.)
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 98

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 99

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 100

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 101

Recommended Exercises
Exercise 9.3 asks you to reimplement this chapter’s CommissionEmployee–BasePlusCommissionEmployee hierarchy using composition, rather than inheritance.
Exercise 9.16 asks you to reimplement the hierarchy using a combination of composition and inheritance in which you’ll see the benefits of composition’s loose coupling.
9.7   Designing with Composition vs. Inheritance (cont.)
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.
