import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from editor import EditorWidget

import database


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.session_id = None

        self.setCentralWidget(EditorWidget())
        self.initWindow()

        self.create_session()

    def initWindow(self):
        self.showMaximized()
        self.setWindowTitle('Code Analyzer')

    def create_session(self):
        db = database.Database()
        db.connect()
        self.session_id = db.execute(
            "INSERT INTO Sessions(start_time) VALUES(NOW()) RETURNING session_id")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()
