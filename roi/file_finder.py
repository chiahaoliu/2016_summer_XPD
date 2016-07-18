"""
This class is meant to help the interface locate and store the files that will
be used in the interface
"""

import os
from tifffile import imread


class FileFinder(object):

    def __init__(self):
        self._directory_name = ''
        self.a = []
        self.file_list = []
        self.pic_list = []

    @property
    def directory_name(self):
        return self._directory_name

    @directory_name.setter
    def directory_name(self, val):
        self._directory_name = val
        self.get_file_list()
        self.get_image_arrays()

    def get_name(self):
        self._directory_name = input('Please input directory location: ')
        self.get_file_list()

    def get_file_list(self):
        self.a = os.listdir(self._directory_name)
        self.file_list = [el for el in self.a if el.endswith('.tif')]
        self.a.sort(key=lambda x: os.path.getmtime(x))
        self.get_image_arrays()

    def get_image_arrays(self):
        self.pic_list = []
        for i in self.file_list:
            self.pic_list.append(imread(self._directory_name + i))
