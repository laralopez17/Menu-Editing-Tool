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
        MainWindow.resize(850, 506)
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        MainWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
        MainWindow.setAcceptDrops(True)
        MainWindow.setStyleSheet(u"")
        MainWindow.setInputMethodHints(Qt.ImhNone)
        self.gridLayout = QGridLayout(MainWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.addSection = QPushButton(MainWindow)
        self.addSection.setObjectName(u"addSection")

        self.gridLayout.addWidget(self.addSection, 4, 4, 1, 1)

        self.sectionList = QComboBox(MainWindow)
        self.sectionList.setObjectName(u"sectionList")

        self.gridLayout.addWidget(self.sectionList, 3, 4, 1, 1)

        self.taxList = QComboBox(MainWindow)
        self.taxList.setObjectName(u"taxList")
        self.taxList.setEditable(False)

        self.gridLayout.addWidget(self.taxList, 1, 4, 1, 1)

        self.itemList = QTextEdit(MainWindow)
        self.itemList.setObjectName(u"itemList")
        self.itemList.setReadOnly(True)

        self.gridLayout.addWidget(self.itemList, 5, 2, 1, 1)

        self.labelSections = QLabel(MainWindow)
        self.labelSections.setObjectName(u"labelSections")

        self.gridLayout.addWidget(self.labelSections, 2, 4, 1, 1)

        self.taxImpSec = QPushButton(MainWindow)
        self.taxImpSec.setObjectName(u"taxImpSec")

        self.gridLayout.addWidget(self.taxImpSec, 6, 4, 1, 1)

        self.allSections = QPushButton(MainWindow)
        self.allSections.setObjectName(u"allSections")

        self.gridLayout.addWidget(self.allSections, 7, 2, 1, 1)

        self.itemSearch = QLineEdit(MainWindow)
        self.itemSearch.setObjectName(u"itemSearch")

        self.gridLayout.addWidget(self.itemSearch, 3, 2, 1, 1)

        self.loadJson = QPushButton(MainWindow)
        self.loadJson.setObjectName(u"loadJson")

        self.gridLayout.addWidget(self.loadJson, 0, 0, 1, 1)

        self.labelItems = QLabel(MainWindow)
        self.labelItems.setObjectName(u"labelItems")

        self.gridLayout.addWidget(self.labelItems, 2, 2, 1, 1)

        self.pbExit = QPushButton(MainWindow)
        self.pbExit.setObjectName(u"pbExit")
        self.pbExit.setMinimumSize(QSize(281, 35))

        self.gridLayout.addWidget(self.pbExit, 7, 4, 1, 1)

        self.labelTax = QLabel(MainWindow)
        self.labelTax.setObjectName(u"labelTax")
        self.labelTax.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelTax, 0, 4, 1, 1)

        self.addedSections = QTextEdit(MainWindow)
        self.addedSections.setObjectName(u"addedSections")
        self.addedSections.setReadOnly(True)

        self.gridLayout.addWidget(self.addedSections, 5, 4, 1, 1)

        self.taxImpIt = QPushButton(MainWindow)
        self.taxImpIt.setObjectName(u"taxImpIt")

        self.gridLayout.addWidget(self.taxImpIt, 6, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 7, 3, 1, 1)

        self.saveJson = QPushButton(MainWindow)
        self.saveJson.setObjectName(u"saveJson")

        self.gridLayout.addWidget(self.saveJson, 1, 0, 1, 1)

        self.removeTax = QPushButton(MainWindow)
        self.removeTax.setObjectName(u"removeTax")

        self.gridLayout.addWidget(self.removeTax, 7, 0, 1, 1)

        self.jsonName = QLabel(MainWindow)
        self.jsonName.setObjectName(u"jsonName")

        self.gridLayout.addWidget(self.jsonName, 0, 2, 1, 1)

        QWidget.setTabOrder(self.loadJson, self.taxList)
        QWidget.setTabOrder(self.taxList, self.itemSearch)
        QWidget.setTabOrder(self.itemSearch, self.sectionList)
        QWidget.setTabOrder(self.sectionList, self.addSection)
        QWidget.setTabOrder(self.addSection, self.taxImpIt)
        QWidget.setTabOrder(self.taxImpIt, self.taxImpSec)
        QWidget.setTabOrder(self.taxImpSec, self.allSections)
        QWidget.setTabOrder(self.allSections, self.pbExit)
        QWidget.setTabOrder(self.pbExit, self.itemList)
        QWidget.setTabOrder(self.itemList, self.addedSections)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.addSection.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.taxList.setCurrentText("")
        self.labelSections.setText(QCoreApplication.translate("MainWindow", u"Please select the sections to modify", None))
        self.taxImpSec.setText(QCoreApplication.translate("MainWindow", u"Implement Sections Tax", None))
        self.allSections.setText(QCoreApplication.translate("MainWindow", u"Change Tax to All Sections", None))
        self.itemSearch.setText("")
        self.loadJson.setText(QCoreApplication.translate("MainWindow", u"Load Json", None))
        self.labelItems.setText(QCoreApplication.translate("MainWindow", u"Write the item name and press enter", None))
        self.pbExit.setText(QCoreApplication.translate("MainWindow", u"EXIT", None))
        self.labelTax.setText(QCoreApplication.translate("MainWindow", u"Please Select Tax Values", None))
        self.taxImpIt.setText(QCoreApplication.translate("MainWindow", u"Implement Item Tax", None))
        self.saveJson.setText(QCoreApplication.translate("MainWindow", u"Save Json", None))
        self.removeTax.setText(QCoreApplication.translate("MainWindow", u"Remove Tax To All menu", None))
        self.jsonName.setText("")
    # retranslateUi

