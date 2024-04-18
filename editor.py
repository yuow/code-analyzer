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

    def compile(self):
        code = self.text()
        with open("code.py", "w") as file:
            file.write(code)

        output = subprocess.getoutput('python code.py')

        os.remove("code.py")

        return output

    def keyPressEvent(self, e):
        super().keyPressEvent(e)
        print(e.key(), e.text())

    def keyReleaseEvent(self, e):
        super().keyReleaseEvent(e)
        print(e.key(), e.text())
