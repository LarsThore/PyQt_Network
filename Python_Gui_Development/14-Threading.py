from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys
import showGUI
import time

class mainDialog(QDialog, showGUI.Ui_mainDialog):

    def __init__(self, parent = None):
        super(mainDialog, self).__init__(parent)

        self.setupUi(self)
        self.showButton.setText('Process')
        self.showButton.clicked.connect(self.processData)

        self.workerThread = WorkerThread()

        # new signal and slot style
        self.workerThread.threadDone.connect(self.threadDone, Qt.DirectConnection)

    def processData(self):
		# call the run method of WorkerThread class
        self.workerThread.start()
        QMessageBox.information(self, 'Done!', 'Done.')

    def threadDone(self):
        QMessageBox.warning(self, "Warning!", 'Thread execution completed.')

class WorkerThread(QThread):
    '''
    You cannot access any other thread (for example the GUI thread) by normal
    means from a QThread. Use signals and slots.
    '''

    threadDone = pyqtSignal()

    def __init__(self, parent = None):
        super(WorkerThread, self).__init__(parent)

    def run(self):
        time.sleep(5)
        # new signal and slot style
        self.threadDone.emit()


app = QApplication(sys.argv)
form = mainDialog()
form.show()
app.exec_()
