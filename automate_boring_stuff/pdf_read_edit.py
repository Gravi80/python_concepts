import PyPDF2
import os

from PyPDF2.pdf import PageObject

# https://automatetheboringstuff.com/src/meetingminutes1.pdf
pdf_file = open(f"{os.getenv('HOME')}/Downloads/meetingminutes1.pdf", 'rb')
reader = PyPDF2.PdfFileReader(pdf_file)
print(reader.numPages)
page_0: PageObject = reader.getPage(0)
print(page_0.extractText())

for page_num in range(reader.numPages):
    print(reader.getPage(page_num).extractText())

pdf_file.close()
# Only supports page level editing, no content editing

# https://automatetheboringstuff.com/src/meetingminutes2.pdf
# Combine  meetingminutes1 with meetingminutes2
pdf1_file = open(f"{os.getenv('HOME')}/Downloads/meetingminutes1.pdf", 'rb')
pdf2_file = open(f"{os.getenv('HOME')}/Downloads/meetingminutes2.pdf", 'rb')
reader1 = PyPDF2.PdfFileReader(pdf1_file)
reader2 = PyPDF2.PdfFileReader(pdf2_file)

writer = PyPDF2.PdfFileWriter()
for page_num in range(reader1.numPages):
    writer.addPage(reader1.getPage(page_num))
for page_num in range(reader2.numPages):
    writer.addPage(reader2.getPage(page_num))

output_pdf = open(f"{os.getenv('HOME')}/Downloads/combinedminutes.pdf", 'wb')
writer.write(output_pdf)
output_pdf.close()
pdf1_file.close()
pdf2_file.close()
