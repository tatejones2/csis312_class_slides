# Chapter 10: Polymorphism and Interfaces

[All chapters](README.md) · [Course guide](../reference/COURSE_GUIDE.md)

## Main concepts

- Superclass references and runtime selection of overridden methods.
- Abstract classes and methods; concrete subclasses.
- Interfaces and common operations across different classes.
- Polymorphic employee payroll and payable/invoice examples.

## Sources

- [JHTP11_10 - UPDATED -CSIS 212 -WK 12-2022 -2023 (2).pptx](../JHTP11_10%20-%20UPDATED%20-CSIS%20212%20-WK%2012-2022%20-2023%20%282%29.pptx)
- [Searchable text: JHTP11_10 - UPDATED -CSIS 212 -WK 12-2022 -2023 (2).md](../reference/extracted/JHTP11_10%20-%20UPDATED%20-CSIS%20212%20-WK%2012-2022%20-2023%20%282%29.md)

## Related instructor examples

These documents cover several chapters; use the examples relevant to this topic.

- [Week 2, 3 & 4 Java CODES-3.docx](../Week%202%2C%203%20%26%204%20Java%20CODES-3.docx) · [Searchable examples](../reference/extracted/Week%202%2C%203%20%26%204%20Java%20CODES-3.txt)

## Reading these notes

The material below preserves the available extracted text. Slide and PDF page numbers
refer to the supplied files, not necessarily the printed textbook page numbers.
Images, diagrams and image-based code require the original documents. OCR can
misread identifiers and punctuation; extracted examples are not verified runnable code.

## Slide text: JHTP11_10 - UPDATED -CSIS 212 -WK 12-2022 -2023 (2).md

### Slide 1

Chapter 10Object-Oriented Programming: Polymorphism and Interfaces
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


1

### Slide 2

Prayers
Importance of prayer in A Christian life
Texts:
Matthew 26:41
Watch and pray, that ye enter not into temptation: the spirit indeed is willing, but the flesh is weak.
Matthew 17:21
Howbeit this kind goeth not out but by prayer and fasting.
Luke 18:1
And he spake a parable unto them to this end, that men ought always to pray, and not to faint;

#### Speaker notes

Organizational Network Analysis


4

### Slide 3

Prayers
You have to PRAY so that you do not become a prey to the machinations of the devil
Texts:
2 CORINTHIANS 2:11
lest Satan should get an advantage over us. For we are not ignorant of his devices.
Matthew 26:41
Watch and pray, that ye enter not into temptation: the spirit indeed is willing, but the flesh is weak.
Matthew 26:41
But while men slept, his enemy came and sowed tares among the wheat, and went his way.


#### Speaker notes

Organizational Network Analysis


5

### Slide 4

 How to obtain knowledge and Wisdom from GOD: Pray and read your Bible
© 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part, except for use as permitted in a license distributed with a certain product or service or otherwise on a password-protected website for classroom use.

#### Speaker notes

Organizational Network Analysis


6

### Slide 5

 How to obtain knowledge and Wisdom from GOD: Pray and read your Bible
© 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part, except for use as permitted in a license distributed with a certain product or service or otherwise on a password-protected website for classroom use.
Mark 9:29, KJV: "And he said unto them, This kind can come forth by nothing, but by prayer and fasting."
James 1:5: If any of you lack wisdom, let him ask of God, that giveth to all men liberally, and upbraideth not; and it shall be given him.
Matthew 7:7-8: 7 Ask, and it shall be given you; seek, and ye shall find; knock, and it shall be opened unto you:
8 For every one that asketh receiveth; and he that seeketh findeth; and to him that knocketh it shall be opened.


Jonah 2:1 :  Then Jonah prayed unto the LORD his God out of the fish's belly,
 Psalm 119:99: I have more understanding than all my teachers: for thy testimonies are my meditation.

#### Speaker notes

Organizational Network Analysis


7

### Slide 6

 How Should We Pray?
© 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part, except for use as permitted in a license distributed with a certain product or service or otherwise on a password-protected website for classroom use.
King James Version (Matthew 6:9-13)(Luke 11:1-13)
9 After this manner therefore pray ye:
Our Father which art in heaven,
Hallowed be thy name.
Thy kingdom come,
Thy will be done in earth,
as it is in heaven.
Give us this day our daily bread.
And forgive us our debts,
as we forgive our debtors.
And lead us not into temptation,
but deliver us from evil:
For thine is the kingdom,
and the power, and the glory,
for ever. Amen.


#### Speaker notes

Organizational Network Analysis


8

### Slide 7

EXAMPLES OF JESUS PRAYERS:
41 So they took away the stone. Then Jesus looked up and said:

 “Father, I thank you that you have heard me. 42 I knew that you always hear me, but I said this for the benefit of the people standing here, that they may believe that you sent me.”

43 When he had said this, Jesus called in a loud voice, “Lazarus, come out!” 44


John 11:38-44

1 Corinthians 11:24and when He had given thanks, He broke it and said, "This is My body, which is for you; do this in remembrance of Me."
Luke 22:17After taking the cup, He gave thanks and said, "Take this and divide it among yourselves.

#### Speaker notes


12

### Slide 8

EXAMPLE: Importance of praising/thanking God
© 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part, except for use as permitted in a license distributed with a certain product or service or otherwise on a password-protected website for classroom use.
Acts 16:25-34

And at midnight Paul and Silas prayed, and sang praises unto God: and the prisoners heard them.
26 And suddenly there was a great earthquake, so that the foundations of the prison were shaken: and immediately all the doors were opened, and every one's bands were loosed.
27

FORGIVENESS OF SINS
Psalm 66:18-
If I regard iniquity in my heart, the Lord will not hear me.

Romans 3:23:
For all have sinned, and come short of the glory of God;

#### Speaker notes


20

### Slide 9

Answers prayer
God answers prayers but the answer could be in different forms:
Yes (i.e. you got what you asked)
Yes (but wait)
Exodus 9:5: And the LORD appointed a set time, saying, To morrow the LORD shall do this thing in the land.
No (if what you are asking for is not right for your soul).
James 4:3: Ye ask, and receive not, because ye ask amiss, that ye may consume it upon your lusts.
Romans 8:26: Likewise the Spirit also helpeth our infirmities: for we know not what we should pray for as we ought: but the Spirit itself maketh intercession for us with groanings which cannot be uttered.

#### Speaker notes

+

Sum = a + b;

String School = “Liberty” + “University”  concatenation
21

### Slide 10

Prayer Time
Now, pray for yourselves
Pray for your families
Pray for the university
Pray for the country
Pray for our world and global peace

#### Speaker notes


22

### Slide 11

Psalm 20: 1-5
1.May the Lord answer you when you are in distress;    may the name of the God of Jacob protect you.2 May he send you help from the sanctuary    and grant you support from Zion.3 May he remember all your sacrifices    and accept your burnt offerings.[b]4 May he give you the desire of your heart    and make all your plans succeed.5 May we shout for joy over your victory    and lift up our banners in the name of our God.
May the Lord grant all your requests (AMEN).

