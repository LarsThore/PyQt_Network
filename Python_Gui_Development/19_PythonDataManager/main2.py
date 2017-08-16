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

from ui_files import pymainWindow2
import preferences
import utilities

# set the default path of the application to HOME/AppDataManager directory
# (soft-coding)
appDataPath = os.environ['HOME'] + '/AppDataManager/'

sqlite3.register_adapter(int, lambda val: int(val))

# if the path does not exist create it
if not os.path.exists(appDataPath):
    try:
        os.makedirs(appDataPath)
    except Exception:
        appDataPath = os.getcwd()

class Main(QMainWindow, pymainWindow2.Ui_mainWindow):

    # make Database path
    dbPath = appDataPath + 'pydata2.db'
    dbConn = sqlite3.connect(dbPath)

    def __init__(self, parent = None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        # create table in database
        self.dbCursor = self.dbConn.cursor()
        self.dbCursor.execute('''CREATE TABLE IF NOT EXISTS Main3(id INTEGER\
            PRIMARY KEY, name TEXT, phone INTEGER)''')

        # save changes to database
        self.dbConn.commit()

        self.addData.clicked.connect(self.add_button_clicked)
        self.removeRow.clicked.connect(self.remove_row_clicked)

        self.dbCursor.execute('''SELECT * FROM Main3''')
        allRows = self.dbCursor.fetchall()

        for row_inx, row in enumerate(allRows):
            self.insert_item(self.mainTable, row_inx, row)

    def insert_item(self, table, row_inx, row):

        table.insertRow(row_inx)
        row = list(row)
        print(row)

        for col_inx, value in enumerate(row[1:]):
            item = QTableWidgetItem()
            item.setData(Qt.EditRole, value)
            table.setItem(row_inx, col_inx, item)

    def add_button_clicked(self):

        name = self.userName.text()
        number = int(self.phoneNumber.text())

        inx = self.mainTable.rowCount()

        number_item = QTableWidgetItem()
        number_item.setData = (Qt.EditRole, number)

        self.mainTable.insertRow(inx)
        self.mainTable.setItem(inx, 0, QTableWidgetItem(name))
        self.mainTable.setItem(inx, 1, number_item)

        # commit changes to Database
        parameters = (None, name, number)
        self.dbCursor.execute('''INSERT INTO Main3 VALUES (?, ?, ?)''',
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
            self.dbCursor.execute('''DELETE FROM Main WHERE name = ?''',
             currentUsername)
            self.dbConn.commit()
            self.mainTable.removeRow(currentRow)


def main():
    QCoreApplication.setApplicationName('PyDataManager')
    QCoreApplication.setApplicationVersion('0.1')
    QCoreApplication.setOrganizationName('PyDataManager')
    QCoreApplication.setOrganizationDomain('pydatamanager.com')

    app = QApplication(sys.argv)
    form = Main()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
