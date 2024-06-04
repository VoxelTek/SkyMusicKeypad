import sys
import webbrowser
import companion_assets_rc
from PyQt6 import QtWidgets, uic

import keybindedit

import json

import serial
from serial.tools import list_ports

Ui_MainWindow1, QtBaseClass1 = uic.loadUiType("KeypadCompanion.ui")

class KeypadCompanion(QtWidgets.QMainWindow, Ui_MainWindow1):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow1.__init__(self)
        self.setupUi(self)

        self.ser = serial.Serial()

        self.config = {}

        self.setFixedSize(600, 400)

        self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).clicked.connect(self.accept)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Cancel).clicked.connect(self.reject)
        self.buttonBox.helpRequested.connect(self.help)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Save).clicked.connect(self.save)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Open).clicked.connect(self.open)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Discard).clicked.connect(self.discard)

        self.validLabel.hide()
        self.noDevice.show()
        self.keypadMode.enabled = False

        self.get_ports()
        self.device.setCurrentIndex(-1)
        self.device.currentIndexChanged.connect(self.switchToSerial)

        self.fileDialog = QtWidgets.QFileDialog()
        self.fileDialog.setFileMode(QtWidgets.QFileDialog.FileMode.AnyFile)
        self.fileDialog.setNameFilter("SkyMusic Keypad Settings (*.smk);;Generic Configuration File (*.json)")
    
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
        out_file = open(filename[0], "w") 
        json.dump(self.config, out_file, indent = 4)
        out_file.close()
    
    def open(self):
        filename = self.fileDialog.getOpenFileName(self, "Open File", "", "SkyMusic Keypad Settings (*.smk);;Generic Configuration File (*.json)")
        configFile = open(filename[0], "r")
        self.config = json.load(configFile)
        configFile.close()
        self.loadModes()



    def discard(self):
        self.config = {}

        if self.device.currentIndex() != -1:
            self.loadConfig()

    def pushSettings(self):
        request = {"type":"setcfg", "cfgdata": self.config}
        request_string = (json.dumps(request) + '\n').encode('utf-8')
        self.ser.write(request_string)
    
    def keymapsToConfig(self):
        if self.config != {}:
            #print("there is a config file")
            if (self.keypadMode.currentIndex() != -1) and (self.device.currentIndex() != -1):
                for keyCount in range(len(self.config["modes"][self.keypadMode.currentText()]) + 1):
                    if not(keyCount == 0):
                        self.config["modes"][self.keypadMode.currentText()][keyCount - 1] = self.findChild(keybindedit.keybindEdit, f"lineEdit_{keyCount:02}").text() 
                print(self.config["modes"][self.keypadMode.currentText()])

    def createNewProfile(self):
        text, ok = QtWidgets.QInputDialog().getText(self, "Create New Profile","Enter Profile Name:")
        if ok and text:
            if text in self.config["modes"].keys():
                alreadyExists = QtWidgets.QMessageBox()
                alreadyExists.setText("This mode already exists!")
                x = alreadyExists.exec()
                self.createNewProfile()
                return
            self.config["modes"][text] = []
            self.loadModes()
            self.keypadMode.setCurrentText(text)
        else:
            self.loadModes()
            return
        

    def loadKeymaps(self):
        #print(self.findChild(keybindedit.keybindEdit, "lineEdit_01"))
        if self.keypadMode.currentIndex() == (self.keypadMode.count() - 1):
            #print("Create New")
            self.createNewProfile()
            return
        
        self.config["mode"] = self.keypadMode.currentText()
        print(self.config["mode"])
        print(self.keypadMode.currentText())

        for keyCount in range(len(self.findChildren(keybindedit.keybindEdit)) + 1):
            if not(keyCount == 0):
                keybind_edit = self.findChild(keybindedit.keybindEdit, f"lineEdit_{keyCount:02}")

                try:
                    keybind_edit.textChanged.disconnect(self.keymapsToConfig)
                except:
                    pass
                #print(f"lineEdit_{keyCount:02}")
                
                try:
                    self.config["modes"][self.keypadMode.currentText()][keyCount - 1]
                except IndexError:
                    self.config["modes"][self.keypadMode.currentText()].append("")
                keybind_edit.setText(self.config["modes"][self.keypadMode.currentText()][keyCount - 1])
                keybind_edit.textChanged.connect(self.keymapsToConfig)
                #print(self.findChild(keybindedit.keybindEdit, f"lineEdit_{keyCount:02}").text())
        print(self.config)

    def loadModes(self):
        try:
            self.keypadMode.currentIndexChanged.disconnect()
        except:
            pass
        self.keypadMode.clear()
        self.keypadMode.setEnabled(True)
        #print(self.config["modes"])

        for key in self.config["modes"].keys():
            self.keypadMode.addItem(key)
        self.keypadMode.addItem("Create New...")
        self.keypadMode.setCurrentIndex(-1)
        self.keypadMode.currentIndexChanged.connect(self.loadKeymaps)

    def loadConfig(self):
        request = {"type":"getcfg"}
        request_string = (json.dumps(request) + '\n').encode('utf-8')
        self.ser.write(request_string)

        response = self.ser.readline().decode('utf-8').strip()
        response = json.loads(response)

        self.config = response["cfgdata"]
        print(self.config)

        self.loadModes()

    def switchToSerial(self):
        portNumber = self.device.currentIndex()
        self.ser = serial.Serial(self.device.currentText(), 115200, timeout=0.1)

        testData = {"type":"ping"}
        
        self.ser.write((json.dumps(testData) + '\n').encode('utf-8'))

        response = self.ser.readline().decode('utf-8').strip()

        print(response)

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
        if port != []:
            self.noDevice.hide()
        else:
            self.noDevice.show()
            self.device.setEnabled(False)
            return
        for p in port:
            print(p.device)
            self.device.addItem(p.device)
 



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = KeypadCompanion()
    window.show()

    sys.exit(app.exec()) 