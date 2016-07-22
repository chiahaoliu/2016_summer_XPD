"""
This file will contain the code to create the XPD view GUI
"""

from xray_vision.qt_widgets import CrossSectionMainWindow
from PyQt4 import QtGui, QtCore
import sys
import os
from Tif_File_Finder import TifFileFinder


class Display(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setWindowTitle('XPD View')

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
