# -*- coding: utf-8 -*-

import sys
from PySide2.QtGui import QGuiApplication
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtWidgets import QApplication, QStyleFactory
from ui.Ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # ↓
        self.__main()

    def __main(self):
        # Making window centered ↓
        self.__makeWindowCenter()

        # Window customizing ↓
        self.setWindowTitle('Tic Tac Toe')

        # Hiding Menu Bar and Status Bar ↓
        self.ui.menubar.hide()
        self.ui.statusbar.hide()

    # For launching windows in center ↓
    def __makeWindowCenter(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QGuiApplication.primaryScreen().geometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())