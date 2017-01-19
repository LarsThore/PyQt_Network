from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWidgets import *

import sys
from showGUI import *
import Haus


class mainDialog(QDialog, showGUI.Ui_mainDialog):

    def __init__(self, parent = None):
        super(mainDialog, self).__init__(parent)