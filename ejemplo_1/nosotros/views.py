from django.shortcuts import render

# Create your views here.
def nosotros_inicio(request):
    #return HttpResponse("Hola mundo con las manos en el codigo")
    return render(request,'nosotros/home.html',{})

def nosotros_nuestro_equipo(request):
    return render(request,'nosotros/nuestro_equipo.html',{})

def nosotros_nuestro_equipo_detalle(request,id,slug):
    #paso de parametros desde el metodo
    nombre="Gustavo Javier Marchena Barenas"
    lista = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
    return render(request,'nosotros/nuestro_equipo_detalle.html',{'id':id,'slug1':slug,'nombre':nombre,'diasSemana':lista}) 