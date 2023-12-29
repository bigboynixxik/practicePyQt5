import sys
from PyQt5.QtWidgets import QApplication
from graphic.classes import *
from graphic.window import MyWindow, MyDialog

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
