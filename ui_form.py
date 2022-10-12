# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.gridLayout = QGridLayout(MainWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.addSection = QPushButton(MainWindow)
        self.addSection.setObjectName(u"addSection")

        self.gridLayout.addWidget(self.addSection, 5, 3, 1, 1)

        self.itemSearch = QLineEdit(MainWindow)
        self.itemSearch.setObjectName(u"itemSearch")

        self.gridLayout.addWidget(self.itemSearch, 10, 3, 1, 1)

        self.taxImpSec = QPushButton(MainWindow)
        self.taxImpSec.setObjectName(u"taxImpSec")

        self.gridLayout.addWidget(self.taxImpSec, 8, 3, 1, 1)

        self.pbExit = QPushButton(MainWindow)
        self.pbExit.setObjectName(u"pbExit")

        self.gridLayout.addWidget(self.pbExit, 13, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.taxList = QComboBox(MainWindow)
        self.taxList.setObjectName(u"taxList")
        self.taxList.setEditable(False)

        self.gridLayout.addWidget(self.taxList, 1, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 9, 3, 1, 1)

        self.succesfull = QLabel(MainWindow)
        self.succesfull.setObjectName(u"succesfull")

        self.gridLayout.addWidget(self.succesfull, 3, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 7, 3, 1, 1)

        self.labelSections = QLabel(MainWindow)
        self.labelSections.setObjectName(u"labelSections")

        self.gridLayout.addWidget(self.labelSections, 5, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 12, 3, 1, 1)

        self.sectionList = QComboBox(MainWindow)
        self.sectionList.setObjectName(u"sectionList")

        self.gridLayout.addWidget(self.sectionList, 4, 3, 1, 1)

        self.labelItems = QLabel(MainWindow)
        self.labelItems.setObjectName(u"labelItems")

        self.gridLayout.addWidget(self.labelItems, 10, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 3, 1, 1)

        self.itemList = QTextEdit(MainWindow)
        self.itemList.setObjectName(u"itemList")
        self.itemList.setReadOnly(True)

        self.gridLayout.addWidget(self.itemList, 11, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 1, 1, 2)

        self.taxImpIt = QPushButton(MainWindow)
        self.taxImpIt.setObjectName(u"taxImpIt")

        self.gridLayout.addWidget(self.taxImpIt, 13, 3, 1, 1)

        self.loadJson = QPushButton(MainWindow)
        self.loadJson.setObjectName(u"loadJson")

        self.gridLayout.addWidget(self.loadJson, 1, 0, 1, 1)

        self.saveJson = QPushButton(MainWindow)
        self.saveJson.setObjectName(u"saveJson")

        self.gridLayout.addWidget(self.saveJson, 2, 0, 1, 1)

        self.labelTax = QLabel(MainWindow)
        self.labelTax.setObjectName(u"labelTax")
        self.labelTax.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelTax, 0, 3, 1, 1)

        self.addedSections = QTextEdit(MainWindow)
        self.addedSections.setObjectName(u"addedSections")
        self.addedSections.setReadOnly(True)

        self.gridLayout.addWidget(self.addedSections, 6, 3, 1, 1)

        self.allSections = QPushButton(MainWindow)
        self.allSections.setObjectName(u"allSections")

        self.gridLayout.addWidget(self.allSections, 2, 3, 1, 1)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.addSection.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.itemSearch.setText("")
        self.taxImpSec.setText(QCoreApplication.translate("MainWindow", u"Implement Sections Tax", None))
        self.pbExit.setText(QCoreApplication.translate("MainWindow", u"EXIT", None))
        self.taxList.setCurrentText("")
        self.succesfull.setText("")
        self.labelSections.setText(QCoreApplication.translate("MainWindow", u"Please select the sections to modify", None))
        self.labelItems.setText(QCoreApplication.translate("MainWindow", u"Please write the item name and press enter", None))
        self.taxImpIt.setText(QCoreApplication.translate("MainWindow", u"Implement Item Tax", None))
        self.loadJson.setText(QCoreApplication.translate("MainWindow", u"Load Json", None))
        self.saveJson.setText(QCoreApplication.translate("MainWindow", u"Save Json", None))
        self.labelTax.setText(QCoreApplication.translate("MainWindow", u"Please Select Tax Values", None))
        self.allSections.setText(QCoreApplication.translate("MainWindow", u"Change Tax to All Sections", None))
    # retranslateUi