#### Speaker notes


23

### Slide 12

Chapter 10Object-Oriented Programming: Polymorphism and Interfaces
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


24

### Slide 13

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


25

### Slide 14

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


26

### Slide 15

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


27

### Slide 16

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


29

### Slide 17

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


31

### Slide 18

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


32

### Slide 19

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


33

### Slide 20

10.1  Introduction
Polymorphism
Enables you to “program in the general” rather than “program in the specific.”
Polymorphism enables you to write programs that process objects that share the same superclass as if they were all objects of the superclass; this can simplify programming.


© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


34

### Slide 21

10.1  Introduction Cont.
Polymorphism
Polymorphism means "many forms", and it occurs when we have many classes that are related to each other by inheritance.
While Inheritance lets us inherit attributes and methods from another class.
Polymorphism uses those methods to perform different tasks.

#### Speaker notes


35

### Slide 22

10.1  Introduction
Polymorphism
This allows us to perform a single action in different ways.
For example, think of a superclass called Animal that has a method called animalSound().
Subclasses of Animals could be Pigs, Cats, Dogs, Birds - And they also have their own implementation of an animal sound (the pig oinks, and the cat meows, etc.):
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


36

### Slide 23

Example of Introduction Polymorphism
class Animal {
  public void animalSound() {
    System.out.println("The animal makes a sound");
  }
}
class Pig extends Animal {
  public void animalSound() {
    System.out.println("The pig says: wee wee");
  }
}
class Dog extends Animal {
  public void animalSound() {
    System.out.println("The dog says: bow wow");
  }
}

#### Speaker notes


37

### Slide 24

10.3  Demonstrating Polymorphic Behavior
In the next example, we aim a superclass reference at a subclass object.
Invoking a method on a subclass object via a superclass reference invokes the subclass functionality
The type of the referenced object, not the type of the variable, determines which method is called
This example demonstrates that an object of a subclass can be treated as an object of its superclass, enabling various interesting manipulations.
A program can create an array of superclass variables that refer to objects of many subclass types.
Allowed because each subclass object is an object of its superclass.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


38

### Slide 25

  What is reference and object?
class Human{ ....
}
class Boy extends Human{

public static void main( String args[]) {

/*This statement simply creates an object of class *Boy and assigns a reference of Boy to it*/

Boy obj1 = new Boy();

/* Since Boy extends Human class. The object creation can be done in this way. Parent class reference can have child class reference assigned to it */
Human obj2 = new Human(); }
}
Association of method definition to the method call is known as binding. There are two types of binding: Static binding and dynamic binding.

#### Speaker notes


46

### Slide 26

Example of Introduction Polymorphism
Now we can create Pig and Dog objects and call the animalSound() method on both of them:

#### Speaker notes


47

### Slide 27

Example of Polymorphism
class Animal {    public void animalSound() {        System.out.println("The animal makes a sound");    } }class Pig extends Animal {    public void animalSound() {        System.out.println("The pig says: wee wee");    } }class Dog extends Animal {    public void animalSound() {        System.out.println("The dog says: bow wow");    } }class Main {    public static void main(String[] args) {        Animal myAnimal = new Animal();  // Create an Animal object        Animal myPig = new Pig();  // Create a Pig object        Animal myDog = new Dog();  // Create a Dog object        myAnimal.animalSound();        myPig.animalSound();        myDog.animalSound();    } }

#### Speaker notes


48

### Slide 28

Create extra two classes for two different additional animals and customize their own animalSound methods e.g.
Cow
Dock
Create their objects in two different ways as shown in the example above e.g.
      myCow = new Cow();  // Create a Cow object        Animal myCow = new Cow();  // Create ALSO a Cow object





CLASS ACTIVITIES

#### Speaker notes


49

### Slide 29

10.3  Demonstrating Polymorphic Behavior (Cont.)
A superclass object cannot be treated as a subclass object, because a superclass object is not an object of any of its subclasses.
The is-a relationship applies only up the hierarchy from a subclass to its direct (and indirect) superclasses, and not down the hierarchy.
The Java compiler does allow the assignment of a superclass reference to a subclass variable if you explicitly cast the superclass reference to the subclass type
A technique known as downcasting that enables a program to invoke subclass methods that are not in the superclass.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


50

### Slide 30

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


51

### Slide 31

Example II of Polymorphism
Example: Suppose we create a program that simulates the movement of several types of animals for a biological study.
Classes Fish, Frog and Bird represent the three types of animals under investigation.
Each class extends superclass Animal, which contains a method move and maintains an animal’s current location as x-y coordinates.
Each subclass implements method move.
A program maintains an Animal array containing references to objects of the various Animal subclasses.
To simulate the animals’ movements, the program sends each object the same message once per second—namely, move.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


52

### Slide 32

Polymorphism  Introduction (Cont.)
Each specific type of Animal responds to a move message in a unique way:
a Fish might swim three feet
a Frog might jump five feet
a Bird might fly ten feet.
The program issues the same message (i.e., move) to each animal object, but each object knows how to modify its x-y coordinates appropriately for its specific type of movement.
Relying on each object to know how to “do the right thing” in response to the same method call is the key concept of polymorphism.
The same message sent to a variety of objects has “many forms” of results—hence the term polymorphism.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


53

### Slide 33

Polymorphism  Introduction (Cont.)
With polymorphism, we can design and implement systems that are easily extensible
New classes can be added with little or no modification to the general portions of the program, as long as the new classes are part of the inheritance hierarchy that the program processes generically.
The new classes simply “plug right in.”
The only parts of a program that must be altered to accommodate new classes are those that require direct knowledge of the new classes that we add to the hierarchy.

#### Speaker notes


54

### Slide 34

Polymorphism  Introduction (Cont.)
Once a class implements an interface, all objects of that class have an is-a relationship with the interface type, and all objects of the class are guaranteed to provide the functionality described by the interface.
This is true of all subclasses of that class as well.
Interfaces are particularly useful for assigning common functionality to possibly unrelated classes.
Allows objects of unrelated classes to be processed polymorphically—objects of classes that implement the same interface can respond to all of the interface method calls.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


56

### Slide 35

Polymorphism  Introduction (Cont.)
The module continues with an introduction to Java interfaces, which are particularly useful for assigning common functionality to possibly unrelated classes.
This allows objects of these classes to be processed polymorphically—objects of classes that implement the same interface can respond to all of the interface method calls.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


57

### Slide 36

10.2  Polymorphism: More Examples
Example: Quadrilaterals
If Rectangle is derived from Quadrilateral, then a Rectangle object is a more specific version of a Quadrilateral.
Any operation that can be performed on a Quadrilateral can also be performed on a Rectangle.
These operations can also be performed on other Quadrilaterals, such as Squares, Parallelograms and Trapezoids.
Polymorphism occurs when a program invokes a method through a superclass Quadrilateral variable—at execution time, the correct subclass version of the method is called, based on the type of the reference stored in the superclass variable.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


58

### Slide 37

10.2  Polymorphism Examples (Cont.)
Example: Space Objects in a Video Game
A video game manipulates objects of classes Martian, Venusian, Plutonian, SpaceShip and LaserBeam. Each inherits from SpaceObject and overrides its draw method.
A screen manager maintains a collection of references to objects of the various classes and periodically sends each object the same message—namely, draw.
Each object responds in a unique way.
A Martian object might draw itself in red with green eyes and the appropriate number of antennae.
A SpaceShip object might draw itself as a bright silver flying saucer.
A LaserBeam object might draw itself as a bright red beam across the screen.
The same message (in this case, draw) sent to a variety of objects has “many forms” of results.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


59

### Slide 38

10.2  Polymorphism Examples (Cont.)
A screen manager might use polymorphism to facilitate adding new classes to a system with minimal modifications to the system’s code.
To add new objects to our video game:
Build a class that extends SpaceObject and provides its own draw method implementation.
When objects of that class appear in the SpaceObject collection, the screen-manager code invokes method draw, exactly as it does for every other object in the collection, regardless of its type.
So the new objects simply “plug right in” without any modification of the screen manager code by the programmer.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


60

### Slide 39

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


61

### Slide 40

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


62

### Slide 41

CODE SAMPLES in MS Word -EXAMPLES FOR POLYMORPHISM TEST (Using the codes we had in Chapter 9)

#### Speaker notes


63

### Slide 42



#### Speaker notes


67

### Slide 43



#### Speaker notes


68

### Slide 44

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


69

### Slide 45

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


70

### Slide 46

10.3  Demonstrating Polymorphic Behavior (Cont.)
When a superclass variable contains a reference to a subclass object, and that reference is used to call a method, the subclass version of the method is called.
The Java compiler allows this “crossover” because an object of a subclass is an object of its superclass (but not vice versa).
When the compiler encounters a method call made through a variable, the compiler determines if the method can be called by checking the variable’s class type.
If that class contains the proper method declaration (or inherits one), the call is compiled.
At execution time, the type of the object to which the variable refers determines the actual method to use.
This process is called dynamic binding.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


71

### Slide 47

10.3   Static and dynamic binding in java
Association of method call to the method body is known as binding.
There are two types of binding:
Static Binding that happens at compile time and
Dynamic Binding that happens at runtime.
Before I explain static and dynamic binding in java, lets see few terms that will help you understand this concept better.

What is reference and object?


#### Speaker notes


73

### Slide 48

