# JHTP11_12 UPDATED-212 -2022- Givingthanks (1).pptx

## Slide 1

LET US PRAY!
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Speaker notes


2

## Slide 2

Chapter 12JavaFX Graphical User Interfaces: Part 1
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

### Speaker notes

Organizational Network Analysis


5

## Slide 3

 Giving Thanks to God (Psalm 100)
1.Make a joyful noise unto the Lord, all ye lands.
2 Serve the Lord with gladness: come before his presence with singing.
3 Know ye that the Lord he is God: it is he that hath made us, and not we ourselves; we are his people, and the sheep of his pasture.
4 Enter into his gates with thanksgiving, and into his courts with praise: be thankful unto him, and bless his name.
5 For the Lord is good; his mercy is everlasting; and his truth endureth to all generations.

3

### Speaker notes

https://www.youtube.com/watch?v=Z1W4E2d4Yxo
30

## Slide 4

 Giving Thanks to God: Paul and Silas in Prison (Acts 16:16-40))
4

## Slide 5

EXAMPLES OF JESUS GIVING THNAKS
41 So they took away the stone. Then Jesus looked up and said:
 “Father, I thank you that you have heard me. 42 I knew that you always hear me, but I said this for the benefit of the people standing here, that they may believe that you sent me.”

43 When he had said this, Jesus called in a loud voice, “Lazarus, come out!” 44


John 11:38-44
1 Corinthians 11:24and when He had given thanks, He broke it and said, "This is My body, which is for you; do this in remembrance of Me."
Luke 22:17After taking the cup, He gave thanks and said, "Take this and divide it among yourselves.

## Slide 6

 Giving Thanks to God (Revelation 4:11) Thou Art Worthy Oh Lord!
6
11 Thou art worthy, O Lord, to receive glory and honour and power: for thou hast created all things, and for thy pleasure they are and were created.

Other psalms for Thanksgiving: Psalm 34, Psalm  111, Psalm 95,  Psalm 44: 4-8, Psalm 92,  Rev 4, etc.

## Slide 7

 Giving Thanks to God (Revelation 4:11) Thou Art Worthy Oh Lord!
7

## Slide 8

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 9

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 10

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 11

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 12

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 13

This is an in-class Exam
The Final Exam
Covers the Chapters 1 - 11 from the textbook.
Contains 100 multiple-choice and true/false questions.
Is limited to 2 hours].
Is worth 150 points.

This exam is closed book and closed note. You have two hours to complete it at which time the exam will but submitted automatically. It consists of 100 true/false and multiple choice questions and is worth 150 points.

This is an in-class exam taken on the day of the final according to the final exam schedule.

## Slide 14

Course Evaluation
© 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part, except for use as permitted in a license distributed with a certain product or service or otherwise on a password-protected website for classroom use.
Time to complete the course evaluation

## Slide 15

JavaFX is easier to use—it provides one API for client functionality, including GUI, graphics and multimedia (images, animation, audio and video).
Swing is only for GUIs, so you need to use other APIs for graphics and multimedia apps.
With Swing, many IDEs provided GUI design tools for dragging and dropping components onto a layout; however, each IDE produced different code.
Though Swing components could be customized, JavaFX gives you complete control over a JavaFX GUI’s look-and-feel.
JavaFX is easier to use

## Slide 16

Most Java textbooks that introduce GUI programming provide hand-coded GUIs—that is, the authors build the GUIs from scratch in Java code, rather than using a visual GUI design tool.
This is due to the fractured Java IDE market—there are many Java IDEs, so authors can’t depend on any one IDE being used, and each generates different code.
JavaFX is organized differently.
The Scene Builder tool is a standalone JavaFX GUI visual layout tool that can also be used with various IDEs, including the most popular ones—Eclipse, IntelliJ IDEA and NetBeans.
You can download Scene Builder at:
http://gluonhq.com/labs/scene-builder/
JavaFX Scene Builder

## Slide 17

JavaFX Scene Builder enables you to create GUIs by dragging and dropping GUI components from Scene Builder’s library onto a design area,
Then modifying and styling the GUI—all without writing any code.
JavaFX Scene Builder’s live editing and preview features allow you to view your GUI as you create and modify it, without compiling and running the app.
You can use Cascading Style Sheets (CSS) to change the entire look-and-feel of your GUI—a concept sometimes called skinning.
JavaFX Scene Builder

