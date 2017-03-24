from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys


__appname__ = "Eigth Video"


class Program(QDialog):

    def __init__(self, parent = None):
        super(Program, self).__init__(parent)

        self.openButton = QPushButton("Open")
        self.saveButton = QPushButton("Save")
        self.dirButton = QPushButton("Directory")
        self.closeButton = QPushButton("Close")

        self.openButton.clicked.connect(self.open_)
        self.saveButton.clicked.connect(self.save_)
        #self.dirButton.clicked.connect(self.dir_)
        #self.closeButton.clicked.connect(self.close_)

        layout = QVBoxLayout()
        layout.addWidget(self.openButton)
        layout.addWidget(self.saveButton)
        layout.addWidget(self.dirButton)
        layout.addWidget(self.closeButton)

        self.setLayout(layout)

    def open_(self):
        fileObj = QFileDialog.getOpenFileName(self, __appname__ + " Open File Dialog",
                                              filter = "text files (*.txt)")
        print (fileObj)
        print (type(fileObj))

        fileName = fileObj[0]

        file = open(fileName, "r")
        read = file.read()
        file.close()
        print (read)


    def save_(self):
        fileObj = QFileDialog.getSaveFileName(self, __appname__, filter = "Text files (*.txt)")

        print (fileObj)
        print (type(fileObj))

        contents = "Hello, welcome to the Bash..."

        fileName = fileObj[0]

        with open(fileName, "w") as file:
            file.write(contents)

        #fileName.close()






app = QApplication(sys.argv)
form = Program()
form.show()
app.exec_()

