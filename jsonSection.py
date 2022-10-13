import json

class jsonSection:
    def __init__(self):
        pass

    def openJson(self,selectedFile):
        with open(selectedFile, encoding="utf-8") as archivoJson:
            datos = json.load(archivoJson)
        return datos

    #sends the tax rates available to the mainwindow
    def slot_mostrarTax(self,datos):
        taxes = list()
        for tax in datos['TaxRates']:
            taxes.append(tax['Name']+ " " + str(tax['Rate'])+ "%")
        return taxes

    #sends the sections available to the mainwindow
    def slot_mostrarSecciones(self,datos):
        secciones = list()
        for section in datos['MenuSections']:
            secciones.append(section['Name'])
        return secciones

    #changes the taxes for the selected sections (only items for now)
    def slot_changeTaxSelectedSections(self,datos,secciones,tax):
        newTaxRateId = 0
        for i in range (0,len(datos['TaxRates'])):
            if i == tax:
                newTaxRateId = datos['TaxRates'][i]['TaxRateId']
        for j in range(0,len(secciones)):
            for i in range(0,len(datos["MenuSections"])):
                section = datos["MenuSections"][i]["Name"]
                if section == secciones[j]:
                    for k in range(0,len(datos["MenuSections"][i]["MenuItems"])):
                        for item in datos["MenuSections"][i]["MenuItems"]:
                            item['TaxRateId'] = newTaxRateId
                            for l in range(0,len(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"])):
                                for os in datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"]:
                                    for osi in datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]['MenuItemOptionSetItems']:
                                        osi['TaxRateId'] = newTaxRateId


    #changes the taxes for the selected items (only items for now)
    def slot_changeTaxSelectedItems(self,datos,itemSelected,tax):
        newTaxRateId = 0
        for i in range (0,len(datos['TaxRates'])):
            if i == tax:
                newTaxRateId = datos['TaxRates'][i]['TaxRateId']
                for j in range(0,len(itemSelected)):
                    for i in range(0,len(datos["MenuSections"])):
                        for k in range(0,len(datos["MenuSections"][i]["MenuItems"])):
                            item = datos["MenuSections"][i]["MenuItems"][k]['Name']
                            if item.lower() == itemSelected[j].lower():
                                datos["MenuSections"][i]["MenuItems"][k]['TaxRateId'] = newTaxRateId
                                for l in range(0,len(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"])):
                                    for os in datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"]:
                                        for osi in datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]['MenuItemOptionSetItems']:
                                            osi['TaxRateId'] = newTaxRateId


    #changes the taxes for all sections (only items for now)
    def slot_changeTaxAllSections(self,datos,tax):
        newTaxRateId = 0
        for i in range (0,len(datos['TaxRates'])):
            if i == tax:
                newTaxRateId = datos['TaxRates'][i]['TaxRateId']
            for i in range (0,len(datos["MenuSections"])):
                for k in range(0,len(datos["MenuSections"][i]["MenuItems"])):
                    for item in datos["MenuSections"][i]["MenuItems"]:
                        item['TaxRateId'] = newTaxRateId
                        for l in range(0,len(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"])):
                            for os in datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"]:
                                for osi in datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]['MenuItemOptionSetItems']:
                                    osi['TaxRateId'] = newTaxRateId

    def slot_RemoveTaxAllItems(self,datos,tax):
        newTaxRateId = tax
        for i in range (0,len(datos['TaxRates'])):
            #if i == tax:
                #newTaxRateId = datos['TaxRates'][i]['TaxRateId']
            for i in range (0,len(datos["MenuSections"])):
                for k in range(0,len(datos["MenuSections"][i]["MenuItems"])):
                    for item in datos["MenuSections"][i]["MenuItems"]:
                        item['TaxRateId'] = newTaxRateId
                        for l in range(0,len(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"])):
                            for os in datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"]:
                                for osi in datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]['MenuItemOptionSetItems']:
                                    osi['TaxRateId'] = newTaxRateId

    #overwrites the json file with the updated one
    def save_json(self,datos,selectedFile):
        with open(selectedFile, 'w') as archivo_nuevo:
            json.dump(datos, archivo_nuevo)
