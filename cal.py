from tkinter import *

# Create window
root = Tk()
root.title("Calculator")
root.geometry("350x500")
root.resizable(False, False)

# Input field
entry = Entry(
    root,
    width=18,
    font=("Arial", 24),
    bd=10,
    relief=RIDGE,
    justify=RIGHT
)
entry.grid(row=0, column=0, columnspan=4, pady=20)

# Function to click buttons
def click(num):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(num))

# Function to clear
def clear():
    entry.delete(0, END)

# Function to calculate
def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Button settings
button_font = ("Arial", 18)
button_width = 5
button_height = 2

# Buttons layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Create buttons
for (text, row, col) in buttons:

    if text == "=":
        Button(
            root,
            text=text,
            width=button_width,
            height=button_height,
            font=button_font,
            command=equal
        ).grid(row=row, column=col, padx=5, pady=5)

    else:
        Button(
            root,
            text=text,
            width=button_width,
            height=button_height,
            font=button_font,
            command=lambda t=text: click(t)
        ).grid(row=row, column=col, padx=5, pady=5)

# Clear button
Button(
    root,
    text="C",
    width=23,
    height=2,
    font=button_font,
    bg="red",
    fg="white",
    command=clear
).grid(row=5, column=0, columnspan=4, pady=10)

# Run app
root.mainloop()

# the feature 
