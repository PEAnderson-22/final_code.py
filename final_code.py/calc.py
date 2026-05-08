#This is where my formulas for each equation will go. The ValueErrors will also be included here.
class Calculator: #This creates a class
    def addition(self,a,b): #This will define the addition function
        if a <=0 or b<=0: #This is making it so the user can't use negative number, and I will put this on all of them.
            raise ValueError("Your number cannot be negative.") #This gives the user a message telling them they can't do a negative.
        return a+b #This just tells the code what to do if the user presses +
    #Each of the following lines does the same as the one above jsut with different operations.
    def subtraction(self,a,b):
        if a <=0 or b<=0:
            raise ValueError("Your number cannot be negative.")
        return a-b
    def multiply(self,a,b):
        if a <=0 or b<=0:
            raise ValueError("Your number cannot be negative.")
        return a*b
    def division(self,a,b):
        if a <=0 or b<=0:
            raise ValueError("Your number cannot be negative.")
        elif b == 0:
            raise ValueError("Can't divide by 0")#This will make it so the user will know that they can;t do that.
        return a/b
#What I have just done is add in all my formulas. These will take the numbers the user selects and do whichever one they choose.

if __name__=="__main__": #Runs this file only when it is opened directly
    c = Calculator() #Creates a Calculator object for testing
    print(c.addition(2, 3)) #This is just a small test to make sure it works.
    

