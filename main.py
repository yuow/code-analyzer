import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from qfluentwidgets import FluentWindow
from qfluentwidgets import FluentIcon as FIF

from browser_window import BrowserWindow
from editor import EditorWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setCentralWidget(EditorWidget())
        self.initWindow()

    def initWindow(self):
        self.showMaximized()
        self.setWindowTitle('Code Analyzer')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()
