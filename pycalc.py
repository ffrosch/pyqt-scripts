import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,
                             QMainWindow,
                             QWidget,
                             QGridLayout,
                             QLineEdit,
                             QPushButton,
                             QVBoxLayout)

__version__ = '0.1'
__author__ = 'Leonadis Pozo Ramos, modified by Florian Frosch'


# Setup the calculator's GUI
class PyCalcUi(QMainWindow):
    '''The View of the MVC framework'''
    def __init__(self):
        super().__init__()
        # Set main window properties
        self.setWindowTitle('PyCalc')
        self.setFixedSize(235, 235)
        # Set general layout and central widget
        self.generalLayout = QVBoxLayout()
        # The central widget is required for a class that inherits from QMainWindow
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # Create the display and the buttons
        self._createDisplay()
        self._createButtons()
        
    def _createDisplay(self):
        '''Create the display for the calculator'''
        self.display = QLineEdit()
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        # Add the display to the general Layout
        self.generalLayout.addWidget(self.display)
        
    def _createButtons(self):
        '''Create the buttons for the calculator'''
        self.buttons = {}
        buttonsLayout = QGridLayout()
        # Button text | Button position on the QGridLayout
        buttons = {'7': (0, 0),
                   '8': (0, 1),
                   '9': (0, 2),
                   '/': (0, 3),
                   'C': (0, 4),
                   '4': (1, 0),
                   '5': (1, 1),
                   '6': (1, 2),
                   '*': (1, 3),
                   '(': (1, 4),
                   '1': (2, 0),
                   '2': (2, 1),
                   '3': (2, 2),
                   '-': (2, 3),
                   ')': (2, 4),
                   '0': (3, 0),
                   '00': (3, 1),
                   '.': (3, 2),
                   '+': (3, 3),
                   '=': (3, 4),
                  }
        # Create the buttons from a dict and add them to the grid layout
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40, 40)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        # Add buttonsLayout to the general layout
        self.generalLayout.addLayout(buttonsLayout)


def main():
    '''Execute the program'''
    # Create a QApplication instance
    pycalc = QApplication(sys.argv)
    # Show the calculator's GUI
    view = PyCalcUi()
    view.show()
    # Run the calculator (start the main loop)
    sys.exit(pycalc.exec())


if __name__ == '__main__':
    main()