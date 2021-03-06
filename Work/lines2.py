#! -*- coding: utf-8 -*- #

from PyQt5.QtCore import Qt, QRectF, QEvent
from PyQt5.QtGui import QColor, QPen, QBrush, QCursor, QImage, QPainter
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.uic import loadUi

from types import MethodType
import sys
import numpy as np

app = QApplication(sys.argv)

##################### importing the file made qt designer #####################
w = loadUi("03-circles.ui")

#################### image for saving the picture of circles ##################
img = QImage(w.widget.width(), w.widget.height(), QImage.Format_RGB32)
img.fill(Qt.white)              # image appears white in the beginning (not black)

################################ set painter ##################################
imgPainter = QPainter()         # first painter
painter = QPainter()            # second painter

################################## set pen ####################################
line_drawer = QPen()
line_drawer.setWidth(4)

################################# set switch ###################################
switch = 0

start_point_list = [0]
end_point_list = [0]

def save_starting_point(event):
    '''
    saves the starting point of the line after a click on the widget
    '''

    start_point = event.pos()
    print ("start")
    start_point_list[0] = start_point

def draw_line(event):
    '''
    uses the starting point and the second point - which is indicated by
    another click - to draw a line between those points
    '''
    
    end_point = event.pos()
    print ("end")

    imgPainter.begin(img)          # use first painter to draw on image
    imgPainter.setPen(line_drawer)
    imgPainter.drawLine(start_point_list[0], end_point)    # draw line from first circle to second circle
    imgPainter.end()


def drawing(self, event):
    print (event.type())
    global switch, line_drawer

    if event.type() == QEvent.MouseButtonPress and switch == 0:

        save_starting_point(event)
        switch = 1

    elif event.type() == QEvent.MouseButtonPress and switch == 1:

        draw_line(event)
        self.update()      # requests a paint event
        switch = 0

    elif event.type() == QEvent.Paint:          # (you're only allowed to draw here (in a paint event) ?)
        painter.begin(self)                     # use second painter to draw image on widget
        painter.drawImage(0, 0, img)
        painter.end()

    return True                     # return True to tell that the event is handled completely



def erase():
    img.fill(Qt.white)
    #circles = ()         ############ TODO deleting circle list does not work ############
    w.widget.update()

w.widget.event = MethodType(drawing, w.widget)  # ersetzt die Funktion, die die Ereignisse behandelt ???
w.eraseButton.clicked.connect(erase)

w.show()
sys.exit(app.exec_())
