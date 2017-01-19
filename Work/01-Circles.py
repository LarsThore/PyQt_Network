from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush
from PyQt5.QtWidgets import QWidget, QApplication

import sys
import numpy as np


__appname__ = "Draw Circles"


class drawCircles(QWidget):

    def __init__(self, parent = None):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(400, 200, 1000, 700)
        self.setWindowTitle("Circles")
        self.show()


    def paintEvent(self, e):            # Wofür steht das e?

        qp = QPainter()
        qp.begin(self)
        self.draw_circles(qp)
        # self.draw_rect(qp)
        qp.end()


    def draw_circles(self, qp):

        qp.setBrush(Qt.red)
        qp.setPen(Qt.red)
        size = self.size()

        for i in range(15):
            x = np.random.randint(10, size.width()-10)
            y = np.random.randint(10, size.height()-10)

            qp.drawEllipse(x, y, 20.0, 20.0)






if __name__ == '__main__':

    app = QApplication(sys.argv)
    form = drawCircles()
    form.show()
    app.exec_()