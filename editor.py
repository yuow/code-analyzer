from functools import partial
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import subprocess
import os
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QWidget,
    QPlainTextEdit,
    QSplitter
)
from qfluentwidgets import PrimaryPushButton
from PyQt6 import Qsci
from browser_window import BrowserWindow
import database
from userDTO import UserDTO
import datetime


class EditorWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("Editor")
        self.setup_layout()

    def setup_layout(self):
        layout = QHBoxLayout()
        self.window_layout = QSplitter()

        self.window_layout.addWidget(self.create_editor_view())
        self.window_layout.addWidget(BrowserWindow())

        layout.addWidget(self.window_layout)
        self.setLayout(layout)

    def create_editor_view(self):
        editor_layout = QSplitter(Qt.Orientation.Vertical)

        self.code_input = CodeEditor()
        editor_layout.addWidget(self.code_input)

        run_button = PrimaryPushButton('Run')
        run_button.clicked.connect(
            lambda: self.code_output.setPlainText(self.code_input.compile()))
        run_button.setShortcut("Ctrl+Return")
        run_button.setToolTip("Ctrl + Enter")

        editor_layout.addWidget(run_button)

        self.code_output = QPlainTextEdit()
        self.code_output.setReadOnly(True)
        editor_layout.addWidget(self.code_output)

        return editor_layout


class CodeEditor(Qsci.QsciScintilla):
    stack = []
    def __init__(self):
        super().__init__()

        lexer = Qsci.QsciLexerPython(self)
        lexer.setFont(QFont("Consolas", 12))
        self.setLexer(lexer)

        self.setAutoIndent(True)
        self.setIndentationWidth(4)
        self.setTabWidth(4)
        self.setIndentationGuides(True)

        self.setMarginLineNumbers(1, True)
        self.setMarginWidth(1, 30)

        self.total_time = 0

        self.focus_in_timestamp = datetime.datetime.now()
        self.keys_pressed = 0

        self.typing_speed = 0

        self.destroyed.connect(partial(CodeEditor._on_destroyed, self.__dict__))

    def compile(self):
        db = database.Database()
        db.connect()
        query = f"INSERT INTO keylogs(session_id, key, keytext, time, release_time) VALUES({UserDTO.session_id}, 0, 'RUN', NOW(), NOW())"
        db.execute(query)
        db.disconnect()

        code = self.text()
        with open("code.py", "w") as file:
            file.write(code)

        output = subprocess.getoutput('python code.py')

        os.remove("code.py")

        return output

    def focusInEvent(self, e):
        self.focus_in_timestamp = datetime.datetime.now()
        print("got focus")

    def focusOutEvent(self, e):
        delta_time = datetime.datetime.now() - self.focus_in_timestamp
        self.total_time += delta_time.total_seconds()
        print(f"{self.total_time=}")
        print("lost focus")


    def keyPressEvent(self, e):
        super().keyPressEvent(e)

        print(e.key(), e.text())
        print(f"{self.keys_pressed=}")
        db = database.Database()
        db.connect()
        query = f"INSERT INTO keylogs(session_id, key, keytext, time, release_time) VALUES({UserDTO.session_id}, {e.key()}, '{e.text()}', NOW(), NULL)"
        db.execute(query)
        db.disconnect()

    def keyReleaseEvent(self, e):
        super().keyReleaseEvent(e)

        print(e.key(), e.text())
        self.keys_pressed += 1
        print(f"{self.keys_pressed=}")
        if self.total_time != 0:
            print(f"typing speed: {self.keys_pressed/self.total_time} symbols per second")
            self.typing_speed = self.keys_pressed / self.total_time
        db = database.Database()
        db.connect()
        query = f"INSERT INTO keylogs(session_id, key, keytext, time, release_time) VALUES({UserDTO.session_id}, {e.key()}, '{e.text()}', NULL, NOW())"
        db.execute(query)
        db.disconnect()

    @staticmethod
    def _on_destroyed(d):
        print("-----------------")
        print("DATA: ")
        print(f"total time: {d['total_time']}")
        print(f"key presses: {d['keys_pressed']}")
        print(f"typing speed: {d['keys_pressed'] / d['total_time']} / sec")

