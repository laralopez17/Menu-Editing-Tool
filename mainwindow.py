from PySide6.QtWidgets import QFileDialog, QMessageBox,QMainWindow
from PySide6.QtGui import QIcon
from jsonSection import jsonSection

from ui_form import Ui_MainWindow
datos = dict()
datos = None

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Tax Editing Tool')
        self.setWindowIcon(QIcon('.\images\iconoFlipdish.png'))

        self.ui.actionLoad_Json.triggered.connect(self.clickedLoad)
        self.ui.actionSave_Json.triggered.connect(self.clickedSave)
        self.ui.actionExit.triggered.connect(self.close)

        self.ui.actionRemove_Tax_from_All_Sections.triggered.connect(self.clickedRemoveTax)
        self.ui.actionApply_Tax_to_All_Sections.triggered.connect(self.clickedAllSections)

        global section
        section = list()
        self.ui.addSection.clicked.connect(self.slot_addedSections)

        self.ui.taxImpSec.clicked.connect(self.clickedSectionImp)
        global item
        item = list()
        self.ui.itemSearch.editingFinished.connect(self.slot_agregarItem)
        self.ui.taxImpIt.clicked.connect(self.clickedItemImp)


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

    def clickedLoad(self):
        archivo = QFileDialog.getOpenFileName(self, ("Open Json"), "C:\\", ("JSON File (*.json)"))
        archivoSeparado = archivo[0].split(sep=',')
        global file
        file1 = "".join(archivoSeparado)
        file1.replace("'","")

        self.ui.itemList.clear()
        self.ui.itemSearch.clear()
        if file1 ==  '':
            self.ui.taxList.clear()
            self.ui.sectionList.clear()
            pass
        else:
            file = file1
            global datos
            datos = jsonSection.openJson(jsonSection,file)
            self.setTaxList()
            self.setSectionList()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        elif reply == QMessageBox.No:
            event.ignore()


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

    def slot_agregarItem(self):
        texto = ''
        if self.ui.itemSearch.text() in item:
            pass
        else:
            item.append(self.ui.itemSearch.text())
            for i in range(0,len(item)):
                texto += item[i]
                if texto != "":
                    texto += "\n"
                    self.ui.itemList.setText(texto)
        self.ui.itemSearch.clear()

    def clickedSectionImp(self):
        global datos
        if datos == None:
            QMessageBox.warning(self, 'Warning',
            'You must load a Json File first!',QMessageBox.Ok)
        else:
            print(section)
            tax = self.ui.taxList.currentIndex()
            jsonSection.slot_changeTaxSelectedSections(jsonSection,datos,section,tax)
            QMessageBox.information(self, 'Success!',
            'The selected sections have been updated',QMessageBox.Ok)
        self.clear_all()

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
        self.clear_all()

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
        self.ui.itemList.clear()
        self.ui.itemSearch.clear()
        self.ui.addedSections.clear()

