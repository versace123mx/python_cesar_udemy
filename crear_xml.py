import xml.etree.ElementTree as ET
root = ET.Element('root')

for numero in range(1,4):
    doc = ET.SubElement(root,'doc')
    ET.SubElement(doc,'nodo1',name='manzan').text=f'Texto nodo1 {numero}'
    ET.SubElement(doc,'nodo2',atributo='naranja').text=f'Texto nodo2 {numero}'

archivo = ET.ElementTree(root)
archivo.write('ejemplo.xml')