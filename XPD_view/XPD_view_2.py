"""
This file will contain the code that makes the XPD view GUI
"""

from PyQt4 import QtGui, QtCore
import os
import sys
import numpy as np
from Tif_File_Finder import TifFileFinder
from plot_analysis import reducedRepPlot


def data_gen(length):
    x, y = [_ * 2 * np.pi / 200 for _ in np.ogrid[-200:200, -200:200]]
    rep = int(np.sqrt(length))
    data = []
    for idx in range(length):
        kx = idx // rep + 1
        ky = idx % rep
        data.append(np.sin(kx * x) * np.cos(ky * y) + 1.05)
    return data


class Display2(QtGui.QMainwindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setWindowTitle('XPD View')
        self.analysis_type = None
        self.file_path = None

        self.key_list = ['Home']
        self.data_list = data_gen(1)
        self.Tif = TifFileFinder()

    def set_path(self):
        popup = QtGui.QFileDialog()
        self.file_path = str(popup.getExistingDirectory())
        self.Tif._directory_name = self.file_path
        self.Tif.get_file_list()
        self.update_data(self.Tif.pic_list, self.Tif.file_list)

    def refresh(self):
        new_file_names, new_data = self.Tif.get_new_files()
        if len(new_file_names) == 0:
            print("No new .tif files found")
        else:
            self.update_data(new_data, new_file_names)

    def update_data(self, data_list, file_list):
        # This method updates the data in the image displayer taking in some new data list and some other
        # list that is normally the list of File names
        old_length = len(self.key_list)
        for file in file_list:
            self.key_list.append(file)
        for data in data_list:
            self.data_list.append(data)
        for i in range(old_length, len(self.key_list)):
            self._main_window._messenger._view._data_dict[self.key_list[i]] = self.data_list[i]
        self._main_window._messenger._ctrl_widget._slider_img.setMaximum(len(self.key_list) - 1)
        self._main_window._messenger._ctrl_widget._spin_img.setMaximum(len(self.key_list) - 1)
