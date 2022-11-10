from PySide6.QtWidgets import QFileDialog, QMessageBox, QMainWindow
from PySide6.QtGui import QIcon, QDoubleValidator
from jsonSection import jsonSection

from ui_form import Ui_MainWindow
datos = dict()
datos = None

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('Menu Editing Tool')
        self.setWindowIcon(QIcon('.\images\iconoFlipdish.png'))

        #self.ui.stackedWidget.hide()
        self.ui.TAXBUTTON.clicked.connect(self.clickedTAXBUTTON)
        self.ui.PRICEBUTTON.clicked.connect(self.clickedPRICEBUTTON)

        self.ui.actionLoad_Json.triggered.connect(self.clickedLoad)
        self.ui.actionSave_Json.triggered.connect(self.clickedSave)
        self.ui.actionExit.triggered.connect(self.close)

        self.ui.actionRemove_Tax_from_All_Sections.triggered.connect(self.clickedRemoveTax)
        self.ui.actionApply_Tax_to_All_Sections.triggered.connect(self.clickedAllSections)

        global section
        section = list()
        self.ui.addSection.clicked.connect(self.slot_addedSections)
        self.ui.taxImpSec.clicked.connect(self.clickedSectionImp)

        self.ui.addSection_2.clicked.connect(self.slot_addedSections2)
        global item
        item = list()
        global aux
        aux = list()
        self.ui.addItem.clicked.connect(self.slot_addedItem)
        self.ui.taxImpIt.clicked.connect(self.clickedItemImp)

        self.ui.addItem_2.clicked.connect(self.slot_addedItem2)
        self.ui.priceImpIt.clicked.connect(self.clickedItemImp2)

        global osFjson
        osFjson = list()

        global os
        os = list()
        global aux2
        aux2 = list()
        global osOption
        osOption = list()
        global auxiliar
        auxiliar = list()
        global auxOS
        auxOS = list()
        global data
        data = list()
        global auxOSMaster
        auxOSMaster = list()
        global osOptions
        osOptions = list()
        global osOptions2
        osOptions2 = list()
        global texto1
        texto1 = str()
        self.ui.osList.activated.connect(self.setOptionList)
        self.ui.addOS.clicked.connect(self.slot_addedOsOption)
        self.ui.taxImpOS.clicked.connect(self.clickedOSImp)

        self.ui.osList_2.activated.connect(self.setOptionList2)
        self.ui.addOS_2.clicked.connect(self.slot_addedOsOption2)
        self.ui.priceImpOS.clicked.connect(self.clickedOSImp2)

        global smartSearch
        smartSearch = list()
        global text
        text = list()
        global auxSS
        auxSS = list()
        global price
        price = float()
        self.ui.leSmartSearch.editingFinished.connect(self.slot_setSSList)
        self.ui.addSmartSearch.clicked.connect(self.slot_addedSS)
        self.ui.taxImpSmartSearch.clicked.connect(self.clickedSSImp)

        self.ui.leSmartSearch_2.editingFinished.connect(self.slot_setSSList2)
        self.ui.addSmartSearch_2.clicked.connect(self.slot_addedSS2)
        self.ui.priceImpSmartSearch.clicked.connect(self.clickedSSImp2)

        self.ui.priceListSelected.activated.connect(self.indexHasChanged)
        self.ui.leIncrease.setValidator(QDoubleValidator(0,10000000,2))
        self.ui.leIncrease.editingFinished.connect(self.slot_Increase)

        self.ui.priceImpSec.clicked.connect(self.clickedSectionImp2)
##########################################################################################
##########################################################################################

#sets the screen for working with TAXES
    def clickedTAXBUTTON(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.taxPage)
        self.clear_all()
        self.ui.stackedWidget.show()

#sets the screen for working with PRICES
    def clickedPRICEBUTTON(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pricePage)
        self.clear_all()
        self.ui.stackedWidget.show()

#opens the json file
    def abrirArchivo(self):
        archivo = QFileDialog.getOpenFileName(self, ("Open Json"), "C:\\", "Text files(*.txt);;Archivo JSON(.json)")
        print(archivo)

