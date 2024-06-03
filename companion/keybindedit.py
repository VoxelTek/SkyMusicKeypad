from PyQt6 import QtWidgets
from PySide6 import QtCore


class keybindEdit(QtWidgets.QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.textEdited.connect(self.keybindChanged)
    
    def keybindChanged(self):
        self.setText(self.text().upper())
        if self.text() == "":
            return
        self.focusNextPrevChild(True)        
    
    def focusInEvent(self, e):
        super().focusInEvent(e)  # Call the base class implementation
        self.selectAll()  # Select all the text