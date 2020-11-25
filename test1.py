import random
import sys

from PyQt5.QtGui import QPainter, QColor, QBrush, QPen
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(513, 482)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Tap"))


class GitCircles(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag = False
        self.s = []
        self.pushButton.clicked.connect(self.click)

    def paintEvent(self, event) -> None:
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            for x, yy, r, color in self.s:
                qp.setBrush(QBrush(color))
                qp.setPen(QPen(color))
                qp.drawEllipse(x, yy, r, r)
            qp.end()
            self.flag = False

    def click(self):
        self.flag = True
        x, y, r = random.randint(30, 400), random.randint(30, 400), random.randint(30, 100)
        color = QColor.fromRgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.s.append((x, y, r, color))
        self.repaint()


app = QApplication([])
ex = GitCircles()
ex.show()
sys.exit(app.exec_())
