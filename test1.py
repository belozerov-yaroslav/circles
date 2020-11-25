import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen
from PyQt5.QtWidgets import QMainWindow, QApplication


class GitCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.flag = False
        self.s = []
        self.pushButton.clicked.connect(self.click)

    def paintEvent(self, event) -> None:
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            y = QColor.fromRgb(255, 255, 0)
            qp.setBrush(QBrush(y))
            qp.setPen(QPen(y))
            for x, yy, r in self.s:
                qp.drawEllipse(x, yy, r, r)
            qp.end()
            self.flag = False

    def click(self):
        self.flag = True
        x, y, r = random.randint(30, 400), random.randint(30, 400), random.randint(30, 100)
        self.s.append((x, y, r))
        self.repaint()


app = QApplication([])
ex = GitCircles()
ex.show()
sys.exit(app.exec_())
