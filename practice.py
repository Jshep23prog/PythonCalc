#impork tk and ast
from tkinter import *
import ast

#create window object
root = Tk()
root.title("James' blind attempt")


#entry field and grid display
display = Entry(root)
display.grid(row = 1, columnspan = 6)

#add buttons 1- 9 with nested for loop
counter = 1
for x in range(3):
  for y in range(3):
    button = Button(text = counter, width = 2, height = 2)
    button.grid(row = x + 2, column = y)
    counter += 1

#need a zero button outside loop
button = Button(text = 0, width = 2, height = 2)
button.grid(row = 5, column = 1)
#keep window running
root.mainloop()