from django import forms


class CursoFormulario(forms.Form):
     nombre = forms.CharField(max_length=64)
     camada = forms.IntegerField()