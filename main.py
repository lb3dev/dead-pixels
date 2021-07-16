import os
import sys
from collections import deque

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


def get_resource_path(resource_path):
    application_path = ''
    if getattr(sys, 'frozen', False):
        application_path = sys._MEIPASS
    elif __file__:
        application_path = os.path.dirname(__file__)
    return os.path.join(application_path, resource_path)


class ColorPanelsWidget(QWidget):

    colors = deque([Qt.black, Qt.white, Qt.red, Qt.green, Qt.blue])

    def __init__(self):
        super(ColorPanelsWidget, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.change_window_background()
        self.showFullScreen()
        self.setWindowIcon(QtGui.QIcon(get_resource_path('icons/dead-pixels.png')))

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Escape or key == Qt.Key_Q:
            self.close()
        if key == Qt.Key_A or key == Qt.Key_Left:
            self.rotate_left()
        if key == Qt.Key_D or key == Qt.Key_Right:
            self.rotate_right()
        event.accept()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.rotate_right()
        if event.button() == Qt.RightButton:
            self.close()

    def rotate_left(self):
        self.colors.rotate(1)
        self.change_window_background()

    def rotate_right(self):
        self.colors.rotate(-1)
        self.change_window_background()

    def change_window_background(self):
        w_palette = self.palette()
        w_palette.setColor(self.backgroundRole(), self.colors[0])
        self.setPalette(w_palette)


if __name__ == '__main__':
    app = QApplication([])

    # Use Fusion style for all OSs
    app.setStyle('Fusion')
    app.setApplicationName('Dead Pixels')

    window = ColorPanelsWidget()

    app.exec_()
