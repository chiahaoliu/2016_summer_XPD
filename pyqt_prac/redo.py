"""
This file is an attempt to recreate the previously constructed GUI in PyQt
to make it easier to use
"""

from roi.roi_definer import ROI
from roi.file_finder import FileFinder
import sys
from PyQt4 import QtGui, QtCore
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt


class MyMplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = plt.figure(figsize=(width, height), dpi=dpi)
        self.axes1 = plt.subplot2grid((1, 1), (0, 0))

        self.axes1.hold(False)

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


class AppWindow(QtGui.QMainWindow):

    def __init__(self):
        super(AppWindow, self).__init__()
        self.setGeometry(100, 100, 600, 550)
        self.main_widget = QtGui.QWidget(self)
        self.main_widget.setGeometry(0, 0, 500, 400)

        self.start = FileFinder()
        self.start.file_name = 'C:/Users/Caleb/2016_summer_XPD/Image/'
        self.start.get_file_list()
        self.start.get_image_arrays()

        self.l, self.sc = self.get_canvas()
        self.im = self.compute_initial_figure()
        self.pic_swap = self.get_pic_swap()
        self.pic_index = self.get_pick_index_display()
        self.pic_swap.valueChanged[int].connect(self.changed_index)

        self.show()

    def get_canvas(self):
        l = QtGui.QVBoxLayout(self.main_widget)
        sc = MyMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        l.addWidget(sc)
        return l, sc

    def compute_initial_figure(self):
        im = self.sc.axes1.imshow(self.start.pic_list[0], cmap='RdBu')
        self.sc.axes1.set_title(self.start.file_list[0])
        return im

    def compute_new_figure(self, value):
        print(value)
        self.im.set_data(self.start.pic_list[value])
        self.sc.axes1.set_title(self.start.file_list[value])

    def get_pic_swap(self):
        pic_swap = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        pic_swap.setGeometry(500, 500, 100, 50)
        pic_swap.setTickPosition(QtGui.QSlider.TicksBelow)
        pic_swap.setRange(0, len(self.start.pic_list)-1)
        return pic_swap

    def get_pick_index_display(self):
        d = QtGui.QLCDNumber(self)
        d.setSegmentStyle(2)
        d.setGeometry(400, 500, 50, 50)
        return d

    def changed_index(self, value):
        self.pic_index.display(value)
        self.compute_new_figure(value)


def main():
    app = QtGui.QApplication(sys.argv)
    gui = AppWindow()
    sys.exit(app.exec_())

main()
