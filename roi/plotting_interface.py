"""
This file is meant to be a prototype for defining ROI's to be used
in later applications
"""
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons, Button
from matplotlib.colorbar import ColorbarBase
from matplotlib.colors import Normalize
import numpy as np
from roi_definer import ROI
from file_finder import FileFinder


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
axbar = plt.subplot2grid((20, 20), (7, 14), rowspan=3, colspan=8)
axzoom = plt.subplot2grid((20, 20), (11, 14), rowspan=3, colspan=8)

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
zoom = RadioButtons(axzoom, ('Home', 'Zoom'))


def pic_switch(event):
    bounds = roi1.export()
    if zoom.value_selected == 'Zoom':
        axpic.cla()
        axpic.imshow(start.pic_list[int(pic_swap.val)], vmin=vmin.val, vmax=vmax.val, cmap=gray.value_selected)
        axpic.set_title(start.file_list[int(pic_swap.val)])
        axpic.set_xlim(bounds[2], bounds[3])
        axpic.set_ylim(bounds[1], bounds[0])
        axpic.axvline(x=bounds[2])
        axpic.axvline(x=bounds[3])
        axpic.axhline(y=bounds[0])
        axpic.axhline(y=bounds[1])
        axbar.cla()
        norm = Normalize(vmin=vmin.val, vmax=vmax.val)
        col = ColorbarBase(axbar, cmap=gray.value_selected, norm=norm, orientation='horizontal')
        col.set_ticks([vmin.val, vmax.val], update_ticks=True)
    else:
        axpic.cla()
        axpic.imshow(start.pic_list[int(pic_swap.val)], vmin=vmin.val, vmax=vmax.val, cmap=gray.value_selected)
        axpic.set_title(start.file_list[int(pic_swap.val)])
        axpic.axvline(x=bounds[2])
        axpic.axvline(x=bounds[3])
        axpic.axhline(y=bounds[0])
        axpic.axhline(y=bounds[1])
        axbar.cla()
        norm = Normalize(vmin=vmin.val, vmax=vmax.val)
        col = ColorbarBase(axbar, cmap=gray.value_selected, norm=norm, orientation='horizontal')
        col.set_ticks([vmin.val, vmax.val], update_ticks=True)


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


roi1 = ROI(rb.val, re.val, cb.val, ce.val, 0, 2048, 0, 2048)


def update_values(event):
    roi1.update(rb.val, re.val, cb.val, ce.val)
    pic_switch(None)

pic_swap.on_changed(pic_switch)
rb.on_changed(update_values)
re.on_changed(update_values)
cb.on_changed(update_values)
ce.on_changed(update_values)
gray.on_clicked(pic_switch)
skipf.on_clicked(forward)
skipb.on_clicked(backward)
pic_switch(None)
vmin.on_changed(pic_switch)
vmax.on_changed(pic_switch)
zoom.on_clicked(pic_switch)

plt.show()
