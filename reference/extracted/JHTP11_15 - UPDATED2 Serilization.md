# JHTP11_15 - UPDATED2 Serilization.pptx

## Slide 1

Chapter 15Files, Input/Output Stream, NIO and XML Serialization
Java How to Program, 11/e

### Speaker notes


1

## Slide 2



### Speaker notes


7

## Slide 3



### Speaker notes


12

## Slide 4

Data stored in variables and arrays is temporary—
it’s lost when a local variable goes out of scope or when the program terminates.
For long-term retention of data, even after the programs that create the data terminate, computers use files.
You use files every day for tasks such as writing a document or creating a spreadsheet.
Computers store files on secondary storage devices, including hard disks, flash drives, DVDs and more.
Data maintained in files is persistent data—it exists beyond the duration of program execution.
In this week, we explain how Java programs create, update and process files
Introduction

### Speaker notes


42

## Slide 5

Java views each file as a sequential stream of bytes (Fig. 15.1).
Every operating system provides a mechanism to determine end of a file,
Such as an end-of-file marker or a count of the total bytes in the file that’s recorded in a system-maintained administrative data structure.
A Java program processing a stream of bytes simply receives an indication from the operating system when it reaches the end of the stream.
In some cases, the end-of-file indication occurs as an exception.
In others, the indication is a return value from a method invoked on a stream-processing object.
Files and Streams

### Speaker notes


56

## Slide 6

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Speaker notes


63

## Slide 7

A Java program opens a file by creating an object and associating a stream of bytes or characters with it.
The object’s constructor interacts with the operating system to open the file.
Java can also associate streams with different devices.
When a Java program begins executing, it creates three stream objects that are associated with devices—System.in, System.out and System.err.
The System.in (standard input stream) object normally enables a program to input bytes from the keyboard.
The System.out (standard output stream) object normally enables a program to output character data to the screen.
Standard Input, Standard Output and Standard Error Streams

### Speaker notes


71

## Slide 8

The System.err (standard error stream) object normally enables a program to output character-based error messages to the screen.
Each stream can be redirected.
For System.in, this capability enables the program to read bytes from a different source.
For System.out and System.err, it enables the output to be sent to a different location, such as a file on disk.
Class System provides methods setIn, setOut and setErr to redirect the standard input, output and error streams, respectively.

Standard Input, Standard Output and Standard Error Streams

### Speaker notes


96

## Slide 9

Java programs perform stream-based processing with classes and interfaces from package java.io and the subpackages of java.nio—Java’s New I/O APIs
Java’s New I/O APIs were first introduced in Java SE 6.
There are also other packages throughout the Java APIs containing classes and interfaces based on those in the java.io and java.nio packages.
Character-based input and output can be performed with classes Scanner and Formatter.
You’ve used class Scanner extensively to input data from the keyboard.
Scanner also can read data from a file.
The java.io and java.nio Packages

## Slide 10

Class Formatter enables formatted data to be output to any text-based stream in a manner similar to method System.out.printf.
Appendix I presents the details of formatted output with printf.
All these features can be used to format text files as well.
The java.io and java.nio Packages Cont.

## Slide 11

Java contains a package named java.io that is designed to handle file input and output procedures.
The package can be made available to a program by including an import statement at the very beginning of the .java file.
This can use the * wildcard character to mean “all classes” in the statement import java.io.* ; .
The java.io package has a class named “File” that can be used to access files or complete directories.
A File object must first be created using the new keyword and specifying the filename, or directory name, as the constructor’s argument.
Handling files .

## Slide 12

For example, the syntax to create a File object named “info” to represent a local file named “info.txt” looks like this:
File info = new File( “info.txt” ) ;
This file would be located in the same directory as the program, but the argument could state the path to a file located elsewhere.
Note that the creation of a File object does not actually create a file, but merely the means to represent a file.
Once a File object has been created to represent a file, its methods can be called to manipulate the file.
The most useful File object methods are listed in this table, together with a brief description:
Handling files Cont.

## Slide 13

The filename specified as the constructor argument must be enclosed within quotes.
The most useful File object methods are listed in this table, together with a brief description:
Handling files Cont.

## Slide 14

Handling files. EXAMPLE

## Slide 15

Handling files. EXAMPLE- OUTPUT

## Slide 16

