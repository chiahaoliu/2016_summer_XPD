#This program will allow interactive analysis of .tif files

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from tifffile import imread
import numpy as np

fig = plt.figure(1)

pic1 = imread('./2016_summer_XPD/Image/CdSeNP_000.tif')
pic2 = imread('./2016_summer_XPD/Image/CdSeNP_001.tif')
pic3 = imread('./2016_summer_XPD/Image/Ni300K.tif')
pic_list = [pic1, pic2, pic3]

rb0 = 400
re0 = 600
cb0 = 400
ce0 = 600

axcolor = 'lightgoldenrodyellow'

axpic = plt.subplot2grid( (20,20), (0,0), rowspan = 13, colspan = 13)

axps = plt.subplot2grid((20,20),(12,16),rowspan = 2, colspan = 6)

axrb = plt.subplot2grid((20,20),(16,0),rowspan = 1, colspan = 20)
axre = plt.subplot2grid((20,20),(17,0),rowspan = 1, colspan = 20)
axcb = plt.subplot2grid((20,20),(18,0),rowspan = 1, colspan = 20)
axce = plt.subplot2grid((20,20),(19,0),rowspan = 1, colspan = 20)

pic_swap = Slider(axps, 'Pic Index', 0, 2.8, valinit=0)

rb = Slider(axrb, 'Row Begin', 0, 2047, valinit=rb0)
re = Slider(axre, 'Row End', 0, 2047, valinit=re0)
cb = Slider(axcb, 'Col Begin', 0, 2047, valinit=cb0)
ce = Slider(axce, 'Col End', 0, 2047, valinit=ce0)

avg_ax = plt.subplot2grid((20,20),(0,14),rowspan = 3, colspan = 3)
std_ax = plt.subplot2grid((20,20),(0,17),rowspan = 3, colspan = 3)
min_ax = plt.subplot2grid((20,20),(3,14),rowspan = 3, colspan = 3)
max_ax = plt.subplot2grid((20,20),(3,17),rowspan = 3, colspan = 3)

button1 = Button(avg_ax, 'Avg', color=axcolor, hovercolor='0.975')
button2 = Button(std_ax, 'StDv', color=axcolor, hovercolor='0.975')
button3 = Button(min_ax, 'Min', color=axcolor, hovercolor='0.975')
button4 = Button(max_ax, 'Max', color=axcolor, hovercolor='0.975')

axnew = plt.subplot2grid((20,20),(6,14),rowspan = 5, colspan = 6)

plot_new = RadioButtons(axnew, ('Plot Avg', 'Plot StDv', 'Clear'))

def avg(event):
    x = 0
    if rb.val < re.val:
        rowb = int(rb.val)
        rowe = int(re.val)
    else:
        rowb = int(re.val)
        rowe = int(rb.val)
    if cb.val < ce.val:
        colb = int(cb.val)
        cole = int(ce.val)
    else:
        colb = int(ce.val)
        cole = int(cb.val)
    num = (rowe - rowb)*(cole - colb)

    for i in range(rowb, rowe + 1):
        for j in range(colb, cole + 1):
            x +=  pic_list[int(pic_swap.val)][i][j]
    return x/num, num, rowb, rowe, colb, cole

def avg_print(event):
    avg0, num, rowb, rowe, colb, cole = avg(event)
    print('The average intensity is ' + str(avg0))
button1.on_clicked(avg_print)

def stan_dev(event):
    x = 0
    avg0, num, rowb, rowe, colb, cole = avg(event)
    for i in range(rowb, rowe + 1):
        for j in range(colb, cole + 1):
            x += (avg0 -  pic_list[int(pic_swap.val)][i][j])**2
    std = (x/num)**0.5
    print('The standard deviations is ' + str(std))
button2.on_clicked(stan_dev)

def get_min(event):
    
    if rb.val < re.val:
        rowb = int(rb.val)
        rowe = int(re.val)
    else:
        rowb = int(re.val)
        rowe = int(rb.val)
    if cb.val < ce.val:
        colb = int(cb.val)
        cole = int(ce.val)
    else:
        colb = int(ce.val)
        cole = int(cb.val)

    z =  pic_list[int(pic_swap.val)][rowb][colb]
    x = rowb
    y = colb
    for i in range(rowb + 1, rowe + 1):
        for j in range(colb + 1, cole + 1):
            if  pic_list[int(pic_swap.val)][i][j] < z:
                z =  pic_list[int(pic_swap.val)][i][j]
                x = i
                y = j
    print('The minimum is ' + str(z) + ' at ' + str(x) + 'x' + str(y))
button3.on_clicked(get_min)

def get_max(event):

    if rb.val < re.val:
        rowb = int(rb.val)
        rowe = int(re.val)
    else:
        rowb = int(re.val)
        rowe = int(rb.val)
    if cb.val < ce.val:
        colb = int(cb.val)
        cole = int(ce.val)
    else:
        colb = int(ce.val)
        cole = int(cb.val)

    z =  pic_list[int(pic_swap.val)][rowb][colb]
    x = rowb
    y = colb
    for i in range(rowb + 1, rowe + 1):
        for j in range(colb + 1, cole + 1):
            if pic_list[int(pic_swap.val)][i][j] > z:
                z =  pic_list[int(pic_swap.val)][i][j]
                x = i
                y = j
    print('The maximum is ' + str(z) + ' at ' + str(x) + 'x' + str(y))
button4.on_clicked(get_max)

def pic_switch(Event):
    axpic.cla()
    axpic.imshow(pic_list[int(pic_swap.val)])
    axpic.axvline(x=rb.val)
    axpic.axvline(x=re.val)
    axpic.axhline(y=cb.val)
    axpic.axhline(y=ce.val)
pic_swap.on_changed(pic_switch)
rb.on_changed(pic_switch)
re.on_changed(pic_switch)
cb.on_changed(pic_switch)
ce.on_changed(pic_switch)

def get_avg_list():
    if rb.val < re.val:
        rowb = int(rb.val)
        rowe = int(re.val)
    else:
        rowb = int(re.val)
        rowe = int(rb.val)
    if cb.val < ce.val:
        colb = int(cb.val)
        cole = int(ce.val)
    else:
        colb = int(cb.val)
        cole = int(ce.val)
    
    avg_list = []
    num = (rowe - rowb)*(cole - colb)

    for k in range(0, len(pic_list)):
        x = 0
        for i in range(rowb, rowe):
            for j in range(colb, cole):
                x += pic_list[k][i][j]
        avg_list.append(x/num)
    return avg_list, num, rowb, rowe, colb, cole

def get_StDv_list():
    stdv_list = []
    avg_list, num, rowb, rowe, colb, cole = get_avg_list()
    for k in range(0,len(pic_list)):
        x = 0
        for i in range(rowb, rowe):
            for j in range(colb, cole):
                x += (pic_list[k][i][j] - avg_list[k])**2
        stdv_list.append((x/num)**0.5)

    return stdv_list

def new_plot(Event):
    print(Event)
    fig2 = plt.figure(2)
    x = np.arange(0, len(pic_list), 1.0)
    if Event == 'Plot Avg':
        y, num, rowb, rowe, colb, cole = get_avg_list()
        plt.plot(x,y)
        plt.show()
    if Event == 'Plot StDv':
        y = get_StDv_list()
        plt.plot(x,y)
        plt.show()
    if Event == 'Clear':
        plt.close(fig2)
plot_new.on_clicked(new_plot)

pic_switch(None)
plt.show()
