# Chapter 14: Strings, Characters and Regular Expressions

[All chapters](README.md) · [Course guide](../reference/COURSE_GUIDE.md)

## Main concepts

- String construction, comparison, searching and manipulation.
- `StringBuilder` and character processing with `Character`.
- Regex character classes, quantifiers and input validation.
- `Pattern`, `Matcher`, replacement and splitting; string comparison examples.

## Sources

- [JHTP11_14 - REGULAR EXPRESSION.pptx](../JHTP11_14%20-%20REGULAR%20EXPRESSION.pptx)
- [Searchable text: JHTP11_14 - REGULAR EXPRESSION.md](../reference/extracted/JHTP11_14%20-%20REGULAR%20EXPRESSION.md)

## Related instructor examples

These documents cover several chapters; use the examples relevant to this topic.

- [Week 7 & 8 Java CODES.docx](../Week%207%20%26%208%20Java%20CODES.docx) · [Searchable examples](../reference/extracted/Week%207%20%26%208%20Java%20CODES.txt)

## Reading these notes

The material below preserves the available extracted text. Slide and PDF page numbers
refer to the supplied files, not necessarily the printed textbook page numbers.
Images, diagrams and image-based code require the original documents. OCR can
misread identifiers and punctuation; extracted examples are not verified runnable code.

## Slide text: JHTP11_14 - REGULAR EXPRESSION.md

### Slide 1

Chapter 14Strings, Characters and Regular Expressions
Java How to Program, 11/e

#### Speaker notes


1

### Slide 2

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


11

### Slide 3

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


13

### Slide 4

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes

{‘L’, ‘I’, ‘b’, ‘e’, ‘r’, ‘t’, ‘y’, ‘ ’, ‘U’, ‘n’, ‘I’, ‘v’, ‘e’, ‘r’, ‘s’, ‘I’, ‘t’, ‘y’}
16

### Slide 5

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


21

### Slide 6

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes

{‘L’, ‘I’, ‘b’, ‘e’, ‘r’, ‘t’, ‘y’, ‘ ’, ‘U’, ‘n’, ‘I’, ‘v’, ‘e’, ‘r’, ‘s’, ‘I’, ‘t’, ‘y’}
22

### Slide 7

This Module introduces Java’s string- and character-processing capabilities.
The techniques discussed here are appropriate for validating program input, displaying information to users and performing other text-based manipulations.
They’re also appropriate for developing text editors, word processors, page-layout software and other kinds of text-processing software.
This module discusses in detail the capabilities of classes String, StringBuilder and Character from the java.lang package
The module also discusses regular expressions that provide applications with the capability to validate input.
The functionality is located in the String class along with classes Matcher and Pattern located in the java.util.regex package.

Introduction: Strings, Characters and Regular Expressions

#### Speaker notes


27

### Slide 8

Characters are the fundamental building blocks of Java source programs.
Every program is composed of a sequence of characters that—when grouped together meaningfully—are interpreted by the Java compiler as a series of instructions used to accomplish a task.
A program may contain character literals.
A character literal is an integer value represented as a character in single quotes.
For example, 'z' represents the integer value of z, and '\t' represents the integer value of a tab character.
The value of a character literal is the integer value of the character in the Unicode character set.
 Fundamentals of Characters and Strings

#### Speaker notes


42

### Slide 9

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


47

### Slide 10

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


48

### Slide 11

Class String provides constructors for initializing String objects in a variety of ways.
Four of the constructors are demonstrated in the main method of Fig. 14.1

  String class constructors

#### Speaker notes


49

### Slide 12

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


54

### Slide 13

  String class constructors
// Fig. 14.1: StringConstructors.java// String class constructors.public class StringConstructors {   public static void main(String[] args) {      char[] charArray = {'b', 'i', 'r', 't', 'h', ' ', 'd', 'a', 'y'};      String s = new String("hello");      // use String constructors      String s1 = new String();      String s2 = new String(s);      String s3 = new String(charArray);      String s4 = new String(charArray, 6, 3);      System.out.printf(         "s1 = %s\ns2 = %s\ns3 = %s\ns4 = %s\n", s1, s2, s3, s4);    }  }

#### Speaker notes


55

### Slide 14

Line 10 instantiates a new String using class String’s no-argument constructor and assigns its reference to s1.
The new String object contains no characters (i.e., the empty string, which can also be represented as "") and has a length of 0.
Line 11 instantiates a new String object using class String’s constructor that takes a String object as an argument and assigns its reference to s2.
The new String object contains the same sequence of characters as the String object s that’s passed as an argument to the constructor.
  String class constructors cont.

#### Speaker notes


56

### Slide 15

Line 13 instantiates a new String object and assigns its reference to s4 using class String’s constructor that takes a char array and two integers as arguments.
The second argument specifies the starting position (the offset) from which characters in the array are accessed.
Remember that the first character is at position 0.
The third argument specifies the number of characters (the count) to access in the array.
The new String object is formed from the accessed characters.
If the offset or the count specified as an argument results in accessing an element outside the bounds of the character array, a StringIndexOutOfBoundsException is thrown.
   String class constructors cont.

#### Speaker notes


57

### Slide 16