#loads the json and sets up all the dropping lists
    def clickedLoad(self):
        archivo = QFileDialog.getOpenFileName(self, ("Open Json"), "C:\\", ("JSON File (*.json)"))
        archivoSeparado = archivo[0].split(sep=',')
        global file
        file1 = "".join(archivoSeparado)
        file1.replace("'","")

        self.clear_all()
        if file1 ==  '':
            self.ui.taxList.clear()
            self.ui.sectionList.clear()
            self.ui.itemsList.clear()
            self.ui.itemsList_2.clear()
            self.ui.osList.clear()
            self.ui.osList_2.clear()
            self.ui.optionsList.clear()
            self.ui.optionsList_2.clear()
            self.ui.addedOS.clear()
            self.ui.addedOS_2.clear()
            self.ui.addedItems_2.clear()
            self.ui.addedItems.clear()
            pass
        else:
            file = file1
            global datos
            datos = jsonSection.openJson(jsonSection,file)
            self.setTaxList()
            self.setSectionList()
            self.setItemsList()
            self.setOSList()
            self.ui.addedOS.clear()
            self.ui.addedOS_2.clear()
            self.ui.addedItems_2.clear()
            self.ui.addedItems.clear()

#closes the program
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        elif reply == QMessageBox.No:
            event.ignore()


#############################################################################################
#############################################################################################
#SETLISTS

#sets the list of taxes that are on the menu
    def setTaxList(self):
        self.ui.taxList.clear()
        taxes = jsonSection.slot_mostrarTax(jsonSection,datos)
        for i in range(0,len(taxes)):
            self.ui.taxList.addItem(taxes[i])

#sets the list of sections that are on the menu
    def setSectionList(self):
        self.ui.sectionList.clear()
        self.ui.sectionList_2.clear()
        secciones = jsonSection.slot_mostrarSecciones(jsonSection,datos)
        for i in range(0,len(secciones)):
            self.ui.sectionList.addItem(secciones[i])
            self.ui.sectionList_2.addItem(secciones[i])

#sets the list of items that are on the menu
    def setItemsList(self):
        self.ui.itemsList.clear()
        self.ui.itemsList_2.clear()
        items = jsonSection.slot_mostrarItems(jsonSection,datos)
        for i in range(0,len(items)):
            for j in range(0,len(datos["MenuSections"])):
                if items[i] == datos["MenuSections"][j]['Name']:
                    section = datos["MenuSections"][j]['Name']
            if section != items[i]:
                self.ui.itemsList.addItem(section + ": " + items[i])
                self.ui.itemsList_2.addItem(section + ": " + items[i])

