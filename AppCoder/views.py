from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from datetime import datetime

from AppCoder.models import Estudiante, Profesor, Curso
from AppCoder.forms import CursoFormulario



def inicio(request):
    return render(
        request=request,
        template_name='AppCoder/inicio.html',
    )


def listar_estudiantes(request):
    contexto = {
        'estudiantes': Estudiante.objects.all()
     }
    return render(
        request=request,
        template_name='AppCoder/lista_estudiantes.html',
        context=contexto,
    )


def listar_profesores(request):

    contexto1= {
        'profesores': Profesor.objects.all()

    } 
    return render(
    request=request, 
    template_name='AppCoder/lista_profesores.html',
    context=contexto1,
    )


def listar_curso(request):

    contexto1= {
        'cursos': Curso.objects.all()

    } 
    return render(
    request=request, 
    template_name='AppCoder/lista_cursos.html',
    context=contexto1,
    )


def ver_curso(request, id):
    curso = Curso.objects.get(id=id)
    contexto1= {
        'cursos': curso

    } 
    return render(
    request=request, 
    template_name='AppCoder/detalle_curso.html',
    context=contexto1,
    )


def crear_curso(request):
    if request.method == "POST": # cuando es post y el form es valido, se crea el formulario y se redirecciona a la url exitosa
        formulario = CursoFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            curso = Curso(nombre=data['nombre'], camada=data['camada'], descripcion=data['descripcion'])
            curso.save()
            url_exitosa = reverse ('listar_curso')
            return redirect(url_exitosa)
    else: #GET
        formulario = CursoFormulario()
    return render(
         request=request,
         template_name='AppCoder/formulario_curso.html',
         context={'formulario':formulario},
    )


def  buscar_curso(request):
    if request.method == "POST":
        data = request.POST
        cursos = Curso.objects.filter(nombre__contains=data['nombre'],)
        contexto = {
            'cursos':cursos
        }
        return render(
            request=request,
            template_name='AppCoder/lista_cursos.html',
            context= contexto,
        )
   