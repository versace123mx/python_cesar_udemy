from django.shortcuts import render

# Create your views here.


def dise_inicio(request):
    #return HttpResponse("Hola mundo con las manos en el codigo")
    return render(request,'diseno/home.html',{})