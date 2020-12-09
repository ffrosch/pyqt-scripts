"""Using layout managers

Form layout example.
This Layout Manager arranges widgets in a two-column layout.
The first column usually displays messages in labels.
The second column usually contains widgets that allow the user to manipulate
data in the first column.
"""

import sys

from PyQt5.QtWidgets import QApplication, QFormLayout, QLineEdit, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QFormLayout')
layout = QFormLayout()
layout.addRow('Name:', QLineEdit())
layout.addRow('Age:', QLineEdit())
layout.addRow('Job:', QLineEdit())
layout.addRow('Hobbies:', QLineEdit())
window.setLayout(layout)
window.show()
sys.exit(app.exec_())