import java.io.* ;class ListFiles{   public static void main( String[] args )   {      File dir = new File( "data" ) ;      if( dir.exists() )      {         String[] files = dir.list() ;         System.out.println( files.length + " files found..." );         for( int i = 0; i < files.length; i++ )         {            System.out.println( files[i] ) ;         }      }      else      {         System.out.println( "Folder not found." ) ;
      }     }  }
C:\Users\foderanti\OneDrive - Liberty University

## Slide 17

5.8  Java API Packages REVISITED
Java contains many predefined classes that are grouped into categories of related classes called packages
Classes relevant for processing files and directories and their methods are in Java.io and Java.nio package
https://docs.oracle.com/javase/7/docs/api/java/io/package-summary.html
  Overview of the packages in Java
http://docs.oracle.com/javase/7/docs/api/overview-summary.html
Additional information about a predefined Java class’s methods
http://docs.oracle.com/javase/7/docs/api/
Index link shows alphabetical list of all the classes and methods in the Java API
Locate the class name and click its link to see the online description of the class
METHOD link shows a table of the class’s methods
Each static method will be listed with the word “static” preceding its return type.

## Slide 18

Midterm Exam

## Slide 19

The java.io package contains a class named FileReader that is especially designed to read text files.
This class is a subclass of the InputStreamReader class
This can be used to read console input by converting a byte stream into integers that represent Unicode character values.
A FileReader object is created using the new keyword, and takes the name of the file to be read as its argument.
Optionally, the argument can include the full path to a file outside the directory where the program is located.
Handling files: Reading files.

## Slide 20

In order to efficiently read the text file line-by-line, the readLine() method of a BufferedReader object can be employed to read the characters decoded by the FileReader object.
This method must be called from within a try catch statement to catch any IOException problems that may arise.
Reading all lines in a text file containing multiple lines of text is accomplished by making repeated calls to the readLine() method in a loop.
At the end of the file the call will return a null value, which can be used to terminate the loop.
Handling files: Reading files Cont.

## Slide 21

Reading files: CLASS ACTIVITIES

## Slide 22

Reading files: CLASS ACTIVITIES Cont.

## Slide 23

Reading files: CLASS ACTIVITIES- OUTPUT

## Slide 24

Reading files: CLASS ACTIVITIES- SOLUTION
import java.io.* ;class ReadFile{   public static void main( String[] args )    {      try      {         FileReader file = new FileReader( "Oscar.txt" ) ;         BufferedReader buffer = new BufferedReader( file );         String line = "" ;         while( ( line = buffer.readLine() ) != null )         {            System.out.println( line ) ;         }         buffer.close() ;      }      catch( IOException e )      {         System.out.println( "A read error has occurred." ) ;      }    }   }
I never saw a man who looked
  With such a wistful eye
Upon that little tent of blue
  Which prisoners call the sky,
And at every drifting cloud that went
  With sails of silver by.
C:\Users\foderanti\OneDrive - Liberty University

## Slide 25

In the java.io package the FileReader and BufferedReader classes, which are used to read text files, have counterparts named FileWriter and BufferedWriter that can be used to write text files.
A FileWriter object is created using the new keyword, and takes the name of the file to be written as its argument.
Optionally, the argument can include the full path to a file to be written in a directory outside that in which the program is located.
The BufferedWriter object is created with the new keyword, and takes the name of the FileWriter object as its argument.
Writing files

## Slide 26

Text can then be written with the write() method of the BufferedWriter object, and lines separated by calling its newLine() method.
These methods should be called from within a try catch statement to catch any IOException problems that may arise.
If a file of the specified name already exists, its contents will be overwritten by the write() method, otherwise a new file of that name will be created and its contents written.
You can call the append() method of the BufferedWriter object to add text – rather than overwriting text with the write() method.
Writing files  Cont.

## Slide 27

Writing files: CLASS ACTIVITIES

## Slide 28

Writing files: CLASS ACTIVITIES Cont.

## Slide 29

Writing files: CLASS ACTIVITIES- OUTPUT

## Slide 30

