import sys
from random import randint

from browser_window import BrowserWindow

from PyQt6.QtGui import QAction

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser_window = BrowserWindow()

        open_browser_action = QAction('&Open Browser', self)
        open_browser_action.triggered.connect(self.open_browser)

        menubar = self.menuBar()

        documentationMenu = menubar.addMenu('&Documentation')
        documentationMenu.addAction(open_browser_action)

        w = QWidget()
        self.setCentralWidget(w)

    def open_browser(self):
        self.browser_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()
