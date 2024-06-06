# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Companion_Advanced.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDockWidget, QGridLayout,
    QLabel, QLayout, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        if not DockWidget.objectName():
            DockWidget.setObjectName(u"DockWidget")
        DockWidget.resize(300, 400)
        DockWidget.setMaximumSize(QSize(300, 400))
        DockWidget.setAllowedAreas(Qt.DockWidgetArea.RightDockWidgetArea)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout = QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.rotaryOptionGrid = QGridLayout()
        self.rotaryOptionGrid.setObjectName(u"rotaryOptionGrid")
        self.rotaryOptionGrid.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.rotaryMIDI = QComboBox(self.dockWidgetContents)
        self.rotaryMIDI.setObjectName(u"rotaryMIDI")

        self.rotaryOptionGrid.addWidget(self.rotaryMIDI, 0, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.rotKey_label = QLabel(self.dockWidgetContents)
        self.rotKey_label.setObjectName(u"rotKey_label")

        self.rotaryOptionGrid.addWidget(self.rotKey_label, 3, 0, 1, 1, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.rotaryOptionGrid.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.rotaryKeyboard = QComboBox(self.dockWidgetContents)
        self.rotaryKeyboard.setObjectName(u"rotaryKeyboard")

        self.rotaryOptionGrid.addWidget(self.rotaryKeyboard, 3, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.rotMIDI_held_label = QLabel(self.dockWidgetContents)
        self.rotMIDI_held_label.setObjectName(u"rotMIDI_held_label")

        self.rotaryOptionGrid.addWidget(self.rotMIDI_held_label, 1, 0, 1, 1, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)

        self.rotMIDI_label = QLabel(self.dockWidgetContents)
        self.rotMIDI_label.setObjectName(u"rotMIDI_label")

        self.rotaryOptionGrid.addWidget(self.rotMIDI_label, 0, 0, 1, 1, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)

        self.rotaryMIDI_held = QComboBox(self.dockWidgetContents)
        self.rotaryMIDI_held.setObjectName(u"rotaryMIDI_held")

        self.rotaryOptionGrid.addWidget(self.rotaryMIDI_held, 1, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.rotKey_held_label = QLabel(self.dockWidgetContents)
        self.rotKey_held_label.setObjectName(u"rotKey_held_label")

        self.rotaryOptionGrid.addWidget(self.rotKey_held_label, 4, 0, 1, 1, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)

        self.rotaryKeyboard_held = QComboBox(self.dockWidgetContents)
        self.rotaryKeyboard_held.setObjectName(u"rotaryKeyboard_held")

        self.rotaryOptionGrid.addWidget(self.rotaryKeyboard_held, 4, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.rotaryOptionGrid.addItem(self.verticalSpacer_2, 2, 1, 1, 1)


        self.gridLayout.addLayout(self.rotaryOptionGrid, 0, 0, 1, 1)

        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)

        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"DockWidget", None))
        self.rotKey_label.setText(QCoreApplication.translate("DockWidget", u"Rotary function -- Keyboard:", None))
        self.rotMIDI_held_label.setText(QCoreApplication.translate("DockWidget", u"Rotary function -- MIDI (held):", None))
        self.rotMIDI_label.setText(QCoreApplication.translate("DockWidget", u"Rotary function -- MIDI:", None))
        self.rotKey_held_label.setText(QCoreApplication.translate("DockWidget", u"Rotary function -- Keyboard (held):", None))
    # retranslateUi

