# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 11:09:36 2019

@author: florian.frosch

TODO: Auswahlliste bei Autocomplete-Box mit Dropdown-Liste & Absturz dabei beheben
"""

from functools import partial
from PyQt5.QtWidgets import (QApplication, QDialog, QGroupBox,
                             QLabel, QProgressBar, QPushButton, QHBoxLayout,
                             QVBoxLayout, QFormLayout, QComboBox, QSpinBox,
                             QCompleter, QLineEdit, QListWidget, QGridLayout,
                             QAbstractButton, QAbstractItemView)
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from PyQt5.QtGui import QStandardItemModel, QStandardItem


NAMES = ['Peter', 'Otto', 'Helga', 'Susie', 'Manuel', 'Manuela', 'Siegfried', 'Dieter', 'Brunhilde', 'Stefan']
NAMES.sort()

class Communicate(QObject):

    value_changed = pyqtSignal()

class FirstApp(QDialog):
    styles = ['Fusion', 'Windows', 'WindowsVista']

    def __init__(self, names):
        super(FirstApp, self).__init__()

        QApplication.setStyle(self.styles[0])

        # Create GUI elements
        self.createFormGroupBox()
        self.createHorizontalGroupBox()
        self.createButtonBox()
        self.createProgressBar()
        self.createAutocompleteBox()

        # Populate QtDialog Window with GUI elements
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(self.horizontalGroupBox)
        mainLayout.addWidget(self.progressBar)
        mainLayout.addWidget(self.autocompleteBox)
        mainLayout.addWidget(self.buttonBox)

        self.setLayout(mainLayout)
        self.setWindowTitle('FirstApp')

        # Change Automatic Focusing Behaviour of QtDialog Window
        for button in self.findChildren(QAbstractButton):
            button.setAutoDefault(False)
            button.setDefault(False)

        # Set Focus to the autocompletion widget
        self.lineEdit.setFocus()

        # Configure signal for changes to the names list
        self.c = Communicate()
        self.c.value_changed.connect(self.onNamesValueChanged)

        # Calls the setter function self.names()
        self.names = names

# Property and Setter Functions for self.names.
# Values are stored in self._names, thus self.names does not for real call
# the values but instead either the property "names" or the setter "names".

    @property
    def names(self):
        return self._names

    @names.setter
    def names(self, value):
        self._names = value
        self.c.value_changed.emit()

    @names.setter
    def appendname(self, name):
        self._names.append(name)
        self._names.sort()
        self.c.value_changed.emit()

    @names.setter
    def popname(self, name):
        idx = self._names.index(name)
        self._names.pop(idx)
        self.c.value_changed.emit()

# These functions are used to create the GUI elements

    def createProgressBar(self):
        self.progressBar = QProgressBar()
        self.progressBar.setRange(0, 100)
        self.progressBar.setValue(5)

    def createButtonBox(self):
        ok = QPushButton('Ok')
        ok.clicked.connect(self.accept)

        cancel = QPushButton('Abbrechen')
        cancel.clicked.connect(self.reject)

        layout = QGridLayout()
        layout.addWidget(ok, 0, 0)
        layout.addWidget(cancel, 0, 1)

        self.buttonBox = QGroupBox()
        self.buttonBox.setLayout(layout)

    def createHorizontalGroupBox(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel('Set Progress'))

        values = [25, 50, 75, 100]
        for i in values:
            button = QPushButton(f'{i}%')
            button.clicked.connect(partial(self.changeProgress, i))
            layout.addWidget(button)

        self.horizontalGroupBox = QGroupBox('Horizontal Group Box')
        self.horizontalGroupBox.setLayout(layout)

    def createFormGroupBox(self):
        combobox = QComboBox()
        combobox.addItems(self.styles)
        combobox.activated[str].connect(self.changeStyle)

        self.spinbox = QSpinBox(minimum=0, maximum=100)
        self.spinbox.valueChanged[int].connect(self.changeProgress)

        layout = QFormLayout()
        layout.addRow(QLabel('Change the style of the Application:'), combobox)
        layout.addRow(QLabel('Set Progress (0-100)'), self.spinbox)

        self.formGroupBox = QGroupBox('Form Group Box')
        self.formGroupBox.setLayout(layout)

    def createAutocompleteBox(self):
        self.lineEdit = QLineEdit()

        self.completer = QCompleter()
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion) # or InlineCompletion
        self.completer.setModelSorting(QCompleter.CaseInsensitivelySortedModel)
        self.completer.activated[str].connect(self.addName)
        self.lineEdit.setCompleter(self.completer)
        #self.lineEdit.returnPressed.connect(self.lineEdit.clear)
        self.lineEdit.textChanged.connect(self.onTextChange)

        self.listWidget = QListWidget()
        self.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)

        layout = QFormLayout()

        layout.addRow(QLabel('Namen eingeben'))
        layout.addRow(self.lineEdit)

        self.listWidgetLabel = QLabel()
        self.listWidgetLabelText = 'Beteiligte Personen ({count})'
        self.setListWidgetLabelText()
        layout.addRow(self.listWidgetLabel)
        layout.addRow(self.listWidget)

        button = QPushButton('Person(en) löschen')
        button.clicked.connect(self.deleteName)
        layout.addWidget(button)

        self.autocompleteBox = QGroupBox('Autocomplete Box')
        self.autocompleteBox.setLayout(layout)

# These functions can be used to change certain attributes.
# Widgets can be connected to these functions to invoke them.

    def changeStyle(self, styleName):
        QApplication.setStyle(styleName)

    def changeProgress(self, newValue):
        self.progressBar.setValue(newValue)
        if self.spinbox.value() != newValue:
            self.spinbox.setValue(newValue)

    def addName(self, name):
        name = name.title()
        print('Name added:', name, QObject.sender(self))
        if name in self.names:
            self.listWidget.addItem(name)
            self.popname = name
            self.lineEdit.clear()

    def deleteName(self):
        items = self.listWidget.selectedItems()
        if len(items) > 0:
            for item in items:
                self.listWidget.takeItem(self.listWidget.row(item))
                self.appendname = item.text()

    def updateCompleterModel(self):
        model = QStandardItemModel()
        for name in self.names:
            item = QStandardItem(name)
            model.appendRow(item)
        self.completer.setModel(model)

    def setListWidgetLabelText(self):
        count = self.listWidget.count()
        text = self.listWidgetLabelText
        self.listWidgetLabel.setText(text.format(count=count))

    def onTextChange(self):
        '''Automatically clear the text that is inserted by the Completer at the end'''
        print('\nText changed:', self.lineEdit.text(), '\nSender:', QObject.sender(self), '\nModified:', self.lineEdit.isModified())
        if self.lineEdit.isModified() == False:
            self.lineEdit.clear()

    # This function is called whenever a name is added or subtracted from
    # the list of available names. It handles all dependent events.
    def onNamesValueChanged(self):
        self.updateCompleterModel()
        self.setListWidgetLabelText()


if __name__ == '__main__':
    import sys

    # sys.argv is empty if no commandline arguments are given
    app = QApplication(sys.argv)
    firstapp = FirstApp(NAMES)
    # run the application until the user closes it
    firstapp.exec_()
    print('Angenommen' if firstapp.result() == 1 else 'Abgebrochen')
