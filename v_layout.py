"""Using layout managers

Vertical layout example.
"""

import sys

from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QVBoxLayout')
layout = QVBoxLayout()
layout.addWidget(QPushButton('Left'))
layout.addWidget(QPushButton('Center'))
layout.addWidget(QPushButton('Right'))
window.setLayout(layout)
window.show()
sys.exit(app.exec_())