"""
This file is meant to recreate the windows made available in the plot2d window
in the x-ray vision package
"""

from xray_vision.qt_widgets import CrossSectionMainWindow, Stack1DMainWindow
from PyQt4 import QtGui, QtCore
import sys
from roi.file_finder import FileFinder


class Display(CrossSectionMainWindow):

    def __init__(self, directory_name='/home/cduff2/2016_intern/2016_summer_XPD/Image/'):
        QtGui.QMainWindow.__init__(self)
        self.setWindowTitle('XPD View')

        self.start = FileFinder()
        self.start.directory_name = directory_name

        self._main_window = CrossSectionMainWindow(data_list=self.start.pic_list,
                                                   key_list=self.start.file_list,
                                                   cmap='RdBu')

        self._main_window.setFocus()
        self.setCentralWidget(self._main_window)
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    viewer = Display()
    sys.exit(app.exec_())

main()
