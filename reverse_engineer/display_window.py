"""
This file is meant to recreate the windows made available in the plot2d window
in the x-ray vision package
"""

from xray_vision.qt_widgets import CrossSectionMainWindow, Stack1DMainWindow
from PyQt4 import QtGui, QtCore
import sys
from roi.file_finder import FileFinder


class Display(CrossSectionMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setWindowTitle('XPD View')

        self.start = FileFinder()
        self.start.file_name = 'C:/Users/Caleb/2016_summer_XPD/Image/'

        key_list, data_list = self.start.file_list, self.start.pic_list
        self._main_window = CrossSectionMainWindow(data_list=data_list,
                                                   key_list=key_list,
                                                   cmap='RdBu')

        self._main_window.setFocus()
        self.setCentralWidget(self._main_window)


def main():
    app = QtGui.QApplication(sys.argv)
    tt = Display()
    tt.show()
    sys.exit(app.exec_())

main()
