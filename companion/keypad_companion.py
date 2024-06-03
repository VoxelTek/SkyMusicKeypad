import sys
import webbrowser
import companion_assets_rc
from PyQt6 import QtWidgets, uic

import serial
from serial.tools import list_ports

Ui_MainWindow1, QtBaseClass1 = uic.loadUiType("KeypadCompanion.ui")


class KeypadCompanion(QtWidgets.QMainWindow, Ui_MainWindow1):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow1.__init__(self)
        self.setupUi(self)

        self.setFixedSize(600, 400)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.buttonBox.helpRequested.connect(self.help)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Save).clicked.connect(self.save)
    
    def accept(self):
        self.pushSettings()
        self.close()
    def reject(self):
        self.close()

    def help(self):
        webbrowser.open("https://github.com/VoxelTek/SkyMusicKeypad/wiki", new=2)

    def save(self):
        pass

    def pushSettings(self):
        pass
 


def get_ports():
    port = list(list_ports.comports())
    for p in port:
        print(p.device)



if __name__ == "__main__":
    get_ports()
    app = QtWidgets.QApplication(sys.argv)
    window = KeypadCompanion()
    window.show()

    sys.exit(app.exec()) 