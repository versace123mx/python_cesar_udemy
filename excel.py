import pandas as pd
from pandas import ExcelWriter
import os

ruta = os.path.dirname(os.path.abspath(__file__))
#print(ruta+'\\hola.txt')
datos = pd.DataFrame({
    'id':[1,2,3,4],
    'nombre':['Juan','Pedro','Luis','Mateo'],
    'apellido':['Martinez','Perez','Ñnadú','Marchena']
})
datos = datos[['id','nombre','apellido']]

writer = ExcelWriter('archivo.xlsx')
datos.to_excel(writer,"Hoja 1",index=False)
writer.close()
