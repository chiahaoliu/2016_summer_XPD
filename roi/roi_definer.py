"""
This file is meant to be a prototype for defining ROI's to be used
in later applications
"""
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons
from tifffile import imread
import os


file_name = input('Please write file name: ')

a = os.listdir(file_name)
file_list = [el for el in a if el.endswith('.tif')]

pic_list = []
for i in file_list:
    pic_list.append(imread(file_name + i))

plt.figure(1)
axpic = plt.subplot2grid((20, 20), (0, 0), rowspan=14, colspan=14)
axps = plt.subplot2grid((20, 20), (19, 10), rowspan=1, colspan=10)
axrb = plt.subplot2grid((20, 20), (15, 10), rowspan=1, colspan=10)
axre = plt.subplot2grid((20, 20), (16, 10), rowspan=1, colspan=10)
axcb = plt.subplot2grid((20, 20), (17, 10), rowspan=1, colspan=10)
axce = plt.subplot2grid((20, 20), (18, 10), rowspan=1, colspan=10)
axgray = plt.subplot2grid((20, 20), (0, 15), rowspan=6, colspan=5)

pic_swap = Slider(axps, 'Pic Index', 0, len(pic_list)-0.2, valinit=0)
rb = Slider(axrb, 'Row Begin', 0, 2047, valinit=100)
re = Slider(axre, 'Row End', 0, 2047, valinit=1900)
cb = Slider(axcb, 'Col Begin', 0, 2047, valinit=100)
ce = Slider(axce, 'Col End', 0, 2047, valinit=1900)
gray = RadioButtons(axgray, ('RdBu', 'BrBG', 'RdYlGn', 'Greys_r'))


def pic_switch(event):
    axpic.cla()
    axpic.imshow(pic_list[int(pic_swap.val)], cmap=gray.value_selected)
    axpic.axvline(x=rb.val)
    axpic.axvline(x=re.val)
    axpic.axhline(y=cb.val)
    axpic.axhline(y=ce.val)


class ROI(object):

    def __init__(self):
        self.rowb = rb.val
        self.rowe = re.val
        self.colb = cb.val
        self.cole = ce.val

    def update(self, event):
        print("Updated!")
        print(self.rowb, self.rowe, self.colb, self.cole)
        pic_switch(None)

roi1 = ROI()

pic_swap.on_changed(pic_switch)
rb.on_changed(roi1.update)
re.on_changed(roi1.update)
cb.on_changed(roi1.update)
ce.on_changed(roi1.update)
gray.on_clicked(pic_switch)


pic_switch(None)

plt.show()
