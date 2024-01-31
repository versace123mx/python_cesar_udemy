import xlrd2
import os

ruta = os.path.dirname(os.path.abspath(__file__))
documento = xlrd2.open_workbook(ruta+'/archivo.xlsx')
hoja = documento.sheet_by_name('Hoja 1') 
for i in range(hoja.nrows):
    if i >= 1:
        print(f"ID = {int(hoja.cell_value(i,0))} | nombre = {hoja.cell_value(i,1)} | apellido ={hoja.cell_value(i,2)}")