import operator as op
import sys

from functools import partial
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,
                             QMainWindow,
                             QWidget,
                             QGridLayout,
                             QLineEdit,
                             QPushButton,
                             QVBoxLayout)

__version__ = '0.1.1'
__author__ = 'Leonadis Pozo Ramos, modified by Florian Frosch'


DIGITS = set('0123456789')
ERROR_MSG = 'ERROR'
OPERATIONS = set(r'+-/*')
PUNCTUATION = set('.()')

ALLOWED = DIGITS | OPERATIONS | PUNCTUATION


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
        
    def setDisplayText(self, text):
        '''Set the display's text'''
        self.display.setText(text)
        self.display.setFocus()
        
    def getDisplayText(self):
        '''Get the display's text'''
        return self.display.text()
        
    def clearDisplay(self):
        '''Clear the display'''
        self.setDisplayText('')


class PyCalcCtrl:
    '''PyCalc Controller'''
    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self._connectSignals()
    
    def _calculateResult(self):
        result = self._evaluate(expression=self._view.getDisplayText())
        self._view.setDisplayText(result)
    
    def _buildExpression(self, sub_exp):
        # clear display after error
        if self._view.getDisplayText() == ERROR_MSG:
            self._view.clearDisplay()
        
        # add new input to display
        expression = self._view.getDisplayText() + sub_exp
        self._view.setDisplayText(expression)
        
    def _connectSignals(self):
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'=', 'C'}:
                btn.clicked.connect(partial(self._buildExpression, btnText))
        
        self._view.buttons['='].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttons['C'].clicked.connect(self._view.clearDisplay)


def evaluateExpression(expression):
    '''Model to calculate the input of the calculator'''
    if set(expression) <= ALLOWED:
        try:
            result = str(eval(expression, {}, {}))
        except Exception:
            result = ERROR_MSG
    else:
        result = ERROR_MSG
    
    return result


def main():
    '''Execute the program'''
    # Create a QApplication instance
    pycalc = QApplication(sys.argv)
    # Show the calculator's GUI
    view = PyCalcUi()
    view.show()
    # Create an instance of the controller
    model = evaluateExpression
    PyCalcCtrl(model=model, view=view)
    # Run the calculator (start the main loop)
    sys.exit(pycalc.exec())


if __name__ == '__main__':
    main()