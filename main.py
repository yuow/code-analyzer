import sys
from random import randint

from browser_window import BrowserWindow
from editor import EditorWidget

from PyQt6.QtGui import QAction

from PyQt6.QtWidgets import (
    QApplication,
)

from qfluentwidgets import FluentWindow
from qfluentwidgets import FluentIcon as FIF

class MainWindow(FluentWindow):
    def __init__(self):
        super().__init__()
        self.homeInterface = BrowserWindow()
        self.editorInterface = EditorWidget()

        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        self.addSubInterface(self.homeInterface, FIF.HOME, 'Home')
        self.addSubInterface(self.editorInterface, FIF.EDIT, 'Editor')

    def initWindow(self):
        self.resize(900, 700)
        self.setWindowTitle('Code Analyzer')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()