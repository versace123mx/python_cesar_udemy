from PyPDF2 import PdfMerger
from datetime import datetime

hoy = datetime.today()
timestamp = datetime.timestamp(hoy)

pdfs=['example.pdf','example_1706691361.532584.pdf','example_1706691478.487452.pdf','example_1706691985.119978.pdf','example_1706692099.958121.pdf','example_1706692219.711503.pdf','example_1706692402.473631.pdf']
nombre_salida = f'joinPDF_{timestamp}.pdf'
fusionar = PdfMerger()
for pdf in pdfs:
    fusionar.append(open(pdf,'rb'))

with open(nombre_salida,'wb') as salida:
    fusionar.write(salida)