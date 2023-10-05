from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import CompraFormulario
from AppCoder.models import *

# Create your views here.
"""
def profe_nuevo(request):
    profeN = Profesor(nombre="Pepe", apellido="Python", email="pepe@python.com", profesion="Biofisico")
    profeN.save()

    return HttpResponse(f"Hemos guardado al profesor {profeN.nombre}")


def curso_nuevo(request):
    mi_curso_favorito = Curso(nombre="Python", comision=44765)
    mi_curso_favorito.save()

    return HttpResponse(f"Bienvenidos al curso {mi_curso_favorito.nombre}")
"""

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def compra(request):

    comp1= Compra(nombre="Correa", numero="25")
    comp1.save

    return HttpResponse(f"El producto que has comprado es {comp1.nombre} y su numero de compra es {comp1.numero}.")

def ver_perros(request):

    return render(request, "AppCoder/ver_perros.html")

def ver_gatos(request):
 
    return render(request, "AppCoder/ver_gatos.html")

def ver_peces(request):

    return render(request, "AppCoder/ver_peces.html")

def compraFormulario(request):

    if request.method == "POST": #despues de dar click al boton enviar

        formulario1 = CompraFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            compra = Compra(producto=info["producto"], numero=info["numero"])

            compra.save()

        return render(request, "AppCoder/inicio.html")
    
    else:

        formulario1= CompraFormulario()

    return render(request, "AppCoder/compraFormulario.html", {"form1":formulario1})


def busquedaCompra(request):

    return render(request, "AppCoder/inicio.html")

def resultados(request):

    if request.GET["numero"]:

        numero = request.GET["numero"]
        compra = Compra.objects.filter(numero__icontains=numero)
    
        return render(request, "AppCoder/inicio.html", {"compras":compra, "numero":numero})
    
    else:

        respuesta = "No enviaste datos."

    return HttpResponse(respuesta)