Writing files: CLASS ACTIVITIES- SOLUTION
import java.io.* ;class WriteFile   {   public static void main( String[] args )     {      try        {           FileWriter file = new FileWriter( "Tam.txt" );         BufferedWriter buffer = new BufferedWriter( file );         buffer.write("The wind blew as if it had blown its last");            buffer.newLine();         buffer.write("The rattling showers rose on its blast");            buffer.newLine();         buffer.write("The speedy gleams the darkness swallowed");            buffer.newLine();         buffer.write("Loud, deep and long the thunder bellowed");            buffer.newLine();         buffer.write("That night a child might understand");            buffer.newLine();         buffer.write("The devil had business on his hand.");         buffer.close();        }      catch( IOException e )       {            System.out.println( "A write error has occurred." );      }       }     }

## Slide 31

You can call the append() method of the BufferedWriter object to add text – rather than overwriting text with the write() method.
Appending text.

## Slide 32

Interfaces Path and DirectoryStream and classes Paths and Files (all from package java.nio.file) are also useful for retrieving information about files and directories on disk:
Path interface—Objects of classes that implement Path represent the location of a file or directory.
Path objects do not open files or provide any file-processing capabilities.
Class File (package java.io) also is used commonly for this purpose.
Paths class—Provides static methods used to get a Path object representing a file or directory location.
Using NIO Classes and Interfaces to Get File and Directory Information

## Slide 33

Files class—Provides static methods for common file and directory manipulations, such as copying files; creating and deleting files and directories; getting information about files and directories; reading the contents of files; getting objects that allow you to manipulate the contents of files and directories; and more.
DirectoryStream interface—Objects of classes that implement this interface enable a program to iterate through the contents of a directory.
Using NIO Classes and Interfaces to Get File and Directory Information Cont.

## Slide 34

You’ll use class static method get of class Paths to convert a String representing a file’s or directory’s location into a Path object.
You can then use the methods of interface Path and class Files to determine information about the specified file or directory.
We discuss some of such methods momentarily.
For complete lists of their methods, visit:
http://docs.oracle.com/javase/8/docs/api/java/nio/file/Path.html  http://docs.oracle.com/javase/8/docs/api/java/nio/file/Files.html
Creating Path Objects

## Slide 35

A file or directory’s path specifies its location on disk.
The path includes some or all of the directories leading to the file or directory.
An absolute path contains all directories, starting with the root directory, that lead to a specific file or directory.
Every file or directory on a particular disk drive has the same root directory in its path.
A relative path is “relative” to another directory—for example, a path relative to the directory in which the application began executing.
Absolute vs. Relative Paths

## Slide 36

An overloaded version of Files static method get uses a URI object to locate the file or directory.
A Uniform Resource Identifier (URI) is a more general form of the Uniform Resource Locators (URLs) that are used to locate websites.
For example, the URL http://www.Liberty.edu/  is the URL for the Liberty University website.
URIs for locating files vary across operating systems.
On Windows platforms, the URI: file://C:/data.txt
identifies the file data.txt stored in the root directory of the C: drive.
On UNIX/Linux platforms, the URI: file:/home/student/data.txt
identifies the file data.txt stored in the home directory of the user student.

Getting Path Objects from URIs

## Slide 37

Figure 15.2 prompts the user to enter a file or directory name, then uses classes Paths, Path, Files and DirectoryStream to output information about that file or directory.
Example: Getting File and Directory Information

## Slide 38

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 39

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 40

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.
C:\Users\foderanti\OneDrive - Liberty University

## Slide 41

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.
C:\Users\foderanti\OneDrive - Liberty University

## Slide 42

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.
C:\Users\foderanti\OneDrive - Liberty University

## Slide 43

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.
// Fig. 15.2: FileAndDirectoryInfo.java// File class used to obtain file and directory information.import java.io.IOException;import java.nio.file.DirectoryStream;import java.nio.file.Files;import java.nio.file.Path;import java.nio.file.Paths;import java.util.Scanner;public class FileAndDirectoryInfo{   public static void main(String[] args) throws IOException   {      Scanner input = new Scanner(System.in);      System.out.println("Enter file or directory name:");      // create Path object based on user input      Path path = Paths.get(input.nextLine());      if (Files.exists(path)) // if path exists, output info about it      {         // display file (or directory) information       System.out.printf("%n%s exists%n", path.getFileName());       System.out.printf("%s a directory%n",           Files.isDirectory(path) ? "Is" : "Is not");       System.out.printf("%s an absolute path%n",           path.isAbsolute() ? "Is" : "Is not");       System.out.printf("Last modified: %s%n",           Files.getLastModifiedTime(path));       System.out.printf("Size: %s%n", Files.size(path));       System.out.printf("Path: %s%n", path);       System.out.printf("Absolute path: %s%n", path.toAbsolutePath());         if (Files.isDirectory(path)) // output directory listing         {            System.out.printf("%nDirectory contents:%n");                        // object for iterating through a directory's contents            DirectoryStream<Path> directoryStream =                Files.newDirectoryStream(path);               for (Path p : directoryStream)               System.out.println(p);         }       }       else // not file or directory, output error message      {         System.out.printf("%s does not exist%n", path);      }      }} // end class FileAndDirectoryInfo

