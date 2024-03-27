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
    QHBoxLayout,
    QWidget,
    QTextEdit,
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

        layout = QVBoxLayout()

        input_widget = QWidget()
        layout.addWidget(input_widget)

        input_widget_layout = QHBoxLayout()
        input_widget.setLayout(input_widget_layout)

        code_input = QTextEdit()
        input_widget_layout.addWidget(code_input)

        code_output = QTextEdit()
        input_widget_layout.addWidget(code_output)
        code_output.setReadOnly(True)

        run_button = QPushButton('Run')
        layout.addWidget(run_button)

        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

    def open_browser(self):
        self.browser_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()
