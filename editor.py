from PyQt6.QtGui import QFont, QFontMetricsF, QSyntaxHighlighter
import subprocess
import os
from PyQt6.QtWidgets import (
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QPlainTextEdit,
)
from qfluentwidgets import PushButton
from PyQt6 import Qsci


class EditorWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("Editor")
        self.setup_layout()

    def setup_layout(self):
        self.layout = QVBoxLayout()
        input_widget = QWidget()
        self.layout.addWidget(input_widget)

        input_widget_layout = QHBoxLayout()
        input_widget.setLayout(input_widget_layout)

        self.code_input = CodeEditor()
        input_widget_layout.addWidget(self.code_input)

        self.code_output = QPlainTextEdit()
        self.code_output.setReadOnly(True)
        input_widget_layout.addWidget(self.code_output)

        run_button = PushButton('Run')
        run_button.clicked.connect(
            lambda: self.code_output.setPlainText(self.code_input.compile()))

        self.layout.addWidget(run_button)
        self.setLayout(self.layout)

class CodeEditor(Qsci.QsciScintilla):
    def __init__(self):
        super().__init__()

        self.lexer = Qsci.QsciLexerPython()
        self.setLexer(self.lexer)

        self.lexer.setFont(QFont("Consolas", 12))
        self.setAutoIndent(True)
        self.setIndentationWidth(4)
        self.setTabWidth(4)
        self.setIndentationGuides(True)

    def compile(self):
        code = self.text()
        with open("code.py", "w") as file:
            file.write(code)

        output = subprocess.getoutput('python code.py')

        os.remove("code.py")

        return output

    def keyPressEvent(self, event):
        print(event.key(), event.text())
        super(CodeEditor, self).keyPressEvent(event)
