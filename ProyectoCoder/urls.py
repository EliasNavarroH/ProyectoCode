from django.urls import path
from django.contrib import admin

from AppCoder.views import inicio, listar_estudiantes, listar_profesores, listar_curso


urlpatterns = [
    path('estudiantes/', listar_estudiantes, name="listar_alumnos"),
    path('profesores/', listar_profesores, name="listar_profesores"),
    path('', inicio, name="inicio"),
    path('admin/', admin.site.urls),
    path('curso', listar_curso, name="listar_curso"),
]
