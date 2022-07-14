import tkinter


window = tkinter.Tk()
window.title('My first GUI program')
window.minsize(600, 400)

#Label




open = True

my_label = tkinter.Label(text='I am a button', font=('Arial', '18', 'bold'))
my_label.grid(column=0, row=0)



def button_clicked():
    text = input.get()
    my_label.config(text=text)



input = tkinter.Entry(width=0)
input.grid(column=1, row=1)


button0 = tkinter.Button(text="Click me", command=button_clicked)
button0.grid(column=2, row=0)
button1 = tkinter.Button(text="Click me", command=button_clicked)
button1.grid(column=3, row=3)




















window.mainloop()