from django.urls import path
from .views import nosotros_inicio,nosotros_nuestro_equipo,nosotros_nuestro_equipo_detalle

urlpatterns = [
    path('',nosotros_inicio,name='nosotros_inicio'),#Esta es el inicio osea nosotros y es la que pinto en el primer link
    path('nuestro-equipo',nosotros_nuestro_equipo,name='nosotros_nuestro_equipo'),
    path('nuestro-equipo/detalle/<int:id>/<str:slug>',nosotros_nuestro_equipo_detalle,name='nosotros_nuestro_equipo_detalle')
]