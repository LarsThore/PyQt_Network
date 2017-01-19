from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys


__appname__ = "Tenth Video"


class Program(QDialog):

    def __init__(self, parent = None):
        super(Program, self).__init__(parent)

        self.setWindowTitle(__appname__)

        btn = QPushButton("Open Dialog")

        self.mainSpinBox = QSpinBox()
        self.mainCheckBox = QCheckBox("Main Checkbox value")

        layout = QVBoxLayout()
        layout.addWidget(self.mainSpinBox)
        layout.addWidget(self.mainCheckBox)
        layout.addWidget(btn)
        self.setLayout(layout)

        btn.clicked.connect(self.dialog_open)


    def dialog_open(self):
        initValues = {"mainSpinBox" : self.mainSpinBox.value(), "mainCheckBox" : self.mainCheckBox.isChecked()}

        dialog = Dialog(initValues)
        if dialog.exec_():
            self.mainSpinBox.setValue(dialog.spinBox.value())
            self.mainCheckBox.setChecked(dialog.checkBox.isChecked())


class Dialog(QDialog):

    def __init__(self, initValues, parent = None):
        super(Dialog, self).__init__(parent)

        self.setWindowTitle("Dialog")

        self.checkBox = QCheckBox()
        self.spinBox = QSpinBox()
        buttonOk = QPushButton("Ok")
        buttonCancel = QPushButton("Cancel")


        layout = QGridLayout()
        layout.addWidget(self.spinBox, 0, 0)
        layout.addWidget(self.checkBox, 0, 1)
        layout.addWidget(buttonCancel)
        layout.addWidget(buttonOk)

        self.setLayout(layout)

        self.checkBox.setChecked(initValues["mainCheckBox"])
        self.spinBox.setValue(initValues["mainSpinBox"])

        buttonOk.clicked.connect(self.accept)
        buttonCancel.clicked.connect(self.reject)


    def accept(self):

        class GreaterThanFive(Exception): pass
        class IsZero(Exception): pass

        try:
            if self.spinBox.value() > 5:
                raise GreaterThanFive("The value must be equal or smaller 5")
            elif self.spinBox.value() == 0:
                raise IsZero("The value cannot equal zero")
            else:
                QDialog.accept(self)

        except GreaterThanFive:
            QMessageBox.warning(self, __appname__, "The value must be equal or smaller 5")
            self.spinBox.selectAll()
            self.checkBox.setFocus()
            return

        except IsZero:
            QMessageBox.warning(self, __appname__, "The value cannot equal zero")
            self.spinBox.selectAll()
            self.checkBox.setFocus()
            return













app = QApplication(sys.argv)
form = Program()
form.show()
app.exec_()