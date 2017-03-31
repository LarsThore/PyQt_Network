#! -*- coding:utf8 -*- #

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import re
import sys

from ui_files import pymainWindow
import sqlite3

class Main(QMainWindow, pymainWindow.Ui_mainWindow):

    def __init__(self, parent = None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

    def load_initial_settings(self):
        '''Loads the initial settings for the application. Sets the mainTable
        columns width. '''
        pass

    def add_button_clicked(self):
        '''Calls the validate_fields method and adds the items to the table
        if true. '''
        pass

    def remove_row_clicked(self):
        '''Removes the selected row from the mainTable.'''
        pass

    def validate_fields(self):
        '''Validates the QLineEdits based on RegEx '''
        pass

    def import_action_triggered(self):
        '''Database import handler.'''
        pass

    def export_action_triggered(self):
        '''Database export handler.'''
        pass

    def preferences_action_triggered(self):
        '''Fires up the Preferences dialog. '''
        pass

    def about_action_triggered(self):
        '''Opens the about dialog. '''
        pass

    def exit_action_triggered(self):
        '''Closes the application. '''
        pass




app = QApplication(sys.argv)
form = Main()
form.show()
app.exec_()
