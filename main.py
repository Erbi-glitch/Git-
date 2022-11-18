import random
import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.pan)
        self.q = False
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def pan(self):
        self.q = True
        self.update()

    def paintEvent(self, event):
        if self.q:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            r = random.randint(5, 500)
            qp.drawEllipse(random.randint(50, 150), random.randint(50, 150), r, r)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
