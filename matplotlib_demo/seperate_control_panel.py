import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons

x = [1,2,3,4,5,6,7,8,9,10]
y1 = [2,4,6,8,10,12,14,16,18,20]
y2 = [4,7,12,19,28,39,52,67,84,103]
y3 = [-2,-5,-8,-11,-14,-17,-20,-23,-26,-29]


plt.figure(1)
axplot = plt.subplot2grid((5,5),(0,0),rowspan = 5,colspan = 5)


fig2 = plt.figure(2)
axRadio = plt.subplot2grid((1,1),(0,0),rowspan = 1,colspan = 1)
plot_add = RadioButtons(axRadio,(1,2,3))

def pick_plot(event):
    plt.figure(1)
    #axplot.cla()
    if event == '1':
        axplot.plot(x,y1)
    if event == '2':
        axplot.plot(x,y2)
    if event == '3':
        axplot.plot(x,y3)
plot_add.on_clicked(pick_plot)
plt.show()