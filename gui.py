from tkinter import *  #Tkinter is needed to give me the tools to create my GUI.
from tkinter import messagebox

history = [] #This will store every equation into a list

def handle_button_press(value): #This is gonna add text to my entry box.
    entry.insert(END, value) #This will insert the pressed button.

def handle_equals():
    try:
        expression = entry.get() #This finds whatever the user types into the box.
        result = str(eval(expression)) #Turns it into a string

        history.append(f"{expression} = {result}") #Saves the equation into the history list.

        entry.delete(0, END) #Clears the entry box
        entry.insert(END, result) #Shows the result in the entry box.

    except Exception:
        messagebox.showerror("Error", "Invalid expression") #Shows an error popup
        entry.delete(0, END) #This will clear the entry box
root = Tk()
root.title("Calculator")
root.geometry("300x500")   #This will give it a title and dimensions.

entry = Entry(root, font=("Arial", 24))
entry.grid(row=0, column=0, columnspan=4) #These 2 lines will make the entry box where everything will appear.



Button(root, text="7", width=5, height=2).grid(row=1, column=0) #This will put the number 7, and it's button, in row one at the base column. It gives it dimensions too.
Button(root, text="8", width=5, height=2).grid(row=1, column=1)
Button(root, text="9", width=5, height=2).grid(row=1, column=2)
Button(root, text="/", width=5, height=2).grid(row=1, column=3)

Button(root, text="4", width=5, height=2).grid(row=2, column=0)
Button(root, text="5", width=5, height=2).grid(row=2, column=1)
Button(root, text="6", width=5, height=2).grid(row=2, column=2)
Button(root, text="*", width=5, height=2).grid(row=2, column=3)

Button(root, text="1", width=5, height=2).grid(row=3, column=0)
Button(root, text="2", width=5, height=2).grid(row=3, column=1)
Button(root, text="3", width=5, height=2).grid(row=3, column=2)
Button(root, text="-", width=5, height=2).grid(row=3, column=3)

Button(root, text="0", width=5, height=2).grid(row=4, column=0)
Button(root, text="=", width=5, height=2).grid(row=4, column=1)
Button(root, text="+", width=5, height=2).grid(row=4, column=3)

#Basically what all of those are doing is alligning the numbers and operations(remembered the word finally). I did have to look up how to allign them properly, but once I got one, the rest were pretty easy to do.The first GUI lab we did was helpful for this part.
root.mainloop()
