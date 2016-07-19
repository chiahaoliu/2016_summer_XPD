import matplotlib.pyplot as plt
from analysis import analysis
from file import get_files


class reducedRepPlot:

    def __init__(self, file_path, x_start, x_stop, y_start, y_stop, sigma=False, min=False, max=False, mean=False):
        """
        constructor for reducedRepPlot object
        :param file_path: path to file directory
        :type file_path: str
        :param x_start: start val for x analysis
        :param x_stop: stop val for x analysis
        :param y_start:
        :param y_stop:
        :param sigma:
        :param min:
        :param max:
        :param mean:
        """
        self.tif_list = get_files(file_path)

        assert x_start >= 0 and x_start < x_stop
        assert x_stop <= 2048 #TODO change so resolution is flexible
        assert y_start >= 0 and y_start < y_stop
        assert y_stop <= 2048 #TODO change so resolution is flexible

        self.x_start = x_start
        self.x_stop = x_stop
        self.y_start = y_start
        self.y_stop = y_stop
        self.sigma = sigma
        self.min = min
        self.max = max
        self.mean = mean


    def plot(self):
        """
        This function will plot analysis data as a funciton of the number of images
        :param func: the function you would like to apply to the data
        :type func: function
        :return: void
        """
        a = analysis(self.tif_list, self.y_start, self.y_stop, self.x_start, self.x_stop)

        x, y, label = a.x_and_y_vals(sigma=self.sigma, min=self.min, max=self.max, mean=self.mean)

        plt.scatter(x, y)

        plt.xlabel("file num")
        plt.ylabel(label)

      #  plt.xscale()

        plt.show()
