# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QLabel, QListWidget, QLineEdit
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


        #self.ui.sectionlist.addItem("Hola")
        self.ui.loadJson.clicked.connect(self.clicked)

    def abrirArchivo(self):
        archivo = QFileDialog.getOpenFileName(self, ("Open Json"), "C:\\", "Text files(*.txt);;Archivo JSON(.json)")
        print(archivo)

    def clicked(self):
        self.ui.labelTax.setText("you pressed the button")
        print("clickkkkk")
        self.update()
        archivo = QFileDialog.getOpenFileName(self, ("Open Json"), "C:\\", ("Text files(*.txt);;JSON File (*.json)"))
        print(archivo)
        archivoSeparado = archivo[0].split(sep=',')
        print(archivoSeparado)
        otroAr = "".join(archivoSeparado)
        otroAr.replace("'","")
        print(otroAr)
        jsonSection.openJson(jsonSection,otroAr)

    def update(self):
        self.ui.labelTax.adjustSize()

    def sectionItems(self,item):
        self.ui.sectionlist.addItem(item)
