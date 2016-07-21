import matplotlib.pyplot as plt
from analysis_concurrent import analysis_concurrent
from file import get_files
import multiprocessing


class reducedRepPlot:

    def __init__(self, file_path, x_start, x_stop, y_start, y_stop, selection):
        """
        constructor for reducedRepPlot object
        :param file_path: path to file directory
        :type file_path: str
        :param x_start: start val for x analysis
        :param x_stop: stop val for x analysis
        :param y_start:
        :param y_stop:
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
        self.selection = selection


    def plot(self):
        """
        This function will plot analysis data as a funciton of the number of images
        :param func: the function you would like to apply to the data
        :type func: function
        :return: void
        """
        a = analysis_concurrent(self.y_start, self.y_stop, self.x_start, self.x_stop, self.selection)
        trunc_list = []
        cpu_count = multiprocessing.cpu_count()
        for i in range(0, cpu_count):
            if i == cpu_count-1:
                temp_list = self.tif_list[(i*len(self.tif_list)//cpu_count) : (((1+i)*len(self.tif_list)//cpu_count) +
                                                                               (len(self.tif_list)%cpu_count))]
            else:
                temp_list = self.tif_list[(i*len(self.tif_list)//cpu_count) : ((1+i)*len(self.tif_list)//cpu_count)]
            trunc_list.append(temp_list)

        process_list = []
        x = range(0,len(self.tif_list))
        y = []
        q = multiprocessing.Queue()
        l = multiprocessing.Lock()
        #p = multiprocessing.Process(a.x_and_y_vals, args=(l,))

        for i in range(0, cpu_count):
            process_list.append(multiprocessing.Process(target=a.x_and_y_vals, args=(l, q, trunc_list[i])))

        for process in process_list:
            process.start()

        for process in process_list:
            process.join()


        for i in range(0,cpu_count):
            y.append(q.get())

        flattened_y = [val for sublist in y for val in sublist]
        assert len(flattened_y) == len(self.tif_list)
        plt.scatter(x, flattened_y)

        plt.xlabel("file num")
        #plt.ylabel(label)

      #  plt.xscale()

        plt.show()
