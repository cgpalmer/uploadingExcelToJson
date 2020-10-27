import os
from PyPDF2 import PdfFileMerger, PdfFileReader



print('received')
    
merger = PdfFileMerger()
pdfs = ['mypdf.pdf', 'mypdf2.pdf' ]

for pdf in pdfs:
    merger.append(pdf)

merger.write('result.pdf')

merger.close()