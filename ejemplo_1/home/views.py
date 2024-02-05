from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404

def home_inicio(request):
    #return HttpResponse("Hola mundo con las manos en el codigo")
    return render(request,'home/home.html',{})