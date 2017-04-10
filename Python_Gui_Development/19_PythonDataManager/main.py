#! -*- coding:utf8 -*- #
__appname__ = 'PyDataManager'
__module__ = 'main'

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import re
import sys
import os
import logging
import csv
import traceback
import sqlite3

from ui_files import pymainWindow
import preferences
import utilities

# set the default path of the application to HOME/AppDataManager directory
# (soft-coding)
appDataPath = os.environ['HOME'] + '/AppDataManager/'

# if the path does not exist create it
if not os.path.exists(appDataPath):
    try:
        os.makedirs(appDataPath)
    except Exception:
        appDataPath = os.getcwd()

# Logging
logging.basicConfig(filename= appDataPath + 'pydatamanager.log',
    format = "%(asctime)-15s: %(name)-18s - %(levelname)-8s - %(module)-15s\
     - %(funcName)-20s - %(lineno)-6d - %(message)s", level = logging.DEBUG)

# define the module name in the basic Configuration
logger = logging.getLogger(name = 'main-gui')




class Main(QMainWindow, pymainWindow.Ui_mainWindow):

    # make Database path
    dbPath = appDataPath + 'pydata.db'
    dbConn = sqlite3.connect(dbPath)



    def __init__(self, parent = None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        logger.debug("Application initialized")

        # create table in database
        self.dbCursor = self.dbConn.cursor()
        self.dbCursor.execute('''CREATE TABLE IF NOT EXISTS Main(id INTEGER\
            PRIMARY KEY, username TEXT, name TEXT, phone TEXT, address TEXT, \
            status TEXT)''')

        # save changes to database
        self.dbConn.commit()

        # save settings to file
        self.settings = QSettings(QSettings.IniFormat, QSettings.UserScope,
            'PyDataManager', 'PyDataManager')

        self.addData.clicked.connect(self.add_button_clicked)
        self.removeRow.clicked.connect(self.remove_row_clicked)

        self.actionExport.triggered.connect(self.export_action_triggered)
        self.actionPreferences.triggered.connect(self.preferences_action_triggered)
        self.actionExit.triggered.connect(self.exit_action_triggered)

        self.showToolbar = utilities.str2bool(self.settings.value(
         "showToolbar", True))
        self.mainToolbar.setVisible(self.showToolbar)

        self.load_initial_settings()

    def load_initial_settings(self):
        '''Loads the initial settings for the application. Sets the mainTable
        columns width. '''
        # select all items from Main
        self.dbCursor.execute('''SELECT * FROM Main''')
        allRows = self.dbCursor.fetchall()

        for row in allRows:
            inx = allRows.index(row)
            self.mainTable.insertRow(inx)
            # insert a QTableWidgetItem in the table
            self.mainTable.setItem(inx, 0, QTableWidgetItem(row[1]))
            self.mainTable.setItem(inx, 1, QTableWidgetItem(row[2]))
            self.mainTable.setItem(inx, 2, QTableWidgetItem(row[3]))
            self.mainTable.setItem(inx, 3, QTableWidgetItem(row[4]))
            self.mainTable.setItem(inx, 4, QTableWidgetItem(row[5]))

    def add_button_clicked(self):
        '''Calls the validate_fields method and adds the items to the table
        if true. '''
        username = self.userName.text()
        first_name = self.firstName.text()
        phone_number = self.phoneNumber.text()
        address = self.address.text()
        approved = self.approved.isChecked()

        # check if field entry has correct structure
        if not self.validate_fields():
            return False

        currentRowCount = self.mainTable.rowCount()

        self.mainTable.insertRow(currentRowCount)
        self.mainTable.setItem(currentRowCount, 0, QTableWidgetItem(username))
        self.mainTable.setItem(currentRowCount, 1, QTableWidgetItem(first_name))
        self.mainTable.setItem(currentRowCount, 2, QTableWidgetItem(phone_number))
        self.mainTable.setItem(currentRowCount, 3, QTableWidgetItem(address))
        self.mainTable.setItem(currentRowCount, 4, QTableWidgetItem(
         'Approved' if approved else 'Not approved'))

        # commit changes to Database
        parameters = (None, username, first_name, phone_number, address,
         str(approved))
        self.dbCursor.execute('''INSERT INTO Main VALUES (?, ?, ?, ?, ?, ?)''',
         parameters)
        self.dbConn.commit()

    def remove_row_clicked(self):
        '''Removes the selected row from the mainTable.'''
        # which row has been selected by the user
        currentRow =self.mainTable.currentRow()

        # if any row is selected
        if currentRow > -1:
            # make a tuple because sqlite needs a tuple as input
            currentUsername = (self.mainTable.item(currentRow, 0).text(), )
            self.dbCursor.execute('''DELETE FROM Main WHERE username = ?''',
             currentUsername)
            self.dbConn.commit()
            self.mainTable.removeRow(currentRow)

    def validate_fields(self):
        '''Validates the QLineEdits based on RegEx '''
        # select one column from the table
        self.dbCursor.execute('''SELECT username FROM Main''')
        usernames = self.dbCursor.fetchall()
        for username_ in usernames:
            if self.userName.text() in username_[0]:
                QMessageBox.warning(self,'Warning!','Such username already exists!')
                return False

        # regaular expression match
        # ^[2-9] --> begins with a 2, 3, 4, ... or 9
        # one digit, two digits - three digits - four digits
        # e.g. 673-734-7384
        if not re.match('^[2-9]\d{2}-\d{3}-\d{4}', self.phoneNumber.text()):
            QMessageBox.warning(self, 'Warning!', 'Phone number seems incorrect!')
            return False

        return True

    def import_action_triggered(self):
        '''Database import handler.'''
        # THIS is HOMEWORK
        # Hint no. 1: read documentation csv.reader
        # Hint no. 2: there is nothing new
        pass

    def export_action_triggered(self):
        '''Database export handler.'''

        self.dbCursor.execute("SELECT * FROM Main")

        dbFile = QFileDialog.getSaveFileName(parent = None, caption = " Export\
         database to a file", directory = ".", filter = "PyDataManager CSV (*.csv)")

        print (dbFile[0])
        if dbFile[0]:
            try:
                with open(dbFile[0], "w", newline = '') as csvFile:
                    csvWriter = csv.writer(csvFile, delimiter = ',',
                     quotechar = "\"", quoting = csv.QUOTE_MINIMAL)

                    rows = self.dbCursor.fetchall()
                    rowCount = len(rows)
                    for row in rows:
                        csvWriter.writerow(row)

                    QMessageBox.information(self, __appname__,
                    'Successfully exported ' + str(rowCount) +
                    ' rows to a file\n\r' + str(QDir.toNativeSeparators(dbFile[0])))

            except Exception as err:
                QMessageBox.critical(self, __appname__,
                 "Error exporting file, error is\n\r" + str(err))
                logger.critical("Error exporting file; the error is " + str(err)
                 + ", dbFile[0] is " + str[dbFile[0]])
                return

    def preferences_action_triggered(self):
        '''Fires up the Preferences dialog. '''

        dlg = preferences.Preferences(self, showToolbar = self.showToolbar)
        sig = dlg.checkBoxSig

        sig.connect(self.show_hide_toolbar)
        dlg.exec_()

    def show_hide_toolbar(self, param):
        '''Shows / hides main toolbar based on the checkbox value from
        preferences.'''

        self.mainToolbar.setVisible(param)

        self.settings.setValue("showToolbar", utilities.bool2str(param))
        # converts to self.settings.setValue("showToolbar", 'True')

    def about_action_triggered(self):
        '''Opens the about dialog. '''
        # HOMEWORK no. 2: write something about yourself and the app
        pass

    def exit_action_triggered(self):
        '''Closes the application. '''
        self.close()

    def closeEvent(self, event, *args, **kwargs):
        '''Overwrite the default close method.'''

        result = QMessageBox.question(self, __appname__,
         'Are you sure you want to exit?', QMessageBox.Yes | QMessageBox.No,
         QMessageBox.Yes)

        if result == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

def unhandled_exceptions(type, value, exp_traceback):
    exception = "".join(traceback.format_exception(type, value, exp_traceback))
    logger.critical(str(exception))
    print(exception)
    print("Process finished with exit code 1")
    sys.exit(1)

def main():
    QCoreApplication.setApplicationName('PyDataManager')
    QCoreApplication.setApplicationVersion('0.1')
    QCoreApplication.setOrganizationName('PyDataManager')
    QCoreApplication.setOrganizationDomain('pydatamanager.com')

    # overwrite default exception handler
    sys.excepthook = unhandled_exceptions

    app = QApplication(sys.argv)
    form = Main()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
