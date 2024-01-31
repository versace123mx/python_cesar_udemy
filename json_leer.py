import json

with open('ejemplo.json') as file:
    datos = json.load(file)

#print(datos)

for dato in datos['post']:
    print(f"ID = {dato['id']}\nTitulo = {dato['titulo']}\nslug={dato['slug']}\nfecha={dato['fecha']}")
    print(f'---------------------------------------------------------------')