## Slide 44

The program begins by prompting the user for a file or directory (line 14).
Line 17 inputs the filename or directory name and passes it to Paths static method get, which converts the String to a Path.
Line 19 invokes Files static method exists, which receives a Path and determines whether it exists (either as a file or as a directory) on disk.
If the name does not exist, control proceeds to line 45, which displays a message containing the Path’s String representation followed by “does not exist.”
Otherwise, lines 21–42 execute the statements in it:
Example explained Cont.

## Slide 45

Otherwise, lines 21–42 execute the:
Path method getFileName (line 21) gets the String name of the file or directory without any location information.
Files static method isDirectory (line 23) receives a Path and returns a boolean indicating whether that Path represents a directory on disk.
Path method isAbsolute (line 25) returns a boolean indicating whether that Path represents an absolute path to a file or directory.
Files static method getLastModifiedTime (line 27) receives a Path and returns a FileTime (package java.nio.file.attribute) indicating when the file was last modified.
The program outputs the FileTime’s default String representation.
Example explained Cont.

## Slide 46

Otherwise, lines 21–42 execute the (CONTINUED):
Files static method size (line 28) receives a Path and returns a long representing the number of bytes in the file or directory.
For directories, the value returned is platform specific.
Path method toString (called implicitly at line 29) returns a String representing the Path.
Path method toAbsolutePath (line 30) converts the Path on which it’s called to an absolute path.
Example explained Cont

## Slide 47

If the Path represents a directory (line 32), lines 36–37 use Files static method newDirectoryStream to get a DirectoryStream containing Path objects for the directory’s contents.
Lines 39–41 display the String representation of each Path in the DirectoryStream.
Example explained Cont

## Slide 48



## Slide 49

A separator character is used to separate directories and files in a path.
On a Windows computer, the separator character is a backslash (\).
On a Linux or macOS system, it’s a forward slash (/).
Java processes both characters identically in a pathname.
For example, if we were to use the path:
c:\Program Files\Java\jdk1.6.0_11\demo/jfc
which employs each separator character, Java would still process the path properly.

Separator Characters

## Slide 50

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 51

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 52

The illustration in this section creates a simple sequential file that might be used in an accounts receivable system to keep track of the amounts owed to a company by its credit clients.
For each client, the program obtains from the user an account number and the client’s name and balance (i.e., the amount the client owes the company for goods and services received).
Each client’s data constitutes a “record” for that client.
This application uses the account number as the record key—the file’s records will be created and maintained in account-number order.
The program assumes that the user enters the records in account-number order.
In a comprehensive accounts receivable system (based on sequential files), a sorting capability would be provided so that the user could enter the records in any order.
The records would then be sorted and written to the file.
Creating a Sequential Text File

## Slide 53

Class CreateTextFile (Fig. 15.3) uses a Formatter to output formatted Strings, using the same formatting capabilities as method System.out.printf.
A Formatter object can output to various locations, such as to a command window or to a file, as we do in this example.
The Formatter object is instantiated in the try-with-resources statement (line 13)—
try-with-resources will close its resource(s) when the try block terminates successfully or due to an exception.
Creating a Sequential Text File: EXAMPLE: Class CreateTextFile

## Slide 54

The constructor we use here takes one argument—a String containing the name of the file, including its path.
If a path is not specified, as is the case here, the JVM assumes that the file is in the directory from which the program was executed.
For text files, we use the .txt file extension.
If the file does not exist, it will be created.
If an existing file is opened, its contents are truncated—all the data in the file is discarded.
If no exception occurs, the file is open for writing and the resulting Formatter object can be used to write data to the file.
Creating a Sequential Text File: EXAMPLE: Class CreateTextFile

