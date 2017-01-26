# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt, QRectF, QEvent
from PyQt5.QtGui import QColor, QPen, QBrush, QCursor, QImage, QPainter
from PyQt5.QtWidgets import (QWidget, QApplication, QGraphicsEllipseItem,
                             QGraphicsScene, QGraphicsView)
from PyQt5.uic import loadUi
from types import MethodType

import sys
import numpy as np

import NW03Circles as circles