  RECALLED: What is reference and object?
class Human{ ....
}
class Boy extends Human{

public static void main( String args[]) {

/*This statement simply creates an object of class *Boy and assigns a reference of Boy to it*/

Boy obj1 = new Boy();

/* Since Boy extends Human class. The object creation can be done in this way. Parent class reference can have child class reference assigned to it */
Human obj2 = new Boy(); }
}
Association of method definition to the method call is known as binding. There are two types of binding: Static binding and dynamic binding.

#### Speaker notes


74

### Slide 49

 Static Binding or Early Binding
The binding which can be resolved at compile time by compiler is known as static or early binding.
The binding of static, private and final methods is  compile-time.
Why? The reason is that these method cannot be overridden and the type of the class is determined at the compile time.
Let us see an example to understand this:


#### Speaker notes


76

### Slide 50

Static binding example
In the example below, we have two classes Human and Boy.
Both the classes have same method walk() but the method is static, which means it cannot be overridden
Even though I have used the object of Boy class while creating object obj, the parent class method is called by it.
Because the reference is of Human type (parent class).
So, whenever a binding of static, private and final methods happens, type of the class is determined by the compiler at compile time and the binding happens then and there.

class Human{

public static void walk() {
System.out.println("Human walks");
} }

class Boy extends Human{
public static void walk(){
System.out.println("Boy walks");

} public static void main( String args[]) {
/* Reference is of Human type and object is * Boy type */
Boy obj = new Boy();
/* Reference is of HUman type and object is * of Human type*/

Human obj2 = new Boy();
obj.walk();
obj2.walk();
} }

#### Speaker notes


77

### Slide 51

Static binding example
class Human{

public static void walk() {
System.out.println("Human walks");
} }

class Boy extends Human{
public static void walk(){
System.out.println("Boy walks");

} public static void main( String args[]) {
/* Reference is of Human type and object is * Boy type */
Human obj = new Boy();
/* Reference is of HUman type and object is * of Human type*/

Human obj2 = new Boy();
obj.walk();
obj2.walk();
} }
Output:
Human walks Human walks
Exercise
Remove “static” from the two methods

#### Speaker notes


78

### Slide 52

Dynamic or Late binding example
When compiler is not able to resolve the call/binding at compile time, such binding is known as Dynamic or late Binding.
Method Overriding is a perfect example of dynamic binding
As in overriding both parent and child classes have same method
And in this case the type of the object determines which method is to be executed.
The type of object is determined at the run time so this is known as dynamic binding.

#### Speaker notes


86

### Slide 53

Dynamic binding example
This is the same example that we have seen above.
The only difference here is that in this example, overriding is actually happening.
Since these methods are not static, private and final.
In case of overriding the call to the overridden method is determined at runtime by the type of object thus late binding happens.
Let us see an example to understand this:

#### Speaker notes


92

### Slide 54

Dynamic binding example
class Human{
//Overridden Method
public void walk() {

System.out.println("Human walks");
}   }

class Demo extends Human{
//Overriding Method
public void walk(){

 System.out.println("Boy walks");
}
public static void main( String args[]) {
/* Reference is of Human type and object is * Boy type */

Human obj = new Demo();
/* Reference is of Human type and object is * of Human type. */

Human obj2 = new Human();
obj.walk();
obj2.walk();
} }
Output:

Boy walks
Human walks
Exercise
Just remove “static” from the two methods in the previous example

#### Speaker notes


98

### Slide 55

Write a java program that uses polymorphism to calculate areas of quadrilaterals to include rectangle, square, parallelogram and trapezoid.
Declare a superclass called Quadrilaterals
This should have a method called area
Method area in class Quadrilaterals should just print out “Areas of quadrilaterals”
Declare four subclasses of quadrilaterals with each of the classes (i.e. rectangle, square, parallelogram and trapezoid) containing method area that polymorphically calculates the area of each quadrilaterals in their respective ways.






CLASS ACTIVITIES

#### Speaker notes


102

### Slide 56

10.4  Abstract Classes and Methods
Abstract classes
Sometimes it’s useful to declare classes for which you never intend to create objects.
Used only as superclasses in inheritance hierarchies, so they are sometimes called abstract superclasses.
Cannot be used to instantiate objects—abstract classes are incomplete.
Subclasses must declare the “missing pieces” to become “concrete” classes, from which you can instantiate objects; otherwise, these subclasses, too, will be abstract.
An abstract class provides a superclass from which other classes can inherit and thus share a common design.

#### Speaker notes


112

### Slide 57

10.4  Abstract Classes and Methods (Cont.)
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.
Data abstraction is the process of hiding certain details and showing only essential information to the user.
Abstraction can be achieved with either abstract classes or  interfaces  (you will learn more about later).
The abstract keyword is a non-access modifier, used for classes and methods:
Abstract class: is a restricted class that cannot be used to create objects (to access it, it must be inherited from another class).
Abstract method: can only be used in an abstract class, and it does not have a body. The body is provided by the subclass (inherited from).
An abstract class can have both abstract and regular methods:

#### Speaker notes


115

### Slide 58

10.4  Abstract Classes and Methods (Cont.)
abstract class Animal {
    public abstract void animalSound();
    public void sleep() {
        System.out.println("Zzz");
} }
From the example above, it is not possible to create an object of the Animal class:
Animal myObj = new Animal(); // will generate an error
To access the abstract class, it must be inherited from another class as in the next slides.

#### Speaker notes


117

### Slide 59

10.4  Abstract Classes  Example
// Abstract class
method (does not have a body)
    abstract class Animal {
// Abstract public abstract void animalSound();
        // Regular method
    public void sleep() {
        System.out.println("Zzz"); } }

// Subclass (inherit from Animal)
class Pig extends Animal {
    public void animalSound() {
// The body of animalSound() is provided here
        System.out.println("The pig says: wee wee"); } }
class Main {
    public static void main(String[] args) {
        Pig myPig = new Pig(); // Create a Pig object
        myPig.animalSound();
        myPig.sleep(); } }

#### Speaker notes


118

### Slide 60

10.4   Why And When To Use Abstract Classes and Methods?
To achieve security - hide certain details and only show the important details of an object.
Note: Abstraction can also be achieved with Interfaces, which you will learn more about in this module.

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


119

### Slide 61

10.4  Abstract Classes and Methods (Cont.)
Classes that can be used to instantiate objects are called concrete classes.
Such classes provide implementations of every method they declare (some of the implementations can be inherited).
Abstract superclasses are too general to create real objects—they specify only what is common among subclasses.
Concrete classes provide the specifics that make it reasonable to instantiate objects.
Not all hierarchies contain abstract classes.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


120

### Slide 62

10.4  Abstract Classes and Methods (Cont.)
Programmers often write client code that uses only abstract superclass types to reduce client code’s dependencies on a range of subclass types.
You can write a method with a parameter of an abstract superclass type.
When called, such a method can receive an object of any concrete class that directly or indirectly extends the superclass specified as the parameter’s type.
Abstract classes sometimes constitute several levels of a hierarchy.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


124

### Slide 63

10.4  Abstract Classes and Methods (Cont.)
You make a class abstract by declaring it with keyword abstract.
An abstract class normally contains one or more abstract methods.
An abstract method is an instance method with keyword abstract in its declaration, as in
    public abstract void draw(); // abstract method
Abstract methods do not provide implementations.
A class that contains abstract methods must be an abstract class even if that class contains some concrete (nonabstract) methods.
Each concrete subclass of an abstract superclass also must provide concrete implementations of each of the superclass’s abstract methods.
Constructors and static methods cannot be declared abstract.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


125

### Slide 64

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


126

### Slide 65

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


127

### Slide 66

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


128

### Slide 67

10.4  Abstract Classes and Methods (Cont.)
Abstract classes require subclasses to provide implementations for the abstract methods.
Let's look at an example of an abstract class, and an abstract method.
Suppose we were modeling the behavior of animals, by creating a class hierarchy that started with a base class called Animal.
Animals are capable of doing different things like flying, digging and walking, but there are some common operations as well e.g. eating, sleeping and making noise
Some common operations are performed by all animals, but in a different way.
When an operation is performed in a different way, it is a good candidate for an abstract method (forcing subclasses to provide a custom implementation).


#### Speaker notes


130

### Slide 68

10.4  Abstract Classes and Methods (Cont.)
The abstract methods merely define a contract that derived classes must implement.
It's is the way how you ensure that they actually always will.
So let's take for example an abstract class Shape.
It would have an abstract method draw() that should draw it.
(Shape is abstract, because we do not know how to draw a general shape).
By having abstract method draw in Shape we guarantee that all derived classed, that actually can be drawn, for example Circle do implement draw.
Later if we forget to implement draw in some class, that is derived from Shape, compiler will actually help as giving an error.


#### Speaker notes


131

### Slide 69

10.4  Abstract Classes and Methods (Cont.)
Cannot instantiate objects of abstract superclasses, but you can use abstract superclasses to declare variables
These can hold references to objects of any concrete class derived from those abstract superclasses.
We’ll use such variables to manipulate subclass objects polymorphically.
Can use abstract superclass names to invoke static methods declared in those abstract superclasses.

#### Speaker notes


132

### Slide 70

10.4  Abstract Classes and Methods (Cont.)
Polymorphism is particularly effective for implementing so-called layered software systems.
Example: Operating systems and device drivers.
Commands to read or write data from and to devices may have a certain uniformity.
Device drivers control all communication between the operating system and the devices.
A write message sent to a device-driver object is interpreted in the context of that driver and how it manipulates devices of a specific type.
The write call itself really is no different from the write to any other device in the system—place some number of bytes from memory onto that device.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


134

### Slide 71

10.4  Abstract Classes and Methods (Cont.)
An object-oriented operating system might use an abstract superclass to provide an “interface” appropriate for all device drivers.
Subclasses are formed that all behave similarly.
The device-driver methods are declared as abstract methods in the abstract superclass.
The implementations of these abstract methods are provided in the subclasses that correspond to the specific types of device drivers.
New devices are always being developed.
When you buy a new device, it comes with a device driver provided by the device vendor and is immediately operational after you connect it and install the driver.
This is another elegant example of how polymorphism makes systems extensible.

#### Speaker notes


135

### Slide 72

Write java program that uses polymorphism to calculate areas of different Shapes to include rectangle, square, parallelogram, trapezoid and circle.
The program should also calculate circumference of circles
Declare an abstract superclass called Shapes
This should have an abstract method called area
This should also have a concrete method called circumference
    The circumference method in the abstract class should just print “This is a circumference”
Declare five subclasses of Shapes with each of the classes (i.e. rectangle, square, parallelogram, trapezoid and circle) containing method area that polymorphically calculates the area of each of the shapes in their respective ways.
Subclass Circle should also implement the concrete method circumference to calculate the circumference of a circle..






CLASS ACTIVITIES

#### Speaker notes


136

### Slide 73

10.5 ACTIVITIES  Case Study: Payroll System Using Polymorphism
Use an abstract method and polymorphism to perform payroll calculations based on the type of inheritance hierarchy headed by an employee.
Enhanced employee inheritance hierarchy requirements:
A company pays its employees on a weekly basis. The employees are of four types: Salaried employees are paid a fixed weekly salary regardless of the number of hours worked, hourly employees are paid by the hour and receive overtime pay (i.e., 1.5 times their hourly salary rate) for all hours worked in excess of 40 hours, commission employees are paid a percentage of their sales and base-salaried commission employees receive a base salary plus a percentage of their sales. For the current pay period, the company has decided to reward base-salaried commission employees by adding 10% to their base salaries. The company wants you to write a Java application that performs its payroll calculations polymorphically.

#### Speaker notes


137

### Slide 74

10.5  Case Study: Payroll System Using Polymorphism (Cont.)
abstract class Employee represents the general concept of an employee.
Subclasses: SalariedEmployee, CommissionEmployee , HourlyEmployee and BasePlusCommissionEmployee  (an indirect subclass)
Fig. 10.2 shows the inheritance hierarchy for our polymorphic employee-payroll application.
Abstract class names are italicized in the UML.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


138

### Slide 75

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


139

### Slide 76

10.5  Case Study: Payroll System Using Polymorphism (Cont.)
Abstract superclass Employee declares the “interface” to the hierarchy—that is, the set of methods that a program can invoke on all Employee objects.
We use the term “interface” here in a general sense to refer to the various ways programs can communicate with objects of any Employee subclass.
Each employee has a first name, a last name and a social security number defined in abstract superclass Employee.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


141

### Slide 77

10.5.1 Abstract Superclass Employee
Class Employee (Fig. 10.4) provides methods earnings and toString, in addition to the get and set methods that manipulate Employee’s instance variables.
An earnings method applies to all employees, but each earnings calculation depends on the employee’s class.
An abstract method—there is not enough information to determine what amount earnings should return.
Each subclass overrides earnings with an appropriate implementation.
Iterate through the array of Employees and call method earnings for each Employee subclass object.
Method calls processed polymorphically.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


142

### Slide 78

10.5.1 Abstract Superclass Employee (Cont.)
The diagram in Fig. 10.3 shows each of the five classes in the hierarchy down the left side and methods earnings and toString across the top.
For each class, the diagram shows the desired results of each method.
Declaring the earnings method abstract indicates that each concrete subclass MUST PROVIDE an appropriate earnings implementation and that a program will be able to use superclass Employee variables to invoke method earnings polymorphically for any type of Employee.

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


144

### Slide 79

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.
The diagram shows how methods earnings and toString will be implemented in each class.

In Abstract class “Employee” earnings is implemented as abstract.

In Class Salaried-Employee, earning is a concrete class and implements as shown, etc.

#### Speaker notes


145

### Slide 80

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


147

### Slide 81

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


150

### Slide 82

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.
10.5.2 Concrete Subclass SalariedEmployee

#### Speaker notes


152

### Slide 83

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


158

### Slide 84

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


165

### Slide 85

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


166

### Slide 86

10.5.3 Concrete Subclass HourlyEmployee

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


171

### Slide 87

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


175

### Slide 88

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


177

### Slide 89

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


178

### Slide 90

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


179

### Slide 91

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


180

### Slide 92

10.5.4 Concrete Subclass CommissionEmployee

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


181

### Slide 93

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


182

### Slide 94

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


184

### Slide 95

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


186

### Slide 96

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


187

### Slide 97

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


188

### Slide 98

10.5.5 Indirect Concrete Subclass BasePlusCommissionEmployee

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


189

### Slide 99

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


190

### Slide 100

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


191

### Slide 101

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


192

### Slide 102

10.5.6 Polymorphic Processing, Operator instanceof and Downcasting
Fig. 10.9 creates an object of each of the four concrete classes.
Manipulates these objects nonpolymorphically, via variables of each object’s own type, then polymorphically, using an array of Employee variables.
While processing the objects polymorphically, the program increases the base salary of each BasePlusCommissionEmployee by 10%
Requires determining the object’s type at execution time.
Finally, the program polymorphically determines and outputs the type of each object in the Employee array.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


195

### Slide 103

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


196

### Slide 104

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


197

### Slide 105

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


198

### Slide 106

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


199

### Slide 107

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


200

### Slide 108

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


201

### Slide 109

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


203

### Slide 110

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 111

Create at least, one additional subclass of Employee Class
E.g. PartTimeEmployee or ContractEmployee
The new class should be plugged into the Inheritance hierarchy as appropriate.
Implement method earnings to Compute the wages of the new staff using your own devised formular.





CLASS ACTIVITIES

### Slide 112

10.5.6 Polymorphic Processing, Operator instanceof and Downcasting (Cont.)
All calls to method toString and earnings are resolved at execution time, based on the type of the object to which currentEmployee refers.
Known as dynamic binding or late binding.
Java decides which class’s toString method to call at execution time rather than at compile time
A superclass reference can be used to invoke only methods of the superclass—the subclass method implementations are invoked polymorphically.
Attempting to invoke a subclass-only method directly on a superclass reference is a compilation error.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 113

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 114

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 115

10.5.6 Polymorphic Processing, Operator instanceof and Downcasting (Cont.)
Every object knows its own class and can access this information through the getClass method, which all classes inherit from class Object.
The getClass method returns an object of type Class (from package java.lang), which contains information about the object’s type, including its class name.
The result of the getClass call is used to invoke getName to get the object’s class name.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 116

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 117

10.6  Summary of the Allowed Assignments Between Superclass and Subclass Variables
There are three proper ways to assign superclass and subclass references to variables of superclass and subclass types.
Assigning a superclass reference to a superclass variable is straightforward.
Assigning a subclass reference to a subclass variable is straightfor-ward.
Assigning a subclass reference to a superclass variable is safe, because the subclass object is an object of its superclass.
The superclass variable can be used to refer only to superclass members.
If this code refers to subclass-only mem-bers through the superclass variable, the compiler reports errors.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.
class Human{
public static void walk() {
System.out.println("Human walks");
} }
class Boy extends Human{
public static void walk(){
System.out.println("Boy walks");

} public static void main( String args[]) {
/* Reference is of Human type and object is * Boy type */

Human obj = new Boy();
/* Reference is of HUman type and object is * of Human type. */
Human obj2 = new Human();
obj.walk();
obj2.walk();
} }
Output:
Human walks
Human walks
Static binding example

### Slide 118

Static binding example
class Human{

public static void walk() {
System.out.println("Human walks");
} }
class Boy extends Human{
public static void walk(){
System.out.println("Boy walks");

} public static void main( String args[]) {
/* Reference is of Human type and object is * Boy type */

Human obj = new Boy();
/* Reference is of HUman type and object is * of Human type. */
Human obj2 = new Human();
obj.walk();
obj2.walk();
} }
Output:
Human walks Human walks

### Slide 119

10.7  final Methods and Classes
A final method in a superclass cannot be overridden in a subclass.
Methods that are declared private are implicitly final, because it’s not possible to override them in a subclass.
Methods that are declared static are implicitly final.
A final method’s declaration can never change, so all subclasses use the same method implementation, and calls to final methods are resolved at compile time—this is known as static binding.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 120

10.7  final Methods and Classes (Cont.)
A final class cannot be extended to create a subclass.
All methods in a final class are implicitly final.
Class String is an example of a final class.
If you were allowed to create a subclass of String, objects of that subclass could be used wherever Strings are expected.
Since class String cannot be extended, programs that use Strings can rely on the functionality of String objects as specified in the Java API.
Making the class final also prevents programmers from creating subclasses that might bypass security restrictions.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 121

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 122

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 123

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 124

10.8  A Deeper Explanation of Issues with Calling Methods from Constructors
Do not call overridable methods from constructors.
When creating a subclass object, this could lead to an overridden method being called before the subclass object is fully initialized.
Recall that when you construct a subclass object, its constructor first calls one of the direct superclass’s constructors.
If the superclass constructor calls an overridable method, the subclass’s version of that method will be called by the superclass constructor—before the subclass constructor’s body has a chance to execute.
This could lead to subtle, difficult-to-detect errors if the subclass method that was called depends on initialization that has not yet been performed in the subclass constructor’s body.
It’s acceptable to call a static method from a constructor.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 125

10.8  A Deeper Explanation of Issues with Calling Methods from Constructors
Let’s assume that a constructor and a set method perform the same validation for a particular instance variable. How should you handle the common code?
If it's brief, you can duplicate it in the constructor and the set method
For lengthier validation, define a static validation method—typically a private static helper method—then call it from the constructor and from the set method. It’s acceptable to call a static method from a constructor, because static methods are not overridable.
It’s also acceptable for a constructor to call a final instance method, provided that the method does not directly or indirectly call any overridable instance methods.

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 126

Java Interface -
Another way to achieve abstraction in Java, is with interfaces.
An interface is a completely "abstract class" that is used to group related methods with empty bodies:

//Example
// interface
interface Animal {

