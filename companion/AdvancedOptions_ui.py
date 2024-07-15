# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AdvancedOptions.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QLabel, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(320, 240)
        self.gridLayoutWidget = QWidget(Dialog)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(9, 9, 304, 221))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)

        self.comboBox_5 = QComboBox(self.gridLayoutWidget)
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.gridLayout.addWidget(self.comboBox_5, 2, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)

        self.comboBox = QComboBox(self.gridLayoutWidget)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.comboBox_3 = QComboBox(self.gridLayoutWidget)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout.addWidget(self.comboBox_3, 1, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)

        self.comboBox_4 = QComboBox(self.gridLayoutWidget)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.gridLayout.addWidget(self.comboBox_4, 4, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)

        self.comboBox_2 = QComboBox(self.gridLayoutWidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 3, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)

        self.comboBox_6 = QComboBox(self.gridLayoutWidget)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.gridLayout.addWidget(self.comboBox_6, 5, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Knob function (keybinds):", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("Dialog", u"Cycle modes", None))

        self.label_2.setText(QCoreApplication.translate("Dialog", u"Knob function (MIDI):", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Volume", None))

        self.label_5.setText(QCoreApplication.translate("Dialog", u"[Clicked] Knob function (keybinds):", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("Dialog", u"Volume", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("Dialog", u"Note", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("Dialog", u"Octave", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("Dialog", u"Pitch", None))

        self.label_4.setText(QCoreApplication.translate("Dialog", u"[Held] Knob function (MIDI):", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Dialog", u"Volume", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Dialog", u"Note", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Dialog", u"Octave", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("Dialog", u"Pitch", None))

        self.label_3.setText(QCoreApplication.translate("Dialog", u"[Held] Knob function (keybinds):", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"[Clicked] Knob function (MIDI):", None))
        self.comboBox_6.setItemText(0, QCoreApplication.translate("Dialog", u"Volume", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("Dialog", u"Note", None))
        self.comboBox_6.setItemText(2, QCoreApplication.translate("Dialog", u"Octave", None))
        self.comboBox_6.setItemText(3, QCoreApplication.translate("Dialog", u"Pitch", None))

    # retranslateUi

