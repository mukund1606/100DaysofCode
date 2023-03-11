# GUI - Graphical User Interface

# Mac Lisa
# Windows 95

## Creating Windows and Labels

from tkinter import *

window = Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)
# window.config(padx=100, pady=200)

# Label

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack()
my_label.grid(column=0, row=0)

my_label["text"] = "New Text"
my_label.config(text="New Text")


# Button


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)


button2 = Button(text="New Button")
# button2.pack()
button2.grid(column=2, row=0)


# Entry

input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)


# Other Widgets
"""
Labels
Buttons
Entries
Text
Spinbox
Scale
Checkbutton
Radiobutton
Listbox
"""

"""
Layout Managers
pack() -> side by side
grid() -> grid
place() -> absolute positioning
"""

window.mainloop()
