## A Very Simple Program

_Adapted from MIT's [open course](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/pages/syllabus/)
6-0001 - Introduction to Computer Science and programming in python, as
offered in 2016_

### Raising a number to a power and taking a logarithm

The goal of this programming exercise is to make sure your python and numpy installations
are correct, to get you more comfortable with using Spyder, and to begin using simple
elements of Python. Standard elements of a program include the ability to print out results
(using the print operation), the ability to read input from a user at the console (for
example using the input function), and the ability to store values in a variable, so that the
program can access that value as needed.

### Assignment:

Write a program that does the following in order:

1. Asks the user to enter a number “x”
2. Asks the user to enter a number “y”
3. Prints out number “x”, raised to the power “y”.
4. Prints out the log (base 2) of “x”.

Use Spyder to create your program, and save your code in a file named ‘ps0.py’.

An example
of an interaction with your program is shown below. The words printed in blue are ones the
computer should print, based on your commands, while the words in black are an example of
a user's input. The colors are simply here to help you distinguish the two components.

```
Enter number x: 2
Enter number y: 3
x**y = 8
log(x) = 1
```

Hints:

* To see how to use the print command, you may find it convenient to look at the
input and output of the Python Wikibook. This will show you how to use print
statements to print out values of variables.
* To see how to read input from a user's console into the Python environment, you
may find it convenient to look at the same section (see for example the input()
function)
* Reference the basic math section of the Python Wikibook to read more about
using basic mathematical operators in Python
* To take the logarithm of a variable, import either of the numpy or pylab
packages. You can then call either numpy.log2 or pylab.log2 to calculate the
logarithm. See the Getting Started document on importing packages and the
many Numpy examples online for more info. Googling the log2 function may
take you here, which has some helpful info.
* Remember that if you want to hold onto a value, you need to store it in a
variable (i.e., give it a name to which you can refer when you want that
value). You may find it convenient to look at the variables and strings section
of the Python Wikibook. (As you read through, remember that in Python 3.x
you should be using input() not raw\_input()). Take a look at the “Combining
Numbers and Strings” sub-section, because you will be working with numbers
and strings in this problem and will have to convert between the two using the
str() and int() functions.

