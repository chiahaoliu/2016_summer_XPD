import matplotlib.pyplot as plt
from analysis import analysis
from file import get_files


class reducedRepPlot:

    def __init__(self, tif_list):
        self.tif_list = tif_list


    def plot(self):
        """
        This function will plot analysis data as a funciton of the number of images
        :param func: the function you would like to apply to the data
        :type func: function
        :return: void
        """
        a = analysis(self.tif_list)

        x, y = a.x_and_y_vals(sigma=True)

        plt.scatter(y, x)

        plt.xlabel("standard deviation")
        plt.ylabel("file num")

      #  plt.xscale()

        plt.show()
