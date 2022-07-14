from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# bg = Tk.PhotoImage(file="OOP-Udemy\Day-28\tomato.png")
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
# window.minsize(width=400, height=300)
window.title('Pomodoro')
window.config(padx=100, pady=50, bg = YELLOW)
img = PhotoImage(file='/home/veggiedev/Curso-Python/OOP-Udemy/Day-28/tomato.png')

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=img)
canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 20, 'bold'))

canvas.pack()












window.mainloop()
# count=300
# def countdown():
#     global count
#     # change text in label        
#     label['text'] = count

#     if count > 0:
#         # call countdown again after 1000ms (1s)
#         window.after(1000, countdown, count-1)




# call countdown first time    


# # window.config(bg = '/home/veggiedev/Curso-Python/OOP-Udemy/Day-28/tomato.png' )


# # pomodoro.minsize(width=500)
# title = Label(text="Break", font=(FONT_NAME, 20), bg="#f7f5dd")
# title.grid(column=1, row=0)
# pomodoro = Label(window,image=img, width=400, 
#                 height=300, bg="#f7f5dd").grid(column=1, row=1)


# label = Label(font=(FONT_NAME,  20), bg = "#f36848")
# label.grid(column=1, row=1)
# # countdown(300)
# # timer = Label(text=countdown(5), font=(FONT_NAME, 20), bg = "#f36848")
# # timer.grid(column=1, row=1)

# start = Button(text="Start", font=(FONT_NAME,  20), command=countdown)
# start.grid(column=0, row=2)

# stop = Button(text="Stop", font=(FONT_NAME, 20))
# stop.grid(column=2, row=2)
