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

#shows a list of the os on the menu
    def slot_mostrarOS(self,datos):
        os = list()
        os1 = ""
        for i in range(0,len(datos["MenuSections"])):
            for k in range(0,len(datos["MenuSections"][i]["MenuItems"])):
                for l in range(0,len(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"])):
                    if datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["IsMasterOptionSet"] == False:
                        os1 = datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["Name"]
                    if len(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"]) == 0:
                        pass
                    elif os1 in os:
                        pass
                    else:
                        os.append(os1)
        return os
#shows a list of the items on the menu and in which sections you can find them
    def slot_mostrarItems(self,datos):
        items = list()
        for i in range(0,len(datos["MenuSections"])):
            section = datos["MenuSections"][i]['Name']
            if len(datos["MenuSections"][i]["MenuItems"]) == 0:
                pass
            elif section in items:
                pass
            else:
                items.append(section)
                for k in range(0,len(datos["MenuSections"][i]["MenuItems"])):
                    item = datos["MenuSections"][i]["MenuItems"][k]['Name']
                    items.append(item)
        return items

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


#changes the taxes for the selected items
    def slot_changeTaxSelectedItems(self,datos,itemSelected,tax):
        newTaxRateId = 0
        for i in range (0,len(datos['TaxRates'])):
            if i == tax:
                newTaxRateId = datos['TaxRates'][i]['TaxRateId']
        for j in range(0,len(itemSelected)):
            for h in range(0,len(datos["MenuSections"])):
                for k in range(0,len(datos["MenuSections"][h]["MenuItems"])):
                    item = datos["MenuSections"][h]["MenuItems"][k]['Name']
                    if item == itemSelected[j][1]:
                        datos["MenuSections"][h]["MenuItems"][k]['TaxRateId'] = newTaxRateId
                        for l in range(0,len(datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"])):
                            for os in datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"]:
                                for osi in datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"][l]['MenuItemOptionSetItems']:
                                    osi['TaxRateId'] = newTaxRateId

#changes the taxes for the selected os options (only items for now)
    def slot_changeTaxSelectedOS(self,datos,osSelected,os,tax):
        newTaxRateId = 0
        for i in range (0,len(datos['TaxRates'])):
            if i == tax:
                newTaxRateId = datos['TaxRates'][i]['TaxRateId']
        for j in range(0,len(osSelected)):
            for i in range(0,len(datos["MenuSections"])):
                for k in range(0,len(datos["MenuSections"][i]["MenuItems"])):
                    for l in range(0,len(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"])):
                        for m in range(0,len(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]['MenuItemOptionSetItems'])):
                            osName = datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["Name"]
                            if osSelected[j] == "Change All":
                                for osi in datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]['MenuItemOptionSetItems']:
                                    if osName == os[j]:
                                        osi['TaxRateId'] = newTaxRateId
                            elif osSelected[j] == datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]['MenuItemOptionSetItems'][m]['Name']:
                                datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]['MenuItemOptionSetItems'][m]['TaxRateId'] = newTaxRateId


    def slot_changeTaxSelectedSS(self,datos,SSitems,text,tax):
        newTaxRateId = 0
        for i in range (0,len(datos['TaxRates'])):
            if i == tax:
                newTaxRateId = datos['TaxRates'][i]['TaxRateId']
        for t in range(0,len(text)):
            for j in range(0,len(SSitems)):
                for i in range(0,len(datos["MenuSections"])):
                    for k in range(0,len(datos["MenuSections"][i]["MenuItems"])):
                        if SSitems[j] == datos["MenuSections"][i]["MenuItems"][k]["Name"]:
                            datos["MenuSections"][i]["MenuItems"][k]['TaxRateId'] = newTaxRateId
                            for l in range(0,len(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"])):
                                for os in datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"]:
                                    for osi in datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]['MenuItemOptionSetItems']:
                                        osi['TaxRateId'] = newTaxRateId

                        for l in range(0,len(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"])):
                            for m in range(0,len(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]['MenuItemOptionSetItems'])):
                                if SSitems[j] == datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]['MenuItemOptionSetItems'][m]['Name']:
                                    datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]['MenuItemOptionSetItems'][m]['TaxRateId'] = newTaxRateId                                   


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

#######################################################################################################################
#######################################################################################################################
##################### PRICE MODIFICATIONS #############################################################################

#changes the prices for the selected sections by percentaje
    def slot_changePricePercentajeSelectedSections(self,datos,secciones,price,MO,SO):
        price = int(price)/100
        actualizados = list()
        increased_price = float()
        original_price = float()
        actualizadosOS = list()
        for j in range(0,len(secciones)):
            for i in range(0,len(datos["MenuSections"])):
                section = datos["MenuSections"][i]["Name"]
                if section == secciones[j]:
                    for k in range(0,len(datos["MenuSections"][i]["MenuItems"])):
                            original_price = 0
                            increased_price = 0
                            new_price = float()
                            original_price = datos["MenuSections"][i]["MenuItems"][k]["Price"]
                            increased_price = float(original_price) * float(price)
                            new_price = float(increased_price) + float(original_price)
                            if datos["MenuSections"][i]["MenuItems"][k]['Name'] not in actualizados:
                                actualizados.append(datos["MenuSections"][i]["MenuItems"][k]['Name'])
                                datos["MenuSections"][i]["MenuItems"][k]['Price'] = float("{0:.2f}".format(new_price))
                            for l in range(0,len(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"])):
                                actualizadosOS.clear()
                                if (datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["IsMasterOptionSet"] == True and MO == True) or datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["IsMasterOptionSet"] == False and SO == True:
                                    for m in range(0,len(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"])):
                                        if datos["MenuSections"][i]["MenuItems"][k]['Name'] not in actualizadosOS:
                                            actualizadosOS.append(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]['Name'])
                                            new_price = float()
                                            original_price = 0
                                            increased_price = 0
                                            original_price = datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]["Price"]
                                            increased_price = float(original_price) * float(price)
                                            new_price = float(increased_price) + float(original_price)
                                            datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]["Price"] = float("{0:.2f}".format(new_price))


#changes the prices for the selected sections by Fixed Amount
    def slot_changePriceFixedAmountSelectedSections(self,datos,secciones,price,MO,SO):
        actualizados = list()
        original_price = float()
        actualizadosOS = list()
        for j in range(0,len(secciones)):
            for i in range(0,len(datos["MenuSections"])):
                section = datos["MenuSections"][i]["Name"]
                if section == secciones[j]:
                    for k in range(0,len(datos["MenuSections"][i]["MenuItems"])):
                        if datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"] == []:
                            original_price = 0
                            new_price = float()
                            original_price = datos["MenuSections"][i]["MenuItems"][k]["Price"]
                            new_price = float(price) + float(original_price)
                            if datos["MenuSections"][i]["MenuItems"][k]['Name'] not in actualizados:
                                actualizados.append(datos["MenuSections"][i]["MenuItems"][k]['Name'])
                                datos["MenuSections"][i]["MenuItems"][k]['Price'] = float("{0:.2f}".format(new_price))
                        else:
                            for l in range(0,len(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"])):
                                original_price = 0
                                new_price = float()
                                original_price = datos["MenuSections"][i]["MenuItems"][k]["Price"]
                                new_price = float(price) + float(original_price)
                                if datos["MenuSections"][i]["MenuItems"][k]['Name'] not in actualizados and datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][0]["IsMasterOptionSet"] != True:
                                    actualizados.append(datos["MenuSections"][i]["MenuItems"][k]['Name'])
                                    datos["MenuSections"][i]["MenuItems"][k]['Price'] = float("{0:.2f}".format(new_price))
                                actualizadosOS.clear()
                                if (datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["IsMasterOptionSet"] == True and MO == True) or datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["IsMasterOptionSet"] == False and SO == True:
                                    for m in range(0,len(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"])):
                                        if datos["MenuSections"][i]["MenuItems"][k]['Name'] not in actualizadosOS:
                                            actualizadosOS.append(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]['Name'])
                                            new_price = float()
                                            original_price = 0
                                            original_price = datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]["Price"]
                                            new_price = float(price) + float(original_price)
                                            datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]["Price"] = float("{0:.2f}".format(new_price))

##changes the full prices for the selected sections
    def slot_changePriceSelectedSections(self,datos,secciones,price,MO,SO):
        actualizados = list()
        actualizadosOS = list()
        for j in range(0,len(secciones)):
            for i in range(0,len(datos["MenuSections"])):
                section = datos["MenuSections"][i]["Name"]
                if section == secciones[j]:
                    for k in range(0,len(datos["MenuSections"][i]["MenuItems"])):
                        if datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"] == []:
                            if datos["MenuSections"][i]["MenuItems"][k]['Name'] not in actualizados:
                                actualizados.append(datos["MenuSections"][i]["MenuItems"][k]['Name'])
                                datos["MenuSections"][i]["MenuItems"][k]['Price'] = float("{0:.2f}".format(price))
                        else:
                            for l in range(0,len(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"])):
                                if datos["MenuSections"][i]["MenuItems"][k]['Name'] not in actualizados and datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][0]["IsMasterOptionSet"] != True:
                                    actualizados.append(datos["MenuSections"][i]["MenuItems"][k]['Name'])
                                    datos["MenuSections"][i]["MenuItems"][k]['Price'] = float("{0:.2f}".format(price))
                                actualizadosOS.clear()
                                if (datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["IsMasterOptionSet"] == True and MO == True) or datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["IsMasterOptionSet"] == False and SO == True:
                                    for m in range(0,len(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"])):
                                        if datos["MenuSections"][i]["MenuItems"][k]['Name'] not in actualizadosOS:
                                            actualizadosOS.append(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]['Name'])
                                            datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]["Price"] = float("{0:.2f}".format(price))


#changes the prices for the selected items by percentaje
    def slot_changePricePercentajeSelectedItems(self,datos,itemSelected,price,MO,SO):
        price = int(price)/100
        actualizados = list()
        increased_price = float()
        original_price = float()
        actualizadosOS = list()
        for j in range(0,len(itemSelected)):
            for i in range(0,len(datos["MenuSections"])):
                for k in range(0,len(datos["MenuSections"][i]["MenuItems"])):
                    item = datos["MenuSections"][i]["MenuItems"][k]['Name']
                    if item == itemSelected[j][1]:
                            original_price = 0
                            increased_price = 0
                            new_price = float()
                            original_price = datos["MenuSections"][i]["MenuItems"][k]["Price"]
                            increased_price = float(original_price) * float(price)
                            new_price = float(increased_price) + float(original_price)
                            if datos["MenuSections"][i]["MenuItems"][k]['Name'] not in actualizados:
                                actualizados.append(datos["MenuSections"][i]["MenuItems"][k]['Name'])
                                datos["MenuSections"][i]["MenuItems"][k]['Price'] = float("{0:.2f}".format(new_price))
                            for l in range(0,len(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"])):
                                actualizadosOS.clear()
                                if (datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["IsMasterOptionSet"] == True and MO == True) or datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["IsMasterOptionSet"] == False and SO == True:
                                    for m in range(0,len(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"])):
                                        if datos["MenuSections"][i]["MenuItems"][k]['Name'] not in actualizadosOS:
                                            actualizadosOS.append(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]['Name'])
                                            new_price = float()
                                            original_price = 0
                                            increased_price = 0
                                            original_price = datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]["Price"]
                                            increased_price = float(original_price) * float(price)
                                            new_price = float(increased_price) + float(original_price)
                                            datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]["Price"] = float("{0:.2f}".format(new_price))

#changes the prices for the selected items by Fixed Amount
    def slot_changePriceFixedAmountSelectedItems(self,datos,itemSelected,price,MO,SO):
        original_price = float()
        actualizados = list()
        actualizadosOS = list()
        for j in range(0,len(itemSelected)):
            for h in range(0,len(datos["MenuSections"])):
                for k in range(0,len(datos["MenuSections"][h]["MenuItems"])):
                    item = datos["MenuSections"][h]["MenuItems"][k]['Name']
                    if item == itemSelected[j][1]:
                        if datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"] == []:
                            original_price = 0
                            new_price = float()
                            original_price = datos["MenuSections"][h]["MenuItems"][k]["Price"]
                            new_price = float(price) + float(original_price)
                            if datos["MenuSections"][h]["MenuItems"][k]['Name'] not in actualizados:
                                actualizados.append(datos["MenuSections"][h]["MenuItems"][k]['Name'])
                                datos["MenuSections"][h]["MenuItems"][k]['Price'] = float("{0:.2f}".format(new_price))
                        else:
                            for l in range(0,len(datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"])):
                                original_price = 0
                                new_price = float()
                                original_price = datos["MenuSections"][h]["MenuItems"][k]["Price"]
                                new_price = float(price) + float(original_price)
                                if datos["MenuSections"][h]["MenuItems"][k]['Name'] not in actualizados and datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"][0]["IsMasterOptionSet"] != True:
                                    actualizados.append(datos["MenuSections"][h]["MenuItems"][k]['Name'])
                                    datos["MenuSections"][h]["MenuItems"][k]['Price'] = float("{0:.2f}".format(new_price))
                                actualizadosOS.clear()
                                if (datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"][l]["IsMasterOptionSet"] == True and MO == True) or datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"][l]["IsMasterOptionSet"] == False and SO == True:
                                    for m in range(0,len(datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"])):
                                        if datos["MenuSections"][h]["MenuItems"][k]['Name'] not in actualizadosOS:
                                            actualizadosOS.append(datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]['Name'])
                                            new_price = float()
                                            original_price = 0
                                            original_price = datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]["Price"]
                                            new_price = float(price) + float(original_price)
                                            datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]["Price"] = float("{0:.2f}".format(new_price))

##changes the full prices for the selected items
    def slot_changePriceSelectedItems(self,datos,itemSelected,price,MO,SO):
        actualizados = list()
        actualizadosOS = list()
        for j in range(0,len(itemSelected)):
            for h in range(0,len(datos["MenuSections"])):
                for k in range(0,len(datos["MenuSections"][h]["MenuItems"])):
                    item = datos["MenuSections"][h]["MenuItems"][k]['Name']
                    if item == itemSelected[j][1]:
                        if datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"] == []:
                            if datos["MenuSections"][h]["MenuItems"][k]['Name'] not in actualizados:
                                actualizados.append(datos["MenuSections"][h]["MenuItems"][k]['Name'])
                                datos["MenuSections"][h]["MenuItems"][k]['Price'] = float("{0:.2f}".format(price))
                        else:
                            for l in range(0,len(datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"])):
                                if datos["MenuSections"][h]["MenuItems"][k]['Name'] not in actualizados and datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"][0]["IsMasterOptionSet"] != True:
                                    actualizados.append(datos["MenuSections"][h]["MenuItems"][k]['Name'])
                                    datos["MenuSections"][h]["MenuItems"][k]['Price'] = float("{0:.2f}".format(price))
                                actualizadosOS.clear()
                                if (datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"][l]["IsMasterOptionSet"] == True and MO == True) or datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"][l]["IsMasterOptionSet"] == False and SO == True:
                                    for m in range(0,len(datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"])):
                                        if datos["MenuSections"][h]["MenuItems"][k]['Name'] not in actualizadosOS:
                                            actualizadosOS.append(datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]['Name'])
                                            datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]["Price"] = float("{0:.2f}".format(price))


#changes the prices for the selected items by percentaje
    def slot_changePricePercentajeSelectedOS(self,datos,osSelected,os,price):
        price = int(price)/100
        increased_price = float()
        original_price = float()
        for j in range(0,len(osSelected)):
            for h in range(0,len(datos["MenuSections"])):
                for k in range(0,len(datos["MenuSections"][h]["MenuItems"])):
                    for l in range(0,len(datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"])):
                        osName = datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"][l]["Name"]
                        for m in range(0,len(datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"][l]['MenuItemOptionSetItems'])):
                            if osSelected[j] == "Change All":
                                if osName == os[j]:
                                    #actualizadosOS.append(datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]['Name'])
                                    new_price = float()
                                    original_price = 0
                                    increased_price = 0
                                    original_price = datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]["Price"]
                                    increased_price = float(original_price) * float(price)
                                    new_price = float(increased_price) + float(original_price)
                                    datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]["Price"] = float("{0:.2f}".format(new_price))
                            elif osSelected[j] == datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"][l]['MenuItemOptionSetItems'][m]['Name']:
                                #actualizadosOS.append(datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]['Name'])
                                new_price = float()
                                original_price = 0
                                increased_price = 0
                                original_price = datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]["Price"]
                                increased_price = float(original_price) * float(price)
                                new_price = float(increased_price) + float(original_price)
                                datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"][l]['MenuItemOptionSetItems'][m]['Price'] = float("{0:.2f}".format(new_price))


#changes the prices for the selected OS by Fixed Amount
    def slot_changePriceFixedAmountSelectedOS(self,datos,osSelected,os,price):
        original_price = float()
        for j in range(0,len(osSelected)):
            for h in range(0,len(datos["MenuSections"])):
                for k in range(0,len(datos["MenuSections"][h]["MenuItems"])):
                    for l in range(0,len(datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"])):
                        osName = datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"][l]["Name"]
                        for m in range(0,len(datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"][l]['MenuItemOptionSetItems'])):
                            if osSelected[j] == "Change All":
                                if osName == os[j]:
                                    #actualizadosOS.append(datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]['Name'])
                                    new_price = float()
                                    original_price = 0
                                    original_price = datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]["Price"]
                                    new_price = float(price) + float(original_price)
                                    datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]["Price"] = float("{0:.2f}".format(new_price))
                            elif osSelected[j] == datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"][l]['MenuItemOptionSetItems'][m]['Name']:
                                #actualizadosOS.append(datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]['Name'])
                                new_price = float()
                                original_price = 0
                                original_price = datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]["Price"]
                                new_price = float(price) + float(original_price)
                                datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"][l]['MenuItemOptionSetItems'][m]['Price'] = float("{0:.2f}".format(new_price))

##changes the full prices for the selected OS
    def slot_changePriceSelectedOS(self,datos,osSelected,os,price):
        for j in range(0,len(osSelected)):
            for h in range(0,len(datos["MenuSections"])):
                for k in range(0,len(datos["MenuSections"][h]["MenuItems"])):
                    for l in range(0,len(datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"])):
                        osName = datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"][l]["Name"]
                        for m in range(0,len(datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"][l]['MenuItemOptionSetItems'])):
                            if osSelected[j] == "Change All":
                                if osName == os[j]:
                                    datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]["Price"] = float("{0:.2f}".format(price))
                            elif osSelected[j] == datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"][l]['MenuItemOptionSetItems'][m]['Name']:
                                datos["MenuSections"][h]["MenuItems"][k]["MenuItemOptionSets"][l]['MenuItemOptionSetItems'][m]['Price'] = float("{0:.2f}".format(price))


#changes the prices by Fixed Amount for the selected items on the Smart Search
    def slot_changePriceFixedAmountSelectedSS(self,datos,SSitems,text,price,MO,SO):
        original_price = float()
        actualizados = list()
        actualizadosOS = list()
        for t in range(0,len(text)):
            for j in range(0,len(SSitems)):
                for i in range(0,len(datos["MenuSections"])):
                    for k in range(0,len(datos["MenuSections"][i]["MenuItems"])):
                        if SSitems[j] == datos["MenuSections"][i]["MenuItems"][k]["Name"]:
                            if datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"] == []:
                                original_price = 0
                                new_price = float()
                                original_price = datos["MenuSections"][i]["MenuItems"][k]["Price"]
                                new_price = float(price) + float(original_price)
                                if datos["MenuSections"][i]["MenuItems"][k]['Name'] not in actualizados:
                                    actualizados.append(datos["MenuSections"][i]["MenuItems"][k]['Name'])
                                    datos["MenuSections"][i]["MenuItems"][k]['Price'] = float("{0:.2f}".format(new_price))
                            else:
                                for l in range(0,len(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"])):
                                    original_price = 0
                                    new_price = float()
                                    original_price = datos["MenuSections"][i]["MenuItems"][k]["Price"]
                                    new_price = float(price) + float(original_price)
                                    if datos["MenuSections"][i]["MenuItems"][k]['Name'] not in actualizados and datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][0]["IsMasterOptionSet"] != True:
                                        actualizados.append(datos["MenuSections"][i]["MenuItems"][k]['Name'])
                                        datos["MenuSections"][i]["MenuItems"][k]['Price'] = float("{0:.2f}".format(new_price))
                                    actualizadosOS.clear()
                                    if (datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["IsMasterOptionSet"] == True and MO == True) or datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["IsMasterOptionSet"] == False and SO == True:
                                        for m in range(0,len(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"])):
                                            if datos["MenuSections"][i]["MenuItems"][k]['Name'] not in actualizadosOS:
                                                actualizadosOS.append(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]['Name'])
                                                new_price = float()
                                                original_price = 0
                                                original_price = datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]["Price"]
                                                new_price = float(price) + float(original_price)
                                                datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]["Price"] = float("{0:.2f}".format(new_price))
                        for l in range(0,len(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"])):
                            for m in range(0,len(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]['MenuItemOptionSetItems'])):
                                if SSitems[j] == datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]['MenuItemOptionSetItems'][m]['Name']:
                                    new_price = float()
                                    original_price = 0
                                    original_price = datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]["Price"]
                                    new_price = float(price) + float(original_price)
                                    datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]['MenuItemOptionSetItems'][m]['Price'] = float("{0:.2f}".format(new_price))

#changes the prices by percentaje for the selected items on the Smart Search
    def slot_changePricePercentajeSelectedSS(self,datos,SSitems,text,price,MO,SO):
        original_price = float()
        price = int(price)/100
        increased_price = float()
        actualizados = list()
        actualizadosOS = list()
        for t in range(0,len(text)):
            for j in range(0,len(SSitems)):
                for i in range(0,len(datos["MenuSections"])):
                    for k in range(0,len(datos["MenuSections"][i]["MenuItems"])):
                        if SSitems[j] == datos["MenuSections"][i]["MenuItems"][k]["Name"]:
                            if datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"] == []:
                                original_price = 0
                                increased_price = 0
                                new_price = float()
                                original_price = datos["MenuSections"][i]["MenuItems"][k]["Price"]
                                increased_price = float(original_price) * float(price)
                                new_price = float(increased_price) + float(original_price)
                                if datos["MenuSections"][i]["MenuItems"][k]['Name'] not in actualizados:
                                    actualizados.append(datos["MenuSections"][i]["MenuItems"][k]['Name'])
                                    datos["MenuSections"][i]["MenuItems"][k]['Price'] = float("{0:.2f}".format(new_price))
                            else:
                                for l in range(0,len(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"])):
                                    original_price = 0
                                    increased_price = 0
                                    new_price = float()
                                    original_price = datos["MenuSections"][i]["MenuItems"][k]["Price"]
                                    increased_price = float(original_price) * float(price)
                                    new_price = float(increased_price) + float(original_price)
                                    if datos["MenuSections"][i]["MenuItems"][k]['Name'] not in actualizados and datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][0]["IsMasterOptionSet"] != True:
                                        actualizados.append(datos["MenuSections"][i]["MenuItems"][k]['Name'])
                                        datos["MenuSections"][i]["MenuItems"][k]['Price'] = float("{0:.2f}".format(new_price))
                                    actualizadosOS.clear()
                                    if (datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["IsMasterOptionSet"] == True and MO == True) or datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["IsMasterOptionSet"] == False and SO == True:
                                        for m in range(0,len(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"])):
                                            if datos["MenuSections"][i]["MenuItems"][k]['Name'] not in actualizadosOS:
                                                actualizadosOS.append(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]['Name'])
                                                new_price = float()
                                                original_price = 0
                                                increased_price = 0
                                                original_price = datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]["Price"]
                                                increased_price = float(original_price) * float(price)
                                                new_price = float(increased_price) + float(original_price)
                                                datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]["Price"] = float("{0:.2f}".format(new_price))
                        for l in range(0,len(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"])):
                            for m in range(0,len(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]['MenuItemOptionSetItems'])):
                                if SSitems[j] == datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]['MenuItemOptionSetItems'][m]['Name']:
                                    new_price = float()
                                    original_price = 0
                                    increased_price = 0
                                    original_price = datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]["Price"]
                                    increased_price = float(original_price) * float(price)
                                    new_price = float(increased_price) + float(original_price)
                                    datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]['MenuItemOptionSetItems'][m]['Price'] = float("{0:.2f}".format(new_price))

##changes the full prices for the selected items on the Smart Search
    def slot_changePriceSelectedSelectedSS(self,datos,SSitems,text,price,MO,SO):
        actualizados = list()
        actualizadosOS = list()
        for t in range(0,len(text)):
            for j in range(0,len(SSitems)):
                for i in range(0,len(datos["MenuSections"])):
                    for k in range(0,len(datos["MenuSections"][i]["MenuItems"])):
                        if SSitems[j] == datos["MenuSections"][i]["MenuItems"][k]["Name"]:
                            if datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"] == []:
                                if datos["MenuSections"][i]["MenuItems"][k]['Name'] not in actualizados:
                                    actualizados.append(datos["MenuSections"][i]["MenuItems"][k]['Name'])
                                    datos["MenuSections"][i]["MenuItems"][k]['Price'] = float("{0:.2f}".format(price))
                            else:
                                for l in range(0,len(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"])):
                                    if datos["MenuSections"][i]["MenuItems"][k]['Name'] not in actualizados and datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][0]["IsMasterOptionSet"] != True:
                                        actualizados.append(datos["MenuSections"][i]["MenuItems"][k]['Name'])
                                        datos["MenuSections"][i]["MenuItems"][k]['Price'] = float("{0:.2f}".format(price))
                                    actualizadosOS.clear()
                                    if (datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["IsMasterOptionSet"] == True and MO == True) or datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["IsMasterOptionSet"] == False and SO == True:
                                        for m in range(0,len(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"])):
                                            if datos["MenuSections"][i]["MenuItems"][k]['Name'] not in actualizadosOS:
                                                actualizadosOS.append(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]['Name'])
                                                datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]["MenuItemOptionSetItems"][m]["Price"] = float("{0:.2f}".format(price))
                        for l in range(0,len(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"])):
                            for m in range(0,len(datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]['MenuItemOptionSetItems'])):
                                if SSitems[j] == datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]['MenuItemOptionSetItems'][m]['Name']:
                                    datos["MenuSections"][i]["MenuItems"][k]["MenuItemOptionSets"][l]['MenuItemOptionSetItems'][m]['Price'] = float("{0:.2f}".format(price))
