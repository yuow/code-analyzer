import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from editor import EditorWidget

import database
from userDTO import UserDTO


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setCentralWidget(EditorWidget())
        self.initWindow()

        self.create_session()

    def initWindow(self):
        self.showMaximized()
        self.setWindowTitle('Code Analyzer')

    def create_session(self):
        db = database.Database()
        db.connect()
        result = db.execute(
            "INSERT INTO Sessions(start_time) VALUES(NOW()) RETURNING session_id")
        UserDTO.session_id = result[0][0]


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()