## Slide 55



## Slide 56



## Slide 57



## Slide 58

// Fig. 15.3: CreateTextFile.java// Writing data to a sequential text file with class Formatter.import java.io.FileNotFoundException;     import java.lang.SecurityException;       import java.util.Formatter;               import java.util.FormatterClosedException;import java.util.NoSuchElementException;  import java.util.Scanner;                 public class CreateTextFile {   public static void main(String[] args) {      Scanner input = new Scanner(System.in);      System.out.printf("%s%n%s%n? ",          "Enter account number, first name, last name and balance.",         "Enter end-of-file indicator to end input.");      // open clients.txt, output data to the file then close clients.txt      try (Formatter output = new Formatter("clients.txt")) {         while (input.hasNext()) { // loop until end-of-file indicator            try {               // output new record to file; assumes valid input               output.format("%d %s %s %.2f%n", input.nextInt(),                    input.next(), input.next(), input.nextDouble());              }             catch (NoSuchElementException elementException) {               System.err.println("Invalid input. Please try again.");               input.nextLine(); // discard input so user can try again            }             System.out.print("? ");            }           }      catch (SecurityException | FileNotFoundException |          FormatterClosedException e) {         e.printStackTrace();         System.exit(1); // terminate the program      }      }    }

## Slide 59

Lines 33–36 are a multi-catch which handles several exceptions:
the SecurityException that occurs if the user does not have permission to write data to the file opened in line 13
the FileNotFoundException that occurs if the file does not exist and a new file cannot be created, or if there’s an error opening the file in line 13,
the FormatterClosedException that occurs if the Formatter object is closed when you attempt to use it in lines 22–23 to write into a file.
Class CreateTextFile: EXAMPLE: Explained

## Slide 60

Lines 15–17 prompt the user to enter the various fields for each record or the end-of-file key sequence when data entry is complete.
Figure 15.4 lists the key combinations for entering end-of-file for various computer systems’ command windows—
Some IDEs do not support these for console-based input (so you might have to execute the programs from command windows).
Line 19 uses Scanner method hasNext to determine whether the end-of-file key combination has been entered.
The loop executes until hasNext encounters end-of-file.
EXAMPLE: Explained- Writing Data to the File

## Slide 61

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 62

Lines 22–23 use a Scanner to read data from the user, then output the data as a record using the Formatter.
Each Scanner input method throws a NoSuchElementException (handled in lines 25–28) if the data is in the wrong format
If no exception occurs, the record’s information is output using method format, which can perform identical formatting to System.out.printf.
Method format writes a formatted String to the Formatter object’s output destination—the file clients.txt.
The format string "%d %s %s %.2f%n“ indicates how the current record will be stored
The data in the text file can be viewed with a text editor or retrieved later by a program designed to read the file.
More info here: https://docs.oracle.com/javase/7/docs/api/java/util/Formatter.html
EXAMPLE: Explained- Writing Data to the File

## Slide 63



## Slide 64

Data is stored in files so that it may be retrieved for processing when needed.
We had demonstrated how to create a file for sequential access.
This section shows how to read data sequentially from a text file.
We demonstrate how class Scanner can be used to input data from a file rather than the keyboard.
The application (Fig. 15.6) reads records from the file "clients.txt" created by the application of Fig. 15.3 and displays the record’s contents.
Line 14 creates the Scanner that will be used to retrieve input from the file.
Reading Data from a Sequential Text File

## Slide 65

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 66



## Slide 67

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.
// Fig. 15.6: ReadTextFile.java// This program reads a text file and displays each record.import java.io.IOException;import java.lang.IllegalStateException;import java.nio.file.Files;import java.nio.file.Path;import java.nio.file.Paths;import java.util.NoSuchElementException;import java.util.Scanner;public class ReadTextFile {   public static void main(String[] args) {      // open clients.txt, read its contents and close the file      try(Scanner input = new Scanner(Paths.get("clients.txt"))) {         System.out.printf("%-10s%-12s%-12s%10s%n", "Account",            "First Name", "Last Name", "Balance");         // read record from file         while (input.hasNext()) { // while there is more to read            // display record contents                                 System.out.printf("%-10d%-12s%-12s%10.2f%n", input.nextInt(),               input.next(), input.next(), input.nextDouble());                   }            }       catch (IOException | NoSuchElementException |          IllegalStateException e) {         e.printStackTrace();      }     }  }

