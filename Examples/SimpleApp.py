from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication

import sys
import time

app = QApplication(sys.argv)

due = QTime.currentTime()
message = "Alert!"


try:

    if len(sys.argv) < 2:
        raise ValueError

    hours, minutes = sys.argv[2].split(':')

    due = QTime(int(hours), int(minutes))

    if not due.isValid():
        raise ValueError

    if len(sys.argv) > 2:
        message = " ".join(sys.argv[2,:])


except:
    print ("python3 SimpleApp.py HH:MM Optional Message")
    sys.exit(0)