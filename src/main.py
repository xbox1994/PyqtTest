#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)
        self.setMouseTracking(True)
        self.setLayout(grid)

        label = RandomImage(self)
        label.setPixmap(QPixmap('smile.png'))
        label.setGeometry(random.randint(0, 300 - 100), random.randint(0, 300 - 100), 100, 100)

        label = RandomImage(self)
        label.setPixmap(QPixmap('jbk.png'))
        label.setGeometry(random.randint(0, 300 - 100), random.randint(0, 300 - 100), 100, 100)

        self.center()
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('鸡巴宽你妈炸了')
        self.setWindowIcon(QIcon('smile.png'))
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()
        print(x, y)


class RandomImage(QLabel):
    def __init__(self, mSelf):
        super().__init__(mSelf)
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.setGeometry(random.randint(0, 300 - 100), random.randint(0, 300 - 100), 100, 100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