## Slide 68

Java provides a mechanism, called object serialization
It enables an object to be represented as a sequence of bytes that includes the object's data as well as information about the object's type and the types of data stored in the object.
After a serialized object has been written into a file, it can be read from the file and deserialized
That is, the type information and bytes that represent the object and its data can be used to recreate the object in memory.

Java - Serialization

## Slide 69

To serialize an object means to convert its state to a byte stream so that the byte stream can be reverted back into a copy of the object.
A Java object is serializable if its class or any of its superclasses implements either the java.io.Serializable interface or its subinterface, java.io.Externalizable.
Deserialization is the process of converting the serialized form of an object back into a copy of the object.
The Java platform specifies a default way by which serializable objects are serialized.
Java – Serialization Cont.

## Slide 70

When an object is serialized, information that identifies its class is recorded in the serialized stream.
However, the class's definition ("class file") itself is not recorded.
It is the responsibility of the system that is deserializing the object to determine how to locate and load the necessary class files.
For example, a Java application might include in its classpath a JAR file that contains the class files of the serialized object(s) or load the class definitions by using information stored in the directory.
Java - Serialization

## Slide 71

Most impressive is that the entire process is JVM independent,
Meaning an object can be serialized on one platform and deserialized on an entirely different platform.
Classes ObjectInputStream and ObjectOutputStream are high-level streams that contain the methods for serializing and deserializing an object.
The ObjectOutputStream class contains many write methods for writing various data types, but one method in particular stands out −

The above method serializes an Object and sends it to the output stream.
The writeObject method is responsible for writing the state of the object
so that the corresponding readObject method can restore it.
Java - Serialization
public final void writeObject(Object x) throws IOException

## Slide 72

Similarly, the ObjectInputStream class contains the following method for deserializing an object −


This method retrieves the next Object out of the stream and deserializes it.
Return value is Object, so you will need to cast it to its appropriate data type.
To demonstrate how serialization works in Java, let us use Employee class that we discussed early.
Suppose that we have the following Employee class, which implements the Serializable interface −


Java - Serialization
public final Object readObject() throws IOException, ClassNotFoundException

## Slide 73

public class Employee implements java.io.Serializable {    public String name;    public String address;    public transient int SSN;    public int number;    public void mailCheck() {        System.out.println("Mailing a check to " + name + " " + address);    }}

## Slide 74

The ObjectOutputStream class is used to serialize an Object.
The following SerializeDemo program instantiates an Employee object and serializes it to a file.
When the program is done executing, a file named employee.ser is created.
The program does not generate any output, but study the code and try to determine what the program is doing.
Note − When serializing an object to a file, the standard convention in Java is to give the file a .ser extension.
Serializing an Object

## Slide 75

import java.io.*;public class SerializeDemo {    public static void main(String [] args) {        Employee e = new Employee();        e.name = "Reyan Ali";        e.address = "Phokka Kuan, Ambehta Peer";        e.SSN = 11122333;        e.number = 101;        try {            FileOutputStream fileOut =                    new FileOutputStream("/tmp/employee.ser");            ObjectOutputStream out = new ObjectOutputStream(fileOut);            out.writeObject(e);            out.close();            fileOut.close();            System.out.printf("Serialized data is saved in /tmp/employee.ser");        } catch (IOException i) {            i.printStackTrace();        }       }  }

## Slide 76

The following DeserializeDemo program deserializes the Employee object created in the SerializeDemo program.
Study the program and try to determine its output −
Deserializing an Object

## Slide 77

import java.io.*;public class DeserializeDemo {    public static void main(String [] args) {        Employee e = null;        try {            FileInputStream fileIn = new FileInputStream("/tmp/employee.ser");            ObjectInputStream in = new ObjectInputStream(fileIn);            e = (Employee) in.readObject();            in.close();            fileIn.close();        } catch (IOException i) {            i.printStackTrace();            return;        } catch (ClassNotFoundException c) {            System.out.println("Employee class not found");            c.printStackTrace();            return;        }        System.out.println("Deserialized Employee...");        System.out.println("Name: " + e.name);        System.out.println("Address: " + e.address);        System.out.println("SSN: " + e.SSN);        System.out.println("Number: " + e.number);    }  }

