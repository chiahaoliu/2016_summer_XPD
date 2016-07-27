"""
This is simply allows various programs to use the features found in the
region of interest object
"""
import numpy as np


class ROI:

    def __init__(self, array=None, rowb=None, rowe=None, colb=None, cole=None):
        """
        Initialize the ROI class for the program

        Args:
            array: numpy arrays only
            rowb: the beginning row for the region of interest
            rowe: the end row for the region of interest
            colb: the beginning column for the region of interest
            cole: the end column for the region of interest
        """

        self.array = array
        self.rowb = rowb
        self.rowe = rowe
        self.colb = colb
        self.cole = cole
        self.frpixel = 0
        self.fcpixel = 0
        self.erpixel = 0
        self.ecpixel = 0
        if array is not None:
            self.load_array(array)

    def load_array(self, array):
        """
        This loads in the array style that will be used for the program

        Args:
            array: numpy array

        Returns:
            Nothing, calls set boundaries for use in rest of program
        """
        self.array = array
        self.boundaries_set()

    def boundaries_set(self):
        """
        This function sets the boundaries automatically

        Returns: Nothing

        """
        size = self.array.shape
        self.frpixel = 0
        self.fcpixel = 0
        self.erpixel = size[0]
        self.ecpixel = size[1]

    def update(self, rowb, rowe, colb, cole):
        """
        This function updates the region of interest

        Args:
            rowb: Beginning row
            rowe: End row
            colb: Column row
            cole: Column end

        Returns:
            displays Invalid Boundaries if out of range set by boundaries function

        """
        if rowb >= self.frpixel and rowe < self.erpixel and colb >= self.fcpixel and cole < self.ecpixel:
            self.rowb = rowb
            self.rowe = rowe
            self.colb = colb
            self.cole = cole

        else:
            print('Invalid Boundaries')

    def export(self):
        """
        This function exports the region of interest as an array

        Returns:
            [rowb, rowe, colb, cole]
        """
        boundaries = [self.rowb, self.rowe, self.colb, self.cole]

        return boundaries
