from PyPDF2 import PdfFileWriter, PdfFileReader
import textract
# pdf_file = "C:/Users/cxd/Desktop/SSD Backup/ALG/MietvertragAusweisETC.pdf"
pdf_file = "C:\\Users\\cxd\\Desktop\\SSD Backup\\Bewerbung\\Zeugnisse_Marvin_Calov.pdf"
# pdf_file = "C:/Users/cxd/Desktop/SSD Backup/Dank_PDF_Files/Mystisch/The Nag Hammadi Library.pdf"
inputpdf = PdfFileReader(open(pdf_file, "rb"),strict=False)
print( inputpdf.getPage(1).extractText())

# for page in inputpdf:
#     print("Neue Seite")
#     print(page.extractText())
output = PdfFileWriter()
for i in range(2,4):
    output.addPage(inputpdf.getPage(i))
for i in range(0,2):
    output.addPage(inputpdf.getPage(i))
pdf_cut = "C:\\Users\\cxd\\Desktop\\SSD Backup\\Bewerbung\\Zeugnisse_neu_Marvin_Calov.pdf"

with open(pdf_cut, "wb") as outputStream:
    output.write(outputStream)
