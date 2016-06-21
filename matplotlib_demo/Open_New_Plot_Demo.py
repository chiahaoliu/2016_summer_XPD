import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons

t = np.arange(0.0, 2.0, 0.01)
s0 = np.sin(2*np.pi*t)
s1 = np.sin(4*np.pi*t)
s2 = np.sin(8*np.pi*t)

fig = plt.figure(1)

rax = plt.subplot2grid((1,1), (0,0))

radio = RadioButtons(rax, ('2 Hz', '4 Hz', '8 Hz', 'Clear'))

def new_plot(Event):
    plt.figure(2)
    if Event == '2 Hz':
        plt.plot(t, s0)
        plt.show()
    if Event == 'Clear':
        plt.clf().figure(2)
    if Event == '8 Hz':
        plt.plot(t, s2)
        plt.show()
    if Event == '4 Hz':
        plt.plot(t,s1)
        plt.show()
radio.on_clicked(new_plot)
plt.show()