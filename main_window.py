"""Mainwindow-style application

A Qt main window has a standard built-in layout:
- One menu bar
- Several toolbars (on the sides of the window) for: tool buttons, widgets like
    QComboBox, QSpinBox, etc.
- One (mandatory) central widget which can be of any type or a composite widget
- Several dock widgets around the central widget. These are small and movable
- One status bar at the bottom of the window
"""

import sys

from PyQt5.QtWidgets import (QApplication,
                             QLabel,
                             QMainWindow,
                             QStatusBar,
                             QToolBar)


class Window(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('QMainWindow')
        # A central widget MUST be defined. It can be a placeholder though.
        self.setCentralWidget(QLabel("I'm the Central Widget"))
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()
        
    def _createMenu(self):
        self.menu = self.menuBar().addMenu('&Menu')  # Alt-M will open Menu
        self.menu.addAction('&Exit', self.close)  # Alt-E will close Application
        
    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('Exit', self.close)
        
    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("I'm the Status Bar")
        self.setStatusBar(status)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())