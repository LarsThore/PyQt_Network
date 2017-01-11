from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys
import math


class Form(QDialog):

    def __init__(self, parent = None):
        super(Form, self).__init__(parent)      # old form of initializing (and using super and init)
        # super().__init__()


        self.resultsList = QTextBrowser()
        self.resultsInput = QLineEdit("Enter an expression and press return key.")


        layout = QVBoxLayout()      # VBox = Vertical Box (the widows are aligned beneath each other)
        layout.addWidget(self.resultsList)
        layout.addWidget(self.resultsInput)     # add both of the widgets to the layout
        self.setLayout(layout)      # set the layout to the real layout of the form (i.e. Form)

        self.resultsInput.selectAll()
        self.resultsInput.setFocus()        # makes sure that the focus is on resultsInput and the text is preselected

        self.resultsInput.returnPressed.connect(self.compute)   # by pressing the return key a signal is created
                                                                # which is passed to the compute method


    def compute(self):
        try:
            text = self.resultsInput.text()     # grasps the text from the input field
            self.resultsList.append("{0} = <b> {1} </b>".format(text, eval(text)))
        except:
            self.resultsList.append("<font color = red> <b> Invalid Expression! </b> </font>")







app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()



























