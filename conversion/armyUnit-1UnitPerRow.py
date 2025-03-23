
from os import listdir
from os.path import isfile

from cassis import *

import xlsxwriter

typeSystemFile = open("./dis-merged-typesystem.xml", 'rb')

typeSystem = load_typesystem(typeSystemFile);
outDir = "../output/"

workbook = xlsxwriter.Workbook("armyUnits-1UnitPerRow.xlsx")
worksheet = workbook.add_worksheet("data")
worksheet.set_column("A:A", 10)
worksheet.set_column("B:B", 100)
worksheet.set_column("C:C", 80)
worksheet.set_column("D:D", 40)

row = 0
col = 0
for header in ["file","Record", "lemmas", "army unit"]:
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
        text = cas.get_covered_text(paragraph).strip()
        if text:
            lemmas = []
            for lemma in cas.select_covered("gr.ilsp.types.Lemma", paragraph):
                lemmas.append("'"+lemma.value+"'")
            addedUnits = set()
            for armyUnit in cas.select_covered("gr.ilsp.nlp.dis.titles.ruta.ArmyUnit.ArmyUnit", paragraph):
                unitText = armyUnit.get_covered_text().strip()
                if unitText not in addedUnits:
                    col = 0
                    worksheet.write(row, col, xmiFileName)
                    col = col + 1
                    worksheet.write(row, col, text)
                    col = col + 1
                    worksheet.write(row, col, " ".join(lemmas))
                    col = col + 1
                    worksheet.write(row, col, armyUnit.get_covered_text())
                    addedUnits.add(unitText)
            if len(addedUnits) > 0:
                row = row + 1

workbook.close()



