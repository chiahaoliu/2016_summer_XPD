""""
This function demonstrates how to have a seperate control panel that allows
for zoom
"""
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider
import numpy as np

arr = np.zeros([100, 100])
for i in range(0, 99):
    for j in range(0, 99):
        if i % 2 == 0 and j % 2 == 0:
            arr[i][j] = 10
        if i % 3 == 0 and j % 3 == 0:
            arr[i][j] = -7
plt.figure(1)
axpic = plt.subplot2grid((1, 1), (0, 0), rowspan=1, colspan=1)

plt.figure(2)
ax1 = plt.subplot2grid((5, 5), (0, 0), rowspan=1, colspan=4)
ax2 = plt.subplot2grid((5, 5), (1, 0), rowspan=1, colspan=4)
ax3 = plt.subplot2grid((5, 5), (2, 0), rowspan=1, colspan=4)
ax4 = plt.subplot2grid((5, 5), (3, 0), rowspan=1, colspan=4)

axbutton = plt.subplot2grid((5, 5), (4, 4), rowspan=1, colspan=1)

s1 = Slider(ax1, 'Row Begin', 0, 99, valinit=0)
s2 = Slider(ax2, 'Row End', 0, 99, valinit=99)
s3 = Slider(ax3, 'Col Begin', 0, 99, valinit=0)
s4 = Slider(ax4, 'Col End', 0, 99, valinit=99)

zoom = Button(axbutton, 'Zoom')


def dat_view_doe(event):
    if event == 'Nothing':
        axpic.imshow(arr, cmap='RdBu')
    else:
        plt.figure(1)
        plt.ylim(s1.val, s2.val)
        plt.xlim(s3.val, s4.val)
        plt.draw()

zoom.on_clicked(dat_view_doe)

dat_view_doe('Nothing')
plt.show()
