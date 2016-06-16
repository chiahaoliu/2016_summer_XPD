#This program will allow interactive analysis of .tif files

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from tifffile import imread

fig, ax = plt.subplots()
plt.subplots_adjust(bottom = 0.3)
pic = imread('./Image/Ni300K.tif')
rb0 = 400
re0 = 600
cb0 = 400
ce0 = 600
plt.imshow(pic)

axcolor = 'lightgoldenrodyellow'
"""
axrb = plt.axes([0.0,0.2,0.65,0.02], axisbg=axcolor)
axre = plt.axes([0.0,0.15,0.65,0.02], axisbg=axcolor)
axcb = plt.axes([0.0,0.1,0.65,0.02], axisbg=axcolor)
axce = plt.axes([0.0,0.05,0.65,0.02], axisbg=axcolor)

rb = Slider(axrb, 'Row Begin', 0, 2047, valinit=rb0)
re = Slider(axre, 'Row End', 0, 2047, valinit=re0)
cb = Slider(axcb, 'Col Begin', 0, 2047, valinit=cb0)
ce = Slider(axce, 'Col End', 0, 2047, valinit=ce0)
"""

avg_ax = plt.axes([0.85,0.2, 0.13, 0.1],axisbg=axcolor)
std_ax = plt.axes([0.85,0.4, 0.13, 0.1],axisbg=axcolor)
min_ax = plt.axes([0.85,0.6, 0.13, 0.1],axisbg=axcolor)
max_ax = plt.axes([0.85,0.8, 0.13, 0.1],axisbg=axcolor)

button1 = Button(avg_ax, 'Average', color=axcolor, hovercolor='0.975')
button2 = Button(std_ax, 'Stan Dev', color=axcolor, hovercolor='0.975')
button3 = Button(min_ax, 'Minimum', color=axcolor, hovercolor='0.975')
button4 = Button(max_ax, 'Maximum', color=axcolor, hovercolor='0.975')

def avg(event):
    x = 0
    if rb0 < re0:
        rowb = int(rb0)
        rowe = int(re0)
    else:
        rowb = int(re0)
        rowe = int(rb0)
    if cb0 < ce0:
        colb = int(cb0)
        cole = int(ce0)
    else:
        colb = int(ce0)
        cole = int(cb0)
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
    
    if rb0 < re0:
        rowb = int(rb0)
        rowe = int(re0)
    else:
        rowb = int(re0)
        rowe = int(rb0)
    if cb0 < ce0:
        colb = int(cb0)
        cole = int(ce0)
    else:
        colb = int(ce0)
        cole = int(cb0)

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

    if rb0 < re0:
       rowb = int(rb0)
       rowe = int(re0)
    else:
       rowb = int(re0)
       rowe = int(rb0)
    if cb0 < ce0:
       colb = int(cb0)
       cole = int(ce0)
    else:
       colb = int(ce0)
       cole = int(cb0)

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

"""
rb.on_changed(print('Moved!'))
re.on_changed(print('Moved!'))
cb.on_changed(print('Moved!'))
ce.on_changed(print('Moved!'))
"""

plt.show()
