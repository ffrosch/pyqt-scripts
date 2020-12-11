"""Signals and slots example."""

import functools
import sys

from PyQt5.QtWidgets import (QApplication,
                             QLabel,
                             QPushButton,
                             QVBoxLayout,
                             QWidget)


def greeting(who):
    """Slot function."""
    if msg.text():
        msg.setText('')
    else:
        msg.setText(f'Hello {who}')
        

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Signals and slots')
layout = QVBoxLayout()

btn = QPushButton('Greet')
# Every widget has its own set of predefined signals -> check them out in the docs
# Arguments can be passed to the function with functools.partial or lambda expressions
btn.clicked.connect(functools.partial(greeting, 'World!'))

layout.addWidget(btn)
msg = QLabel('')
layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec())