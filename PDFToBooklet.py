from PyPDF4 import PdfFileWriter, PdfFileReader
import sys
import math

###################################################################################### Functions
def createBookletPages():
    
    # Page Count Check
    pageCount = pdf.getNumPages()
    if pageCount < 3:
        print(pdfFileName," : Single Sheet Only. Nothing to do.")
        sys.exit(1)

    # How many sheets and sides do we need?
    blankPageCheck = pageCount % 2
    requiredSheets = math.floor(pageCount / 2) + blankPageCheck
    print("Requires ",requiredSheets," sheets with ",blankPageCheck," blank side.")

    # Variables 
    outputArray = []

    # Reverse the first 2 pages then continue
    outputArray.append(1)
    outputArray.append(0)
    for i in range(pageCount):
        if i > 1:
            outputArray.append(i)
    if blankPageCheck == 1:
        outputArray.append(-1)
    
    return outputArray

###################################################################################### Starting Checks
try:
    pdfFileName = sys.argv[1]
    pdf = PdfFileReader(pdfFileName)
    print("Reading ",pdfFileName)
    firstPage = pdf.getPage(0)
    pageW = firstPage.mediaBox.getWidth()
    pageH = firstPage.mediaBox.getHeight()
except:
    print("No valid file specified.")
    sys.exit(1)

###################################################################################### Write Out the Result
output = PdfFileWriter()
for i in createBookletPages():
    if i < 0:
        output.addBlankPage(pageW,pageH)
    else:
        output.addPage(pdf.getPage(i))

outputStream = open(pdfFileName + '_book.pdf', "wb")
output.write(outputStream)
outputStream.close()
print("Completed.")