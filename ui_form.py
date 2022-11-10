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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QTabWidget, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(860, 734)
        font = QFont()
        font.setFamilies([u"Yu Gothic"])
        font.setPointSize(9)
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
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.TAXBUTTON = QPushButton(self.centralwidget)
        self.TAXBUTTON.setObjectName(u"TAXBUTTON")

        self.gridLayout_3.addWidget(self.TAXBUTTON, 0, 0, 1, 1)

        self.PRICEBUTTON = QPushButton(self.centralwidget)
        self.PRICEBUTTON.setObjectName(u"PRICEBUTTON")

        self.gridLayout_3.addWidget(self.PRICEBUTTON, 0, 1, 1, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.pricePage = QWidget()
        self.pricePage.setObjectName(u"pricePage")
        self.gridLayout_10 = QGridLayout(self.pricePage)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.leIncrease = QLineEdit(self.pricePage)
        self.leIncrease.setObjectName(u"leIncrease")

        self.gridLayout_10.addWidget(self.leIncrease, 1, 4, 1, 2)

        self.line_2 = QFrame(self.pricePage)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_10.addWidget(self.line_2, 3, 0, 1, 7)

        self.tabWidget_2 = QTabWidget(self.pricePage)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_13 = QGridLayout(self.tab_5)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.sectionModification_2 = QGroupBox(self.tab_5)
        self.sectionModification_2.setObjectName(u"sectionModification_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sectionModification_2.sizePolicy().hasHeightForWidth())
        self.sectionModification_2.setSizePolicy(sizePolicy)
        self.gridLayout_12 = QGridLayout(self.sectionModification_2)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.addSection_2 = QPushButton(self.sectionModification_2)
        self.addSection_2.setObjectName(u"addSection_2")

        self.gridLayout_12.addWidget(self.addSection_2, 3, 1, 1, 2)

        self.sectionList_2 = QComboBox(self.sectionModification_2)
        self.sectionList_2.setObjectName(u"sectionList_2")
        self.sectionList_2.setEnabled(True)

        self.gridLayout_12.addWidget(self.sectionList_2, 1, 1, 1, 2)

        self.priceImpSec = QPushButton(self.sectionModification_2)
        self.priceImpSec.setObjectName(u"priceImpSec")

        self.gridLayout_12.addWidget(self.priceImpSec, 6, 1, 1, 2)

        self.addedSections_2 = QTextEdit(self.sectionModification_2)
        self.addedSections_2.setObjectName(u"addedSections_2")

        self.gridLayout_12.addWidget(self.addedSections_2, 5, 1, 1, 2)

        self.labelSection_2 = QLabel(self.sectionModification_2)
        self.labelSection_2.setObjectName(u"labelSection_2")
        font1 = QFont()
        font1.setFamilies([u"Yu Gothic"])
        font1.setPointSize(10)
        self.labelSection_2.setFont(font1)

        self.gridLayout_12.addWidget(self.labelSection_2, 0, 1, 1, 2, Qt.AlignHCenter)

        self.modOS = QCheckBox(self.sectionModification_2)
        self.modOS.setObjectName(u"modOS")
        self.modOS.setCheckable(True)

        self.gridLayout_12.addWidget(self.modOS, 2, 2, 1, 1)

        self.modMO = QCheckBox(self.sectionModification_2)
        self.modMO.setObjectName(u"modMO")
        self.modMO.setCheckable(True)
        self.modMO.setChecked(True)

        self.gridLayout_12.addWidget(self.modMO, 2, 1, 1, 1)


        self.gridLayout_13.addWidget(self.sectionModification_2, 0, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_13, 0, 0, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_14, 0, 4, 1, 1)

        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_15 = QGridLayout(self.tab_6)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.horizontalSpacer_15 = QSpacerItem(231, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_15, 0, 0, 1, 1)

        self.itemsModification_2 = QGroupBox(self.tab_6)
        self.itemsModification_2.setObjectName(u"itemsModification_2")
        sizePolicy.setHeightForWidth(self.itemsModification_2.sizePolicy().hasHeightForWidth())
        self.itemsModification_2.setSizePolicy(sizePolicy)
        self.gridLayout_14 = QGridLayout(self.itemsModification_2)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.priceImpIt = QPushButton(self.itemsModification_2)
        self.priceImpIt.setObjectName(u"priceImpIt")

        self.gridLayout_14.addWidget(self.priceImpIt, 6, 0, 1, 2)

        self.itemsList_2 = QComboBox(self.itemsModification_2)
        self.itemsList_2.setObjectName(u"itemsList_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.itemsList_2.sizePolicy().hasHeightForWidth())
        self.itemsList_2.setSizePolicy(sizePolicy1)
        self.itemsList_2.setModelColumn(0)

        self.gridLayout_14.addWidget(self.itemsList_2, 1, 0, 1, 2)

        self.addedItems_2 = QTextEdit(self.itemsModification_2)
        self.addedItems_2.setObjectName(u"addedItems_2")

        self.gridLayout_14.addWidget(self.addedItems_2, 5, 0, 1, 2)

        self.labelItems_2 = QLabel(self.itemsModification_2)
        self.labelItems_2.setObjectName(u"labelItems_2")
        self.labelItems_2.setFont(font1)

        self.gridLayout_14.addWidget(self.labelItems_2, 0, 0, 1, 2, Qt.AlignHCenter)

        self.addItem_2 = QPushButton(self.itemsModification_2)
        self.addItem_2.setObjectName(u"addItem_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.addItem_2.sizePolicy().hasHeightForWidth())
        self.addItem_2.setSizePolicy(sizePolicy2)

        self.gridLayout_14.addWidget(self.addItem_2, 3, 0, 1, 2)

        self.modMO1 = QCheckBox(self.itemsModification_2)
        self.modMO1.setObjectName(u"modMO1")
        self.modMO1.setChecked(True)

        self.gridLayout_14.addWidget(self.modMO1, 2, 0, 1, 1)

        self.modSO1 = QCheckBox(self.itemsModification_2)
        self.modSO1.setObjectName(u"modSO1")

        self.gridLayout_14.addWidget(self.modSO1, 2, 1, 1, 1)


        self.gridLayout_15.addWidget(self.itemsModification_2, 0, 1, 2, 1)

        self.horizontalSpacer_16 = QSpacerItem(227, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_16, 0, 2, 1, 1)

        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.gridLayout_17 = QGridLayout(self.tab_7)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.horizontalSpacer_17 = QSpacerItem(231, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_17, 0, 0, 1, 1)

        self.optionSetModification_2 = QGroupBox(self.tab_7)
        self.optionSetModification_2.setObjectName(u"optionSetModification_2")
        sizePolicy.setHeightForWidth(self.optionSetModification_2.sizePolicy().hasHeightForWidth())
        self.optionSetModification_2.setSizePolicy(sizePolicy)
        self.gridLayout_16 = QGridLayout(self.optionSetModification_2)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.addOS_2 = QPushButton(self.optionSetModification_2)
        self.addOS_2.setObjectName(u"addOS_2")

        self.gridLayout_16.addWidget(self.addOS_2, 3, 0, 1, 2)

        self.osList_2 = QComboBox(self.optionSetModification_2)
        self.osList_2.setObjectName(u"osList_2")

        self.gridLayout_16.addWidget(self.osList_2, 1, 0, 1, 2)

        self.labelOS_2 = QLabel(self.optionSetModification_2)
        self.labelOS_2.setObjectName(u"labelOS_2")

        self.gridLayout_16.addWidget(self.labelOS_2, 0, 0, 1, 2, Qt.AlignHCenter)

        self.priceImpOS = QPushButton(self.optionSetModification_2)
        self.priceImpOS.setObjectName(u"priceImpOS")

        self.gridLayout_16.addWidget(self.priceImpOS, 5, 0, 1, 2)

        self.optionsList_2 = QComboBox(self.optionSetModification_2)
        self.optionsList_2.setObjectName(u"optionsList_2")

        self.gridLayout_16.addWidget(self.optionsList_2, 2, 0, 1, 2)

        self.addedOS_2 = QTextEdit(self.optionSetModification_2)
        self.addedOS_2.setObjectName(u"addedOS_2")

        self.gridLayout_16.addWidget(self.addedOS_2, 4, 0, 1, 2)


        self.gridLayout_17.addWidget(self.optionSetModification_2, 0, 1, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(231, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_18, 0, 2, 1, 1)

        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.gridLayout_19 = QGridLayout(self.tab_8)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.horizontalSpacer_19 = QSpacerItem(231, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_19, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.tab_8)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_18 = QGridLayout(self.groupBox_2)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.modMO2 = QCheckBox(self.groupBox_2)
        self.modMO2.setObjectName(u"modMO2")
        self.modMO2.setCheckable(True)
        self.modMO2.setChecked(True)

        self.gridLayout_18.addWidget(self.modMO2, 3, 0, 1, 1)

        self.modSO2 = QCheckBox(self.groupBox_2)
        self.modSO2.setObjectName(u"modSO2")

        self.gridLayout_18.addWidget(self.modSO2, 3, 1, 1, 1)

        self.smartSearchList_2 = QComboBox(self.groupBox_2)
        self.smartSearchList_2.setObjectName(u"smartSearchList_2")

        self.gridLayout_18.addWidget(self.smartSearchList_2, 2, 0, 1, 2)

        self.leSmartSearch_2 = QLineEdit(self.groupBox_2)
        self.leSmartSearch_2.setObjectName(u"leSmartSearch_2")

        self.gridLayout_18.addWidget(self.leSmartSearch_2, 1, 0, 1, 2)

        self.labelSmartSearch_2 = QLabel(self.groupBox_2)
        self.labelSmartSearch_2.setObjectName(u"labelSmartSearch_2")

        self.gridLayout_18.addWidget(self.labelSmartSearch_2, 0, 0, 1, 2, Qt.AlignHCenter)

        self.addSmartSearch_2 = QPushButton(self.groupBox_2)
        self.addSmartSearch_2.setObjectName(u"addSmartSearch_2")

        self.gridLayout_18.addWidget(self.addSmartSearch_2, 6, 0, 1, 2)

        self.addedSS_2 = QTextEdit(self.groupBox_2)
        self.addedSS_2.setObjectName(u"addedSS_2")

        self.gridLayout_18.addWidget(self.addedSS_2, 7, 0, 1, 2)

        self.priceImpSmartSearch = QPushButton(self.groupBox_2)
        self.priceImpSmartSearch.setObjectName(u"priceImpSmartSearch")

        self.gridLayout_18.addWidget(self.priceImpSmartSearch, 8, 0, 1, 2)


        self.gridLayout_19.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(231, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_20, 0, 2, 1, 1)

        self.tabWidget_2.addTab(self.tab_8, "")

        self.gridLayout_10.addWidget(self.tabWidget_2, 4, 0, 1, 7)

        self.priceListSelected = QComboBox(self.pricePage)
        self.priceListSelected.addItem("")
        self.priceListSelected.addItem("")
        self.priceListSelected.addItem("")
        self.priceListSelected.setObjectName(u"priceListSelected")

        self.gridLayout_10.addWidget(self.priceListSelected, 1, 0, 1, 3)

        self.price = QLabel(self.pricePage)
        self.price.setObjectName(u"price")

        self.gridLayout_10.addWidget(self.price, 2, 2, 1, 4)

        self.labelInfo = QLabel(self.pricePage)
        self.labelInfo.setObjectName(u"labelInfo")

        self.gridLayout_10.addWidget(self.labelInfo, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.pricePage)
        self.taxPage = QWidget()
        self.taxPage.setObjectName(u"taxPage")
        self.gridLayout_11 = QGridLayout(self.taxPage)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.taxList = QComboBox(self.taxPage)
        self.taxList.setObjectName(u"taxList")

        self.gridLayout_11.addWidget(self.taxList, 2, 1, 1, 1)

        self.tabWidget = QTabWidget(self.taxPage)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setFocusPolicy(Qt.TabFocus)
        self.tabWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_8 = QGridLayout(self.tab)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.sectionModification = QGroupBox(self.tab)
        self.sectionModification.setObjectName(u"sectionModification")
        sizePolicy.setHeightForWidth(self.sectionModification.sizePolicy().hasHeightForWidth())
        self.sectionModification.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.sectionModification)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.addSection = QPushButton(self.sectionModification)
        self.addSection.setObjectName(u"addSection")

        self.gridLayout_2.addWidget(self.addSection, 3, 1, 1, 2)

        self.sectionList = QComboBox(self.sectionModification)
        self.sectionList.setObjectName(u"sectionList")
        self.sectionList.setEnabled(True)

        self.gridLayout_2.addWidget(self.sectionList, 1, 1, 1, 2)

        self.taxImpSec = QPushButton(self.sectionModification)
        self.taxImpSec.setObjectName(u"taxImpSec")

        self.gridLayout_2.addWidget(self.taxImpSec, 6, 1, 1, 2)

        self.addedSections = QTextEdit(self.sectionModification)
        self.addedSections.setObjectName(u"addedSections")

        self.gridLayout_2.addWidget(self.addedSections, 5, 1, 1, 2)

        self.labelSection = QLabel(self.sectionModification)
        self.labelSection.setObjectName(u"labelSection")
        self.labelSection.setFont(font1)

        self.gridLayout_2.addWidget(self.labelSection, 0, 1, 1, 2, Qt.AlignHCenter)


        self.gridLayout_8.addWidget(self.sectionModification, 0, 2, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_8, 0, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_6, 0, 4, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_7 = QGridLayout(self.tab_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.itemsModification = QGroupBox(self.tab_2)
        self.itemsModification.setObjectName(u"itemsModification")
        sizePolicy.setHeightForWidth(self.itemsModification.sizePolicy().hasHeightForWidth())
        self.itemsModification.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.itemsModification)
        self.gridLayout.setObjectName(u"gridLayout")
        self.taxImpIt = QPushButton(self.itemsModification)
        self.taxImpIt.setObjectName(u"taxImpIt")

        self.gridLayout.addWidget(self.taxImpIt, 6, 0, 1, 2)

        self.itemsList = QComboBox(self.itemsModification)
        self.itemsList.setObjectName(u"itemsList")
        sizePolicy1.setHeightForWidth(self.itemsList.sizePolicy().hasHeightForWidth())
        self.itemsList.setSizePolicy(sizePolicy1)
        self.itemsList.setModelColumn(0)

        self.gridLayout.addWidget(self.itemsList, 1, 0, 1, 2)

        self.addedItems = QTextEdit(self.itemsModification)
        self.addedItems.setObjectName(u"addedItems")

        self.gridLayout.addWidget(self.addedItems, 5, 0, 1, 2)

        self.labelItems = QLabel(self.itemsModification)
        self.labelItems.setObjectName(u"labelItems")
        self.labelItems.setFont(font1)

        self.gridLayout.addWidget(self.labelItems, 0, 0, 1, 2, Qt.AlignHCenter)

        self.addItem = QPushButton(self.itemsModification)
        self.addItem.setObjectName(u"addItem")
        sizePolicy2.setHeightForWidth(self.addItem.sizePolicy().hasHeightForWidth())
        self.addItem.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.addItem, 3, 0, 1, 2)


        self.gridLayout_7.addWidget(self.itemsModification, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_7, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_6 = QGridLayout(self.tab_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.optionSetModification = QGroupBox(self.tab_3)
        self.optionSetModification.setObjectName(u"optionSetModification")
        sizePolicy.setHeightForWidth(self.optionSetModification.sizePolicy().hasHeightForWidth())
        self.optionSetModification.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QGridLayout(self.optionSetModification)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.addOS = QPushButton(self.optionSetModification)
        self.addOS.setObjectName(u"addOS")

        self.gridLayout_4.addWidget(self.addOS, 3, 0, 1, 2)

        self.osList = QComboBox(self.optionSetModification)
        self.osList.setObjectName(u"osList")

        self.gridLayout_4.addWidget(self.osList, 1, 0, 1, 2)

        self.labelOS = QLabel(self.optionSetModification)
        self.labelOS.setObjectName(u"labelOS")

        self.gridLayout_4.addWidget(self.labelOS, 0, 0, 1, 2, Qt.AlignHCenter)

        self.taxImpOS = QPushButton(self.optionSetModification)
        self.taxImpOS.setObjectName(u"taxImpOS")

        self.gridLayout_4.addWidget(self.taxImpOS, 5, 0, 1, 2)

        self.optionsList = QComboBox(self.optionSetModification)
        self.optionsList.setObjectName(u"optionsList")

        self.gridLayout_4.addWidget(self.optionsList, 2, 0, 1, 2)

        self.addedOS = QTextEdit(self.optionSetModification)
        self.addedOS.setObjectName(u"addedOS")

        self.gridLayout_4.addWidget(self.addedOS, 4, 0, 1, 2)


        self.gridLayout_6.addWidget(self.optionSetModification, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_9, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_9 = QGridLayout(self.tab_4)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.groupBox = QGroupBox(self.tab_4)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_5 = QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.leSmartSearch = QLineEdit(self.groupBox)
        self.leSmartSearch.setObjectName(u"leSmartSearch")

        self.gridLayout_5.addWidget(self.leSmartSearch, 1, 0, 1, 1)

        self.labelSmartSearch = QLabel(self.groupBox)
        self.labelSmartSearch.setObjectName(u"labelSmartSearch")

        self.gridLayout_5.addWidget(self.labelSmartSearch, 0, 0, 1, 1, Qt.AlignHCenter)

        self.addedSS = QTextEdit(self.groupBox)
        self.addedSS.setObjectName(u"addedSS")

        self.gridLayout_5.addWidget(self.addedSS, 4, 0, 1, 1)

        self.taxImpSmartSearch = QPushButton(self.groupBox)
        self.taxImpSmartSearch.setObjectName(u"taxImpSmartSearch")

        self.gridLayout_5.addWidget(self.taxImpSmartSearch, 5, 0, 1, 1)

        self.addSmartSearch = QPushButton(self.groupBox)
        self.addSmartSearch.setObjectName(u"addSmartSearch")

        self.gridLayout_5.addWidget(self.addSmartSearch, 3, 0, 1, 1)

        self.smartSearchList = QComboBox(self.groupBox)
        self.smartSearchList.setObjectName(u"smartSearchList")

        self.gridLayout_5.addWidget(self.smartSearchList, 2, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox, 0, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_10, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")

        self.gridLayout_11.addWidget(self.tabWidget, 4, 0, 1, 3)

        self.labelTax = QLabel(self.taxPage)
        self.labelTax.setObjectName(u"labelTax")

        self.gridLayout_11.addWidget(self.labelTax, 1, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_5, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.line = QFrame(self.taxPage)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.line, 3, 0, 1, 3)

        self.stackedWidget.addWidget(self.taxPage)

        self.gridLayout_3.addWidget(self.stackedWidget, 1, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 860, 29))
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
        QWidget.setTabOrder(self.tabWidget, self.sectionList)
        QWidget.setTabOrder(self.sectionList, self.addSection)
        QWidget.setTabOrder(self.addSection, self.addedSections)
        QWidget.setTabOrder(self.addedSections, self.taxImpSec)
        QWidget.setTabOrder(self.taxImpSec, self.itemsList)
        QWidget.setTabOrder(self.itemsList, self.addedItems)
        QWidget.setTabOrder(self.addedItems, self.taxImpIt)
        QWidget.setTabOrder(self.taxImpIt, self.osList)
        QWidget.setTabOrder(self.osList, self.optionsList)
        QWidget.setTabOrder(self.optionsList, self.addOS)
        QWidget.setTabOrder(self.addOS, self.addedOS)
        QWidget.setTabOrder(self.addedOS, self.taxImpOS)
        QWidget.setTabOrder(self.taxImpOS, self.leSmartSearch)
        QWidget.setTabOrder(self.leSmartSearch, self.smartSearchList)
        QWidget.setTabOrder(self.smartSearchList, self.addSmartSearch)
        QWidget.setTabOrder(self.addSmartSearch, self.addedSS)
        QWidget.setTabOrder(self.addedSS, self.taxImpSmartSearch)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menuFile.addAction(self.actionLoad_Json)
        self.menuFile.addAction(self.actionSave_Json)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.menuTax_Options.menuAction())
        self.menuTax_Options.addAction(self.actionApply_Tax_to_All_Sections)
        self.menuTax_Options.addAction(self.actionRemove_Tax_from_All_Sections)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


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
        self.TAXBUTTON.setText(QCoreApplication.translate("MainWindow", u"Tax Modifications", None))
        self.PRICEBUTTON.setText(QCoreApplication.translate("MainWindow", u"Price Modifications", None))
        self.sectionModification_2.setTitle(QCoreApplication.translate("MainWindow", u"Section Modifications", None))
        self.addSection_2.setText(QCoreApplication.translate("MainWindow", u"Add Section", None))
        self.priceImpSec.setText(QCoreApplication.translate("MainWindow", u"Implement Price", None))
        self.labelSection_2.setText(QCoreApplication.translate("MainWindow", u"Select the Sections to Modify", None))
        self.modOS.setText(QCoreApplication.translate("MainWindow", u"Modify OS", None))
        self.modMO.setText(QCoreApplication.translate("MainWindow", u"Modify MO", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Section Modifications", None))
        self.itemsModification_2.setTitle(QCoreApplication.translate("MainWindow", u"Item Modifications", None))
        self.priceImpIt.setText(QCoreApplication.translate("MainWindow", u"Implement Price", None))
        self.labelItems_2.setText(QCoreApplication.translate("MainWindow", u"Select the Items to Modify", None))
        self.addItem_2.setText(QCoreApplication.translate("MainWindow", u"Add Item", None))
        self.modMO1.setText(QCoreApplication.translate("MainWindow", u"Modify MO", None))
        self.modSO1.setText(QCoreApplication.translate("MainWindow", u"Modify OS", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Item Modifications", None))
        self.optionSetModification_2.setTitle(QCoreApplication.translate("MainWindow", u"Option Set Modifications", None))
        self.addOS_2.setText(QCoreApplication.translate("MainWindow", u"Add Option", None))
        self.labelOS_2.setText(QCoreApplication.translate("MainWindow", u"Select the OS to Modify", None))
        self.priceImpOS.setText(QCoreApplication.translate("MainWindow", u"Implement Price", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Option Set Modifications", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Smart Search", None))
        self.modMO2.setText(QCoreApplication.translate("MainWindow", u"Modify MO", None))
        self.modSO2.setText(QCoreApplication.translate("MainWindow", u"Modify OS", None))
        self.labelSmartSearch_2.setText(QCoreApplication.translate("MainWindow", u"Smart Search", None))
        self.addSmartSearch_2.setText(QCoreApplication.translate("MainWindow", u"Add Item", None))
        self.priceImpSmartSearch.setText(QCoreApplication.translate("MainWindow", u"Implement Price", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"Smart Search", None))
        self.priceListSelected.setItemText(0, QCoreApplication.translate("MainWindow", u"Change Price", None))
        self.priceListSelected.setItemText(1, QCoreApplication.translate("MainWindow", u"Increase or Decrease %", None))
        self.priceListSelected.setItemText(2, QCoreApplication.translate("MainWindow", u"Increase or Decrease Fixed Amount", None))

        self.price.setText("")
        self.labelInfo.setText("")
        self.sectionModification.setTitle(QCoreApplication.translate("MainWindow", u"Section Modifications", None))
        self.addSection.setText(QCoreApplication.translate("MainWindow", u"Add Section", None))
        self.taxImpSec.setText(QCoreApplication.translate("MainWindow", u"Implement Tax", None))
        self.labelSection.setText(QCoreApplication.translate("MainWindow", u"Select the Sections to Modify", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Section Modifications", None))
        self.itemsModification.setTitle(QCoreApplication.translate("MainWindow", u"Item Modifications", None))
        self.taxImpIt.setText(QCoreApplication.translate("MainWindow", u"Implement Tax", None))
        self.labelItems.setText(QCoreApplication.translate("MainWindow", u"Select the Items to Modify", None))
        self.addItem.setText(QCoreApplication.translate("MainWindow", u"Add Item", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Items Modifications", None))
        self.optionSetModification.setTitle(QCoreApplication.translate("MainWindow", u"Option Set Modifications", None))
        self.addOS.setText(QCoreApplication.translate("MainWindow", u"Add Option", None))
        self.labelOS.setText(QCoreApplication.translate("MainWindow", u"Select the OS to Modify", None))
        self.taxImpOS.setText(QCoreApplication.translate("MainWindow", u"Implement Tax", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Option Set Modifications", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Smart Search", None))
        self.labelSmartSearch.setText(QCoreApplication.translate("MainWindow", u"Smart Search", None))
        self.taxImpSmartSearch.setText(QCoreApplication.translate("MainWindow", u"Implement Tax", None))
        self.addSmartSearch.setText(QCoreApplication.translate("MainWindow", u"Add Item", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Smart Search", None))
        self.labelTax.setText(QCoreApplication.translate("MainWindow", u"Please Select Tax Values", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuTax_Options.setTitle(QCoreApplication.translate("MainWindow", u"Tax Options", None))
    # retranslateUi

