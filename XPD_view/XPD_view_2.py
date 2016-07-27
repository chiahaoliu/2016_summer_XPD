"""
This file will contain the code that makes the XPD view GUI
"""

from PyQt4 import QtGui, QtCore
import os
import sys
import numpy as np
from Tif_File_Finder import TifFileFinder
from plot_analysis import reducedRepPlot
from xray_vision.messenger.mpl.cross_section_2d import CrossSection2DMessenger


def data_gen(length):
    x, y = [_ * 2 * np.pi / 200 for _ in np.ogrid[-200:200, -200:200]]
    rep = int(np.sqrt(length))
    data = []
    for idx in range(length):
        kx = idx // rep + 1
        ky = idx % rep
        data.append(np.sin(kx * x) * np.cos(ky * y) + 1.05)
    return data


class Display2(QtGui.QMainWindow):

    def __init__(self):
        # This is just setting up some of the beginning variables
        QtGui.QMainWindow.__init__(self)
        self.setWindowTitle('XPD View')
        self.analysis_type = None
        self.file_path = None
        self.key_list = ['Home']
        data_list = data_gen(1)
        self.Tif = TifFileFinder()

        # These commands initialize the 2D cross section widget to draw itself
        self.messenger = CrossSection2DMessenger(data_list=data_list,
                                                 key_list=self.key_list)
        self.ctrls = self.messenger._ctrl_widget
        self.ctrls.set_image_intensity_behavior('full range')
        self.messenger.sl_update_image(0)
        self.data_dict = self.messenger._view._data_dict

        # This makes the layout for the main window
        self.frame = QtGui.QFrame()
        self.main_layout = QtGui.QVBoxLayout()
        self.frame.setLayout(self.main_layout)
        self.setCentralWidget(self.frame)
        self.display = self.messenger._display
        self.display_box = QtGui.QHBoxLayout()
        self.display_box.addWidget(self.display)
        self.tools_box = QtGui.QHBoxLayout()
        self.main_layout.addLayout(self.display_box)
        self.main_layout.addLayout(self.tools_box)

        # These methods will set up the menu bars and the tool bars
        self.name_label = QtGui.QLabel()
        self.set_up_tool_bar()
        self.set_up_menu_bar()

    def set_up_menu_bar(self):
        # set path option
        setpath = QtGui.QAction("&Set Directory", self)
        setpath.setShortcut("Ctrl+O")
        setpath.setStatusTip("Set image directory")
        setpath.triggered.connect(self.set_path)

        # sets up menu refresh option
        refresh_path = QtGui.QAction('&Refresh', self)
        refresh_path.setShortcut('Ctrl+R')
        refresh_path.triggered.connect(self.refresh)

        # This sets up all of the menu widgets that are used in the GUI
        mainmenu = self.menuBar()
        filemenu = mainmenu.addMenu("&File")
        graph_menu = mainmenu.addMenu('&Reduced Representation')
        filemenu.addAction(setpath)
        filemenu.addAction(refresh_path)

    def set_up_tool_bar(self):
        # All these commands will extract the desired widgets from x-ray_vision for our purposes
        self.tools_box.addWidget(self.ctrls._slider_img)
        self.tools_box.addWidget(self.ctrls._spin_img)
        self.tools_box.addWidget(self.ctrls._cm_cb)
        self.tools_box.addWidget(self.ctrls._cmbbox_intensity_behavior)
        min_label = QtGui.QLabel()
        min_label.setText('Int Min')
        self.tools_box.addWidget(min_label)
        self.tools_box.addWidget(self.ctrls._spin_min)
        max_label = QtGui.QLabel()
        max_label.setText('Int Max')
        self.tools_box.addWidget(max_label)
        self.tools_box.addWidget(self.ctrls._spin_max)

        # This makes the Label that is used to display the current key name
        self.name_label.setText('Current File: '+self.key_list[0])
        self.tools_box.addWidget(self.name_label)
        self.ctrls._spin_img.valueChanged.connect(self.change_display_name)

        # This makes the refresh button
        refresh = QtGui.QPushButton('Refresh', self)
        refresh.clicked.connect(self.refresh)
        self.tools_box.addWidget(refresh)

    def set_path(self):
        popup = QtGui.QFileDialog()
        self.file_path = str(popup.getExistingDirectory())
        self.Tif._directory_name = self.file_path
        self.Tif.get_file_list()
        if len(self.Tif.pic_list) == 0:
            print('No .tif files in directory')
        else:
            self.update_data(self.Tif.pic_list, self.Tif.file_list)
            # This will make the home page no longer an option so that user does not have to see it any more
            self.ctrls._slider_img.setMinimum(1)
            self.ctrls._spin_img.setMinimum(1)

    def refresh(self):
        new_file_names, new_data = self.Tif.get_new_files()
        if len(new_file_names) == 0:
            print("No new .tif files found")
        else:
            self.update_data(new_data, new_file_names)

    def update_data(self, data_list, file_list):
        # This method updates the data in the image display taking in some new data list and some other
        # list that is normally the list of File names. The other list is represented as the new key names.
        old_length = len(self.key_list)
        for file in file_list:
            self.key_list.append(file)
        for i in range(old_length, len(self.key_list)):
            self.data_dict[self.key_list[i]] = data_list[i - old_length]
        self.ctrls._slider_img.setMaximum(len(self.key_list) - 1)
        self.ctrls._spin_img.setMaximum(len(self.key_list) - 1)

    def change_display_name(self, val):
        # This is how the display updates the current name displayed
        self.name_label.setText("Current: " + self.key_list[val])


def main():
    app = QtGui.QApplication(sys.argv)
    viewer = Display2()
    viewer.show()
    sys.exit(app.exec_())
main()
