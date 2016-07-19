import sys
from PyQt4 import QtGui, QtCore
from plot_analysis import reducedRepPlot


class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("pyQt tutorial")
        self.file_path = ""

        #main menu
        extractAction = QtGui.QAction("&TEST MESSAGE", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip("leave the app")
        extractAction.triggered.connect(self.close_application)

        #set path
        setPath = QtGui.QAction("&Set Directory", self)
        setPath.setShortcut("Ctrl+O")
        setPath.setStatusTip("Set image directory")
        setPath.triggered.connect(self.set_path)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&file")
        graph_menu = mainMenu.addMenu('&Graph Settings')
        fileMenu.addAction(extractAction)
        fileMenu.addAction(setPath)

        self.home()
        self.show()

    def home(self):
        btn = QtGui.QPushButton("Plot", self)

        btn.clicked.connect(self.plot_analysis)
        btn.resize(100,100)
        btn.move(100, 100)

    def close_application(self):
        print("application closed succesfully")
        sys.exit()

    def set_path(self):
        popup = QtGui.QInputDialog()
        text, ok = popup.getText(self, "What is the filepath for the image directory?", "set filepath")
        if ok:
            self.file_path = text
            print( self.file_path)

    def plot_analysis(self):
        reducedRepPlot.__init__(self, self.file_path, 0, 2048, 0, 2048, mean=True)
        reducedRepPlot.plot(self)

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()