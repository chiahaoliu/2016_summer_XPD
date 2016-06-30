"""
This is simply allows various programs to use the features found in the
region of interest object
"""
import numpy as np


class ROI:

    def __init__(self, array=None, rowb=None, rowe=None, colb=None, cole=None):
        self.array = array
        self.rowb = rowb
        self.rowe = rowe
        self.colb = colb
        self.cole = cole
        self.frpixel = 0
        self.fcpixel = 0
        self.erpixel = 0
        self.ecpixel = 0

    def load_array(self, array):
        self.array = array
        self.boundaries_set()

    def boundaries_set(self):
        size = self.array.shape
        self.frpixel = 0
        self.fcpixel = 0
        self.erpixel = size[0] - 1
        self.ecpixel = size[1] - 1

    def update(self, rowb, rowe, colb, cole):
        if rowb >= self.frpixel and rowe < self.erpixel and colb >= self.fcpixel and cole < self.ecpixel:
            self.rowb = rowb
            self.rowe = rowe
            self.colb = colb
            self.cole = cole

        else:
            print('Invalid Boundaries')

    def export(self):
        boundaries = [self.rowb, self.rowe, self.colb, self.cole]

        return boundaries
