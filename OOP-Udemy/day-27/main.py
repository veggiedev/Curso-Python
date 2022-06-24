import tkinter


window = tkinter.Tk()
window.title('My first GUI program')
window.minsize(600, 400)

#Label




open = True

my_label = tkinter.Label(text='I am a button', font=('Arial', '18', 'bold'))
my_label.pack()

def button_clicked():
    text = input.get()
    my_label.config(text=text)







input = tkinter.Entry(width=0)
input.pack()
button = tkinter.Button(text="Click me", command=button_clicked)
button.pack()
# input.bind(button, button_clicked)




















window.mainloop()