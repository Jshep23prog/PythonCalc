#impork tk and ast
from tkinter import *
import ast

#create window object
root = Tk()
root.title("James' blind attempt")

#write function that adds text to entry field
i = 0
def get_number(num):
  global i
  display.insert(i, num) #add to entry widget
  i += 1 #increment every button click

#write a function to get operands
def get_operands(op):
  global i
  length = len(op) #to handle multi digit ops like pi
  display.insert(i, op)
  i += length

#write all clear function
def clear_all():
  display.delete(0, END)

#write calculate function
def calculate():
  entire_string = display.get()
  try:
    node = ast.parse(entire_string, mode = "eval")
    result = eval(compile(node, "<string>", "eval"))
    clear_all()
    display.insert(0, result)
  except Exception:
    clear_all()
    display.insert(0, "Flagrant System Error")

#backspace function
def undo():
  entire_string = display.get()
  if len(entire_string):
    new_string = entire_string[:-1]
    clear_all()
    display.insert(0, new_string)
  else: clear_all
  display.insert(0, "")

#entry field and grid display
display = Entry(root)
display.grid(row = 1, columnspan = 6)

#add buttons 1- 9 with nested for loop
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num_count = 0
for x in range(3):
  for y in range(3):
    button_text = numbers[num_count]
    button = Button(root, text = button_text, width = 2, height = 2, command = lambda text = button_text: get_number(text)) #add lambda function to call get_num
    button.grid(row = x + 2, column = y)
    num_count += 1

#need a zero button outside loop
button = Button(root, text = "0", width = 2, height = 2, command = lambda text = button_text: get_number(0))
button.grid(row = 5, column = 1)

# need AC, = and backspace
button = Button(root, text = "AC", width = 2, height = 2, command = clear_all).grid (row = 5, column = 0)

button = Button(root, text = "=", width = 2, height = 2, command = calculate).grid (row = 5, column = 2)

button = Button(root, text = "<-", width = 2, height = 2, command = lambda: undo()).grid (row = 5, column = 4)
#add operands
op_count = 0
operations = ["+", "-", "*", "/", "*3.14", "%", "(", "**", ")", "**2"]
#nested for loop
for x in range(4):
  for y in range(3):
    #logic for pressing on buttons
    if op_count < len(operations):
      button = Button(root, text = operations[op_count], width = 2, height = 2, command = lambda text = operations[op_count]: get_operands(text))
      op_count += 1
      button.grid(row = x + 2, column = y + 3)
#keep window running
root.mainloop()