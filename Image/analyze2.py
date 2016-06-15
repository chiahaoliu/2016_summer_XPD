#This program will allow interactive analysis of .tif files

import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from tifffile import imread

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.0, bottom=0.25)
pic = imread('./Ni300K.tif')
rb0 = 400
re0 = 600
cb0 = 400
ce0 = 600
plt.imshow(pic)
plt.axis([2047,0,2047,0])

axcolor = 'lightgoldenrodyellow'
axrb = plt.axes([0.0,0.2,0.65,0.02], axisbg=axcolor)
axre = plt.axes([0.0,0.15,0.65,0.02], axisbg=axcolor)
axcb = plt.axes([0.0,0.1,0.65,0.02], axisbg=axcolor)
axce = plt.axes([0.0,0.05,0.65,0.02], axisbg=axcolor)

rb = Slider(axrb, 'Row Begin', 0, 2047, valinit=rb0)
re = Slider(axre, 'Row End', 0, 2047, valinit=re0)
cb = Slider(axcb, 'Col Begin', 0, 2047, valinit=cb0)
ce = Slider(axce, 'Col End', 0, 2047, valinit=ce0)
def update(val):
    plt.axhline(y = rb.val)
    plt.axhline(y = re.val)
    plt.axvline(x = cb.val)
    plt.axvline(x = ce.val)
    fig.canvas.draw_idle()

rb.on_changed(update)
re.on_changed(update)
cb.on_changed(update)
ce.on_changed(update)


plt.show()
