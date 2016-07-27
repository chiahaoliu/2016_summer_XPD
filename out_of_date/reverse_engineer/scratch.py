import sys
from PyQt4 import QtCore, QtGui


class StartQT4(QtGui.QMainWindow):
    def __init__(self):
        super(StartQT4, self).__init__()
        # This sets the where the window appears and how big
        self.setGeometry(100, 100, 500, 300)
        # This create the frame that we can put the layouts in
        self.frame = QtGui.QFrame()
        # This will create the layout
        self.layout = QtGui.QVBoxLayout()
        # This will set the layout of your frame to your frame
        self.frame.setLayout(self.layout)
        # This will make the line edit
        self.le = QtGui.QLineEdit()
        # THIS MUST BE DONE EVERY TIME YOU USE A MAIN WINDOW
        self.setCentralWidget(self.frame)
        # This command allows the line edit to do something
        # whenever enter is pressed
        self.le.returnPressed.connect(self.something)
        # This will allow the button that pulls up directories to pop up
        # to be right next to the line edit
        self.layout_mini = QtGui.QHBoxLayout()
        # This makes the button
        self.btn = QtGui.QPushButton('...')
        # This will set the hbox to the layout
        self.layout.addLayout(self.layout_mini)
        # This will set the line edit and button to the hbox
        self.layout_mini.addWidget(self.le)
        self.layout_mini.addWidget(self.btn)
        # This will make the button open the directory
        self.btn.clicked.connect(self.open_directory)


    def something(self):
        txt = self.le.text()
        print(txt)

    def open_directory(self):
        self.le.setText(QtGui.QFileDialog.getExistingDirectory())


def main():
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
main()
