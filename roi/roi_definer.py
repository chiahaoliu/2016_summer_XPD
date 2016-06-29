"""
This is simply allows various programs to use the features found in the
region of interest object
"""


class ROI:

    def __init__(self, rowb, rowe, colb, cole, frpixel, erpixel, fcpixel, ecpixel):
        self.rowb = rowb
        self.rowe = rowe
        self.colb = colb
        self.cole = cole
        self.frpixel = frpixel
        self.erpixel = erpixel
        self.fcpixel = fcpixel
        self.ecpixel = ecpixel

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