## Slide 78

This will produce the following result −
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.
Deserialized Employee...
Name: Reyan Ali Address:Phokka Kuan, Ambehta Peer SSN: 0
Number:101

## Slide 79

In the last lecture, we demonstrated how to write the individual fields of a record into a file as text, and how to read those fields from a file.
Sometimes we want to write an entire object to or read an entire object from a file.
XML is another format commonly used to represent objects.
We could manipulate objects using JAXB (Java Architecture for XML Binding).
JAXB enables you to perform XML serialization—which JAXB refers to as marshaling.
A serialized object is represented by XML that includes the object’s data.
After a serialized object has been written into a file, it can be read from the file and deserialized—
That is, the XML that represents the object and its data can be used to recreate the object in memory.
XML Serialization

## Slide 80

The serialization we show in this section is performed with character-based streams, so the result will be a text file that you can view in standard text editors.
We begin by creating and writing serialized objects to a file.
Creating a Sequential File Using XML Serialization

## Slide 81

We begin by defining class Account (Fig. 15.9), which encapsulates the client record information used by the serialization examples.
Class Account contains private instance variables account, firstName, lastName and balance (lines 4–7) and set and get methods for accessing these instance variables.
Declaring Class Account

## Slide 82

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 83

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 84

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 85

As you’ll see in Fig. 15.11, this example stores Account objects in a List, then serializes the entire List into a file with one operation.
To serialize a List, it must be defined as an instance variable of a class.
For that reason, we encapsulate the List in class Accounts (Fig. 15.10).
Fig. 15.9 = Account.java
Fig. 15.10 = Accounts.java
Declaring Class Accounts

## Slide 86

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 87

Lines 9–10 declare and initialize the List instance variable accounts.
JAXB enables you to customize many aspects of XML serialization, such as serializing a private instance variable or a read-only property.
The annotation @XMLElement (line 9; package javax.xml.bind.annotation) indicates that the private instance variable should be serialized.
The annotation is required because the instance variable is not public and there’s no corresponding public read–write property.
Writing XML Serialized Objects to a File.

## Slide 88

The program of Fig. 15.11 serializes an Accounts object to a text file.
The program is similar to the one we have discussed earlier, so we focus only on the new features.
Line 9 imports the JAXB class from package javax.xml.bind.
This package contains many related classes that implement the XML serializations we perform,
But the JAXB class contains easy-to-use static methods that perform the most common operations.
Writing XML Serialized Objects to a File

## Slide 89

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 90

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 91

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 92

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 93

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 94

To open the file, lines 14–15 call Files static method newBufferedWriter,
This receives a Path specifying the file to open for writing ("clients.xml") and—if the file exists—returns a BufferedWriter that class JAXB will use to write text to the file.
Line 20 creates the Accounts object that contains the List.
Lines 26–41 input each record, create an Account object (lines 29–30) and add to the List (line 33).
Writing XML Serialized Objects . Cont.

## Slide 95

When the user enters the end-of-file indicator to terminate input, line 44 uses class JAXB’s static method marshal to serialize as XML the Accounts object containing the List.
The first argument is the object to serialize.
The second argument to this particular overload of method marshal is a Writer (package java.io) that’s used to output the XML—BufferedWriter is a subclass of Writer.
The BufferedWriter obtained in lines 14–15 outputs the XML to a file.
Note that only one statement is required to write the entire Accounts object and all of the objects in its List.
In the sample execution for the program in Fig. 15.11, we entered information for five accounts—the same information shown in Fig. 15.5.
Writing XML Serialized Objects . Cont.

## Slide 96

The preceding section showed how to create a file containing XML serialized objects.
In this section, we show how to read serialized data from a file.
Figure 15.13 reads objects from the file created by the program in Section 15.5.1, then displays the contents.
The program opens the file for input by calling Files static method newBufferedReader, which receives a Path specifying the file to open
and, if the file exists and no exceptions occur, returns a BufferedReader for reading from the file.
Reading and Deserializing Data from a Sequential File

## Slide 97

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 98

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.
