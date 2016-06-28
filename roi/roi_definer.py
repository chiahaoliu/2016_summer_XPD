class ROI:

    def __init__(self, rowb, rowe, colb, cole):
        self.rowb = rowb
        self.rowe = rowe
        self.colb = colb
        self.cole = cole

    def update(self, rowb, rowe, colb, cole):
        if rowb >= 0 and rowe < 2048 and colb >= 0 and cole < 2048:
            self.rowb = rowb
            self.rowe = rowe
            self.colb = colb
            self.cole = cole

        else:
            print('Invalid Boundaries')

    def export(self):
        boundaries = [self.rowb, self.rowe, self.colb, self.cole]

        return boundaries
