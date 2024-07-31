#import all classes/functions from tkinter library
from tkinter import *

#create window object
root = Tk() #instance of the Tk class

#add an input field using grid method
display = Entry(root)
display.grid(row=1, columnspan=6)

#add 9 buttons with nested for loop
#counter increases to dynamically render button numbers
counter = 1
for x in range(3):
    for y in range(3):
        button = Button(root, text = counter, width = 2, height = 2)
        button.grid(row = x + 2, column = y) #add + 2 to row so it doesnt superimpose on entry field
        counter += 1
#outside of loop, create a zero button
button = Button(root, text = "0", width = 2, height = 2)
button.grid(row = 5, column = 1)

#keep the window running with mainloop function on the root object
root.mainloop()