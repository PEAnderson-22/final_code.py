Final Project
Author: Pinager Anderson
Class: Intermediate Programming
Teach: Sebastian Talamantes
Date Started: 5/4/26
Date Finished: 5/8/26

Overview:
    This project is a basic calculator built with Python and Tkinter.  
    The program creates a GUI that lets the user perform the four main math operations:
    - addition
    - subtraction
    - multiplication
    - division

The calculator displays the numbers the user clicks, solves the equation when = is pressed, and then stores every equation the user does in a history list.

Files Included:

    gui.py:
    This file has all the tkinter code that I used to build the calculator.  
    It includes:
    - the Entry box where numbers and answers appear  
    - all the buttons for the numbers and the formulas 
    - the functions that run when each button is pressed  
    - the equals function  
    - the history list that will store all your past equations.

    calc.py:
    This file has all the calculations for each operation, making sure the right one is done when the user presses it.
    It includes:
    - the calculations for each operation
    - ValueErrors for each operation

The Features:
    - GUI made using Tkinter
    - Buttons for all of the numbers, 0-9
    - Buttons for each operation, -,+,*, and /
    - A text box that displays the numbers and operations that the user clicks
    - error messages for when the user puts a non working thing in, like a letter
    - And a history list that will store each equation the user does.

How to run the Program:
    1. Python must be installed
    2. go to gui.py and run it, that will start the calculator.
    3. Use the buttons to type in numbers and operations, just like any calculator would work.
    4. Of course press the = button to make it display your solution.
