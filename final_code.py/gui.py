from tkinter import *  #Tkinter is needed to give me the tools to create my GUI.
from tkinter import messagebox #Allows the error message to appear, if the user does something wrong.

history = [] #This will store every equation into a list

#These will give each one of my buttons the ability to actually type the number or operation you press.
def press_7(): entry.insert(END, "7")
def press_8(): entry.insert(END, "8")
def press_9(): entry.insert(END, "9")  #END just means it's putting it at the end of the text box. That way when you press 2 buttons it does it in the correct order.
def press_div(): entry.insert(END, "/")

def press_4(): entry.insert(END, "4")
def press_5(): entry.insert(END, "5")
def press_6(): entry.insert(END, "6")
def press_mul(): entry.insert(END, "*")

def press_1(): entry.insert(END, "1")
def press_2(): entry.insert(END, "2")
def press_3(): entry.insert(END, "3")
def press_minus(): entry.insert(END, "-")

def press_0(): entry.insert(END, "0")
def press_plus(): entry.insert(END, "+")
#I did look up a way to condense all these so it didn't take up half the program. I didn't know you could keep it on the same line and it would still function correctly.
#Now my gui will actually display your numbers.

def handle_equals(): #This will define my equal button.
    try:
        expression = entry.get() #This finds whatever the user types into the box.
        result = str(eval(expression)) #Turns it into a string
        history.append(f"{expression} = {result}") #Saves the equation into the history list.
        entry.delete(0, END) #Clears the entry box
        entry.insert(END, result) #Shows the result in the entry box.
    except Exception:
        messagebox.showerror("Error", "Invalid expression") #Shows an error popup
        entry.delete(0, END) #This will clear the entry box


root = Tk() #This will create the window that shows the calculator
root.title("Calculator") #This will give it a title
root.geometry("300x500")   #This will give it dimensions.

entry = Entry(root, font=("Arial", 24)) 
entry.grid(row=0, column=0, columnspan=4) #These 2 lines will make the entry box where everything will appear, giving it dimensions and the font and size it will display everything in.



#This will put the numbers, and it's button, in it's corrrect row and column. It gives it dimensions too.
Button(root, text="7", width=5, height=2, command=press_7).grid(row=1, column=0)
Button(root, text="8", width=5, height=2, command=press_8).grid(row=1, column=1)
Button(root, text="9", width=5, height=2, command=press_9).grid(row=1, column=2)
Button(root, text="/", width=5, height=2, command=press_div).grid(row=1, column=3)

Button(root, text="4", width=5, height=2, command=press_4).grid(row=2, column=0)
Button(root, text="5", width=5, height=2, command=press_5).grid(row=2, column=1)
Button(root, text="6", width=5, height=2, command=press_6).grid(row=2, column=2)
Button(root, text="*", width=5, height=2, command=press_mul).grid(row=2, column=3)

Button(root, text="1", width=5, height=2, command=press_1).grid(row=3, column=0)
Button(root, text="2", width=5, height=2, command=press_2).grid(row=3, column=1)
Button(root, text="3", width=5, height=2, command=press_3).grid(row=3, column=2)
Button(root, text="-", width=5, height=2, command=press_minus).grid(row=3, column=3)

Button(root, text="0", width=5, height=2, command=press_0).grid(row=4, column=0)
Button(root, text="=", width=5, height=2, command=handle_equals).grid(row=4, column=2)
Button(root, text="+", width=5, height=2, command=press_plus).grid(row=4, column=3)
#Basically what all of those are doing is alligning the numbers and operations(remembered the word finally). I did have to look up how to allign them properly, but once I got one, the rest were pretty easy to do.The first GUI lab we did was helpful for this part.
root.mainloop() #This will keep the window open and keep it running until the user closes it.
