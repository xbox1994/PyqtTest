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

        for num in range(0, 100):
            RandomImage(self, 'smile.png')

        RandomImage(self, 'jbk.png')

        self.center()
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('嘻嘻')
        self.setWindowIcon(QIcon('smile.png'))
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class RandomImage(QLabel):
    const_image = 30

    def __init__(self, mSelf, imagePath):
        super().__init__(mSelf)
        self.setMouseTracking(True)
        self.setPixmap(QPixmap(imagePath).scaled(self.const_image, self.const_image))
        self.setGeometry(random.randint(0, 300 - self.const_image), random.randint(0, 300 - self.const_image), self.const_image, self.const_image)

    def mouseMoveEvent(self, event):
        self.setGeometry(random.randint(0, 300 - self.const_image), random.randint(0, 300 - self.const_image), self.const_image, self.const_image)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
