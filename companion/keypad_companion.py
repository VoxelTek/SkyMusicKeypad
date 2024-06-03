import sys
import webbrowser
import companion_assets_rc
from PyQt6 import QtWidgets, uic

import json

import serial
from serial.tools import list_ports

Ui_MainWindow1, QtBaseClass1 = uic.loadUiType("KeypadCompanion.ui")

port = None

ser = serial.Serial()

config = {}

class KeypadCompanion(QtWidgets.QMainWindow, Ui_MainWindow1):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow1.__init__(self)
        self.setupUi(self)

        self.setFixedSize(600, 400)

        self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).clicked.connect(self.accept)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Cancel).clicked.connect(self.reject)
        self.buttonBox.helpRequested.connect(self.help)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Save).clicked.connect(self.save)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Open).clicked.connect(self.open)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Discard).clicked.connect(self.discard)

        self.get_ports()
        self.device.setCurrentIndex(-1)
        self.device.currentIndexChanged.connect(self.switchToSerial)

        

        self.fileDialog = QtWidgets.QFileDialog()
        self.fileDialog.setFileMode(QtWidgets.QFileDialog.FileMode.AnyFile)
        self.fileDialog.setNameFilter("SkyMusic Keypad Settings (*.smk);;Generic Configuration File (*.json)")

        self.validLabel.hide()
    
    def accept(self):
        print("accept")
        self.pushSettings()
        self.close()
    def reject(self):
        print("reject")
        self.close()

    def help(self):
        webbrowser.open("https://github.com/VoxelTek/SkyMusicKeypad/wiki", new=2)

    def save(self):
        filename = self.fileDialog.getSaveFileName(self, "Save File", "", "SkyMusic Keypad Settings (*.smk);;Generic Configuration File (*.json)")
        print(filename[0])
    
    def open(self):
        filename = self.fileDialog.getOpenFileName(self, "Open File", "", "SkyMusic Keypad Settings (*.smk);;Generic Configuration File (*.json)")
        print(filename[0])

    def discard(self):
        pass

    def pushSettings(self):
        pass

    def loadConfig(self):
        pass

    def checkIfValidDevice(self):
        ser.write(b'{"type":"ping"}')
        response = ser.readline()
        print(response)
        if response == b'{"type":"pong"}':
            print("Device is valid")
            self.validLabel.hide()
        else:
            print("Device is not valid")
            self.validLabel.show()
        loadConfig()

    def switchToSerial(self):
        portNumber = self.device.currentIndex()
        ser = serial.Serial(self.device.currentText(), 115200, timeout=1)

        testData = {"type":"ping"}
        
        ser.write((json.dumps(testData) + '\n').encode('utf-8'))
        #print((str(testData)))
        response = ser.readline().decode('utf-8').strip()
        print(response)

        print(json.loads(response))

        try:
            response = json.loads(response)
        except:
            print("Device is not valid")
            self.validLabel.show()
            return
        if response["type"] == "pong":
            print("Device is valid")
            self.validLabel.hide()
        else:
            print("Device is not valid")
            self.validLabel.show()
            return
        self.loadConfig()
        
        #self.checkIfValidDevice()
    
    def get_ports(self):
        self.device.clear()
        port = list(list_ports.comports())
        for p in port:
            print(p.device)
            self.device.addItem(p.device)
 



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = KeypadCompanion()
    window.show()

    sys.exit(app.exec()) 