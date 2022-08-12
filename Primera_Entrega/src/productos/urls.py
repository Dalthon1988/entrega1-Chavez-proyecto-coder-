from django.urls import path
from productos.views import *

urlpatterns= [
    
    path("",inicio),
    path("vegetales/",vegetales,name='vegetales'),
    path("perecederos/",perecederos,name='perecederos'),
    path("noperecederos/",noperecederos,name='noperecederos'),
    path("vegetal/crear",crear_vegetal,name='vegetal_crear'),
    path("perecedero/crear",crear_perecedero,name='perecedero_crear'),
    path("noperece/crear",crear_noperece,name="noperece_crear")
   # path("agregar/",agregar_producto)
    
    
    
]


