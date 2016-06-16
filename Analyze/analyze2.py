#This program will allow interactive analysis of .tif files

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from tifffile import imread

fig = plt.figure()
#fig, ax = plt.subplots()
#plt.subplots_adjust(bottom = 0.3)
pic = imread('./Image/Ni300K.tif')
rb0 = 400
re0 = 600
cb0 = 400
ce0 = 600

axcolor = 'lightgoldenrodyellow'

axpic = plt.subplot2grid((20,20),(0,0),rowspan = 14, colspan = 14)
axpic.imshow(pic)

axrb = plt.subplot2grid((20,20),(16,0),rowspan = 1, colspan = 20)
axre = plt.subplot2grid((20,20),(17,0),rowspan = 1, colspan = 20)
axcb = plt.subplot2grid((20,20),(18,0),rowspan = 1, colspan = 20)
axce = plt.subplot2grid((20,20),(19,0),rowspan = 1, colspan = 20)

rb = Slider(axrb, 'Row Begin', 0, 2047, valinit=rb0)
re = Slider(axre, 'Row End', 0, 2047, valinit=re0)
cb = Slider(axcb, 'Col Begin', 0, 2047, valinit=cb0)
ce = Slider(axce, 'Col End', 0, 2047, valinit=ce0)

avg_ax = plt.subplot2grid((20,20),(0,15),rowspan = 3, colspan = 6)
std_ax = plt.subplot2grid((20,20),(3,15),rowspan = 3, colspan = 6)
min_ax = plt.subplot2grid((20,20),(6,15),rowspan = 3, colspan = 6)
max_ax = plt.subplot2grid((20,20),(9,15),rowspan = 3, colspan = 6)

button1 = Button(avg_ax, 'Average', color=axcolor, hovercolor='0.975')
button2 = Button(std_ax, 'Stan Dev', color=axcolor, hovercolor='0.975')
button3 = Button(min_ax, 'Minimum', color=axcolor, hovercolor='0.975')
button4 = Button(max_ax, 'Maximum', color=axcolor, hovercolor='0.975')

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
            x += pic[i][j]
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
            x += (avg0 - pic[i][j])**2
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

    z = pic[rowb][colb]
    x = rowb
    y = colb
    for i in range(rowb + 1, rowe + 1):
        for j in range(colb + 1, cole + 1):
            if pic[i][j] < z:
                z = pic[i][j]
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

    z = pic[rowb][colb]
    x = rowb
    y = colb
    for i in range(rowb + 1, rowe + 1):
        for j in range(colb + 1, cole + 1):
            if pic[i][j] > z:
                z = pic[i][j]
                x = i
                y = j
    print('The maximum is ' + str(z) + ' at ' + str(x) + 'x' + str(y))
button4.on_clicked(get_max)

def if_moving(event):
    pass
rb.on_changed(if_moving)
re.on_changed(if_moving)
cb.on_changed(if_moving)
ce.on_changed(if_moving)

plt.show()