 public void animalSound();
// interface method (does not have a body)
public void run();

// interface method (does not have a body) }

### Slide 127

Java Interface -
To access the interface methods, the interface must be "implemented" (kinda like inherited) by another class with the implements keyword (instead of extends).

The body of the interface method is provided by the "implement" class:

### Slide 128

Java Interface -
// Interface
interface Animal {
public void animalSound(); // interface method (does not have a body)
public void sleep(); // interface method (does not have a body)
}
// Pig "implements" the Animal interface

class Pig implements Animal {
    public void animalSound() {
        // The body of animalSound() is provided here
        System.out.println("The pig says: wee wee"); }
    public void sleep() {
        // The body of sleep() is provided here
        System.out.println("Zzz"); } }

class Main {
    public static void main(String[] args) {
        Pig myPig = new Pig(); // Create a Pig object
        myPig.animalSound();
        myPig.sleep();
} }

### Slide 129

Create additional method in the interface as animalWalk()
Create extra two classes for two different additional animals and customize their own animalSound() and Sleep() methods e.g.
Cow
Duck
Create their objects in two different ways as shown in the example above e.g.
    myCow = new Cow();  // Create a Cow object  Animal myCow = new Cow();  // Create ALSO a Cow object






CLASS ACTIVITIES

### Slide 130

Notes on Interfaces: -
Like abstract classes, interfaces cannot be used to create objects
In the example above, it is not possible to create an "Animal" object in the Main Class
Interface methods do not have a body - the body is provided by the "implement" class
On implementation of an interface, you must override all of its methods
Interface methods are by default abstract and public
Interface attributes are by default public, static and final
An interface cannot contain a constructor (as it cannot be used to create objects)


### Slide 131

Why And When To Use Interfaces?: -
To achieve security - hide certain details and only show the important details of an object (interface).
Java does not support "multiple inheritance" (a class can only inherit from one superclass).
However, it can be achieved with interfaces, because the class can implement multiple interfaces.
Note: To implement multiple interfaces, separate them with a comma (see example in the next slides).

### Slide 132

Multiple Interfaces?: -
To implement multiple interfaces, separate them with a comma:
interface FirstInterface {
public void myMethod(); // interface method
}
interface SecondInterface {
public void myOtherMethod(); // interface method
} // DemoClass "implements" FirstInterface and SecondInterface

class DemoClass implements FirstInterface, SecondInterface {
public void myMethod() {
System.out.println("Some text..");
}
public void myOtherMethod() {
System.out.println("Some other text...");
} }
class MyMainClass {
public static void main(String[] args) {
DemoClass myObj = new DemoClass();
myObj.myMethod();
 myObj.myOtherMethod();
} }

### Slide 133

Create one additional interface in the program with its own method and at least one additional concrete class.
Let the DemoClass and the new class you created implement ALL the interfaces (including the new one)
Create their objects as shown in the example above e.g.

