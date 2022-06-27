from lzma import _FilterChain
from django import http
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def saludo(request):

    fecha_hora_ahora = datetime.now()
    return HttpResponse(f"hola mundo {fecha_hora_ahora}")
