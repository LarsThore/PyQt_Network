#! -*- coding:utf8 -*- #

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys
import showGUI
import time

class MainDialog(QDialog):

    myOwnSignal = pyqtSignal((int,), (str,))

    def __init__(self, parent = None):
        super(MainDialog, self).__init__(parent)

        self.btn1 = QPushButton('Button')

        layout = QVBoxLayout()
        layout.addWidget(self.btn1)
        self.setLayout(layout)

        self.btn1.clicked.connect(self.btn1_clicked)

        self.myOwnSignal.connect(self.my_own_signal)
        self.myOwnSignal[str].connect(self.my_own_signal)

    def btn1_clicked(self):
        self.myOwnSignal[str].emit('Hello')
        # QMessageBox.information(self, 'Hello', 'Button 1 clicked!')

    def my_own_signal(self, param):
        print ('Signal emitted.' + str(param))
        print (type(param))




app = QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()
