import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Widget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.widget_layout = QVBoxLayout()
        self.table_widget = QTableWidget(10, 1)
        self.entryWidget = QLineEdit()

        self.widget_layout.addWidget(self.entryWidget)
        self.widget_layout.addWidget(self.table_widget)
        self.setLayout(self.widget_layout)

        self.entryWidget.returnPressed.connect(self.enter_pressed)
        self.entryWidget.setFocus()

        for num in range(9, -1, -1):
            self.insert_item(num, num)

    def insert_item(self, num, inx):
        item = QTableWidgetItem()
        item.setData(Qt.EditRole, num)
        self.table_widget.setItem(inx, 0, item)

    def enter_pressed(self):

        number = int(self.entryWidget.text())
        row_count = self.table_widget.rowCount()

        self.table_widget.insertRow(row_count)
        self.insert_item(number, row_count)

        self.entryWidget.clear()
        self.entryWidget.setFocus()

if __name__ == '__main__':
  app = QApplication(sys.argv)
  widget = Widget()
  widget.show()
  sys.exit(app.exec_())
