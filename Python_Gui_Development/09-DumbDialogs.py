from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys


__appname__ = "Ninth Video"


class Program(QDialog):

    def __init__(self, parent = None):
        super(Program, self).__init__(parent)

        self.setWindowTitle(__appname__)

        btn = QPushButton("Open Dialog")

        self.label1 = QLabel("Label 1 Result")
        self.label2 = QLabel("Label 2 Result")

        layout = QVBoxLayout()
        layout.addWidget(btn)
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        self.setLayout(layout)

        btn.clicked.connect(self.dialog_open)


    def dialog_open(self):

        dialog = Dialog()
        if dialog.exec_():
            self.label1.setText("Spinbox value is " + str(dialog.spinbox.value()))
            self.label2.setText("Checkbox is " + str(dialog.checkbox.isChecked()))
        else:
            QMessageBox.warning(self, __appname__, "Dialog was cancelled!")


class Dialog(QDialog):

    def __init__(self, parent = None):
        super(Dialog, self).__init__(parent)

        self.setWindowTitle("Dialog")

        self.checkbox = QCheckBox()
        self.spinbox = QSpinBox()
        buttonOk = QPushButton("Ok")
        buttonCancel = QPushButton("Cancel")


        layout = QGridLayout()
        layout.addWidget(self.spinbox, 0, 0)
        layout.addWidget(self.checkbox, 0, 1)
        layout.addWidget(buttonCancel)
        layout.addWidget(buttonOk)

        self.setLayout(layout)

        buttonOk.clicked.connect(self.accept)
        buttonCancel.clicked.connect(self.reject)













app = QApplication(sys.argv)
form = Program()
form.show()
app.exec_()