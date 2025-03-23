
from os import listdir
from os.path import isfile

from cassis import *

import xlsxwriter

typeSystemFile = open("./dis-merged-typesystem.xml", 'rb')

typeSystem = load_typesystem(typeSystemFile);
outDir = "../output/"

workbook = xlsxwriter.Workbook("lemmas_ane_tokens.xlsx")
lemmasSheet = workbook.add_worksheet("lemmas")
tokensSheet = workbook.add_worksheet("tokens")


xmiFileNames = []
for fileName in listdir(outDir):
    if isfile(outDir + fileName) and fileName.endswith("xmi"):
        xmiFileNames.append(fileName)


lemmasRow = 0
col = 0
for header in ["file","Type","Text"]:
    lemmasSheet.write(lemmasRow, col, header)
    col = col + 1
lemmasSheet.set_column("A:A", 10)
lemmasSheet.set_column("B:B", 10)
lemmasSheet.set_column("C:C", 200)


tokensRow = 0
col = 0
for header in ["file","Token", "lemma","PostTag"]:
    tokensSheet.write(tokensRow, col, header)
    col = col + 1
tokensSheet.set_column("A:A", 10)
tokensSheet.set_column("B:B", 20)
tokensSheet.set_column("C:C", 20)
tokensSheet.set_column("D:D", 20)

xmiFileNames = sorted(xmiFileNames)
for xmiFileName in xmiFileNames:
    print(xmiFileName)
    xmiFile = open(outDir + xmiFileName, 'rb')
    cas = load_cas_from_xmi(xmiFile, typesystem=typeSystem)
    lemmasRow = lemmasRow + 1
    for paragraph in cas.select('gr.ilsp.types.Paragraph'):
        text = cas.get_covered_text(paragraph).strip()
        if text:
            lemmas = []
            for lemma in cas.select_covered("gr.ilsp.types.Lemma", paragraph):
                lemmas.append("'"+lemma.value+"'")
            lemmasSheet.write(lemmasRow, 0, xmiFileName)
            lemmasSheet.write(lemmasRow, 1, "Sentence")
            lemmasSheet.write(lemmasRow, 2, text)
            lemmasRow = lemmasRow + 1
            lemmasSheet.write(lemmasRow, 0, xmiFileName)
            lemmasSheet.write(lemmasRow, 1, "Lemmas")
            lemmasSheet.write(lemmasRow, 2, " ".join(lemmas))
            lemmasRow = lemmasRow + 1
    tokensRow = tokensRow + 1
    for token in cas.select('gr.ilsp.types.Token'):
        tokenText = cas.get_covered_text(token).strip()
        tokensSheet.write(tokensRow, 0, xmiFileName)
        tokensSheet.write(tokensRow, 1, tokenText)
        tokensSheet.write(tokensRow, 2, token.lemma.value)
        tokensSheet.write(tokensRow, 3, token.posTag.value)
        tokensRow = tokensRow + 1

workbook.close()



