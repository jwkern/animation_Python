import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc


def init():
    line.set_data([], [])
    return (line,)

def init2():
    line2.set_data([], [])
    return (line2,)

def animate(i):
    t = np.linspace(0, 0.01*i, 5000)
    s = np.sin(45 * 2 * np.pi * t) + np.sin(49 * 2 * np.pi * t) + np.sin(85 * 2 * np.pi * t) + np.sin(86 * 2 * np.pi * t) + np.sin(87 * 2 * np.pi * t) + np.sin(88 * 2 * np.pi * t) + np.sin(89 * 2 * np.pi * t) + np.sin(125 * 2 * np.pi * t) + np.sin(127 * 2 * np.pi * t) + np.sin(129 * 2 * np.pi * t)
    line.set_data(t, s)
    return (line,)

def animate2(i):
    t = np.linspace(0, 0.01*i, 5000)
    s = np.sin(45 * 2 * np.pi * t) + np.sin(49 * 2 * np.pi * t) + np.sin(85 * 2 * np.pi * t) + np.sin(86 * 2 * np.pi * t) + np.sin(87 * 2 * np.pi * t) + np.sin(88 * 2 * np.pi * t) + np.sin(89 * 2 * np.pi * t) + np.sin(125 * 2 * np.pi * t) + np.sin(127 * 2 * np.pi * t) + np.sin(129 * 2 * np.pi * t)
    fft = np.fft.fft(s)
    T = t[1] - t[0]  #cadence 
    N = s.size
    f = np.linspace(0, 1 / T, N) #1/T cutoff freque
    y = np.abs(fft)*1/N
    line2.set_data(f, y)             
    return (line2,)

fig, ax = plt.subplots(2)
line, = ax[0].plot([], [], lw=2)
line2, = ax[1].plot([], [], lw=2)
fig.subplots_adjust(hspace=1.0)
ax[0].set_ylabel('Amplitude')
ax[0].set_xlabel('Time (s)')
ax[0].set_title('Lightcurve of ASTR8100')
ax[0].set_xlim(( 0, 2.5))
ax[0].set_ylim((-12.25, 12.25))
ax[1].set_ylabel('Amplitude')
ax[1].set_xlabel('Frequency (Hz)')
ax[1].set_title('Fourier Transform of ASTR8100')
ax[1].set_xlim(30, 140)
ax[1].set_ylim(0, 1.25)
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=250, interval=80, blit=True)
anim2 = animation.FuncAnimation(fig, animate2, init_func=init2, frames=250, interval=80, blit=True)
plt.show()
