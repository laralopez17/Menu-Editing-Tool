# This Python file uses the following encoding: utf-8

import json
#from PySide6.QtWidgets import QListWidgetItem, QListWidget
#from mainwindow import MainWindow
#from ui_form import Ui_MainWindow

class jsonSection:
    def __init__(self):
        pass

    def openJson(self,selectedFile):
        if ".json" in selectedFile:
            with open(selectedFile, encoding="utf-8") as archivoJson:
                datos = json.load(archivoJson)
            j = len(datos["MenuSections"])

            for i in range (0,j):
               # print(datos["MenuSections"][i]["Name"])
                item1 = datos["MenuSections"][i]["Name"]
                print(item1)


            #item = QListWidgetItem(item1)
            #widget.ui.sectionlist.addItem(item1)
            #widget.show()

            #print(item)
            #widget.ui.sectionlist(widget,item)
            #widget.sectionItems(MainWindow,item)
