"""Signals and slots example."""

import sys

from PyQt5.QtWidgets import (QApplication,
                             QLabel,
                             QPushButton,
                             QVBoxLayout,
                             QWidget)


def greeting():
    """Slot function."""
    if msg.text():
        msg.setText('')
    else:
        msg.setText('Hello World')
        

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Signals and slots')
layout = QVBoxLayout()

btn = QPushButton('Greet')
# Every widget has its own set of predefined signals -> check them out in the docs
btn.clicked.connect(greeting)

layout.addWidget(btn)
msg = QLabel('')
layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec())