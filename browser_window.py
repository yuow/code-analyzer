from PyQt6.QtCore import QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import QVBoxLayout, QWidget


class BrowserWindow(QWidget):
    def __init__(self):
        super().__init__()

        webview = QWebEngineView()
        webview.load(QUrl("https://python.org"))

        layout = QVBoxLayout()
        layout.addWidget(webview)
        self.setLayout(layout)

        self.setObjectName("Home")
