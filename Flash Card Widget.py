from tkinter import *
from random import randint
from tkinter import font

root = Tk()
root.title("Flashcard App")
root.geometry("400x400")
root.iconbitmap('G:\PyTkinter/python.ico')

# Create Our Addition Function
def add():
    hide_menu_frames()
    add_frame.pack(fill="both", expand=1)

    # Create Two Randoms Numbers
    num_1 = randint(0,10)
    num_2 = randint(0,10)

    # Put Our Random Numders
    add_flash = Label(add_frame, text=str(num_1) + "+" + str(num_2), font=("helvetica", 32))
    add_flash.pack(pady=10)

# Create Our Subtration Function
def subtract():
    hide_menu_frames()
    subtract_frame.pack(fill="both", expand=1)

# Create Our Multiplication Function
def multiply():
    hide_menu_frames()
    multiply_frame.pack(fill="both", expand=1)

# Create Our Division Function
def divide():
    hide_menu_frames()
    divide_frame.pack(fill="both", expand=1)

# Hide Frame Function
def hide_menu_frames():
    add_frame.pack_forget()
    subtract_frame.pack_forget()
    multiply_frame.pack_forget()
    divide_frame.pack_forget()

# Define Main Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Menu Items
math_menu = Menu(my_menu)
my_menu.add_cascade(label="MathCards", menu=math_menu)
math_menu.add_command(label="Add", command=add)
math_menu.add_command(label="Subtract", command=subtract)
math_menu.add_command(label="Multiply", command=multiply)
math_menu.add_command(label="Divide", command=divide)
math_menu.add_command(label="Exit", command=root.quit)
math_menu.add_separator()

# Create Math Frames
add_frame = Frame(root, width=400, height=400)
subtract_frame = Frame(root, width=400, height=400, bg="yellow")
multiply_frame = Frame(root, width=400, height=400, bg="orange")
divide_frame = Frame(root, width=400, height=400, bg="red")

root.mainloop()