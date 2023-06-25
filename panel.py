from tkinter import *
import tkinter.messagebox
master = Tk()
master.geometry("300x300")
master.title("")

def start_func():
    tkinter.messagebox.showinfo(message="Hello, about to start")

start_button = Button(master, command=start_func, text = "Start",
                      width=10).grid(row=1, column=10)
#start_button.pack()

sq_size_label = Label(master, text="Adjust the scaler for square size").grid(row=4, column=10)
sq_size_scaler = Scale(master, from_=0, to=10, orient=HORIZONTAL, length=250).grid(row=5, column=10)
#sq_size_scaler.pack()

sound_freq_label = Label(master, text="Adjust the scaler for beep frequency").grid(row=6, column=10)
sound_freq_scaler = Scale(master, from_=0, to=10, orient=HORIZONTAL, length=250).grid(row=7, column=10)
#sound_freq_scaler.pack()

sub_and_run = Button(master, text = "Test").grid(row=12, column=10)
#sub_and_run.pack(side=BOTTOM)

master.mainloop()
