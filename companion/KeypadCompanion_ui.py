# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'KeypadCompanion.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGridLayout, QLabel, QLineEdit,
    QSizePolicy, QWidget)
import companion_assets_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(600, 400)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(5, 350, 591, 41))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Help|QDialogButtonBox.StandardButton.Ok|QDialogButtonBox.StandardButton.Open|QDialogButtonBox.StandardButton.RestoreDefaults|QDialogButtonBox.StandardButton.Save)
        self.buttonBox.setCenterButtons(False)
        self.keypadMode = QComboBox(Dialog)
        self.keypadMode.setObjectName(u"keypadMode")
        self.keypadMode.setGeometry(QRect(290, 50, 100, 21))
        self.label_mapMode = QLabel(Dialog)
        self.label_mapMode.setObjectName(u"label_mapMode")
        self.label_mapMode.setGeometry(QRect(150, 42, 141, 36))
        self.label_device = QLabel(Dialog)
        self.label_device.setObjectName(u"label_device")
        self.label_device.setGeometry(QRect(240, 2, 51, 36))
        self.device = QComboBox(Dialog)
        self.device.setObjectName(u"device")
        self.device.setGeometry(QRect(290, 10, 100, 21))
        self.gridLayoutWidget = QWidget(Dialog)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(50, 110, 491, 231))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_5 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(15)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet(u"image: url(:/keyIcons/assets/skyMusic_circle.svg);")
        self.lineEdit_5.setText(u"")
        self.lineEdit_5.setMaxLength(1)
        self.lineEdit_5.setFrame(False)
        self.lineEdit_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_5, 0, 9, 1, 1)

        self.lineEdit_4 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setAutoFillBackground(False)
        self.lineEdit_4.setStyleSheet(u"image: url(:/keyIcons/assets/skyMusic_square.svg);")
        self.lineEdit_4.setText(u"")
        self.lineEdit_4.setMaxLength(1)
        self.lineEdit_4.setFrame(False)
        self.lineEdit_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_4, 0, 8, 1, 1)

        self.lineEdit_1 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        sizePolicy.setHeightForWidth(self.lineEdit_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_1.setSizePolicy(sizePolicy)
        self.lineEdit_1.setFont(font)
        self.lineEdit_1.setStyleSheet(u"image: url(:/keyIcons/assets/skyMusic_both.svg);")
        self.lineEdit_1.setText(u"")
        self.lineEdit_1.setMaxLength(1)
        self.lineEdit_1.setFrame(False)
        self.lineEdit_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_1, 0, 5, 1, 1)

        self.lineEdit_9 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        sizePolicy.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setAutoFillBackground(False)
        self.lineEdit_9.setStyleSheet(u"image: url(:/keyIcons/assets/skyMusic_square.svg);")
        self.lineEdit_9.setText(u"")
        self.lineEdit_9.setMaxLength(1)
        self.lineEdit_9.setFrame(False)
        self.lineEdit_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_9, 1, 8, 1, 1)

        self.lineEdit_3 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet(u"image: url(:/keyIcons/assets/skyMusic_circle.svg);")
        self.lineEdit_3.setText(u"")
        self.lineEdit_3.setMaxLength(1)
        self.lineEdit_3.setFrame(False)
        self.lineEdit_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_3, 0, 7, 1, 1)

        self.lineEdit_10 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        sizePolicy.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setStyleSheet(u"image: url(:/keyIcons/assets/skyMusic_circle.svg);")
        self.lineEdit_10.setText(u"")
        self.lineEdit_10.setMaxLength(1)
        self.lineEdit_10.setFrame(False)
        self.lineEdit_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_10, 1, 9, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setStyleSheet(u"image: url(:/keyIcons/assets/skyMusic_square.svg);")
        self.lineEdit_2.setText(u"")
        self.lineEdit_2.setMaxLength(1)
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_2, 0, 6, 1, 1)

        self.lineEdit_6 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        sizePolicy.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet(u"image: url(:/keyIcons/assets/skyMusic_circle.svg);")
        self.lineEdit_6.setText(u"")
        self.lineEdit_6.setMaxLength(1)
        self.lineEdit_6.setFrame(False)
        self.lineEdit_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_6, 1, 5, 1, 1)

        self.lineEdit_8 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        sizePolicy.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setStyleSheet(u"image: url(:/keyIcons/assets/skyMusic_both.svg);")
        self.lineEdit_8.setText(u"")
        self.lineEdit_8.setMaxLength(1)
        self.lineEdit_8.setFrame(False)
        self.lineEdit_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_8, 1, 7, 1, 1)

        self.lineEdit_7 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        sizePolicy.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setAutoFillBackground(False)
        self.lineEdit_7.setStyleSheet(u"image: url(:/keyIcons/assets/skyMusic_square.svg);")
        self.lineEdit_7.setText(u"")
        self.lineEdit_7.setMaxLength(1)
        self.lineEdit_7.setFrame(False)
        self.lineEdit_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_7, 1, 6, 1, 1)

        self.lineEdit_11 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        sizePolicy.setHeightForWidth(self.lineEdit_11.sizePolicy().hasHeightForWidth())
        self.lineEdit_11.setSizePolicy(sizePolicy)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setStyleSheet(u"image: url(:/keyIcons/assets/skyMusic_circle.svg);")
        self.lineEdit_11.setText(u"")
        self.lineEdit_11.setMaxLength(1)
        self.lineEdit_11.setFrame(False)
        self.lineEdit_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_11, 2, 5, 1, 1)

        self.lineEdit_12 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        sizePolicy.setHeightForWidth(self.lineEdit_12.sizePolicy().hasHeightForWidth())
        self.lineEdit_12.setSizePolicy(sizePolicy)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setAutoFillBackground(False)
        self.lineEdit_12.setStyleSheet(u"image: url(:/keyIcons/assets/skyMusic_square.svg);")
        self.lineEdit_12.setText(u"")
        self.lineEdit_12.setMaxLength(1)
        self.lineEdit_12.setFrame(False)
        self.lineEdit_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_12, 2, 6, 1, 1)

        self.lineEdit_13 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        sizePolicy.setHeightForWidth(self.lineEdit_13.sizePolicy().hasHeightForWidth())
        self.lineEdit_13.setSizePolicy(sizePolicy)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setStyleSheet(u"image: url(:/keyIcons/assets/skyMusic_circle.svg);")
        self.lineEdit_13.setText(u"")
        self.lineEdit_13.setMaxLength(1)
        self.lineEdit_13.setFrame(False)
        self.lineEdit_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_13, 2, 7, 1, 1)

        self.lineEdit_14 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        sizePolicy.setHeightForWidth(self.lineEdit_14.sizePolicy().hasHeightForWidth())
        self.lineEdit_14.setSizePolicy(sizePolicy)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setAutoFillBackground(False)
        self.lineEdit_14.setStyleSheet(u"image: url(:/keyIcons/assets/skyMusic_square.svg);")
        self.lineEdit_14.setText(u"")
        self.lineEdit_14.setMaxLength(1)
        self.lineEdit_14.setFrame(False)
        self.lineEdit_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_14, 2, 8, 1, 1)

        self.lineEdit_15 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        sizePolicy.setHeightForWidth(self.lineEdit_15.sizePolicy().hasHeightForWidth())
        self.lineEdit_15.setSizePolicy(sizePolicy)
        self.lineEdit_15.setFont(font)
        self.lineEdit_15.setStyleSheet(u"image: url(:/keyIcons/assets/skyMusic_both.svg);")
        self.lineEdit_15.setText(u"")
        self.lineEdit_15.setMaxLength(1)
        self.lineEdit_15.setFrame(False)
        self.lineEdit_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_15, 2, 9, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Sky Keypad Companion", None))
        self.label_mapMode.setText(QCoreApplication.translate("Dialog", u"Keypad Mapping Mode:", None))
        self.label_device.setText(QCoreApplication.translate("Dialog", u"Device:", None))
    # retranslateUi

