import tkinter as tk
from tkinter import *
import tkinter.messagebox
import numpy as np
from moving_square import what_happens_when_test
import time
root = tk.Tk()
root.title('Psychophysics course project - Welcome')

def inst_func():
    instructions = """
                    1. Once you start the experiment, two videos will be played (choice A & B)\n
                    2. Two things need to be observed a) Square size b) Sound beep frequency\n
                    3. Adjust the scaler for size & beep frequency to make choices A & B same\n
                    4. After adjusting scaler, hit "test" button to run the videos\n
                    5. Adjust until you're sure that they both are same. Hit "Submit" to complete\n
                    """
    tk.messagebox.showinfo(message=instructions)

def submit_func():
    candidate_name = T1.get("1.0", "end-1c")
    tk.messagebox.showinfo(message="Thank you '" + candidate_name + "' for your time")
    data_csv = np.vstack((true_square_side_monitor, square_side_monitor,
               true_beep_freq_monitor, beep_freq_monitor,
               reaction_time_monitor))
    np.savetxt(candidate_name+str(mode.get())+".csv", data_csv.T, delimiter=",")
    root.destroy()


def prepare_running_test():
    reaction_time_monitor.append(time.time()-reaction_time_monitor[-1])
    square_scale2 = int(S1.get())
    square_dim2 = (canvas_dim // canva_sq_ratio)*(1+square_scale2)
    beep_freq2 = freq_sampler[int(S2.get())]
    square_side_monitor.append(square_scale2)
    beep_freq_monitor.append(beep_freq2)
    true_square_side_monitor.append(square_scale1)
    true_beep_freq_monitor.append(beep_freq1)
    what_happens_when_test(num_squares, colors,
                            (square_dim1, square_dim2),
                            num_beeps, (beep_freq1, beep_freq2),
                            beep_timestamps, init_pos, res_pos, stride_len,
                            canvas_dim, time_steps, mode)

canvas_dim = 1024
max_stride_len = canvas_dim // 10
num_squares = np.random.randint(3, 7)
colors = np.random.randint(0, 255, (num_squares, 3))
canva_sq_ratio = 20
square_scale1 = np.random.randint(0, 10)
square_dim1 = (canvas_dim // canva_sq_ratio)*(1+square_scale1)
square_scale2 = np.random.randint(0, 10)
square_dim2 = (canvas_dim // canva_sq_ratio)*(1+square_scale2)

freq_sampler = np.linspace(200, 3000, 10)
time_steps = 20
num_beeps = np.random.randint(2, 4)
beep_freq1 = np.random.choice(freq_sampler)
beep_freq2 = np.random.choice(freq_sampler)
beep_timestamps = np.sort(np.random.randint(0, time_steps, num_beeps))
max_square_dim = (canvas_dim // canva_sq_ratio)*(11) #max([square_dim1, square_dim2])
init_pos_x = np.random.randint(0, canvas_dim-max_square_dim, num_squares)
init_pos_y = np.random.randint(0, canvas_dim-max_square_dim, num_squares)
res_pos_x = np.random.randint(0, canvas_dim-max_square_dim, num_squares)
res_pos_y = np.random.randint(0, canvas_dim-max_square_dim, num_squares)
stride_len_x = np.random.randint(-max_stride_len, max_stride_len, num_squares)
stride_len_y = np.random.randint(-max_stride_len, max_stride_len, num_squares)

true_square_side_monitor = [square_scale1]
square_side_monitor = [square_scale2]
true_beep_freq_monitor = [beep_freq1]
beep_freq_monitor = [beep_freq2]
reaction_time_monitor = [0.0]

init_pos = (init_pos_x, init_pos_y)
res_pos = (res_pos_x, res_pos_y)
stride_len = (stride_len_x, stride_len_y)
mode = IntVar()

L1 = Label(root, text="Welcome👋")
L2 = Label(root, text="Enter your name:")
T1 = Text(root, height = 1, width = 30)
B1 = Button(root, command=inst_func, text = "Read Instructions", width=20)
R1 = Radiobutton(root, text="Visual", variable=mode, value=0)
R2 = Radiobutton(root, text="Audio", variable=mode, value=1)
R3 = Radiobutton(root, text="Visual&Audio", variable=mode, value=2)
R3.select()

L3 = Label(root, text="Adjust the scaler for square size")
S1 = Scale(root, from_=0, to=10, orient=HORIZONTAL, length=250)
L4 = Label(root, text="Adjust the scaler for beep frequency")
S2 = Scale(root, from_=0, to=9, orient=HORIZONTAL, length=250)

L5 = Label(root, text="Click to run the animation")
B2 = Button(root, text = "Test",
                   command=prepare_running_test)

L6 = Label(root, text="Click to submit and quit")
B3 = Button(root, text = "Submit", command=submit_func)

L1.pack()
L2.pack()
T1.pack()
B1.pack()
R1.pack()
R2.pack()
R3.pack()
L3.pack()
S1.pack()
L4.pack()
S2.pack()
L5.pack()
B2.pack()
L6.pack()
B3.pack()
root.mainloop()
