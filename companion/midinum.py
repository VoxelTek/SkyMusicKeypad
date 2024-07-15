from PySide6 import QtWidgets

class midiNum(QtWidgets.QSpinBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons) 
        self.setMaximum(108)
        self.setMinimum(0)