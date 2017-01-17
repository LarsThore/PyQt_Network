from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

class ZeroSpinBox(QSpinBox):

    zeros = 0
    atZero = pyqtSignal(int, int)

    def __init__(self, parent = None):
        super(ZeroSpinBox, self).__init__(parent)

        self.valueChanged.connect(self.check_zero)

    def check_zero(self, value):
        if value == 0:
            self.zeros += 1
            self.constant = 5
            self.atZero.emit(self.zeros, self.constant)



class Form(QDialog):

    def __init__(self, parent = None):
        super().__init__()

        self.dial = QDial()
        self.dial.setNotchesVisible(True)

        self.spinbox = ZeroSpinBox()

        layout = QVBoxLayout()
        layout.addWidget(self.dial)
        layout.addWidget(self.spinbox)

        self.setLayout(layout)      # from QDialog class

        self.dial.valueChanged.connect(self.spinbox.setValue)       # set signal slot pairs
        self.spinbox.valueChanged.connect(self.dial.setValue)

        self.spinbox.atZero.connect(self.print_value)

    def print_value(self, zeros, constant):
        print ("The SpinBox has been at zero {0} times.".format(zeros))
        print ("the constant is {0}".format(constant))



app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()