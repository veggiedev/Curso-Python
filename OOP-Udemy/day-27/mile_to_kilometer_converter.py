from ctypes import alignment
from tkinter import *
from tokenize import Number


window = Tk()
window.title("Miles to  Kilometers")
window.minsize(width=200, height=100)
entry = Entry()
km = 1.609344
enter_label = Label(text="Enter miles:")
enter_label.config(width=10)
enter_label.grid(column=0, row=0)



miles_input = Entry(text="0")
miles_input.config(width=2)
miles_input.insert(END, string="0")
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.config(width=10)
miles_label.grid(column=2, row=0)

def m_to_km():
    number = float(miles_input.get())
    resultado= round(number * km, 2 )
    result.config(text=resultado)

equal_label = Label(text="is equal to")
equal_label.config(width=10)
equal_label.grid(column=0, row=1)


result = Label(text="0")
result.config(width=2)
result.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.config(width=10)

km_label.grid(column=2, row=1)

button = Button(text="Go", command=m_to_km)
button.config(width=2)
button.grid(column=1, row=2)

window.mainloop()