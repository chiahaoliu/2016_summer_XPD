"""
This class is meant to help the interface locate and store the files that will
be used in the interface
"""
import os
from tifffile import imread


class FileFinder(object):

    def __init__(self):
        self.file_name = ''
        self.a = []
        self.file_list = []
        self.pic_list = []

    def get_name(self):
        self.file_name = input('Please input directory location: ')
        self.get_file_list()

    def get_file_list(self):
        self.a = os.listdir(self.file_name)
        self.file_list = [el for el in self.a if el.endswith('.tif')]
        self.get_image_arrays()

    def get_image_arrays(self):
        self.pic_list = []
        for i in self.file_list:
            self.pic_list.append(imread(self.file_name + i))
