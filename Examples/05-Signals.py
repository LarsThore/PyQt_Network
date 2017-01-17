from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys


class Form(QDialog):

    def __init__(self, parent = None):
        super().__init__()

        self.dial = QDial()
        self.dial.setNotchesVisible(True)

        self.spinbox = QSpinBox()

        layout = QVBoxLayout()
        layout.addWidget(self.dial)
        layout.addWidget(self.spinbox)

        self.setLayout(layout)      # from QDialog class

        self.dial.valueChanged.connect(self.spinbox.setValue)
        self.spinbox.valueChanged.connect(self.dial.setValue)



app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
