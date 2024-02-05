from django.urls import path
from .views import dise_inicio

urlpatterns = [
    path('',dise_inicio,name='diseno_inicio')
]