## Slide 18

As you create and modify a GUI, JavaFX Scene Builder generates FXML (FX Markup Language)
—an XML vocabulary for defining and arranging JavaFX GUI controls without writing any Java code.
XML (eXtensible Markup Language) is a widely used language for describing things—it’s readable both by computers and by humans.
In JavaFX, FXML concisely describes GUI, graphics and multimedia elements.
You do not need to know FXML or XML to develop java GUI.
JavaFX Scene Builder hides the FXML details from you, so you can focus on defining what the GUI should contain without specifying how to generate it—this is an example of declarative programming.
FXML (FX Markup Language)

## Slide 19

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 20

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 21



## Slide 22

Swing has a large following, has a proven track record and a wide availability of 3rd party support.
The future is a difficult thing to predict and is always fluent.
There are still some companies using AWT (Abstract Window Toolkit).
Majority of existing GUI java codebases are Swing and likely will stay that way until the codebase rots and nobody maintains it anymore.

Is Swing Still in Use Today?

## Slide 23

Majority of new GUI java codebases are using JavaFX, which is the Swing replacement in Java8 and is part of the standard java library now.
FXML can replace 3,000 lines of extended JFrame class code for a Swing GUI, with 50 lines of FXML.
Swing is still used heavily, and will continue to be for a long while
Swing was the only choice for Java for a loooong time.
JavaFX, however, is refreshingly nice, and very-much-so worth learning.
Is Swing Still in Use Today? Cont,

