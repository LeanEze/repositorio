from multiprocessing import context
from django import http
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from mi_app.models import Curso, Estudiante


def saludo(request):

    fecha_hora_ahora = datetime.now()
    return HttpResponse(f"hola mundo {fecha_hora_ahora}")

def saludar_a(request, nombre):
    return HttpResponse(f"hola como estas{nombre.capitalize()}")


def saludo_personalizado(request): 
    context = {}
    
    if request.GET: 
        context["nombre"] = request.GET["nombre"]

    return render(request, "mi_app/index.html", context)

def listar_cursos(request):
    context = {}
    context["cursos"] = Curso.objects.all()#modelo
    return render(request, "mi_app/lista_cursos.html", context)#templete

def lista_estudadores(request):#intentar q funciones empiecen con un verbo.
    context = {}
    context["estudiante"] = Estudiante.objects.all()#model
    return render(request, 'Estudiante.html', context)