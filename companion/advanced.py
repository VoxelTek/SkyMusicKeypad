import sys

from PySide6 import QtWidgets, QtCore

import AdvancedOptions_ui


class AdvancedOptions(QtWidgets.QMainWindow, AdvancedOptions_ui.Ui_Dialog):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Advanced Options")


    def close(self, *args, **kwargs):
        print("Advanced Options Dialog hidden")
        super(AdvancedOptions, self).close(*args, **kwargs)

    def accept(self):
        pass

    def reject(self):
        pass