from os import listdir
from os.path import isfile

from cassis import *

import xlsxwriter

typeSystemFile = open("./dis-merged-typesystem.xml", 'rb')

typeSystem = load_typesystem(typeSystemFile)
outDir = "../output/"

workbook = xlsxwriter.Workbook("armyUnits.xlsx")
worksheet = workbook.add_worksheet("data")
worksheet.set_column("A:A", 10)
worksheet.set_column("B:B", 100)
row = 0
col = 0
for header in ["file", "Record", "doctype", "date", "subject", "sender", "adressee", "unit1", "unit2", "unit3", "unit4",
               "geo1", "geo2", "geo3", "geo4"]:
    worksheet.write(row, col, header)
    col = col + 1

xmiFileNames = []
for fileName in listdir(outDir):
    if isfile(outDir + fileName) and fileName.endswith("xmi"):
        xmiFileNames.append(fileName)

xmiFileNames = sorted(xmiFileNames)

for xmiFileName in xmiFileNames:
    print(xmiFileName)
    xmiFile = open(outDir + xmiFileName, 'rb')
    cas = load_cas_from_xmi(xmiFile, typesystem=typeSystem)
    row = row + 1
    for paragraph in cas.select('gr.ilsp.types.Paragraph'):
        col = 0
        worksheet.write(row, col, xmiFileName)
        col = col + 1
        worksheet.write(row, col, cas.get_covered_text(paragraph))

        for annotation in ["gr.ilsp.types.dis.DISDocType", "gr.ilsp.types.dis.DISDate", "gr.ilsp.types.dis.DISSubject",
                           "gr.ilsp.types.dis.DISSender", "gr.ilsp.types.dis.DISAddressee"]:
            col = col + 1
            value = next(cas.select_covered(annotation, paragraph), None)
            if value:
                worksheet.write(row, col, value.get_covered_text().strip())

        addedUnits = []
        for armyUnit in cas.select_covered("gr.ilsp.nlp.dis.titles.ruta.ArmyUnit.ArmyUnit", paragraph):
            unitText = armyUnit.get_covered_text().strip()
            if unitText not in addedUnits:
                if len(addedUnits) < 4:
                    col = col + 1
                    worksheet.write(row, col, unitText)
                    addedUnits.append(unitText)
        col = col + 4 - len(addedUnits)

        addedGeoNames = []
        for geoName in cas.select_covered("gr.ilsp.types.dis.Geoname", paragraph):
            geoText = geoName.get_covered_text().strip()
            if geoText not in addedGeoNames:
                if len(addedGeoNames) < 4:
                    col = col + 1
                    worksheet.write(row, col, geoText)
                    addedUnits.append(geoText)
        row = row + 1

workbook.close()



