from django.urls import path
from django.contrib import admin

from AppCoder.views import inicio, listar_estudiantes, listar_profesores, listar_curso, crear_curso, buscar_curso, ver_curso


urlpatterns = [
    path('estudiantes/', listar_estudiantes, name="listar_alumnos"),
    path('profesores/', listar_profesores, name="listar_profesores"),
    path('', inicio, name="inicio"),
    path('admin/', admin.site.urls),
    path('curso/', listar_curso, name="listar_curso"),
    path('enviar-curso/', crear_curso, name="crear_curso"),
    path('buscar-curso/', buscar_curso, name="buscar_curso"),
    path('curso/<int:id>/', ver_curso, name="ver_curso"),
]