## Slide 24

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.
import javax.swing.*;class TextFields extends JFrame {   JPanel pnl = new JPanel();   JTextField txt1 = new JTextField( 38 ) ;   JTextField txt2 = new JTextField( "Default Text", 38 ) ;      JTextArea txtArea = new JTextArea( 5, 37 ) ;      JScrollPane pane = new JScrollPane( txtArea ) ;   public TextFields()   {      super( "Swing Window" );      setSize( 500,200 );      setDefaultCloseOperation( EXIT_ON_CLOSE );      add(pnl);      txtArea.setLineWrap( true ) ;      txtArea.setWrapStyleWord( true ) ;      pane.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_ALWAYS);            pnl.add( txt1 ) ;      pnl.add( txt2 ) ;      pnl.add( pane ) ;      setVisible( true );   }   public static void main ( String[] args )   {      TextFields gui = new TextFields();   } }
Examples of Swing Coding
import javax.swing.* ;import java.awt.*;class Layout extends JFrame{   Container contentPane = getContentPane();   JPanel pnl = new JPanel();   JPanel grid = new JPanel(new GridLayout(2,2));   public Layout()   {      super( "Swing Window" );      setSize( 500,200 );      setDefaultCloseOperation( EXIT_ON_CLOSE );               pnl.add(new JButton("Yes") );           pnl.add(new JButton("No") );      pnl.add(new JButton("Cancel") );           grid.add(new JButton("1"));           grid.add(new JButton("2"));           grid.add(new JButton("3"));           grid.add(new JButton("4"));       contentPane.add("North", pnl );           contentPane.add("Center", grid );           contentPane.add("West",new JButton("West"));       setVisible( true );   }      public static void main( String[] args )    {      Layout gui = new Layout() ;   }  }
import javax.swing.*;class Window extends JFrame {   JPanel pnl = new JPanel();      public Window()   {      super("Swing Window");      setSize( 500,200 );      setDefaultCloseOperation( EXIT_ON_CLOSE );      add(pnl);      setVisible( true );   }   public static void main ( String[] args )   {      Window gui = new Window();   }

## Slide 25

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.
Examples of Swing Coding
import javax.swing.*;class Radios extends JFrame {   JPanel pnl = new JPanel();      JRadioButton rad1 = new JRadioButton( "Red", true ) ;   JRadioButton rad2 = new JRadioButton( "Ros�" ) ;   JRadioButton rad3 = new JRadioButton( "White" ) ;   ButtonGroup wines = new ButtonGroup() ;       public Radios()   {      super( "Swing Window" );      setSize( 500,200 );      setDefaultCloseOperation( EXIT_ON_CLOSE );      add(pnl);      wines.add( rad1 ) ;      wines.add( rad2 ) ;      wines.add( rad3 ) ;      pnl.add( rad1 ) ;      pnl.add( rad2 ) ;      pnl.add( rad3 ) ;      setVisible( true );   }   public static void main ( String[] args )   {      Radios gui = new Radios();   }  }
import javax.swing.*;class Buttons extends JFrame {   JPanel pnl = new JPanel();   ClassLoader ldr = this.getClass().getClassLoader();   java.net.URL tickURL = ldr.getResource("Tick.png");   java.net.URL crossURL = ldr.getResource("Cross.png");   //ImageIcon tick = new ImageIcon( tickURL );  // ImageIcon cross = new ImageIcon( crossURL );   ImageIcon tick = new ImageIcon( "tick.png" );   ImageIcon cross = new ImageIcon( "cross.png" );   JButton btn = new JButton( "Click Me" );   JButton tickBtn = new JButton( tick );   JButton crossBtn = new JButton( "STOP", cross );      public Buttons()   {      super("Swing Window");      setSize( 500,200 );      setDefaultCloseOperation( EXIT_ON_CLOSE );      add(pnl);         pnl.add( btn );      pnl.add( tickBtn );      pnl.add( crossBtn );      setVisible( true );   }   public static void main ( String[] args )   {      Buttons gui = new Buttons();   } }

## Slide 26



## Slide 27

Controls
Controls are GUI components, such as Labels that display text, TextFields that enable a program to receive user input, Buttons that users click to initiate actions, and more.
Stage
 The window in which a JavaFX app’s GUI is displayed is known as the stage and is an instance of class Stage (package javafx.stage).
Scene
 The stage contains one active scene that defines the GUI as a scene graph—such as GUI controls, shapes, images, video, text and more
FXML (FX Markup Language)

## Slide 28

Nodes
Each visual element in the scene graph is a node—an instance of a subclass of Node (package javafx.scene).
With the exception of the first node in the scene graph—the root node—each node in the scene graph has one parent.
Nodes can have transforms (e.g., moving, rotating and scaling), opacity (whether a node is transparent, partially transparent or opaque), effects (e.g., drop shadows, blurs, reflection and lighting) and more.
Layout Containers Nodes that have children are typically layout containers that arrange their child nodes in the scene.
FXML (FX Markup Language)

## Slide 29

Event Handler and Controller Class
When the user interacts with a control, such as clicking a Button or typing text into a TextField, the control generates an event.
Programs can respond to these events—known as event handling—to specify what should happen when each user interaction occurs.
An event handler is a method that responds to a user interaction.
An FXML GUI’s event handlers are defined in a so-called controller class (as you’ll see in Section
FXML (FX Markup Language)

## Slide 30

JavaFX is easier to use (It is an art and design but not coding!)

## Slide 31

Java FX Scene Builder Excercises
If you have the recommended textbook, practice with many of the exercises including :
12.4 Welcome App—Displaying Text and an Image
12.5 Tip Calculator App—Introduction to Event Handling


## Slide 32

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 33

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 34

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 35

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 36

Java FX Scene Builder Excercises
If you have the recommended textbook, practice with many of the exercises including :
12.4 Welcome App—Displaying Text and an Image
12.5 Tip Calculator App—Introduction to Event Handling.
Ensure you practice THOROUGHLY

## Slide 37

Class Activities/Excercises
With Chapter 12 TipCalculator exercise, you will practice with that and include an extra row in the GridPane
Follow the exercise in 12.5 from beginning to the end to produce/draw your own TipCalculator GUI and generate your own FXML (DO NOT USE THE SAMPLE FROM CANVAS BUT DRAW/CREATE YOUR OWN FROM SCRATCH.
Reproduce the TopCalculator codes.
In the extra row you calculate tax of 10% of the actual price and add this to the amount and the tips.
The overall addition of amount + 10% tax of amount +  tip =  Total.


## Slide 38

Example of Class Activities/Excercises
© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 39

Java FX Scene Builder Excercises
EXTRA SLIDES FOR YOUR PRIVATE PRACTICE


## Slide 40

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 41

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 42

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 43

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 44

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 45

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 46

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 47

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 48

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 49

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 50

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 51

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 52

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 53

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 54

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 55

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 56

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 57

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 58

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 59

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 60

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.

## Slide 61

© Copyright 1992-2018 by Pearson Education, Inc. All Rights Reserved.