Class Activities
Modify the program in previous slide as follows:
Change charArray assignment and assign to it:
char[] charArray = {‘L’, ‘I’, ‘b’, ‘e’, ‘r’, ‘t’, ‘y’, ‘ ’, ‘U’, ‘n’, ‘I’, ‘v’, ‘e’, ‘r’, ‘s’, ‘I’, ‘t’, ‘y’}
 String s = new String(“Christian");
Compile the program again.
Find:
String s5 = new String(charArray, 8, 10);
Compile the program again
Later and lastly:
 String s6 = new String(charArray, 10, 20);
Compile the program again


#### Speaker notes


60

### Slide 17

String methods length, charAt and getChars return the length of a String, obtain the character at a specific location in a String and retrieve a set of characters from a String as a char array, respectively.
Figure 14.2 demonstrates each of these methods.
   String Methods length, charAt and getChars

#### Speaker notes


66

### Slide 18

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


79

### Slide 19

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


83

### Slide 20

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


88

### Slide 21

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.
public class StringMiscellaneous {   public static void main(String[] args) {      String s1 = "hello there";      char[] charArray = new char[5];      System.out.printf("s1: %s", s1);      // test length method      System.out.printf("\nLength of s1: %d", s1.length());      // loop through characters in s1 with charAt and display reversed      System.out.printf("%nThe string reversed is: ");      for (int count = s1.length() - 1; count >= 0; count--) {         System.out.printf("%c ", s1.charAt(count));      }      // copy characters from string into charArray      s1.getChars(0, 5, charArray, 0);      System.out.printf("%nThe character array is: ");      for (char character : charArray) {         System.out.print(character);       }      System.out.println();   }    }

#### Speaker notes


89

### Slide 22

Class Activities
Modify the program in previous slide as follows:
Write a new program that takes input from keyboard (i.e. using Scanner object)
It should allow you to enter firstname and lastname from keyboard
Print the name in CORRECT ORDER using the FOR statement as shown in example in previous slide.
Print the name in REVERSE ORDER using the FOR statement as shown in example in previous slide
Print character at position 6.
Repeat the program for at least three names from your family members by entering their names from the keyboard.
Compile and program again.

#### Speaker notes


90

### Slide 23

Line 13 uses String method length to determine the number of characters in String s1.
Like arrays, strings know their own length.
However, unlike arrays, you access a String’s length via class String’s length method.
Lines 18–20 print the characters of the String s1 in reverse order (and separated by spaces).
String method charAt (line 19) returns the character at a specific position in the String.
Method charAt receives an integer argument that’s used as the index and returns the character at that position.
   String Methods length, charAt and getChars

#### Speaker notes

14.4.5 StringBuilder Insertion and Deletion Methods

95

### Slide 24

Like arrays, the first element of a String is at position 0.
Line 23 uses String method getChars to copy the characters of a String into a character array.
The first argument is the starting index from which characters are to be copied.
The second argument is the index that’s one past the last character to be copied from the String.
to test this, change the no 5 to 3, etc in Line 23 in Fig 14.2.
to test this, change to s1.getChars(1, 5, charArray, 0);  in Line 23 in Fig 14.2.
The third argument is the character array into which the characters are to be copied.
The last argument is the starting index where the copied characters are placed in the target character array.
Next, lines 26–28 print the char array contents one character at a time.
   String Methods length, charAt and getChars

#### Speaker notes

14.4.5 StringBuilder Insertion and Deletion Methods

96

### Slide 25

Class String provides methods for comparing strings, as demonstrated in the next two examples.
To understand what it means for one string to be greater than or less than another,
Consider the process of alphabetizing a series of last names.
No doubt, you’d place “Jones” before “Smith” because the first letter of “Jones” comes before the first letter of “Smith” in the alphabet.
But the alphabet is more than just a list of 26 letters—it’s an ordered list of characters.
   Comparing Strings

#### Speaker notes


103

### Slide 26

Each letter occurs in a specific position within the list.
Z is more than just a letter of the alphabet—it’s specifically the twenty-sixth letter of the alphabet.
How does the computer know that one letter “comes before” another?
All characters are represented in the computer as numeric codes.
When the computer compares Strings, it actually compares the numeric codes of the characters in the Strings.
Figure 14.3 demonstrates String methods equals, equalsIgnoreCase, compareTo and regionMatches and using the equality operator == to compare String objects.
   Comparing Strings

#### Speaker notes


104

### Slide 27

All uppercase letters come before lower case letters.
If two letters are the same case, then alphabetic order is used to compare them.
If two strings contain the same characters in the same positions, then the shortest string comes first.
 All the uppercase letters precede all the lowercase letters.
This order is what the compareTo() method of class String uses.


   Comparing Strings: Lexicographic Order

#### Speaker notes


105

### Slide 28

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


113

### Slide 29

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


114

### Slide 30

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


115

### Slide 31

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


116

### Slide 32

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


117

### Slide 33

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


118

### Slide 34

Example 1 code in MS Word file
Class Activities
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


119

### Slide 35

 // Fig. 14.3: StringCompare.java// String methods equals, equalsIgnoreCase, compareTo and regionMatches.public class StringCompare {   public static void main(String[] args) {      String s1 = new String("hello"); // s1 is a copy of "hello"      String s2 = "goodbye";      String s3 = "Happy Birthday";      String s4 = "happy birthday";      System.out.printf(         "s1 = %s\ns2 = %s\ns3 = %s\ns4 = %s\n\n", s1, s2, s3, s4);         // test for equality      if (s1.equals("hello")) { // true         System.out.println("s1 equals \"hello\"");      }      else {         System.out.println("s1 does not equal \"hello\"");       }      // test for equality with ==      if (s1 == "hello") { // false; they are not the same object         System.out.println("s1 is the same object as \"hello\"");      }      else {         System.out.println("s1 is not the same object as \"hello\"");      }      // test for equality (ignore case)      if (s3.equalsIgnoreCase(s4)) { // true         System.out.printf("%s equals %s with case ignored\n", s3, s4);      }      else {         System.out.println("s3 does not equal s4");      }      // test compareTo      System.out.printf(         "\ns1.compareTo(s2) is %d", s1.compareTo(s2));      System.out.printf(         "\ns2.compareTo(s1) is %d", s2.compareTo(s1));      System.out.printf(         "\ns1.compareTo(s1) is %d", s1.compareTo(s1));      System.out.printf(         "\ns3.compareTo(s4) is %d", s3.compareTo(s4));      System.out.printf(         "\ns4.compareTo(s3) is %d\n\n", s4.compareTo(s3));      // test regionMatches (case sensitive)      if (s3.regionMatches(0, s4, 0, 5)) {         System.out.println("First 5 characters of s3 and s4 match");      }      else {         System.out.println(            "First 5 characters of s3 and s4 do not match");      }      // test regionMatches (ignore case)      if (s3.regionMatches(true, 0, s4, 0, 5)) {         System.out.println(            "First 5 characters of s3 and s4 match with case ignored");      }      else {         System.out.println(            "First 5 characters of s3 and s4 do not match");      }   } }


#### Speaker notes


120

### Slide 36

Importance of practicing to prepare for assignments and exams

#### Speaker notes


121

### Slide 37

Line 15 uses method equals (an Object method overridden in String) to compare String s1 and the String literal "hello" for equality.
For Strings, the method determines whether the contents of the two Strings are identical.
If so, it returns true; otherwise, it returns false.
The preceding condition is true because String s1 was initialized with the literal "hello".
Method equals uses a lexicographical comparison—it compares the integer Unicode values that represent each character in each String.
Thus, if the String "hello" is compared to the string "HELLO", the result is false, because the integer representation of a lowercase letter is different from that of the corresponding uppercase letter.
String Method equals

#### Speaker notes


122

### Slide 38

Java String compareTo() Method
The compareTo() method compares two strings lexicographically.
The comparison is based on the Unicode value of each character in the strings.
The method returns 0 if the string is equal to the other string.
A value less than 0 is returned if the string is less than the other string (less characters) and a value greater than 0 if the string is greater than the other string (more characters or higher in hierachy).

Tip: Use compareToIgnoreCase() to compare two strings lexicographyically, ignoring lower case and upper case differences.

Tip: Use the equals() method to compare two strings without consideration of Unicode values.

Returns:
An int value: 0 if the string is equal to the other string.< 0 if the string is lexicographically less than the other string> 0 if the string is lexicographically greater than the other string (more characters)

#### Speaker notes


123

### Slide 39

The condition at line 23 uses the equality operator == to compare String s1 for equality with the String literal "hello".
When primitive-type values are compared with ==, the result is true if both values are identical.
When references are compared with ==, the result is true if both references refer to the same object in memory.
To compare the actual contents (or state information) of objects for equality, a method must be invoked.
In the case of Strings, that method is equals.
The condition evaluates to false at line 23 because the reference s1 was initialized with the statement
Comparing Strings with the == Operator
s1 = new String("hello");

#### Speaker notes


124

### Slide 40

The condition evaluates to false at line 23 because the reference s1 was initialized with the statement :
Which creates a new String object with a copy of string literal "hello" and assigns the new object to variable s1.
If s1 had been initialized with the statement:
Which directly assigns the string literal "hello" to variable s1, the condition would be true.
Remember that Java treats all string literal objects with the same contents as one String object to which there can be many references.
Thus, the "hello" literals in lines 6, 15 and 23 all refer to the same String object.
Comparing Strings with the == Operator
s1 = new String("hello");
s1 = "hello";

#### Speaker notes


126

### Slide 41

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


129

### Slide 42

String Methods startsWith and endsWith
Figure 14.4 demonstrates String methods startsWith and endsWith.
Method main creates array strings containing "started", "starting", "ended" and "ending".
The remainder of method main consists of three “FOR” statements that test the elements of the array to determine whether they start with or end with a particular set of characters.

#### Speaker notes


130

### Slide 43

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


131

### Slide 44

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


132

### Slide 45

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

#### Speaker notes


134

### Slide 46

public class StringStartEnd {   public static void main(String[] args) {      String[] strings = {"started", "starting", "ended", "ending"};      // test method startsWith      for (String string : strings) {         if (string.startsWith("st")) {            System.out.printf("\"%s\" starts with \"st\"\n", string);         }          }       System.out.println();      // test method startsWith starting from position 2 of string      for (String string : strings) {         if (string.startsWith("art", 2)) {            System.out.printf(               "\"%s\" starts with \"art\" at position 2\n", string);         }         }       System.out.println();      // test method endsWith      for (String string : strings) {         if (string.endsWith("ed")) {            System.out.printf("\"%s\" ends with \"ed\"\n", string);         }        }      }   }

#### Speaker notes


143

### Slide 47

String Methods startsWith and endsWith
Lines 9–13 use the version of method startsWith that takes a String argument.
The condition in the if statement (line 10) determines whether each String in the array starts with the characters "st".
If so, the method returns true and the application prints that String.
Otherwise, the method returns false and nothing happens.
Lines 18–23 use the startsWith method that takes a String and an integer as arguments.
The integer specifies the index at which the comparison should begin in the String.

#### Speaker notes


144

### Slide 48

String Methods startsWith and endsWith
The condition in the if statement (line 19) determines whether each String in the array has the characters "art" beginning with the third character in each String.
If so, the method returns true and the application prints the String. The third for statement (lines 28–32) uses method endsWith, which takes a String argument.
The condition at line 29 determines whether each String in the array ends with the characters "ed".
If so, the method returns true and the application prints the String.

#### Speaker notes


145

### Slide 49

Locating Characters and Substrings in Strings
Often, it’s useful to search a string for a character or set of characters.
For example, if you’re creating your own word processor, you might want to provide a capability for searching through documents.
Figure 14.5 demonstrates the many versions of String methods indexOf and lastIndexOf that search for a specified character or substring in a String.

#### Speaker notes


146

### Slide 50

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 51

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 52

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 53

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 54

public class StringIndexMethods {   public static void main(String[] args) {      String letters = "abcdefghijklmabcdefghijklm";      // test indexOf to locate a character in a string      System.out.printf(         "'c' is located at index %d\n", letters.indexOf('c'));      System.out.printf(         "'a' is located at index %d\n", letters.indexOf('a', 1));      System.out.printf(         "'$' is located at index %d\n\n", letters.indexOf('$'));      // test lastIndexOf to find a character in a string      System.out.printf("Last 'c' is located at index %d\n",         letters.lastIndexOf('c'));      System.out.printf("Last 'a' is located at index %d\n",         letters.lastIndexOf('a', 25));      System.out.printf("Last '$' is located at index %d\n\n",         letters.lastIndexOf('$'));      // test indexOf to locate a substring in a string      System.out.printf("\"def\" is located at index %d\n",          letters.indexOf("def"));      System.out.printf("\"def\" is located at index %d\n",         letters.indexOf("def", 7));      System.out.printf("\"hello\" is located at index %d\n\n",         letters.indexOf("hello"));      // test lastIndexOf to find a substring in a string      System.out.printf("Last \"def\" is located at index %d\n",         letters.lastIndexOf("def"));      System.out.printf("Last \"def\" is located at index %d\n",         letters.lastIndexOf("def", 25));      System.out.printf("Last \"hello\" is located at index %d\n",         letters.lastIndexOf("hello"));   }  }

### Slide 55

Locating Characters and Substrings in Strings
All the searches in this example are performed on the String letters (initialized with "abcdefghijklmabcdefghijklm").
Lines 9–14 use method indexOf to locate the first occurrence of a character in a String.
If the method finds the character, it returns the character’s index in the String—otherwise, it returns –1.
There are two versions of indexOf that search for characters in a String.
Line 10 uses the version of method indexOf that takes an integer representation of the character to find.
Line 12 uses another version of method indexOf, which takes two integer arguments—the character and the starting index at which the search of the String should begin.

### Slide 56

Locating Characters and Substrings in Strings
Lines 17–22 use method lastIndexOf to locate the last occurrence of a character in a String.
It searches from the end of the String toward the beginning.
If it finds the character, it returns the character’s index in the String—
otherwise, it returns –1.
There are two versions of lastIndexOf that search for characters in a String.
Line 18 uses the version that takes the integer representation of the character.
Line 20 uses the version that takes two integer arguments—the integer representation of the character and the index from which to begin searching backward.
Lines 25–38 demonstrate versions of methods indexOf and lastIndexOf that each take a String as the first argument.

### Slide 57

Extracting Substrings from Strings
Class String provides two substring methods to enable a new String object to be created by copying part of an existing String object.
Each method returns a new String object.
Both methods are demonstrated in Fig. 14.6
For more information on class String in Java API, see here:
https://docs.oracle.com/javase/7/docs/api/java/lang/String.html

### Slide 58

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 59

// Fig. 14.6: SubString.java// String class substring methods.public class SubString {   public static void main(String[] args) {      String letters = "abcdefghijklmabcdefghijklm";      // test substring methods      System.out.printf("Substring from index 20 to end is \"%s\"\n",         letters.substring(20));      System.out.printf("%s \"%s\"\n",          "Substring from index 3 up to, but not including, 6 is",         letters.substring(3, 6));   } }

### Slide 60

Concatenating Strings
String method concat (Fig. 14.7) concatenates two String objects (similar to using the + operator)
Returns a new String object containing the characters from both original Strings.
The expression s1.concat(s2) at line 11 forms a String by appending the characters in s2 to the those in s1.
The original Strings to which s1 and s2 refer are not modified.

### Slide 61

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 62

// Fig. 14.7: StringConcatenation.java// String method concat.public class StringConcatenation {   public static void main(String[] args) {      String s1 = "Happy ";      String s2 = "Birthday";      System.out.printf("s1 = %s\ns2 = %s\n\n",s1, s2);      System.out.printf(         "Result of s1.concat(s2) = %s\n", s1.concat(s2));      System.out.printf("s1 after concatenation = %s\n", s1);   }   }

### Slide 63

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 64

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 65

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 66

String Method valueOf
As we’ve seen, every object in Java has a toString method that enables a program to obtain the object’s string representation.
Class String provides static methods that take an argument of any type and convert it to a String object.
Figure 14.9 demonstrates the String class valueOf methods.
For more information on class String in Java API, see here:
https://docs.oracle.com/javase/7/docs/api/java/lang/String.html



### Slide 67

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 68

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 69

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 70

// Fig. 14.9: StringValueOf.java// String valueOf methods.public class StringValueOf {   public static void main(String[] args) {      char[] charArray = {'a', 'b', 'c', 'd', 'e', 'f'};      boolean booleanValue = true;      char characterValue = 'Z';      int integerValue = 7;      long longValue = 10000000000L; // L suffix indicates long      float floatValue = 2.5f; // f indicates that 2.5 is a float      double doubleValue = 33.333; // no suffix, double is default      Object objectRef = "hello"; // assign string to an Object reference      System.out.printf(         "char array = %s\n", String.valueOf(charArray));      System.out.printf("part of char array = %s\n",          String.valueOf(charArray, 3, 3));      System.out.printf(         "boolean = %s\n", String.valueOf(booleanValue));      System.out.printf(         "char = %s\n", String.valueOf(characterValue));      System.out.printf("int = %s\n", String.valueOf(integerValue));      System.out.printf("long = %s\n", String.valueOf(longValue));       System.out.printf("float = %s\n", String.valueOf(floatValue));       System.out.printf(         "double = %s\n", String.valueOf(doubleValue));       System.out.printf("Object = %s\n", String.valueOf(objectRef));   }   }

### Slide 71

Class Activities
We have explored few methods on class String but there are still plenty of methods in the class.

For you class participation, go to class String in the Java API and implement 10 more methods with detailed comments within the code and the screenshots of your compilation output/result.


### Slide 72

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 73

StringBuilder Class
Class StringBuilder  is useful for creating and manipulating dynamic string information—that is, modifiable strings.
Every StringBuilder is capable of storing a number of characters specified by its capacity.
If a StringBuilder’s capacity is exceeded, the capacity expands to accommodate the additional characters.
The StringBuilder in Java represents a mutable sequence of characters.
Since the String Class in Java creates an immutable sequence of characters, the StringBuilder class provides an alternative to String Class, as it creates a mutable sequence of characters.
Class StringBuilder provides four constructors.
We demonstrate three of these in Fig. 14.10.


### Slide 74

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 75

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 76

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 77

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.
// Fig. 14.10: StringBuilderConstructors.java// StringBuilder constructors.public class StringBuilderConstructors {   public static void main(String[] args) {      StringBuilder buffer1 = new StringBuilder();      StringBuilder buffer2 = new StringBuilder(10);      StringBuilder buffer3 = new StringBuilder("hello");      System.out.printf("buffer1 = \"%s\"\n", buffer1);      System.out.printf("buffer2 = \"%s\"\n", buffer2);      System.out.printf("buffer3 = \"%s\"\n", buffer3);   }   }

### Slide 78

StringBuilder Constructors Explained
Line 6 uses the no-argument StringBuilder constructor to create a String-Builder with no characters in it and an initial capacity of 16 characters (the default for a StringBuilder).
Line 7 uses the StringBuilder constructor that takes an integer argument to create a StringBuilder with no characters in it and the initial capacity specified by the integer argument (i.e., 10).
Line 8 uses the StringBuilder constructor that takes a String argument to create a StringBuilder containing the characters in the String argument.
The initial capacity is the number of characters in the String argument plus 16.
Lines 10–12 implicitly use the method toString of class StringBuilder to output the StringBuilders with the printf method.

### Slide 79

Class StringBuilder’s length return the number of characters currently in a StringBuilder.
Class StringBuilder’s capacity method return the number of characters that can be stored without allocating more memory, respectively.
Method ensureCapacity guarantees that a String-Builder has at least the specified capacity.
Method setLength increases or decreases the length of a StringBuilder.
Figure 14.11 demonstrates these methods.
For more information on class StringBuilder in Java API, see here:
https://docs.oracle.com/javase/7/docs/api/java/lang/StringBuilder.html


StringBuilder Methods length, capacity, setLength and ensureCapacity

### Slide 80

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 81

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 82

// Fig. 14.11: StringBuilderCapLen.java// StringBuilder length, setLength, capacity and ensureCapacity methods.public class StringBuilderCapLen {   public static void main(String[] args) {      StringBuilder buffer = new StringBuilder("Hello, how are you?");      System.out.printf("buffer = %s\nlength = %d\ncapacity = %d\n\n",         buffer.toString(), buffer.length(), buffer.capacity());      buffer.ensureCapacity(75);      System.out.printf("New capacity = %d\n\n", buffer.capacity());      buffer.setLength(10);      System.out.printf("New length = %d\nbuffer = %s\n",          buffer.length(), buffer.toString());   }   }

### Slide 83

The application contains one StringBuilder called buffer.
Line 6 uses the String-Builder constructor that takes a String argument to initialize the StringBuilder with "Hello, how are you?".
Lines 8–9 print the contents, length and capacity of the String-Builder.
Note in the output window that the capacity of the StringBuilder is initially 35.
Recall StringBuilder constructor that takes a String argument initializes the capacity to the length of the string passed as an argument plus 16.
Line 11 uses method ensureCapacity to expand the capacity of the StringBuilder to a minimum of 75 characters.
Line 14 uses method setLength to set the length of the StringBuilder to 10.
StringBuilder Methods length, capacity, setLength and ensureCapacity

### Slide 84



### Slide 85

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 86

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 87

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 88

// Fig. 14.12: StringBuilderChars.java
// StringBuilder methods charAt, setCharAt, getChars and reverse.
public class StringBuilderChars {
   public static void main(String[] args) {
      StringBuilder buffer = new StringBuilder("hello there");

      System.out.printf("buffer = %s\n", buffer.toString());
      System.out.printf("Character at 0: %s\nCharacter at 4: %s\n\n",
         buffer.charAt(0), buffer.charAt(4));

      char[] charArray = new char[buffer.length()];
      buffer.getChars(0, buffer.length(), charArray, 0);
      System.out.print("The characters are: ");

      for (char character : charArray) {
         System.out.print(character);
      }
      buffer.setCharAt(0, 'H');
      buffer.setCharAt(6, 'T');
      System.out.printf("\n\nbuffer = %s", buffer.toString());

      buffer.reverse();
      System.out.printf("\n\nbuffer = %s\n", buffer.toString());
   }  }

### Slide 89

Class StringBuilder provides overloaded append methods (Fig. 14.13) to allow values of various types to be appended to the end of a StringBuilder.
Versions are provided for each of the primitive types and for character arrays, Strings, Objects, and more.
(Remember that method toString produces a string representation of any Object.)
Each method takes its argument, converts it to a string and appends it to the StringBuilder.
The call System.getProperty("line.separator") returns a platform-independent newline.
14.4.4 StringBuilder append Methods

### Slide 90

The compiler can use StringBuilder and the append() methods to implement the + and += String concatenation operators.
For example, assuming the declarations.
the statement
14.4.4 StringBuilder append Methods
String s = string1 + string2 + value;
concatenates "hello", "BC" and 22.
The concatenation can be performed as follows:
String s = new StringBuilder().append("hello").append("BC").
   append(22).toString();
First, the preceding statement creates an empty StringBuilder, then appends to it the strings "hello" and "BC" and the integer 22.

Next, StringBuilder’s toString method converts the StringBuilder to a String object to be assigned to String s.

### Slide 91

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 92

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 93

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 94

// Fig. 14.13: StringBuilderAppend.java
// StringBuilder append methods.
public class StringBuilderAppend {
   public static void main(String[] args) {
      Object objectRef = "hello";
      String string = "goodbye";
      char[] charArray = {'a', 'b', 'c', 'd', 'e', 'f'};
      boolean booleanValue = true;
      char characterValue = 'Z';
      int integerValue = 7;
      long longValue = 10000000000L;
      float floatValue = 2.5f;
      double doubleValue = 33.333;

      StringBuilder lastBuffer = new StringBuilder("last buffer");
      StringBuilder buffer = new StringBuilder();

      buffer.append(objectRef)
            .append(System.getProperty("line.separator"))
            .append(string)
            .append(System.getProperty("line.separator"))
            .append(charArray)
            .append(System.getProperty("line.separator"))
            .append(charArray, 0, 3)
            .append(System.getProperty("line.separator"))
            .append(booleanValue)
            .append(System.getProperty("line.separator"))
            .append(characterValue)
            .append(System.getProperty("line.separator"))
            .append(integerValue)
            .append(System.getProperty("line.separator"))
            .append(longValue)
            .append(System.getProperty("line.separator"))
            .append(floatValue)
            .append(System.getProperty("line.separator"))
            .append(doubleValue)
            .append(System.getProperty("line.separator"))
            .append(lastBuffer);

      System.out.printf("buffer contains%n%s%n", buffer.toString());
   } }

### Slide 95

StringBuilder provides overloaded insert methods to insert values of various types at any position in a StringBuilder.
Versions are provided for the primitive types and for character arrays, Strings, Objects and CharSequences.
Each method takes its second argument and inserts it at the index specified by the first argument.
If the first argument is less than 0 or greater than the StringBuilder’s length, a StringIndexOutOfBounds-Exception occurs.
14.4.5 StringBuilder Insertion and Deletion Methods

### Slide 96

Class StringBuilder also provides methods delete and deleteCharAt to delete characters at any position in a StringBuilder.
Method delete takes two arguments—the starting index and the index one past the end of the characters to delete.
All characters beginning at the starting index up to but not including the ending index are deleted.
Method deleteCharAt takes one argument—the index of the character to delete.
Invalid indices cause both methods to throw a StringIndexOutOfBoundsException.
Figure 14.14 demonstrates methods insert, delete and deleteCharAt.
14.4.5 StringBuilder Insertion and Deletion Methods

### Slide 97

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 98

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 99

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 100

// Fig. 14.14: StringBuilderInsertDelete.java
// StringBuilder methods insert, delete and deleteCharAt.

public class StringBuilderInsertDelete {
   public static void main(String[] args) {
      Object objectRef = "hello";
      String string = "goodbye";
      char[] charArray = {'a', 'b', 'c', 'd', 'e', 'f'};
      boolean booleanValue = true;
      char characterValue = 'K';
      int integerValue = 7;
      long longValue = 10000000;
      float floatValue = 2.5f; // f suffix indicates that 2.5 is a float
      double doubleValue = 33.333;

      StringBuilder buffer = new StringBuilder();

      buffer.insert(0, objectRef)
            .insert(0, "  ") // each of these contains new line
            .insert(0, string)
            .insert(0, "  ")
            .insert(0, charArray)
            .insert(0, "  ")
            .insert(0, charArray, 3, 3)
            .insert(0, "  ")
            .insert(0, booleanValue)
            .insert(0, "  ")
            .insert(0, characterValue)
            .insert(0, "  ")
            .insert(0, integerValue)
            .insert(0, "  ")
            .insert(0, longValue)
            .insert(0, "  ")
            .insert(0, floatValue)
            .insert(0, "  ")
            .insert(0, doubleValue);

      System.out.printf(
         "buffer after inserts:\n%s\n\n", buffer.toString());

      buffer.deleteCharAt(10); // delete 5 in 2.5
      buffer.delete(2, 6); // delete .333 in 33.333

      System.out.printf(
         "buffer after deletes:\n%s\n", buffer.toString());
   } }

### Slide 101

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.
Prayers

### Slide 102

Class Activities
We have explored few methods on class StringBuilder but there are still plenty of methods in the class.

For you class participation, go to class StringBuilder in the Java API and implement 5 more methods with detailed comments within the code and the screenshots of your compilation output/result.


### Slide 103

In this section, we present class Character—the type-wrapper class for primitive type char.
Most Character methods are static methods designed for convenience in processing individual char values.
These methods take at least a character argument and perform either a test or a manipulation of the character.
Class Character also contains a constructor that receives a char argument to initialize a Character object.
Class Character has many methods and few examples shown in next codes.
For more information on class Character (and all the type-wrapper classes), see the java.lang package in the Java API documentation.

Class Character

### Slide 104

Figure 14.15 demonstrates static methods that test characters to determine whether they’re a specific character type and the static methods that perform case conversions on characters.
You can enter any character and apply the methods to the character.
Line 13 uses Character method isDefined to determine whether character c is defined in the Unicode character set.
If so, the method returns true; otherwise, it returns false.
Line 14 uses Character method isDigit to determine whether character c is a defined Unicode digit.
If so, the method returns true, and otherwise, false.
For more information on class Character (and all the type-wrapper classes), see:  https://docs.oracle.com/javase/7/docs/api/java/lang/Character.html

Class Character cont.

### Slide 105

Line 16 uses Character method isJavaIdentifierStart to determine whether c is a character that can be the first character of an identifier in Java—that is, a letter, an underscore (_) or a dollar sign ($).
If so, the method returns true, and otherwise, false.
Line 18 uses Character method isJavaIdentifierPart to determine whether character c is a character that can be used in an identifier in Java—that is, a digit, a letter, an underscore (_) or a dollar sign ($).
Line 19 uses Character method isLetter to determine whether character c is a letter.
Line 21 uses Character method isLetterOrDigit(c) to determine whether character c is a letter or a digit.
Line 23 uses Character method isLowerCase to determine whether c is a lowercase letter.
Class Character

### Slide 106

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 107

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 108

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 109

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 110

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 111

import java.util.Scanner;public class StaticCharMethods {   public static void main(String[] args) {      Scanner scanner = new Scanner(System.in); // create scanner      System.out.println("Enter a character and press Enter");      String input = scanner.next();       char c = input.charAt(0); // get input character      // display character info      System.out.printf("is defined: %b\n", Character.isDefined(c));      System.out.printf("is digit: %b\n", Character.isDigit(c));      System.out.printf("is first character in a Java identifier: %b\n",         Character.isJavaIdentifierStart(c));      System.out.printf("is part of a Java identifier: %b\n",         Character.isJavaIdentifierPart(c));      System.out.printf("is letter: %b\n", Character.isLetter(c));      System.out.printf(         "is letter or digit: %b\n", Character.isLetterOrDigit(c));      System.out.printf(         "is lower case: %b\n", Character.isLowerCase(c));      System.out.printf(         "is upper case: %b\n", Character.isUpperCase(c));      System.out.printf(         "to upper case: %s\n", Character.toUpperCase(c));      System.out.printf(         "to lower case: %s\n", Character.toLowerCase(c));   }  }

### Slide 112

Class Activities
We have explored few methods on Class Character but there are still plenty of methods in the class.

For you class participation, go to Class Character in the Java API and implement 10 more methods with detailed comments within the code and the screenshots of your compilation output/result.


### Slide 113

What is a Regular Expression?
A regular expression is a sequence of characters that forms a search pattern.
When you search for data in a text, you can use this search pattern to describe what you are searching for.
A regular expression can be a single character, or a more complicated pattern.
Regular expressions can be used to perform all types of text search and text replace operations.

Java Regular Expressions

### Slide 114

A regular expression is a String that describes a search pattern for matching characters in other Strings.
Such expressions are useful for validating input and ensuring that data is in a particular format.
For example, a ZIP code must consist of five digits, and a last name must contain only letters, spaces, apostrophes and hyphens.
One application of regular expressions is to facilitate the construction of a compiler.
Often, a large and complex regular expression is used to validate the syntax of a program.
If the program code does not match the regular expression, the compiler knows that there’s a syntax error in the code.
Java Regular Expressions

### Slide 115

Class String provides several methods for performing regular-expression operations, the simplest of which is the matching operation.
String method matcher receives a String that specifies the regular expression and matches the contents of the String object on which it’s called to the regular expression.
The method returns a boolean indicating whether the match succeeded.
A regular expression consists of literal characters and special symbols..
Java Regular Expressions

### Slide 116

Regular expressions can be used to perform all types of text search and text replace operations.
Java does not have a built-in Regular Expression class, but we can import the java.util.regex package to work with regular expressions.
The package includes the following classes:


Java Regular Expressions Cont.
Pattern Class - Defines a pattern (to be used in a search)
Matcher Class - Used to search for the pattern
PatternSyntaxException Class - Indicates syntax error in a regular expression pattern

### Slide 117

Example
To find out if there are any occurrences of the word “Liberty" in a sentence: Liberty University

Java Regular Expressions: Class Activities

### Slide 118

Java Regular Expressions: Class Activities
import java.util.regex.Matcher;import java.util.regex.Pattern;public class Main {    public static void main(String[] args) {        Pattern pattern = Pattern.compile("Liberty", Pattern.CASE_INSENSITIVE);        Matcher myMatcher = pattern.matcher("Liberty University!");        boolean matchFound = myMatcher.find();        if(matchFound) {            System.out.println("Match found");        } else {            System.out.println("Match not found");        }        }    }

### Slide 119

In this example, The word “Liberty" is being searched for in a sentence.
First, the pattern is created using the Pattern.compile() method.
The first parameter indicates which pattern is being searched for and the second parameter has a flag to indicates that the search should be case-insensitive.
The second parameter is optional.
The matcher() (in Class Pattern) method is used to search for the pattern in a string.
It returns a Matcher object which contains information about the search that was performed.
The find() (in Class Matcher) method returns true if the pattern was found in the string and false if it was not found.
Example Explained

### Slide 120

Example Explained : Flags
Flags in the compile() method change how the search is performed. Here are a few of them:
Pattern.CASE_INSENSITIVE - The case of letters will be ignored when performing a search.
Pattern.LITERAL - Special characters in the pattern will not have any special meaning and will be treated as ordinary characters when performing a search.
Pattern.UNICODE_CASE - Use it together with the CASE_INSENSITIVE flag to also ignore the case of letters outside of the English alphabet

### Slide 121

Regular Expression Patterns
The first parameter of the Pattern.compile() method is the pattern.
It describes what is being searched for.
For more information on package RegeX (and all the type-wrapper classes), see:
https://docs.oracle.com/javase/8/docs/api/index.html?java/util/regex/package-summary.html

### Slide 122

The appendReplacement(StringBuilder, String) method of Matcher Class behaves as a append-and-replace method.
This method reads the input string and replace it with the matched pattern in the matcher string.
Matcher appendReplacement(StringBuilder, String) method in Java with Examples
public Matcher appendReplacement(StringBuilder builder, String stringToBeReplaced)

### Slide 123

Parameters: This method takes two parameters:
builder: which is the StringBuilder that stores the target string.
stringToBeReplaced: which is the String to be replaced in the matcher.
Return Value: This method returns a Matcher with the target String replaced.
Exception: This method throws following exceptions:

Matcher appendReplacement(StringBuilder, String) method in Java with Examples
public Matcher appendReplacement(StringBuilder builder, String stringToBeReplaced)

### Slide 124

Exception: This method throws following exceptions:
IllegalStateException: If no match has yet been attempted, or if the previous match operation failed
IllegalArgumentException: If the replacement string refers to a named-capturing group that does not exist in the pattern
IndexOutOfBoundsException: If the replacement string refers to a capturing group that does not exist in the pattern
Below examples illustrate the Matcher.appendReplacement() method:

Matcher appendReplacement(StringBuilder, String) method in Java with Examples

### Slide 125

Below examples illustrate the Matcher.appendReplacement() method:
// Example 2:
//Example 3
// Java code to illustrate appendReplacement() method

CLASS ACTIVITIES

### Slide 126

// Example 2:
// Java code to illustrate appendReplacement() method
import java.util.regex.*;

public class AppendReplacement {
    public static void main(String[] args)
    {
        // Get the regex to be checked
        String regex = "Liberty";

        // Create a pattern from regex
        Pattern pattern = Pattern.compile(regex);

        // Get the String to be matched
        String stringToBeMatched = "I love Liberty University, I attend Liberty University";

        // Create a matcher for the input String
        Matcher matcher = pattern.matcher(stringToBeMatched);

        System.out.println("Before Replacement: " + stringToBeMatched);

        // Get the String to be replaced
        String stringToBeReplaced = Christian";
        StringBuilder builder = new StringBuilder();

        // Replace every matched pattern
        // with the target String
        // using appendReplacement() method
        while (matcher.find()) {
            matcher.appendReplacement(builder, stringToBeReplaced);
        }
        matcher.appendTail(builder);

        // Print the replaced matcher
        System.out.println("After Replacement: " + builder.toString());
    }  }
debug:
Before Replacement: I love Liberty University, I attend Liberty University


After Replacement: I love Christian University, I attend Christian University

### Slide 127



### Slide 128

// Example 3: Further Java code to illustrate appendReplacement() method
// Java code to illustrate appendReplacement() method
import java.util.regex.*;

public class AppendReplacement2 {
    public static void main(String[] args)
    {

        // Get the regex to be checked
        String regex = "(LIBERTY)";

        // Create a pattern from regex
        Pattern pattern = Pattern.compile(regex);

        // Get the String to be matched
        String stringToBeMatched = "LIBERTY UNIVERSTY LIBERTY UNIVERSTY LIBERTY UNIVERSTY LIBERTY UNIVERSTY ";

        // Create a matcher for the input String
        Matcher matcher = pattern.matcher(stringToBeMatched);

        System.out.println("Before Replacement: " + stringToBeMatched);

        // Get the String to be replaced
        String stringToBeReplaced = "CHRISTIAN";
        StringBuilder builder = new StringBuilder();
    // Replace every matched pattern
        // with the target String
        // using appendReplacement() method
        while (matcher.find()) {
            matcher.appendReplacement(builder, stringToBeReplaced);
        }
        matcher.appendTail(builder);

        // Print the replaced matcher
        System.out.println("After Replacement: " + builder.toString());
    }
}
// Example 3
OUTPUT
Before Replacement: LIBERTY UNIVERSTY LIBERTY UNIVERSTY LIBERTY UNIVERSTY LIBERTY UNIVERSTY

After Replacement: CHRISTIAN UNIVERSTY CHRISTIAN UNIVERSTY CHRISTIAN UNIVERSTY CHRISTIAN UNIVERSTY

### Slide 129

14.7  Regular Expressions, Class Pattern and Class Matcher
A regular expression is a specially formatted String that describes a search pattern for matching characters in other Strings.
Useful for validating input and ensuring that data is in a particular format.
One application of regular expressions is to facilitate the construction of a compiler.
Often, a large and complex regular expression is used to validate the syntax of a program.
If the program code does not match the regular expression, the compiler knows that there is a syntax error within the code.
© Copyright 1992-2015 by Pearson Education, Inc. All Rights Reserved.

### Slide 130

14.7  Regular Expressions, Class Pattern and Class Matcher (cont.)
String method matches receives a String that specifies the regular expression and matches the contents of the String object on which it’s called to the regular expression.
The method returns a boolean indicating whether the match succeeded.
A regular expression consists of literal characters and special symbols.
© Copyright 1992-2015 by Pearson Education, Inc. All Rights Reserved.

### Slide 131

14.7  Regular Expressions, Class Pattern and Class Matcher (cont.)
Figure 14.19 specifies some predefined character classes that can be used with regular expressions.
A character class is an escape sequence that represents a group of characters.
A digit is any numeric character.
A word character is any letter (uppercase or lowercase), any digit or the underscore character.
A white-space character is a space, a tab, a carriage return, a newline or a form feed.
Each character class matches a single character in the String we’re attempting to match with the regular expression.
Regular expressions are not limited to predefined character classes.
The expressions employ various operators and other forms of notation to match complex patterns.

### Slide 132

14.7  Regular Expressions, Class Pattern and Class Matcher (cont.)
To match a set of characters that does not have a predefined character class, use square brackets, [].
The pattern "[aeiou]" matches a single character that’s a vowel.
Character ranges are represented by placing a dash (-) between two characters.
"[A-Z]" matches a single uppercase letter.
If the first character in the brackets is "^", the expression accepts any character other than those indicated.
"[^Z]" is not the same as "[A-Y]", which matches uppercase letters A–Y—
"[^Z]" matches any character other than capital Z, including lowercase letters and nonletters such as the newline character.

### Slide 133

© Copyright 1992-2015 by Pearson Education, Inc. All Rights Reserved.
More information here:
https://docs.oracle.com/javase/tutorial/essential/regex/pre_char_classes.html

### Slide 134

Java Regular Expressions Summary

### Slide 135

© Copyright 1992-2015 by Pearson Education, Inc. All Rights Reserved.

### Slide 136

© Copyright 1992-2015 by Pearson Education, Inc. All Rights Reserved.

### Slide 137

© Copyright 1992-2015 by Pearson Education, Inc. All Rights Reserved.

### Slide 138

© Copyright 1992-2015 by Pearson Education, Inc. All Rights Reserved.

### Slide 139

© Copyright 1992-2015 by Pearson Education, Inc. All Rights Reserved.

### Slide 140

© Copyright 1992-2015 by Pearson Education, Inc. All Rights Reserved.

### Slide 141

// Fig. 14.20: ValidateInput.java// Validating user information using regular expressions.public class ValidateInput {   // validate first name   public static boolean validateFirstName(String firstName) {      return firstName.matches("[A-Z][a-zA-Z]*");   }    // validate last name   public static boolean validateLastName(String lastName) {      return lastName.matches("[a-zA-z]+(['-][a-zA-Z]+)*");   }    // validate address   public static boolean validateAddress(String address) {      return address.matches(         "\\d+\\s+([a-zA-Z]+|[a-zA-Z]+\\s[a-zA-Z]+)");   }   // validate city   public static boolean validateCity(String city) {      return city.matches("([a-zA-Z]+|[a-zA-Z]+\\s[a-zA-Z]+)");   }    // validate state   public static boolean validateState(String state) {      return state.matches("([a-zA-Z]+|[a-zA-Z]+\\s[a-zA-Z]+)") ;   }   // validate zip   public static boolean validateZip(String zip) {      return zip.matches("\\d{5}");   }   // validate phone   public static boolean validatePhone(String phone) {      return phone.matches("[1-9]\\d{2}-[1-9]\\d{2}-\\d{4}");   }  }

### Slide 142

// Fig. 14.21: Validate.java// Input and validate data from user using the ValidateInput class.import java.util.Scanner;public class Validate {   public static void main(String[] args) {      // get user input      Scanner scanner = new Scanner(System.in);      System.out.println("Please enter first name:");      String firstName = scanner.nextLine();      System.out.println("Please enter last name:");      String lastName = scanner.nextLine();      System.out.println("Please enter address:");      String address = scanner.nextLine();      System.out.println("Please enter city:");      String city = scanner.nextLine();      System.out.println("Please enter state:");      String state = scanner.nextLine();      System.out.println("Please enter zip:");      String zip = scanner.nextLine();      System.out.println("Please enter phone:");      String phone = scanner.nextLine();      // validate user input and display error message      System.out.println("\nValidate Result:");      if (!ValidateInput.validateFirstName(firstName)) {         System.out.println("Invalid first name");      }      else if (!ValidateInput.validateLastName(lastName)) {         System.out.println("Invalid last name");      }      else if (!ValidateInput.validateAddress(address)) {         System.out.println("Invalid address");      }      else if (!ValidateInput.validateCity(city)) {         System.out.println("Invalid city");      }      else if (!ValidateInput.validateState(state)) {         System.out.println("Invalid state");      }      else if (!ValidateInput.validateZip(zip)) {         System.out.println("Invalid zip code");      }      else if (!ValidateInput.validatePhone(phone)) {         System.out.println("Invalid phone number");      }      else {         System.out.println("Valid input.  Thank you.");      }   } }

### Slide 143

14.7  Regular Expressions, Class Pattern and Class Matcher (cont.)
Ranges in character classes are determined by the letters’ integer values.
"[A-Za-z]" matches all uppercase and lowercase letters.
The range "[A-z]" matches all letters and also matches those characters (such as [ and \) with an integer value between uppercase Z and lowercase a.
Like predefined character classes, character classes delimited by square brackets match a single character in the search object.
© Copyright 1992-2015 by Pearson Education, Inc. All Rights Reserved.

### Slide 144

14.7  Regular Expressions, Class Pattern and Class Matcher (cont.)
When the regular-expression operator "*" appears in a regular expression, the application attempts to match zero or more occurrences of the subexpression immediately preceding the "*".
Operator "+" attempts to match one or more occurrences of the subexpression immediately preceding "+".
The character "|" matches the expression to its left or to its right.
"Hi (John|Jane)" matches both "Hi John" and "Hi Jane".
Parentheses are used to group parts of the regular expression.
© Copyright 1992-2015 by Pearson Education, Inc. All Rights Reserved.

### Slide 145

14.7  Regular Expressions, Class Pattern and Class Matcher (cont.)
Sometimes it’s useful to replace parts of a string or to split a string into pieces. For this purpose, class String provides methods replaceAll, replaceFirst and split.
© Copyright 1992-2015 by Pearson Education, Inc. All Rights Reserved.

### Slide 146

14.7  Regular Expressions, Class Pattern and Class Matcher (cont.)
String method replaceAll replaces text in a String with new text (the second argument) wherever the original String matches a regular expression (the first argument).
Escaping a special regular-expression character with \ instructs the matching engine to find the actual character.
String method replaceFirst replaces the first occurrence of a pattern match.
© Copyright 1992-2015 by Pearson Education, Inc. All Rights Reserved.

### Slide 147

© Copyright 1992-2015 by Pearson Education, Inc. All Rights Reserved.

### Slide 148



### Slide 149

© Copyright 1992-2015 by Pearson Education, Inc. All Rights Reserved.

### Slide 150

// Fig. 14.23: RegexSubstitution.java// String methods replaceFirst, replaceAll and split.import java.util.Arrays;public class RegexSubstitution {   public static void main(String[] args) {      String firstString = "This sentence ends in 5 stars *****";      String secondString = "1, 2, 3, 4, 5, 6, 7, 8";               System.out.printf("Original String 1: %s\n", firstString);      // replace '*' with '^'      firstString = firstString.replaceAll("\\*", "^");      System.out.printf("^ substituted for *: %s\n", firstString);      // replace 'stars' with 'carets'      firstString = firstString.replaceAll("stars", "carets");      System.out.printf(         "\"carets\" substituted for \"stars\": %s\n", firstString);      // replace words with 'word'      System.out.printf("Every word replaced by \"word\": %s\n\n",         firstString.replaceAll("\\w+", "word"));      System.out.printf("Original String 2: %s\n", secondString);      // replace first three digits with 'digit'           for (int i = 0; i < 3; i++) {         secondString = secondString.replaceFirst("\\d", "digit");      }      System.out.printf(         "First 3 digits replaced by \"digit\" : %s\n", secondString);      System.out.print("String split at commas: ");      String[] results = secondString.split(",\\s*"); // split on commas      System.out.println(Arrays.toString(results)); // display results   }  }

### Slide 151

5.8  Java API Packages
Java contains many predefined classes that are grouped into categories of related classes called packages
Known as the Java Application Programming Interface (Java API), or the Java class library
String/StringBuilder Classes and their methods are in Java.Lang package
  Overview of the packages in Java
http://docs.oracle.com/javase/7/docs/api/overview-summary.html
Additional information about a predefined Java class’s methods
http://docs.oracle.com/javase/7/docs/api/
Index link shows alphabetical list of all the classes and methods in the Java API
Locate the class name and click its link to see the online description of the class
METHOD link shows a table of the class’s methods
Each static method will be listed with the word “static” preceding its return type.

### Slide 152

Programming Assignment 3 and Exams
Programming Assignment 4 and Exams.

### Slide 153

Class Activities
Your Assignment 4 covers everything we have discussed in this chapter.

For you class participation and to help in your Assignment 4, go to package Regex in the Java API and familiarize yourself with the methods of the classes therein.

Most importantly, farmiliarize yourself with the “Summary of regular-expression constructs” in class Pattern in package Regex.

For class participation, implement as many methods and constructs as you can with detailed comments within the code and the screenshots of your compilation output/result.


### Slide 154

EXTRA SLIDES FOR YOUR PRIVATE PRACTICE


### Slide 155

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 156

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 157

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

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 163

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 164

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 165

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 166

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 167

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 168

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 169

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 170

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Slide 171

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

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.
