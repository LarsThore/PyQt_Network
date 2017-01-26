# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt, QRectF, QEvent
from PyQt5.QtGui import QColor, QPen, QBrush, QCursor, QImage, QPainter
from PyQt5.QtWidgets import (QWidget, QApplication, QGraphicsEllipseItem,
                             QGraphicsScene, QGraphicsView)
from PyQt5.uic import loadUi
from types import MethodType

import network_data as data

import sys
import numpy as np

app = QApplication(sys.argv)

# importing the file made qt designer
w = loadUi("03-circles.ui")

# image for saving the picture of circles
img = QImage(w.widget.width(), w.widget.height(), QImage.Format_RGB32)
img.fill(Qt.white)              # image appears white in the beginning (not black)
imgPainter = QPainter()         # first painter
painter = QPainter()            # second painter

def drawNodes(self, event):
    print (event.type())

    if event.type() == QEvent.MouseButtonPress:  # recognize mouse click

        imgPainter.begin(img)          # use first painter to draw on image
        imgPainter.setBrush(Qt.red)
        event_position = event.pos()

        print ( (event_position.x()), (event_position.y()) ),
        imgPainter.drawEllipse(event_position, 20, 20)    # draw Ellipse

        imgPainter.end()
        self.update()                           # requests a paint event

    elif event.type() == QEvent.Enter:
        pass
        # print ("I am entering the widget")

    elif event.type() == QEvent.Leave:
        pass
        # print ("I am leaving the widget")

    elif event.type() == QEvent.Paint:          # you're only allowed to draw here (in a paint event)
        painter.begin(self)                     # use second painter to draw image on widget
        painter.drawImage(0, 0, img)
        painter.end()

    return True                                 # ???

def drawEdges(self, event):
    pass




def erase():
    img.fill(Qt.white)
    w.widget.update()

w.widget.event = MethodType(drawNodes, w.widget)  # ???
w.eraseButton.clicked.connect(erase)

w.show()
sys.exit(app.exec_())
