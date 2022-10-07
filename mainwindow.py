# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QLabel, QListWidget, QLineEdit

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
        self.ui.loadJson.clicked.connect(self.clicked)

    def abrirArchivo(self):
        archivo = QFileDialog.getOpenFileName(self, ("Open Json"), "C:\\", ("Text files (*.txt);;Archivo JSON (.json)"))
        print(archivo)

    def buttonPressed(self):
        self.ui.loadJson.clicked.connect(self.clicked)

    def clicked(self):
        self.ui.labelTax.setText("you pressed the button")
        print("clickkkkk")
        self.update()
        archivo = QFileDialog.getOpenFileName(self, ("Open Json"), "C:\\", ("Text files (*.txt)"))
        print(archivo)

    def update(self):
        self.ui.labelTax.adjustSize()
