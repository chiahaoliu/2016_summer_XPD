#This file is meant to be a prototype for defining ROI's to be used
#in later applications
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from tifffile import imread
import os


file_name = input('Please write file name: ')

a = os.listdir(file_name)
file_list = [el for el in a if el.endswith('.tif')]

pic_list = []
for i in file_list:
    pic_list.append(imread(file_name + i))

axpic = plt.subplot2grid( (1,1), (0,0), rowspan = 1, colspan = 1)

def pic_switch(Event):
    plt.figure()
    axpic.imshow(pic_list[int(pic_swap.val)], cmap = gray.value_selected)
    axpic.axvline(x = rb.val)
    axpic.axvline(x = re.val)
    axpic.axhline(y = cb.val)
    axpic.axhline(y = ce.val)

plt.figure()
axps = plt.subplot2grid((10,10),(7,0),rowspan = 1, colspan = 7)
axrb = plt.subplot2grid((10,10), (0,0), rowspan = 1, colspan = 7)
axre = plt.subplot2grid((10,10), (1,0), rowspan = 1, colspan = 7)
axcb = plt.subplot2grid((10,10), (2,0), rowspan = 1, colspan = 7)
axce = plt.subplot2grid((10,10), (3,0), rowspan = 1, colspan = 7)
axgray = plt.subplot2grid((10,10), (4,0),rowspan = 2, colspan = 3)
axzoom = plt.subplot2grid((10,10), (0,9), rowspan = 1, colspan = 1)

pic_swap = Slider(axps, 'Pic Index', 0, len(pic_list)-0.2, valinit = 0)

rb = Slider(axrb, 'Row Begin', 0, 2047, valinit = 100)
re = Slider(axre, 'Row End', 0, 2047, valinit = 1900)
cb = Slider(axcb, 'Col Begin', 0, 2047, valinit = 100)
ce = Slider(axce, 'Col End', 0, 2047, valinit = 1900)

gray = RadioButtons(axgray, ('RdBu','Greys_r'))

zoom = Button(axzoom, 'Zoom')

pic_swap.on_changed(pic_switch)
rb.on_changed(pic_switch)
re.on_changed(pic_switch)
cb.on_changed(pic_switch)
ce.on_changed(pic_switch)
gray.on_clicked(pic_switch)

pic_switch('Greys_r')

plt.show()