import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

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
        # Set the central widget (required for a class that inherits from QMainWindow
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)


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