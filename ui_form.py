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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(772, 451)
        font = QFont()
        font.setFamilies([u"Yu Gothic"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        self.actionLoad_Json = QAction(MainWindow)
        self.actionLoad_Json.setObjectName(u"actionLoad_Json")
        icon = QIcon()
        icon.addFile(u"images/loadJson.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionLoad_Json.setIcon(icon)
        self.actionSave_Json = QAction(MainWindow)
        self.actionSave_Json.setObjectName(u"actionSave_Json")
        icon1 = QIcon()
        icon1.addFile(u"images/saveJson.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave_Json.setIcon(icon1)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon2 = QIcon()
        icon2.addFile(u"images/exit.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExit.setIcon(icon2)
        self.actionApply_Tax_to_All_Sections = QAction(MainWindow)
        self.actionApply_Tax_to_All_Sections.setObjectName(u"actionApply_Tax_to_All_Sections")
        self.actionRemove_Tax_from_All_Sections = QAction(MainWindow)
        self.actionRemove_Tax_from_All_Sections.setObjectName(u"actionRemove_Tax_from_All_Sections")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.addSection = QPushButton(self.centralwidget)
        self.addSection.setObjectName(u"addSection")

        self.gridLayout.addWidget(self.addSection, 4, 2, 1, 1)

        self.addedSections = QTextEdit(self.centralwidget)
        self.addedSections.setObjectName(u"addedSections")

        self.gridLayout.addWidget(self.addedSections, 7, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 7, 0, 1, 1)

        self.itemSearch = QLineEdit(self.centralwidget)
        self.itemSearch.setObjectName(u"itemSearch")

        self.gridLayout.addWidget(self.itemSearch, 4, 1, 1, 1)

        self.taxImpIt = QPushButton(self.centralwidget)
        self.taxImpIt.setObjectName(u"taxImpIt")

        self.gridLayout.addWidget(self.taxImpIt, 11, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 3, 1, 1, 1, Qt.AlignHCenter)

        self.itemList = QTextEdit(self.centralwidget)
        self.itemList.setObjectName(u"itemList")

        self.gridLayout.addWidget(self.itemList, 7, 1, 1, 1)

        self.sectionList = QComboBox(self.centralwidget)
        self.sectionList.setObjectName(u"sectionList")

        self.gridLayout.addWidget(self.sectionList, 3, 2, 1, 1)

        self.taxImpSec = QPushButton(self.centralwidget)
        self.taxImpSec.setObjectName(u"taxImpSec")

        self.gridLayout.addWidget(self.taxImpSec, 11, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 8, 0, 1, 1)

        self.taxList = QComboBox(self.centralwidget)
        self.taxList.setObjectName(u"taxList")

        self.gridLayout.addWidget(self.taxList, 4, 0, 1, 1)

        self.labelTax = QLabel(self.centralwidget)
        self.labelTax.setObjectName(u"labelTax")

        self.gridLayout.addWidget(self.labelTax, 3, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 772, 29))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuTax_Options = QMenu(self.menuEdit)
        self.menuTax_Options.setObjectName(u"menuTax_Options")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menuFile.addAction(self.actionLoad_Json)
        self.menuFile.addAction(self.actionSave_Json)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.menuTax_Options.menuAction())
        self.menuTax_Options.addAction(self.actionApply_Tax_to_All_Sections)
        self.menuTax_Options.addAction(self.actionRemove_Tax_from_All_Sections)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionLoad_Json.setText(QCoreApplication.translate("MainWindow", u"Load Json", None))
#if QT_CONFIG(shortcut)
        self.actionLoad_Json.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_Json.setText(QCoreApplication.translate("MainWindow", u"Save Json", None))
#if QT_CONFIG(shortcut)
        self.actionSave_Json.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionApply_Tax_to_All_Sections.setText(QCoreApplication.translate("MainWindow", u"Apply Tax to All Sections", None))
#if QT_CONFIG(shortcut)
        self.actionApply_Tax_to_All_Sections.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+T", None))
#endif // QT_CONFIG(shortcut)
        self.actionRemove_Tax_from_All_Sections.setText(QCoreApplication.translate("MainWindow", u"Remove Tax from All Sections", None))
#if QT_CONFIG(shortcut)
        self.actionRemove_Tax_from_All_Sections.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.addSection.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.taxImpIt.setText(QCoreApplication.translate("MainWindow", u"Implement Item Tax", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Write the item name and press enter", None))
        self.taxImpSec.setText(QCoreApplication.translate("MainWindow", u"Implement Sections Tax", None))
        self.labelTax.setText(QCoreApplication.translate("MainWindow", u"Please Select Tax Values", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuTax_Options.setTitle(QCoreApplication.translate("MainWindow", u"Tax Options", None))
    # retranslateUi

