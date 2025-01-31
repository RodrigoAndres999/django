from django.shortcuts import render

from .models import Genero,Alumno
# Create your views here.

def index(request):
    alumnos = Alumno.objects.all()
    context = {"alumnos":alumnos}
    return render(request,"alumnos/index.html",context)

def listadoSQL(request):
    alumnos = Alumno.objects.raw('SELECT * FROM alumnos_alumno')
    print(alumnos)
    context = { "alumnos":alumnos }
    return render(request,"alumnos/listadoSQL.html", context)