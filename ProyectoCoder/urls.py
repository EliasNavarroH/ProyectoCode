from django.urls import path
from django.contrib import admin

from AppCoder.views import (inicio,listar_profesores, listar_curso, crear_curso, buscar_curso, ver_curso,eliminar_curso,
                            editar_curso, EstudiantesListView,EstudiantesCreateView, EstudiantesDeleteView,EstudiantesUpdateView,
                            EstudiantesDetailView,
)


urlpatterns = [
    path('profesores/', listar_profesores, name="listar_profesores"),
    path('', inicio, name="inicio"),
    path('admin/', admin.site.urls),
    path('curso/', listar_curso, name="listar_curso"),
    path('enviar-curso/', crear_curso, name="crear_curso"),
    path('buscar-curso/', buscar_curso, name="buscar_curso"),
    path('curso/<int:id>/', ver_curso, name="ver_curso"),
    path('editar-curso/<int:id>/', editar_curso, name="editar_curso"),
    path('eliminar-curso/<int:id>/', eliminar_curso, name="eliminar_curso"),
    #Vistas basadas en Class Based Views (Estudiantes)
    path('estudiantes/', EstudiantesListView.as_view(), name="lista_estudiantes"),
    path('crear-estudiantes/',EstudiantesCreateView.as_view(), name="crear_estudiantes"),
    path('editar-estudiantes/',EstudiantesUpdateView.as_view(), name="editar_estudiantes"),
    path('eliminar-estudiantes/',EstudiantesDeleteView.as_view(), name="eliminar_estudiantes"),
    path('estudiantes/<int:pk>/', EstudiantesDetailView.as_view(), name="ver_estudiante"),

]