    myCow = new Cow();  // Create a Cow object  Animal myCow = new Cow();  // Create ALSO a Cow object






CLASS ACTIVITIES

### Slide 134

10.9  Creating and Using Interfaces
Our next example reexamines the payroll system of Section 10.5.
Suppose that the company involved wishes to perform several accounting operations in a single accounts payable application
Calculating the earnings that must be paid to each employee
Calculate the payment due on each of several invoices (i.e., bills for goods purchased)
Both operations have to do with obtaining some kind of payment amount.
For an employee, the payment refers to the employee’s earnings.
For an invoice, the payment refers to the total cost of the goods listed on the invoice.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 135

10.9  Creating and Using Interfaces (Cont.)
Example: The controls on a radio serve as an interface between radio users and a radio’s internal components.
Can perform only a limited set of operations (e.g., change the station, adjust the volume, choose between AM and FM)
Different radios may implement the controls in different ways (e.g., using push buttons, dials, voice commands).
The interface specifies what operations a radio must permit users to perform but does not specify how the operations are performed.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 136

10.9  Creating and Using Interfaces (Cont.)
Interfaces offer a capability requiring that unrelated classes implement a set of common methods.
Interfaces define and standardize the ways in which things such as people and systems can interact with one another.


### Slide 137

10.9  Creating and Using Interfaces (Cont.)
Example: Similarly, in our car analogy, a “basic-driving-capabilities” interface consisting of a steering wheel, an accelerator pedal and a brake pedal would enable a driver to tell the car what to do
Once you know how to use this interface for turning, accelerating and braking, you can drive many types of cars, even though manufacturers may implement these systems differently
e.g., there are many types of braking systems—disc brakes, drum brakes, antilock brakes, hydraulic brakes, air brakes and more.
When you press the brake pedal, your car’s actual brake system is irrelevant—all that matters is that the car slows down when you press the brake.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 138

10.9  Creating and Using Interfaces (Cont.)
A Java interface describes a set of methods that can be called on an object.
An interface declaration begins with the keyword interface and contains only constants and abstract methods.
All interface members must be public.
Interfaces may not specify any implementation details, such as concrete method declarations and instance variables.
All methods declared in an interface are implicitly public abstract methods.
All fields are implicitly public, static and final.

### Slide 139

10.9  Creating and Using Interfaces (Cont.)
To use an interface, a concrete class must specify that it implements the interface and must declare each method in the interface with specified signature.
Add the implements keyword and the name of the interface to the end of your class declaration’s first line.
A class that does not implement all the methods of the interface is an abstract class and must be declared abstract.
Implementing an interface is like signing a contract with the compiler that states, “I will declare all the methods specified by the interface or I will declare my class abstract.”
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 140

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 141

10.9  Creating and Using Interfaces (Cont.)
An interface is often used when disparate classes (i.e., unrelated classes) need to share common methods and constants.
Allows objects of unrelated classes to be processed polymorphically by responding to the same method calls.
You can create an interface that describes the desired functionality, then implement this interface in any classes that require that functionality.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 142

10.9  Creating and Using Interfaces (Cont.)
An interface should be used in place of an abstract class when there is no default implementation to inherit—that is, no fields and no concrete method implementations.
Like public abstract classes, interfaces are typically public types.
A public interface must be declared in a file with the same name as the interface and the .java filename extension.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 143

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 144

10.9  Creating and Using Interfaces
Our next example reexamines the payroll system of Section 10.5.
Suppose that the company involved wishes to perform several accounting operations in a single accounts payable application
Calculating the earnings that must be paid to each employee
Calculate the payment due on each of several invoices (i.e., bills for goods purchased)
Both operations have to do with obtaining some kind of payment amount.
For an employee, the payment refers to the employee’s earnings.
For an invoice, the payment refers to the total cost of the goods listed on the invoice.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 145

10.9.1 Developing a Payable Hierarchy
The example builds an application that can determine payments for employees and invoices alike.
Classes Invoice and Employee both represent things for which the company must be able to calculate a payment amount.
Both classes implement the Payable interface, so a program can invoke method getPaymentAmount on Invoice objects and Employee objects alike.
Enables the polymorphic processing of Invoices and Employees.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 146

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 147

10.9.1 Developing a Payable Hierarchy (Cont.)
Fig. 10.10 shows the accounts payable hierarchy.
The UML distinguishes an interface from other classes by placing «interface» above the interface name.
The UML expresses the relationship between a class and an interface through a realization.
A class is said to “realize,” or implement, the methods of an interface.
A class diagram models a realization as a dashed arrow with a hollow arrowhead pointing from the implementing class to the interface.
A subclass inherits its superclass’s realization relationships.

### Slide 148

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 149

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 150

10.9.2 Interface Payable
Fig. 10.11 shows the declaration of interface Payable.
Interface methods are always public and abstract, so they do not need to be declared as such.
Interfaces can have any number of methods.
Interfaces may also contain final and static constants
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 151

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 152

10.9.3 Class Invoice
Class Invoice (Fig. 19.12) represents a simple invoice that contains billing information for only one kind of part
Java does not allow subclasses to inherit from more than one superclass, but it allows a class to inherit from one superclass and implement as many interfaces as it needs.
To implement more than one, use a comma-separated list of interface names after keyword implements in the class declaration, as in:
    public class ClassName extends SuperclassName    implements FirstInterface, SecondInterface, …
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 153

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 154

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 155

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 156

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 157

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 158

10.9.4 Modifying Class Employee to Implement Interface Payable
We now modify class Employee to implement interface Payable. This class declaration is identical to previous one  with two exceptions:
Line 4 of  indicates that class Employee now implements Payable.
Line 38 implements interface Payable’s getPaymentAmount method.
getPaymentAmount simply calls Employee’s abstract method earnings
At execution time, when getPaymentAmount is called on an object of an Employee subclass, getPaymentAmount calls that subclass’s concrete earnings method, which knows how to calculate earnings for objects of that subclass type.

### Slide 159

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 160

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 161

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 162

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 163

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 164

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 165

10.9.5 Using Interface Payable to Process Invoices and Employees Polymorphically
PayableInterfaceTest (Fig. 10.14) illustrates that interface Payable can be used to process a set of Invoices and Employees polymorphically in a single application.
Lines 18–23 polymorphically process each Payable object in payableObjects, displaying each object’s String representation and payment amount
Line 21 invokes method toString via a Payable interface reference, even though toString is not declared in interface Payable—all references (including those of interface types) refer to objects that extend Object and therefore have a toString method


© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 166

10.9.5 Using Interface Payable to Process Invoices and Employees Polymorphically
Line 22 invokes Payable method getPaymentAmount to obtain the payment amount for each object in payableObjects, regardless of the actual type of the object. The output reveals that each of the method calls in lines 21–22 invokes the appropriate class’s toString and getPayment-Amount methods.

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 167

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 168

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 169

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 170

In the program above, four classes have been created for you namely:
Fig. 10.11: Payable.java
Fig. 10.12: Invoice.java
Fig. 10.13: Employee.java
Fig. 10.14: PayableInterfaceTest.java
You should create the create the fifth class i.e.   SalariedEmployee.java according to the UML and the flow of the four classes above.






CLASS ACTIVITIES

### Slide 171

10.9.7 Some Common Interfaces of the Java API
You’ll use interfaces extensively when developing Java applications. The Java API contains numerous interfaces, and many of the Java API methods take interface arguments and return interface values.
Figure 10.16 overviews a few of the more popular interfaces of the Java API.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 172

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 173

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 174

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 175

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 176


EXTRA SLIDES FOR YOUR PRIVATE PRACTICE


### Slide 177

10.10  Java SE 8 Interface Enhancements
This section introduces interface features that were added in
 Java SE
We discuss these in more detail in later in the course.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 178

10.10.1 default Interface Methods
Prior to Java SE 8, interface methods could be only public abstract methods.
An interface specified what operations an implementing class must perform but not how the class should perform them.
In Java SE 8, interfaces also may contain public default methods with concrete default implementations that specify how operations are performed when an implementing class does not override the methods.
If a class implements such an interface, the class also receives the interface’s default implementations (if any).
To declare a default method, place the keyword default before the method’s return type and provide a concrete method implementation.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 179

10.10.1 default Interface Methods (Cont.)
Adding Methods to Existing Interfaces
Any class that implements the original interface will not break when a default method is added.
The class simply receives the new default method.
When a class implements a Java SE 8 interface, the class “signs a contract” with the compiler that says,
“I will declare all the abstract methods specified by the interface or I will declare my class abstract”
The implementing class is not required to override the interface’s default methods, but it can if necessary.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 180

10.10.1 default Interface Methods (Cont.)
Interfaces vs. abstract Classes
Prior to Java SE 8, an interface was typically used (rather than an abstract class) when there were no implementation details to inherit—no fields and no method implementations.
With default methods, you can instead declare common method implementations in interfaces
This gives you more flexibility in designing your classes, because a class can implement many interfaces, but can extend only one superclass

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 181

10.10.2 static Interface Methods (Cont.)
Prior to Java SE 8, it was common to associate with an interface a class containing static helper methods for working with objects that implemented the interface.
In Chapter 16, you’ll learn about class Collections which contains many static helper methods for working with objects that implement interfaces Collection, List, Set and more.
Collections method sort can sort objects of any class that implements interface List.
With static interface methods, such helper methods can now be declared directly in interfaces rather than in separate classes.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 182

10.10.3 Functional Interfaces
As of Java SE 8, any interface containing only one abstract method is known as a functional interface—also called SAM (Single Abstract Method) interfaces
Functional interfaces that you’ll use in this book include:
ActionListener (Chapter 12)—You’ll implement this interface to define a method that’s called when the user clicks a button.
Comparator (Chapter 16)—You’ll implement this interface to define a method that can compare two objects of a given type to determine whether the first object is less than, equal to or greater than the second.
Runnable (Chapter 23)—You’ll implement this interface to define a task that may be run in parallel with other parts of your program.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 183

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 184

10.11  Java SE 9 private Interface Methods
As you know, a class’s private helper methods may be called only by the class’s other methods
As of Java SE 9, you can declare helper methods in interfaces via private interface methods
An interface’s private instance methods can be called directly (i.e., without an object reference) only by the interface’s other instance methods
An interface’s private static methods can be called by any of the interface’s instance or static methods

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 185

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 186

10.12  private Constructors
Sometimes it’s useful to declare one or more of a class’s constructors as private.
Preventing Object Instantiation
You can prevent client code from creating objects of a class by making the class’s constructors private
Consider class Math, which contains only public static constants and public static methods
There’s no need to create a Math object to use the class’s constants and methods, so its constructor is private

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 187

10.12  private Constructors (cont.)
Sharing Initialization Code in Constructors
One common use of a private constructor is sharing initialization code among a class’s other constructors
You can use delegating constructors (introduced in Fig. 8.5) to call the private constructor that contains the shared initialization code

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 188

10.12  private Constructors (cont.)
Factory Methods
Another common use of private constructors is to force client code to use so-called “factory methods” to create objects
A factory method is a public static method that creates and initializes an object of a specified type (possibly of the same class), then returns a reference to it
A key benefit of this architecture is that the method’s return type can be an interface or a superclass (either abstract or concrete)
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 189

10.13  Program to an Interface, Not an Implementation
Recall that Java does not allow a class to inherit from more than one superclass
With interface inheritance, a class implements an interface describing various abstract methods that the new class must provide
The new class also may inherit some method implementations (allowed in interfaces as of Java SE 8), but no instance variables
Recall that Java allows a class to implement multiple interfaces in addition to extending one class
An interface also may extend one or more other interfaces.

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 190

10.13.1  Implementation Inheritance Is Best for Small Numbers of Tightly Coupled Classes
Implementation inheritance is primarily used to declare closely related classes
many of the same instance variables and method implementations
Every subclass object has the is-a relationship with the superclass
anywhere a superclass object is expected, a subclass object may be provided
Classes declared with implementation inheritance are tightly coupled
you define the common instance variables and methods once in a superclass, then inherit them into subclasses
Changes to a superclass directly affect all corresponding subclasses
When you use a superclass variable, only a superclass object or one of its subclass objects may be assigned to the variable.

### Slide 191

10.13.1  Implementation Inheritance Is Best for Small Numbers of Tightly Coupled Classes (cont.)
A key disadvantage of implementation inheritance is that the tight coupling among the classes can make it difficult to modify the hierarchy
As we mentioned in Chapter 9, small inheritance hierarchies under the control of one person tend to be more manageable than large ones maintained by many people
This is true even with the tight coupling associated with implementation inheritance

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 192

10.13.2  Interface Inheritance Is Best for Flexibility
Interface inheritance often requires more work than implementation inheritance, because you must provide implementations of the interface’s abstract methods
even if those implementations are similar or identical among classes
Gives you additional flexibility by eliminating the tight coupling between classes
When you use a variable of an interface type, you can assign it an object of any type that implements the interface directly or indirectly
Allows you to add new types to your code easily and to replace existing objects with objects of new and improved implementation classes.
Device drivers are a good example of how interfaces enable systems to be modified easily

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 193

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 194

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 195

10.13.3  Rethinking the Employee Hierarchy
Let's reconsider the Employee hierarchy with composition and an interface
Can say that each type of employee in the hierarchy is an Employee that has a CompensationModel
Can declare CompensationModel as an interface with an abstract earnings method, then declare implementations of CompensationModel that specify the various ways in which an Employee gets paid
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 196

10.13.3  Rethinking the Employee Hierarchy
A SalariedCompensationModel would contain a weeklySalary instance variable and would implement earnings to return the weeklySalary.
An HourlyCompensationModel would contain wage and hours instance variables and would implement earnings based on the number of hours worked, with 1.5 * wage for any hours over 40.
A CommissionCompensationModel would contain grossSales and commissionRate instance variables and would implement earnings to return grossSales * commissionRate.
A BasePlusCommissionCompensationModel would contain instance variables grossSales, commissionRate and baseSalary and would implement earnings to return baseSalary + grossSales * commissionRate
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 197

10.13.3  Rethinking the Employee Hierarchy
Each Employee object you create can then be initialized with an object of the appropriate CompensationModel implementation
Class Employee’s earnings method would simply use the class’s composed CompensationModel instance variable to call the earnings method of the corresponding CompensationModel object

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 198

10.13.3  Rethinking the Employee Hierarchy
Flexibility if Compensation Models Change
Declaring the CompensationModels as separate classes that implement the same interface provides flexibility for future changes
Assume Employees who are paid by commission based on gross sales should get an extra 10% commission, but those who have a base salary should not
In the original Employee hierarchy, making this change to class CommissionEmployee’s earnings method directly affects how BasePlusCommissionEmployees are paid, because BasePlusCommissionEmployee’s earnings method calls CommissionEmployee’s earnings method.
But changing the CommissionCompensationModel’s earnings implementation does not affect BasePlusCommissionCompensationModel, because these classes are not tightly coupled by inheritance
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 199

10.13.3  Rethinking the Employee Hierarchy
Flexibility if Employees Are Promoted
Interface-based composition is more flexible than Section 10.5’s class hierarchy if an Employee gets promoted
Class Employee can provide a setCompensationModel method that receives a CompensationModel and assigns it to the Employee’s composed CompensationModel variable
When an Employee gets promoted, you’d simply call setCompensationModel to replace the Employee’s existing CompensationModel object with an appropriate new one
To promote an employee using ’s Employee hierarchy, you’d need to change the employee’s type by creating a new object of the appropriate class and moving data from the old object into the new one.
Exercise 10.18 asks you to reimplement Exercise 9.16 using interface CompensationModel as described in this section.

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 200

10.13.3  Rethinking the Employee Hierarchy
Flexibility if Employees Acquire New Capabilities
Using composition and interfaces also is more flexible than Section 10.5’s class hierarchy for enhancing class Employee
Let’s assume we decide to support retirement plans (such as 401Ks and IRAs). We could say that every Employee has a RetirementPlan and define interface RetirementPlan with a makeRetirementDeposit method
Then, we can provide appropriate implementations for various retirement-plan types

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 201

10.14  (Optional) GUI and Graphics Case Study: Drawing with Polymorphism
Shape classes have many similarities.
Using inheritance, we can “factor out” the common features from all three classes and place them in a single shape superclass.
Then, using variables of the superclass type, we can manipulate objects of all three shape objects polymorphically.
Removing the redundancy in the code will result in a smaller, more flexible program that is easier to maintain.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 202

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 203

10.14  (Optional) GUI and Graphics Case Study: Drawing with Polymorphism (Cont.)
Class MyBoundedShape can be used to factor out the common features of classes MyOval and MyRectangle.
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 204

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.
