from xml.dom import minidom

xml = minidom.parse('ejemplo.xml')
docs = xml.getElementsByTagName('doc')
for doc in docs:
    nodo1 = doc.getElementsByTagName('nodo1')[0]
    nodo2 = doc.getElementsByTagName('nodo2')[0]
    print(f"nodo1 = {nodo1.firstChild.data} | nodo2 = {nodo2.firstChild.data}")