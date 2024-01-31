import json
data = {}
data['post'] = []
for i in range(1,11):
    data['post'].append({
        'id':i,
        'titulo':f'Titulo de la publicación {i}',
        'slug':f'titulo-de-la-publicacion-{i}',
        'detalle':f'texto de detalle {i}',
        'fecha':'2022-04-30'
    })

with open('ejemplo.json','w') as file:
    json.dump(data,file,indent=4)