from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
)
from PyQt6.QtCore import QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView

class BrowserWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        webview = QWebEngineView()
        webview.load(QUrl("https://python.org"))
        layout.addWidget(webview)
        self.setLayout(layout)

