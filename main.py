from time import *
from tkinter import *


# Update the time & date
def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000, update)


window = Tk()
# window.geometry("306x190")
window.configure(background="Black")
window.resizable(0, 0)
window.title("Digital Colck")
# window.overrideredirect(1)
time_label = Label(window, font=("ds-digital", 50), fg="cyan", bg="black")
time_label.pack()

day_label = Label(window, font=("Ink Free", 25, "bold"), fg="Red", bg="black")
day_label.pack()

date_label = Label(window, font=("Ink Free", 30), fg="orange", bg="black")
date_label.pack()

update()

window.mainloop()
