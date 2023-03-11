from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)

# Entry

input = Entry(width=7)
input.grid(column=1, row=0)

# Labels

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_label = Label(text="0")
km_label.grid(column=1, row=1)

km_label2 = Label(text="Km")
km_label2.grid(column=2, row=1)


# Button


def button_clicked():
    miles = float(input.get())
    km = round(miles * 1.609, 2)
    km_label.config(text=f"{km}")


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()
