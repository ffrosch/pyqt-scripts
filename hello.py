"""Simple Hello World example with PyQt5
created: 09.12.2020
"""

# The `sys` module will allow us to handle the exit status of the application
import sys

# 1. Import `QApplication` and all the required widgets
from PyQt5.QtWidgets import QApplication, QLabel, QWidget


# 2. Create an instance of QApplication first (longest initialization time)
# PyQt can handle commandline arguments
# If the application does not use commandline arguments, pass '[]'
app = QApplication(sys.argv)

# Get center coordinates of the screen
screen = app.primaryScreen()
rect = screen.availableGeometry()
width = rect.width()
height = rect.height()
center = (width//2, height//2)

# 3. Create an instance of the applications GUI
# QWidget is the base class of all user interface objects in PyQt
# Every widget in PyQt5 is a subclass of QWidget
# Every widget can be a main/top-level window if no parent is passed
window = QWidget()
window.setWindowTitle('PyQt5 hello-world-app')
window.setGeometry(100, 100, 280, 80)
window.move(*center)
# A widget which has a parent is contained/shown within its  parent
helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
helloMsg.move(60, 15)

# 4. Show the app's GUI
# This adds a new event to the app's event queue (event = paint GUI)
window.show()

# 5. Run the app's event/main loop
sys.exit(app.exec_())