"""
This file is meant to be a prototype for defining ROI's to be used
in later applications
"""
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons, Button
from tifffile import imread
import numpy as np
import os


class FileFinder(object):

    def __init__(self):
        self.file_name = ''
        self.a = []
        self.file_list = []
        self.pic_list = []

    def get_name(self):
        self.file_name = input('Please input directory location: ')
        self.get_file_list()

    def get_file_list(self):
        self.a = os.listdir(self.file_name)
        self.file_list = [el for el in self.a if el.endswith('.tif')]
        self.get_image_arrays()

    def get_image_arrays(self):
        self.pic_list = []
        for i in self.file_list:
            self.pic_list.append(imread(self.file_name + i))

start = FileFinder()
start.get_name()

plt.figure(1)
axpic = plt.subplot2grid((20, 20), (0, 0), rowspan=14, colspan=14)
axps = plt.subplot2grid((20, 20), (19, 10), rowspan=1, colspan=10)
axrb = plt.subplot2grid((20, 20), (15, 10), rowspan=1, colspan=10)
axre = plt.subplot2grid((20, 20), (16, 10), rowspan=1, colspan=10)
axcb = plt.subplot2grid((20, 20), (17, 10), rowspan=1, colspan=10)
axce = plt.subplot2grid((20, 20), (18, 10), rowspan=1, colspan=10)
axgray = plt.subplot2grid((20, 20), (0, 15), rowspan=6, colspan=5)
axskipf = plt.subplot2grid((20, 20), (19, 5), rowspan=1, colspan=2)
axskipb = plt.subplot2grid((20, 20), (19, 3), rowspan=1, colspan=2)
axvmin = plt.subplot2grid((20, 20), (15, 0), rowspan=2, colspan=5)
axvmax = plt.subplot2grid((20, 20), (17, 0), rowspan=2, colspan=5)

pic_swap = Slider(axps, 'Pic Index', 0, len(start.pic_list)-1, valinit=0)
rb = Slider(axrb, 'Row Begin', 0, 2047, valinit=100)
re = Slider(axre, 'Row End', 0, 2047, valinit=1900)
cb = Slider(axcb, 'Col Begin', 0, 2047, valinit=100)
ce = Slider(axce, 'Col End', 0, 2047, valinit=1900)
gray = RadioButtons(axgray, ('RdBu', 'BrBG', 'RdYlGn', 'Greys_r'))
skipf = Button(axskipf, '>')
skipb = Button(axskipb, '<')
abs_min_V = np.min(start.pic_list[int(pic_swap.val)])
abs_max_V = np.max(start.pic_list[int(pic_swap.val)])
vmin = Slider(axvmin, 'Vmin', abs_min_V, abs_max_V, abs_min_V)
vmax = Slider(axvmax, 'Vmax', abs_min_V, abs_max_V, abs_max_V)


def pic_switch(event):
    axpic.cla()
    axpic.imshow(start.pic_list[int(pic_swap.val)], vmin=vmin.val, vmax=vmax.val, cmap=gray.value_selected)
    axpic.set_title(start.file_list[int(pic_swap.val)])
    axpic.axvline(x=rb.val)
    axpic.axvline(x=re.val)
    axpic.axhline(y=cb.val)
    axpic.axhline(y=ce.val)


def forward(event):
    if pic_swap.val + 1 > len(start.pic_list) - 1:
        pass
    else:
        x = pic_swap.val + 1
        pic_swap.set_val(x)


def backward(event):
    if pic_swap.val - 1 < 0:
        pass
    else:
        x = pic_swap.val - 1
        pic_swap.set_val(x)


class ROI(object):

    def __init__(self):
        self.rowb = rb.val
        self.rowe = re.val
        self.colb = cb.val
        self.cole = ce.val

    def update(self, event):
        if rb.val >= 0 and re.val < 2048 and cb.val >= 0 and ce.val < 2048:
            self.rowb = rb.val
            self.rowe = re.val
            self.colb = cb.val
            self.cole = ce.val
            pic_switch(None)

        else:
            print('Invalid Boundaries')

    def export(self):
        boundaries = [self.rowb, self.rowe, self.colb, self.cole]

        return boundaries

roi1 = ROI()

pic_swap.on_changed(pic_switch)
rb.on_changed(roi1.update)
re.on_changed(roi1.update)
cb.on_changed(roi1.update)
ce.on_changed(roi1.update)
gray.on_clicked(pic_switch)
skipf.on_clicked(forward)
skipb.on_clicked(backward)
pic_switch(None)
vmin.on_changed(pic_switch)
vmax.on_changed(pic_switch)

plt.show()
