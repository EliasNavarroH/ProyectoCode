from django import forms


class CursoFormulario(forms.Form):
     nombre = forms.CharField(max_length=64)
     camada = forms.IntegerField(required=True) #si no se envia la camada, el formulario envia error