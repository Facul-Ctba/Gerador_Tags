import sys

from PySide6 import QtCore, QtWidgets


class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        lay = QtWidgets.QVBoxLayout(self)

        for i in range(10):
            le = QtWidgets.QLineEdit()
            lay.addWidget(le)

    def event(self, event):
        if event.type() == QtCore.QEvent.KeyPress:
            if event.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
                self.focusNextPrevChild(True)
        return super().event(event)


app = QtWidgets.QApplication(sys.argv)

w = Widget()
w.show()

sys.exit(app.exec())
