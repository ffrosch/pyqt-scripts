"""Dialog-style application

There are two types of dialogs:
- Modal: call .exec_(), block input to any other visible windows in the same application
- Modeless: call .show(), dialog is independent of other windows in the same application

Dialogs with a `parent` will be centered on top of the parent and share its entry in the system's taskbar.
Dialogs without a `parent` will get their own entry in the systems taskbar
"""

import sys

from PyQt5.QtWidgets import (QApplication,
                             QDialog,
                             QDialogButtonBox,
                             QFormLayout,
                             QLineEdit,
                             QVBoxLayout)


class Dialog(QDialog):
    """Dialog."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('QDialog')
        dlgLayout = QVBoxLayout()
        formLayout = QFormLayout()
        formLayout.addRow('Name:', QLineEdit())
        formLayout.addRow('Age:', QLineEdit())
        formLayout.addRow('Job:', QLineEdit())
        formLayout.addRow('Hobbies:', QLineEdit())
        dlgLayout.addLayout(formLayout)
        btns = QDialogButtonBox()
        btns.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        dlgLayout.addWidget(btns)
        self.setLayout(dlgLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())