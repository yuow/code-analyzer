from PyQt6 import QtCore
from PyQt6.QtCore import QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import QVBoxLayout, QWidget


class BrowserWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.addWidget(WebView())
        self.setLayout(layout)

        self.setObjectName("Home")


class WebView(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.load(QUrl("https://google.com"))
        self.urlChanged.connect(self.log_url)

    @QtCore.pyqtSlot(QUrl, name="url")
    def log_url(self, url):
        print(url.toString())
