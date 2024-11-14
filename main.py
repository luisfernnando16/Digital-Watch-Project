from tkinter import *
from time import strftime

def update_clock():
    current_time = strftime('%H:%M:%S %p')
    watch_label.config(text=current_time)
    watch_label.after(1000, update_clock)

window = Tk()
window.title('Simple Digital Watch')

watch_label = Label(
    window,
    font=('Arial', 40, 'bold'),
    background='gray',
    foreground='white'
)

watch_label.pack(anchor='center')

update_clock()

window.mainloop()
