import fitz
pdf_file = "C:/Users/cxd/Desktop/SSD Backup/Dank_PDF_Files/Mystisch/The Nag Hammadi Library.pdf"
# pdf_file = "C:/Users/cxd/Desktop/SSD Backup/Dank_PDF_Files/Mystisch/The Nag Hammadi Library.pdf"
doc = fitz.open(pdf_file)
for page in doc:
    print("PAGE NUMBER" + str(page.number))
    print(page.get_text())