import re
from django.shortcuts import render
from django.http import HttpResponse
from productos.models import Vegetales,Perecederos,NoPerecederos
from productos.forms import FormularioBusqueda,FormularioPerecederos,FormularioNoPerece, FormularioVegetal,FormularioPeredce,FormularioNoperece
# Create your views here.

def inicio(request):
    
    return render(request,"productos/index.html")

    
    
def vegetales(request):
    
    lista_vegetales  = Vegetales.objects.all()
    
    if request.GET.get("nombre_vegetal"):
         formulario = FormularioBusqueda(request.GET)
        
         if formulario.is_valid():
            data = formulario.cleaned_data
            lista_vegetales = Vegetales.objects.filter(nombre__icontains = data["nombre_vegetal"])
            
         return render(request,"productos/vegetales.html",{"vegetales":lista_vegetales,"formulario": formulario})
        
    else:
        formulario = FormularioBusqueda()    
        return render(request,"productos/vegetales.html",{"vegetales": lista_vegetales,"formulario": formulario})
    
    
    
def perecederos(request):
    
    lista_perecederos  = Perecederos.objects.all()
    
    if request.GET.get("nombre_perece"):
         formulario = FormularioPerecederos(request.GET)
        
         if formulario.is_valid():
            data2 = formulario.cleaned_data
            lista_perecederos = Perecederos.objects.filter(nombre__icontains = data2["nombre_perece"])
            
         return render(request,"productos/perecederos.html",{"perecederos":lista_perecederos,"formulario": formulario})
        
    else:
        formulario = FormularioPerecederos()    
        return render(request,"productos/perecederos.html",{"perecederos": lista_perecederos,"formulario": formulario})
    
    
    
    
def noperecederos(request):
    
    lista_productos  = NoPerecederos.objects.all()
    
    if request.GET.get("nombre_noperece"):
         formulario = FormularioNoPerece(request.GET)
        
         if formulario.is_valid():
            data = formulario.cleaned_data
            lista_productos = NoPerecederos.objects.filter(nombre__icontains = data["nombre_noperece"])
            
         return render(request,"productos/noperecederos.html",{"productos":lista_productos,"formulario": formulario})
        
    else:
        formulario = FormularioNoPerece()    
        return render(request,"productos/noperecederos.html",{"productos": lista_productos,"formulario": formulario})  


def prueba(request):
    
    return render(request, "productos/prueba.html")
    


def crear_vegetal(request):
    

    if request.method == "GET":
        form_vege = FormularioVegetal()
        return render(request, "productos/form_vegetal.html", {"form_vege":form_vege})
    else:

        form_vege = FormularioVegetal(request.POST)

        if form_vege.is_valid():

            data = form_vege.cleaned_data

            nombre = data.get("nombre")
            cosecha = data.get("cosecha")
            precio = data.get("precio")
            vege = Vegetales(nombre=nombre,cosecha=cosecha,precio=precio)
            

            vege.save()

            return render(request, "productos/index.html")
        
        else:
            return HttpResponse("Formulario no valido")


def crear_perecedero(request):
    
    if request.method == "GET":
        form_perece = FormularioPeredce()
        return render(request, "productos/form_perece.html", {"form_perece":form_perece})
    else:

        form_perece = FormularioPeredce(request.POST)

        if form_perece.is_valid():

            data = form_perece.cleaned_data

            nombre = data.get("nombre")
            fecha_vencimiento = data.get("fecha_vencimiento")
            precio = data.get("precio")
            pere = Perecederos(nombre=nombre,fecha_vencimiento=fecha_vencimiento,precio=precio)
            

            pere.save()

            return render(request, "productos/index.html")
        
        else:
            return HttpResponse("Formulario no valido")


def crear_noperece(request):
    
    if request.method == "GET":
        form_noperece = FormularioNoperece()
        return render(request, "productos/form_noperece.html", {"form_noperece":form_noperece})
    else:

        form_noperece = FormularioNoperece(request.POST)

        if form_noperece.is_valid():

            data = form_noperece.cleaned_data

            nombre = data.get("nombre")            
            precio = data.get("precio")
            nopere = Perecederos(nombre=nombre,precio=precio)
            

            nopere.save()

            return render(request, "productos/index.html")
        
        else:
            return HttpResponse("Formulario no valido")