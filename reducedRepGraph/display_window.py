import sys
from PyQt4 import QtGui, QtCore
from plot_analysis import reducedRepPlot
import multiprocessing


class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("reducedRepGraph")
        self.file_path = None
        self.analysis_type = None

        # main menu
        extractAction = QtGui.QAction("&Quit", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip("leave the app")
        extractAction.triggered.connect(self.close_application)

        # set path
        setPath = QtGui.QAction("&Set Directory", self)
        setPath.setShortcut("Ctrl+O")
        setPath.setStatusTip("Set image directory")
        setPath.triggered.connect(self.set_path)

        #set analysis type
        select_mean = QtGui.QAction("&mean", self)
        select_mean.triggered.connect(self.set_type_mean)

        select_std_dev = QtGui.QAction("&standard deviation", self)
        select_std_dev.triggered.connect(self.set_type_stddev)

        select_min = QtGui.QAction("&min", self)
        select_min.triggered.connect(self.set_type_min)

        select_max = QtGui.QAction("&max", self)
        select_max.triggered.connect(self.set_type_max)

        select_total_intensity = QtGui.QAction("&total intensity", self)
        select_total_intensity.triggered.connect(self.set_type_total)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&file")
        graph_menu = mainMenu.addMenu('&Graph Settings')
        analysis_submenu = QtGui.QMenu("analysis settings", graph_menu)
        fileMenu.addAction(extractAction)
        fileMenu.addAction(setPath)
        analysis_submenu.addAction(select_max)
        analysis_submenu.addAction(select_min)
        analysis_submenu.addAction(select_mean)
        analysis_submenu.addAction(select_std_dev)
        analysis_submenu.addAction(select_total_intensity)
        graph_menu.addMenu(analysis_submenu)

        self.home()
        self.show()

    def home(self):
        btn = QtGui.QPushButton("Plot", self)

        btn.clicked.connect(self.plot_analysis)
        btn.resize(100, 100)
        btn.move(100, 100)

    def close_application(self):
        print("application closed succesfully")
        sys.exit()

    def set_path(self):
        popup = QtGui.QFileDialog()
        self.file_path = str(popup.getExistingDirectory())
        print(self.file_path)

    def set_type_mean(self):
        self.analysis_type = "mean"
        print("mean")

    def set_type_min(self):
        self.analysis_type = "min"
        print("min")

    def set_type_stddev(self):
        self.analysis_type = "sigma"
        print("sigma")

    def set_type_max(self):
        self.analysis_type = "max"
        print("max")

    def set_type_total(self):
        self.analysis_type = "total intensity"
        print("total intensity")

    def plot_analysis(self):
        try:
            rpp = reducedRepPlot(self.file_path, 200, 600, 200, 600, self.analysis_type)
            rpp.plot()
        except NotADirectoryError:
            print("exception excepted")
            err_msg_file = QtGui.QMessageBox()
            err_msg_file.setIcon(QtGui.QMessageBox.Critical)
            err_msg_file.setWindowTitle("Error")
            err_msg_file.setText("You did not specify a file path.")
            err_msg_file.setInformativeText("click open to set the file path")
            err_msg_file.setStandardButtons(QtGui.QMessageBox.Open)
            err_msg_file.buttonClicked.connect(self.set_path)
            err_msg_file.exec_()
        except AssertionError:
            err_msg_analysis = QtGui.QMessageBox()
            err_msg_analysis.setIcon(QtGui.QMessageBox.Critical)
            err_msg_analysis.setWindowTitle("Error")
            err_msg_analysis.setText("You did not specify an analysis type")
            err_msg_analysis.setInformativeText("please go to the menu and select an analysis type before proceeding")
            err_msg_analysis.setStandardButtons(QtGui.QMessageBox.Close)
            #err_msg_analysis.buttonClicked.connect(self.set_path)
            err_msg_analysis.exec_()


        #todo add multiprocessing to function in plot_analysis
        # rpp = reducedRepPlot(self.file_path, 500, 700, 500, 700, self.analysis_type)
        #
        # p = multiprocessing.Process(target=rpp.plot)
        # p.start()

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
