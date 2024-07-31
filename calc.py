#import all classes/functions from tkinter library
from tkinter import *

#create window object
root = Tk() #instance of the Tk class

#write the function that adds text to the entry field
i = 0
def get_number(num): #whenever button is clicked, it will be passed to the function
    global i #so we can access i outside of this function
    display.insert(i, num) # add to entry widget
    i += 1 #increment every time a button is clicked

#similar function for operations
def get_operand(operator):
    global i #this will keep track of the index regardless of number or operand input
    length = len(operator) #to handle operands over one length such as pi
    display.insert(i, operator) # add to entry widget
    i += length

#add an input field using grid method
display = Entry(root)
display.grid(row=1, columnspan = 6)


#add 9 buttons with nested for loop
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9] #get values from the array
#counter increases to dynamically render button numbers
counter = 0
for x in range(3):
    for y in range(3):
        button_text = numbers[counter]
        button = Button(root, text = button_text, width = 2, height = 2, command = lambda text = button_text: get_number(text))
        button.grid(row = x + 2, column = y) #add + 2 to row so it does not superimpose on entry field
        counter += 1
#outside of loop, create a zero button
button = Button(root, text = "0", width = 2, height = 2, command = lambda text = button_text: get_number(0)) #copy lambda func for our separate zero
button.grid(row = 5, column = 1)

#next add operations to the window add, subtract, multiply, division, pi, percentage, parenthesis, exponent, and square
count = 0
operations = ["+", "-", "*", "/", "*3.14", "%", "(", "**", ")", "**2"]
#loop through operations and make buttons for them in a four by three grid
for x in range(4):
    for y in range(3):
        if count < len(operations):
            button = Button(root, text = operations[count],  width = 2, height = 2, highlightbackground="gray42",
                            command = lambda text = operations[count]: get_operand(text))
            count += 1
            button.grid(row = x + 2, column = y + 3) #column + 3 to put operands on the side
#keep the window running with mainloop function on the root object
root.mainloop()