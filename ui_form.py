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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.gridLayout = QGridLayout(MainWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.taxlist = QListWidget(MainWindow)
        self.taxlist.setObjectName(u"taxlist")
        self.taxlist.setTabKeyNavigation(True)

        self.gridLayout.addWidget(self.taxlist, 0, 2, 2, 1)

        self.taxImp = QPushButton(MainWindow)
        self.taxImp.setObjectName(u"taxImp")

        self.gridLayout.addWidget(self.taxImp, 7, 2, 1, 1)

        self.labelSections = QLabel(MainWindow)
        self.labelSections.setObjectName(u"labelSections")

        self.gridLayout.addWidget(self.labelSections, 3, 1, 1, 1)

        self.saveJson = QPushButton(MainWindow)
        self.saveJson.setObjectName(u"saveJson")

        self.gridLayout.addWidget(self.saveJson, 1, 0, 1, 1)

        self.sectionlist = QListWidget(MainWindow)
        self.sectionlist.setObjectName(u"sectionlist")
        self.sectionlist.setTabKeyNavigation(True)
        self.sectionlist.setSelectionMode(QAbstractItemView.MultiSelection)

        self.gridLayout.addWidget(self.sectionlist, 3, 2, 1, 1)

        self.loadJson = QPushButton(MainWindow)
        self.loadJson.setObjectName(u"loadJson")

        self.gridLayout.addWidget(self.loadJson, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 4, 2, 1, 1)

        self.labelTax = QLabel(MainWindow)
        self.labelTax.setObjectName(u"labelTax")

        self.gridLayout.addWidget(self.labelTax, 0, 1, 1, 1)

        self.itemSearch = QLineEdit(MainWindow)
        self.itemSearch.setObjectName(u"itemSearch")

        self.gridLayout.addWidget(self.itemSearch, 5, 2, 1, 1)

        self.labelItems = QLabel(MainWindow)
        self.labelItems.setObjectName(u"labelItems")

        self.gridLayout.addWidget(self.labelItems, 5, 1, 1, 1)

        self.itemList = QTextEdit(MainWindow)
        self.itemList.setObjectName(u"itemList")
        self.itemList.setReadOnly(True)

        self.gridLayout.addWidget(self.itemList, 6, 2, 1, 1)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.taxImp.setText(QCoreApplication.translate("MainWindow", u"Implement Tax", None))
        self.labelSections.setText(QCoreApplication.translate("MainWindow", u"Please select as the sections to modify", None))
        self.saveJson.setText(QCoreApplication.translate("MainWindow", u"Save Json", None))
        self.loadJson.setText(QCoreApplication.translate("MainWindow", u"Load Json", None))
        self.labelTax.setText(QCoreApplication.translate("MainWindow", u"Please select Tax values", None))
        self.itemSearch.setText("")
        self.labelItems.setText(QCoreApplication.translate("MainWindow", u"Please write the item name and press enter", None))
    # retranslateUi

