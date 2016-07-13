"""
This file is meant to be used to experiment with the pyqtgraph package
in order to assess its usefulness. So far not too much appears to be useful.
This is mostly due to lack of documentation.
"""

import pyqtgraph as pg
from PyQt4 import QtGui
import sys


class Box(pg.PlotWindow):

    def __init__(self):
        super(Box, self).__init__()
        self.x = self.get_x(None)
        self.main_layout = QtGui.QVBoxLayout()
        self.setLayout(self.main_layout)
        self.resize(600, 600)
        self.plot(self.x)
        self.show_window()

    def get_x(self, x):
        if x is None:
            x = []
            for i in range(30):
                x.append(i ** 2 - 3 * i + 2)
            return x
        else:
            return x

    def show_window(self):
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    gui = Box()
    sys.exit(app.exec_())

main()
