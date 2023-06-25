from matplotlib import pyplot as plt
import numpy as np
#from celluloid import Camera
import matplotlib.animation as animation
import winsound

def what_happens_when_test(num_squares, colors, square_dim,
                           num_beeps, beep_freq,
                           beep_timestamps, init_pos, res_pos, stride_len,
                           canvas_dim, time_steps, mode):
    mode = int(mode.get())
    fig, axs = plt.subplots(1, 2)
    (init_pos_x, init_pos_y) = init_pos
    res_pos = (res_pos_x, res_pos_y) = res_pos
    (stride_len_x, stride_len_y) = stride_len

    canvas = np.zeros((canvas_dim, canvas_dim, 3))
    #square_dim = canvas_dim // canva_sq_ratio
    #camera = Camera(fig)

    beep_duration = 500
    choices = ['A', 'B']

    for ch in range(2):
        squares = np.ones((num_squares, square_dim[ch], square_dim[ch], 3))
        beeps_done = 0
        onset_x = init_pos_x
        onset_y = init_pos_y
        axs[(ch-1)%2].clear()

        for t in range(time_steps):
            canvas = np.zeros((canvas_dim, canvas_dim, 3))
            axs[ch].clear()
            for s in range(num_squares):
                square = squares[s] * colors[s:s+1]
                if ((max([onset_x[s], onset_y[s]]) + square_dim[ch]) > canvas_dim) or (min([onset_x[s], onset_y[s]]) <= 0):
                    onset_x[s] = res_pos_x[s]
                    onset_y[s] = res_pos_y[s]
                canvas[onset_x[s]:onset_x[s]+square_dim[ch], onset_y[s]:onset_y[s]+square_dim[ch],:] = square
                onset_x[s] += stride_len_x[s]
                onset_y[s] += stride_len_y[s]
            if beeps_done < num_beeps and t == beep_timestamps[beeps_done] and mode!=0:
                winsound.Beep(int(beep_freq[ch]), beep_duration)
                beeps_done += 1
            if mode != 1:
                axs[ch].imshow(canvas/255)
                axs[ch].axis('off')
                axs[ch].set_title('Choice '+choices[ch])
                plt.pause(0.005)
    plt.close()
    #camera.snap()
    #animation = camera.animate()
    #FFwriter = animation.FFMpegWriter(fps=10)
    #animation.save('test.mp4', writer=FFwriter, fps=10)
    #animation.save('test.mp4', writer='PillowWriter', fps=10)
