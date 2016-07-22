import sys

from xray_vision import QtGui, QtCore
import numpy as np

from xray_vision.messenger.mpl.cross_section_2d import CrossSection2DMessenger

from xray_vision.qt_widgets import CrossSectionMainWindow


def data_gen(length):
    x, y = [_ * 2 * np.pi / 200 for _ in np.ogrid[-200:200, -200:200]]
    rep = int(np.sqrt(length))
    data = []
    lbls = []
    for idx in range(length):
        lbls.append(str(idx))
        kx = idx // rep + 1
        ky = idx % rep
        data.append(np.sin(kx * x) * np.cos(ky * y) + 1.05)
    return lbls, data


class StackExplorer(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent=parent)
        self.setWindowTitle('StackExplorer')
        menu_bar = self.menuBar()
        add_image = menu_bar.addMenu("&Get New")
        add_something = QtGui.QAction("&try", self)
        add_something.triggered.connect(self.new_data)
        add_image.addAction(add_something)
        self.counter = 20
        self.key_list, self.data_list = data_gen(20)
        self._main_window = CrossSectionMainWindow(data_list=self.data_list,
                                                   key_list=self.key_list)

        self._main_window.setFocus()
        self.setCentralWidget(self._main_window)

    def new_data(self):
        key_name = [str(self.counter)]
        self.key_list.append(key_name[0])
        self.counter += 1
        ignore, new_data = data_gen(1)
        self._main_window._messenger._view._data_dict[key_name[0]] = new_data[0]
        num_images = self.counter
        self._main_window._messenger._ctrl_widget._slider_img.setMaximum(num_images-1)
        self._main_window._messenger._ctrl_widget._spin_img.setMaximum(num_images-1)


app = QtGui.QApplication(sys.argv)
tt = StackExplorer()
tt.show()
sys.exit(app.exec_())
