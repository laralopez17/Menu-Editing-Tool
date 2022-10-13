# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox
from PySide6.QtGui import QIcon
from jsonSection import jsonSection
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Menu Team')
        self.setWindowIcon(QIcon('iconoFlipdish.png'))
        self.ui.loadJson.clicked.connect(self.clickedLoad)
        self.ui.saveJson.clicked.connect(self.clickedSave)
        self.ui.pbExit.clicked.connect(self.closeEvent)
        global section
        section = list()
        self.ui.addSection.clicked.connect(self.slot_addedSections)
        self.ui.allSections.clicked.connect(self.clickedAllSections)
        self.ui.taxImpSec.clicked.connect(self.clickedSectionImp)
        global item
        item = list()
        self.ui.itemSearch.editingFinished.connect(self.slot_agregarItem)
        self.ui.taxImpIt.clicked.connect(self.clickedItemImp)
        self.ui.removeTax.clicked.connect(self.clickedRemoveTax)

    def abrirArchivo(self):
        archivo = QFileDialog.getOpenFileName(self, ("Open Json"), "C:\\", "Text files(*.txt);;Archivo JSON(.json)")
        print(archivo)

    def setTaxList(self):
        self.ui.taxList.clear()
        taxes = jsonSection.slot_mostrarTax(jsonSection,datos)
        for i in range(0,len(taxes)):
            self.ui.taxList.addItem(taxes[i])

    def setSectionList(self):
        self.ui.sectionList.clear()
        secciones = jsonSection.slot_mostrarSecciones(jsonSection,datos)
        for i in range(0,len(secciones)):
            self.ui.sectionList.addItem(secciones[i])

    def update(self):
        self.ui.labelTax.adjustSize()

    def clickedLoad(self):
        self.update()
        archivo = QFileDialog.getOpenFileName(self, ("Open Json"), "C:\\Users\laral\Downloads", ("JSON File (*.json)"))
        archivoSeparado = archivo[0].split(sep=',')
        global file
        file1 = "".join(archivoSeparado)
        file1.replace("'","")
        global datos
        datos = dict()
        if file1 ==  '':
            pass
        else:
            file = file1
            datos = jsonSection.openJson(jsonSection,file)
        self.setTaxList()
        self.setSectionList()
        self.ui.itemList.setText("")

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            print('Window closed')
            self.destroy()
            sys. exit()

    def slot_addedSections (self):
        texto = ""
        if self.ui.sectionList.currentText() in section:
            pass
        else:
            section.append(self.ui.sectionList.currentText())
        for i in range(0,len(section)):
            texto += section[i] + "\n"
            self.ui.addedSections.setText(texto)

    def slot_agregarItem(self):
        texto = ""
        if self.ui.itemSearch.text() in item:
            pass
        else:
            item.append(self.ui.itemSearch.text())
            for i in range(0,len(item)):
                texto += item[i] + "\n"
                self.ui.itemList.setText(texto)

    def clickedSectionImp(self):
        print(section)
        tax = self.ui.taxList.currentIndex()
        jsonSection.slot_changeTaxSelectedSections(jsonSection,datos,section,tax)
        reply = QMessageBox.information(self, 'Success!',
        'The selected sections have been updated',QMessageBox.Ok,)

    def clickedAllSections(self):
        tax = self.ui.taxList.currentIndex()
        jsonSection.slot_changeTaxAllSections(jsonSection,datos,tax)
        reply = QMessageBox.information(self, 'Success!',
        'All the items have been updated',QMessageBox.Ok,)

    def clickedItemImp(self):
        tax = self.ui.taxList.currentIndex()
        jsonSection.slot_changeTaxSelectedItems(jsonSection,datos,item,tax)
        reply = QMessageBox.information(self, 'Success!',
        'The selected items have been updated',QMessageBox.Ok,)

    def clickedRemoveTax(self):
        tax = None
        jsonSection.slot_RemoveTaxAllItems(jsonSection,datos,tax)
        reply = QMessageBox.information(self, 'Success!',
        'All taxes have been removed from your Menu',QMessageBox.Ok,)


    def clickedSave(self):
        jsonSection.save_json(jsonSection,datos,file)
        reply = QMessageBox.information(self, 'Success!',
        'Json Succesfully Saved!',QMessageBox.Ok,)
