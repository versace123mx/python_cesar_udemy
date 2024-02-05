import zipfile
from datetime import datetime

hoy = datetime.today()
timestamp = datetime.timestamp(hoy)

archivo = zipfile.ZipFile('pruebaZip_'+str(timestamp)+'.zip','w')
files = ['ejemplo.json','ejemplo.xml','archivo.xlsx','example_1706692402.473631.pdf','joinPDF_1706722090.959337.pdf']
for file in files:
    archivo.write(file,compress_type=zipfile.ZIP_DEFLATED)

archivo.close()