#sets the list of OS available on the menu
    def setOSList(self):
        global osFjson
        self.ui.osList.clear()
        self.ui.osList_2.clear()
        osFjson = jsonSection.slot_mostrarOS(jsonSection,datos)
        os = ""
        osOp = list()
        for i in range(0,len(osFjson)):
            for j in range(0,len(datos["MenuSections"])):
                for k in range(0,len(datos["MenuSections"][j]["MenuItems"])):
                    for l in range(0,len(datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"])):
                        if osFjson[i] == datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]['Name']:
                            os = datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]['Name']
                            for m in range(0,len(datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"])):
                                osOp.append(datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]['Name'])
            if os == None and osOp == []:
                pass
            elif os != None and osOp == []:
                pass
            else:
                self.ui.osList.addItem(os)
                self.ui.osList_2.addItem(os)
                self.setOptionList()
                self.setOptionList2()
            osOp.clear()

#sets the list of options that are on each OS on the menu
    def setOptionList(self):
        global osOptions
        global data
        osOptions.clear()
        self.ui.optionsList.clear()
        for i in range(0,len(osFjson)):
            for j in range(0,len(datos["MenuSections"])):
                for k in range(0,len(datos["MenuSections"][j]["MenuItems"])):
                    for l in range(0,len(datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"])):
                        if self.ui.osList.currentText() == "" and datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]['Name'] == None:
                            data = datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]['Name']
                            for m in range(0,len(datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"])):
                                if datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["IsMasterOptionSet"] == False:
                                    smt = datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]['Name']
                                    if smt not in osOptions:
                                        osOptions.append(smt)
                        elif self.ui.osList.currentText() == datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]['Name']:
                            data = datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]['Name']
                            for m in range(0,len(datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"])):
                                if datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["IsMasterOptionSet"] == False:
                                    smt = datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]['Name']
                                    if smt not in osOptions:
                                        osOptions.append(smt)
        osOptions.insert(0,"Change All")
        for i in range(0,len(osOptions)):
            if self.ui.osList.currentText()== "":
                selfCurrentT = None
            if self.ui.osList.currentText() == data or selfCurrentT == data:
                self.ui.optionsList.addItem(osOptions[i])

#sets the list of options that are on each OS on the menu
    def setOptionList2(self):
        global osOptions2
        global data
        osOptions2.clear()
        self.ui.optionsList_2.clear()
        for i in range(0,len(osFjson)):
            for j in range(0,len(datos["MenuSections"])):
                for k in range(0,len(datos["MenuSections"][j]["MenuItems"])):
                    for l in range(0,len(datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"])):
                        if self.ui.osList_2.currentText() == "" and datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]['Name'] == None:
                            data = datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]['Name']
                            for m in range(0,len(datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"])):
                                if datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["IsMasterOptionSet"] == False:
                                    smt = datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]['Name']
                                    if smt not in osOptions2:
                                        osOptions2.append(smt)
                        elif self.ui.osList_2.currentText() == datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]['Name']:
                            data = datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]['Name']
                            for m in range(0,len(datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"])):
                                if datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["IsMasterOptionSet"] == False:
                                    smt = datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]['Name']
                                    if smt not in osOptions2:
                                        osOptions2.append(smt)
        osOptions2.insert(0,"Change All")
        for i in range(0,len(osOptions2)):
            if self.ui.osList_2.currentText()== "":
                selfCurrentT2 = None
            if self.ui.osList_2.currentText() == data or selfCurrentT2 == data:
                self.ui.optionsList_2.addItem(osOptions2[i])

#sets the list of options and items that matches the search
    def slot_setSSList(self):
        self.ui.smartSearchList.clear()
        smartSearch.clear()
        textito = ""
        textito = self.ui.leSmartSearch.text()
        for j in range(0,len(datos["MenuSections"])):
            for k in range(0,len(datos["MenuSections"][j]["MenuItems"])):
                itemsSS = datos["MenuSections"][j]["MenuItems"][k]["Name"]
                if textito.lower() in ascii(datos["MenuSections"][j]["MenuItems"][k]["Name"]).lower():
                    if itemsSS not in smartSearch:
                        smartSearch.append(itemsSS)
                        if textito not in text:
                            text.append(textito)
                if len(datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"]) == 0:
                    pass
                else:
                    for l in range(0,len(datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"])):
                        for m in range(0,len(datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"])):
                            opSS = datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]['Name']
                            if textito.lower() in ascii(datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]['Name']).lower() and opSS not in smartSearch:
                                smartSearch.append(opSS)
                                if textito not in text:
                                    text.append(textito)
        if len(smartSearch) != 0:
            smartSearch.insert(0,"Change All")
        for i in range(0,len(smartSearch)):
            self.ui.smartSearchList.addItem(smartSearch[i])
        self.ui.leSmartSearch.clear()


#sets the list of options and items that matches the search
    def slot_setSSList2(self):
        self.ui.smartSearchList_2.clear()
        smartSearch.clear()
        textito = ""
        textito = self.ui.leSmartSearch_2.text()
        for j in range(0,len(datos["MenuSections"])):
            for k in range(0,len(datos["MenuSections"][j]["MenuItems"])):
                itemsSS = datos["MenuSections"][j]["MenuItems"][k]["Name"]
                if textito.lower() in ascii(datos["MenuSections"][j]["MenuItems"][k]["Name"]).lower():
                    if itemsSS not in smartSearch:
                        smartSearch.append(itemsSS)
                        if textito not in text:
                            text.append(textito)
                if len(datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"]) == 0:
                    pass
                else:
                    for l in range(0,len(datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"])):
                        for m in range(0,len(datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"])):
                            opSS = datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]['Name']
                            if textito.lower() in ascii(datos["MenuSections"][j]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]['Name']).lower() and opSS not in smartSearch:
                                smartSearch.append(opSS)
                                if textito not in text:
                                    text.append(textito)
        if len(smartSearch) != 0:
            smartSearch.insert(0,"Change All")
        for i in range(0,len(smartSearch)):
            self.ui.smartSearchList_2.addItem(smartSearch[i])
        self.ui.leSmartSearch_2.clear()
################################################################################
################################################################################

#Set Lists of selected items/sections/etc

#shows the sections selected on the text edit
    def slot_addedSections (self):
        texto = ''
        if self.ui.sectionList.currentText() in section:
            pass
        else:
            section.append(self.ui.sectionList.currentText())
        for i in range(0,len(section)):
            texto += section[i]
            if texto != "":
                texto += "\n"
                self.ui.addedSections.setText(texto)

#
    def slot_addedSections2(self):
        texto = ''
        if self.ui.sectionList_2.currentText() in section:
            pass
        else:
            section.append(self.ui.sectionList_2.currentText())
        for i in range(0,len(section)):
            texto += section[i]
            if texto != "":
                texto += "\n"
                self.ui.addedSections_2.setText(texto)

#shows the items selected on the text edit
    def slot_addedItem(self):
        texto = ''
        if self.ui.itemsList.currentText() in aux:
            pass
        else:
            aux.append(self.ui.itemsList.currentText())
            for i in range(0,len(aux)):
                texto += aux[i]
                item.append(aux[i].split(sep=': '))
                if texto != "":
                    texto += "\n"
                    self.ui.addedItems.setText(texto)

#shows the items selected on the text edit
    def slot_addedItem2(self):
        texto = ''
        if self.ui.itemsList_2.currentText() in aux:
            pass
        else:
            aux.append(self.ui.itemsList_2.currentText())
            for i in range(0,len(aux)):
                texto += aux[i]
                item.append(aux[i].split(sep=': '))
                if texto != "":
                    texto += "\n"
                    self.ui.addedItems_2.setText(texto)


#shows the OS options selected on the text edit
    def slot_addedOsOption(self):
        texto = ''
        if self.ui.optionsList.currentText() in auxOS:
            if self.ui.osList.currentText() in auxOSMaster:
                pass
            else:
                auxOS.append(self.ui.optionsList.currentText())
                auxOSMaster.append(self.ui.osList.currentText())
                for i in range(0,len(auxOS)):
                    texto += auxOSMaster[i] + ": " + auxOS[i]
                    if texto != "":
                        texto += "\n"
                        self.ui.addedOS.setText(texto)
        else:
            auxOS.append(self.ui.optionsList.currentText())
            auxOSMaster.append(self.ui.osList.currentText())
            for i in range(0,len(auxOS)):
                texto += auxOSMaster[i] + ": " + auxOS[i]
                if texto != "":
                    texto += "\n"
                    self.ui.addedOS.setText(texto)


#shows the OS options selected on the text edit
    def slot_addedOsOption2(self):
        texto = ''
        if self.ui.optionsList_2.currentText() in auxOS:
            if self.ui.osList_2.currentText() in auxOSMaster:
                pass
            else:
                auxOS.append(self.ui.optionsList_2.currentText())
                auxOSMaster.append(self.ui.osList_2.currentText())
                for i in range(0,len(auxOS)):
                    texto += auxOSMaster[i] + ": " + auxOS[i]
                    if texto != "":
                        texto += "\n"
                        self.ui.addedOS_2.setText(texto)
        else:
            auxOS.append(self.ui.optionsList_2.currentText())
            auxOSMaster.append(self.ui.osList_2.currentText())
            for i in range(0,len(auxOS)):
                texto += auxOSMaster[i] + ": " + auxOS[i]
                if texto != "":
                    texto += "\n"
                    self.ui.addedOS_2.setText(texto)

#shows the SS options selected on the text edit
    def slot_addedSS(self):
        texto = ''
        if self.ui.smartSearchList.currentText() in auxSS:
                pass
        elif self.ui.smartSearchList.currentText() == "Change All":
            for i in range(1,len(smartSearch)):
                auxSS.append(smartSearch[i])
            for i in range(0,len(auxSS)):
                texto += auxSS[i]
                if texto != "":
                    texto += "\n"
                    self.ui.addedSS.setText(texto)
        else:
            auxSS.append(self.ui.smartSearchList.currentText())
            for i in range(0,len(auxSS)):
                texto += auxSS[i]
                if texto != "":
                    texto += "\n"
                    self.ui.addedSS.setText(texto)

#shows the SS (price) options selected on the text edit
    def slot_addedSS2(self):
        texto = ''
        if self.ui.smartSearchList_2.currentText() in auxSS:
                pass
        elif self.ui.smartSearchList_2.currentText() == "Change All":
            for i in range(1,len(smartSearch)):
                auxSS.append(smartSearch[i])
            for i in range(0,len(auxSS)):
                texto += auxSS[i]
                if texto != "":
                    texto += "\n"
                    self.ui.addedSS_2.setText(texto)
        else:
            auxSS.append(self.ui.smartSearchList_2.currentText())
            for i in range(0,len(auxSS)):
                texto += auxSS[i]
                if texto != "":
                    texto += "\n"
                    self.ui.addedSS_2.setText(texto)

#button that applies tax to the selected sections
    def clickedSectionImp(self):
        global datos
        if datos == None:
            QMessageBox.warning(self, 'Warning',
            'You must load a Json File first!',QMessageBox.Ok)
        else:
            tax = self.ui.taxList.currentIndex()
            jsonSection.slot_changeTaxSelectedSections(jsonSection,datos,section,tax)
            QMessageBox.information(self, 'Success!',
            'The selected sections have been updated',QMessageBox.Ok)
        section.clear()
        self.ui.addedSections.clear()

#button that applies tax to the selected items
    def clickedItemImp(self):
        global datos
        if datos == None:
            QMessageBox.warning(self, 'Warning',
            'You must load a Json File first!',QMessageBox.Ok)
        else:
            tax = self.ui.taxList.currentIndex()
            jsonSection.slot_changeTaxSelectedItems(jsonSection,datos,item,tax)
            QMessageBox.information(self, 'Success!',
            'The selected items have been updated',QMessageBox.Ok)
        aux.clear()
        item.clear()
        self.ui.addedItems.clear()

#button that applies tax to the selected option OS
    def clickedOSImp(self):
        global datos
        if datos == None:
            QMessageBox.warning(self, 'Warning',
            'You must load a Json File first!',QMessageBox.Ok)
        else:
            tax = self.ui.taxList.currentIndex()
            jsonSection.slot_changeTaxSelectedOS(jsonSection,datos,auxOS,auxOSMaster,tax)
            QMessageBox.information(self, 'Success!',
            'The selected sections have been updated',QMessageBox.Ok)
        osOptions.clear()
        auxOSMaster.clear()
        auxOS.clear()
        self.ui.addedOS.clear()

#button that applies tax to the selected SS items
    def clickedSSImp(self):
        global datos
        if datos == None:
            QMessageBox.warning(self, 'Warning',
            'You must load a Json File first!',QMessageBox.Ok)
        else:
            tax = self.ui.taxList.currentIndex()
            jsonSection.slot_changeTaxSelectedSS(jsonSection,datos,auxSS,text,tax)
            QMessageBox.information(self, 'Success!',
            'The selected items have been updated',QMessageBox.Ok)
        auxSS.clear()
        text.clear()
        self.ui.smartSearchList.clear()
        self.ui.addedSS.clear()

#applies taxes to all the menu
    def clickedAllSections(self):
        global datos
        if datos == None:
            QMessageBox.warning(self, 'Warning',
            'You must load a Json File first!',QMessageBox.Ok)
        else:
            tax = self.ui.taxList.currentIndex()
            jsonSection.slot_changeTaxAllSections(jsonSection,datos,tax)
            QMessageBox.information(self, 'Success!',
            'All the items have been updated',QMessageBox.Ok)
        self.clear_all()

#removes taxes from all the menu
    def clickedRemoveTax(self):
        global datos
        if datos == None:
            QMessageBox.warning(self, 'Warning',
            'You must load a Json File first!',QMessageBox.Ok)
        else:
            tax = None
            jsonSection.slot_RemoveTaxAllItems(jsonSection,datos,tax)
            QMessageBox.information(self, 'Success!',
            'All taxes have been removed from your Menu',QMessageBox.Ok)
        self.clear_all()

#saves the json file
    def clickedSave(self):
        global datos
        if datos == None:
            QMessageBox.warning(self, 'Warning',
            'You must load a Json File first!',QMessageBox.Ok)
        else:
            jsonSection.save_json(jsonSection,datos,file)
            QMessageBox.information(self, 'Success!',
            'Json Succesfully Saved!',QMessageBox.Ok)
        self.clear_all()

    def clear_all(self):
        self.ui.addedItems.clear()
        self.ui.addedSections.clear()
        self.ui.addedOS.clear()
        self.ui.addedItems_2.clear()
        self.ui.addedSections_2.clear()
        self.ui.addedOS_2.clear()
        self.ui.smartSearchList.clear()
        self.ui.addedSS.clear()
        self.ui.smartSearchList_2.clear()
        self.ui.addedSS_2.clear()
        auxSS.clear()
        auxOS.clear()
        osOptions.clear()
        auxOSMaster.clear()
        item.clear()
        section.clear()
        aux.clear()
        text.clear()

###############################################################################
###############################################################################


#PRICE MODIFICATIONS
    def indexHasChanged(self):
        if self.ui.priceListSelected.currentIndex() == 0:
            self.ui.price.clear()
            self.ui.leIncrease.clear()
            self.ui.leIncrease.setValidator(QDoubleValidator(0,1000000000,2))
            self.ui.labelInfo.hide()
        elif self.ui.priceListSelected.currentIndex() == 1:
            self.ui.price.clear()
            self.ui.leIncrease.clear()
            self.ui.leIncrease.setValidator(QDoubleValidator(-100,100,2))
            self.ui.labelInfo.setText("To decrease use '-'")
            self.ui.labelInfo.show()
        else :
            self.ui.price.clear()
            self.ui.leIncrease.clear()
            self.ui.leIncrease.setValidator(QDoubleValidator(-10000000,10000000,2))
            self.ui.labelInfo.setText("To decrease use '-'")
            self.ui.labelInfo.show()

    def slot_Increase(self):
        global price
        if self.ui.priceListSelected.currentIndex() == 0:
            self.ui.price.setText("The price will be updated to " + self.ui.leIncrease.text())
            aux = self.ui.leIncrease.text()
            price = float(aux.replace(",", "."))
            self.ui.leIncrease.clear()
        elif self.ui.priceListSelected.currentIndex() == 1:
            self.ui.price.setText("The price will be updated by " + self.ui.leIncrease.text() + "%")
            aux = self.ui.leIncrease.text()
            price = float(aux.replace(",", "."))
            self.ui.leIncrease.clear()
        else:
            self.ui.price.setText("The price will be updated by " + self.ui.leIncrease.text())
            aux = self.ui.leIncrease.text()
            price = float(aux.replace(",", "."))
            self.ui.leIncrease.clear()

#button that applies new price to the selected sections
    def clickedSectionImp2(self):
        global datos
        if datos == None:
            QMessageBox.warning(self, 'Warning',
            'You must load a Json File first!',QMessageBox.Ok)
        else:
            if self.ui.priceListSelected.currentText() == "Change Price":
                jsonSection.slot_changePriceSelectedSections(jsonSection,datos,section,price,self.ui.modMO.isChecked(),self.ui.modOS.isChecked())
                QMessageBox.information(self, 'Success!',
                'The selected sections have been updated',QMessageBox.Ok)
            elif self.ui.priceListSelected.currentText() == "Increase or Decrease %":
                jsonSection.slot_changePricePercentajeSelectedSections(jsonSection,datos,section,price,self.ui.modMO.isChecked(),self.ui.modOS.isChecked())
                QMessageBox.information(self, 'Success!',
                'The selected sections have been updated',QMessageBox.Ok)
            else:
                jsonSection.slot_changePriceFixedAmountSelectedSections(jsonSection,datos,section,price,self.ui.modMO.isChecked(),self.ui.modOS.isChecked())
                QMessageBox.information(self, 'Success!',
                'The selected sections have been updated',QMessageBox.Ok)
        section.clear()
        self.ui.addedSections_2.clear()

#button that applies new price to the selected items
    def clickedItemImp2(self):
        global datos
        if datos == None:
            QMessageBox.warning(self, 'Warning',
            'You must load a Json File first!',QMessageBox.Ok)
        else:
            if self.ui.priceListSelected.currentText() == "Change Price":
                jsonSection.slot_changePriceSelectedItems(jsonSection,datos,item,price,self.ui.modMO1.isChecked(),self.ui.modSO1.isChecked())
                QMessageBox.information(self, 'Success!',
                'The selected sections have been updated',QMessageBox.Ok)
            elif self.ui.priceListSelected.currentText() == "Increase or Decrease %":
                jsonSection.slot_changePricePercentajeSelectedItems(jsonSection,datos,item,price,self.ui.modMO1.isChecked(),self.ui.modSO1.isChecked())
                QMessageBox.information(self, 'Success!',
                'The selected items have been updated',QMessageBox.Ok)
            else:
                jsonSection.slot_changePriceFixedAmountSelectedItems(jsonSection,datos,item,price,self.ui.modMO1.isChecked(),self.ui.modSO1.isChecked())
                QMessageBox.information(self, 'Success!',
                'The selected items have been updated',QMessageBox.Ok)
        aux.clear()
        item.clear()
        self.ui.addedItems_2.clear()

#button that applies new price to the selected option OS
    def clickedOSImp2(self):
        global datos
        if datos == None:
            QMessageBox.warning(self, 'Warning',
            'You must load a Json File first!',QMessageBox.Ok)
        else:
            if self.ui.priceListSelected.currentText() == "Change Price":
                jsonSection.slot_changePriceSelectedOS(jsonSection,datos,auxOS,auxOSMaster,price)
                QMessageBox.information(self, 'Success!',
                'The selected sections have been updated',QMessageBox.Ok)
            elif self.ui.priceListSelected.currentText() == "Increase or Decrease %":
                jsonSection.slot_changePricePercentajeSelectedOS(jsonSection,datos,auxOS,auxOSMaster,price)
                QMessageBox.information(self, 'Success!',
                'The selected sections have been updated',QMessageBox.Ok)
            else:
                jsonSection.slot_changePriceFixedAmountSelectedOS(jsonSection,datos,auxOS,auxOSMaster,price)
                QMessageBox.information(self, 'Success!',
                'The selected sections have been updated',QMessageBox.Ok)
        osOptions.clear()
        auxOSMaster.clear()
        auxOS.clear()
        self.ui.addedOS_2.clear()

#button that applies new price to the selected SS items
    def clickedSSImp2(self):
        global datos
        if datos == None:
            QMessageBox.warning(self, 'Warning',
            'You must load a Json File first!',QMessageBox.Ok)
        else:
            if self.ui.priceListSelected.currentText() == "Change Price":
                jsonSection.slot_changePriceSelectedSelectedSS(jsonSection,datos,auxSS,text,price,self.ui.modMO2.isChecked(),self.ui.modSO2.isChecked())
                QMessageBox.information(self, 'Success!',
                'The selected sections have been updated',QMessageBox.Ok)
            elif self.ui.priceListSelected.currentText() == "Increase or Decrease %":
                jsonSection.slot_changePricePercentajeSelectedSS(jsonSection,datos,auxSS,text,price,self.ui.modMO2.isChecked(),self.ui.modSO2.isChecked())
                QMessageBox.information(self, 'Success!',
                'The selected sections have been updated',QMessageBox.Ok)
            else:
                jsonSection.slot_changePriceFixedAmountSelectedSS(jsonSection,datos,auxSS,text,price,self.ui.modMO2.isChecked(),self.ui.modSO2.isChecked())
                QMessageBox.information(self, 'Success!',
                'The selected sections have been updated',QMessageBox.Ok)
        auxSS.clear()
        text.clear()
        self.ui.smartSearchList_2.clear()
        self.ui.addedSS_2.clear()
