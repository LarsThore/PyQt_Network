from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys
import showGUI


class mainDialog(QDialog, showGUI.Ui_mainDialog):

    def __init__(self, parent = None):
        super(mainDialog, self).__init__(parent)

        self.setupUi(self)

        self.showButton.clicked.connect(self.showMessageBox)


    def showMessageBox(self):
        QMessageBox.information(self, "Hello!", "Hello there, " +
                                self.nameEdit.text())




app = QApplication(sys.argv)
form = mainDialog()
form.show()
app.exec_()
