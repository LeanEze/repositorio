from django.contrib import admin
from django.urls import path
from mi_app.views import (listar_cursos, saludo, saludar_a, saludo_personalizado, lista_estudadores)



urlpatterns = [
    path('admin/', admin.site.urls),
    path("hola/",saludo),
    path('saludar/persona/<nombres>',saludar_a),
    path('saludo_personalizado/',saludo_personalizado), 
    path('listar_cursos/', listar_cursos)
    path('listar_estudiantes/', listar_Estudiantes)
    
    ]