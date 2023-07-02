from django import forms
from .models import Categoría, Recetas

class busca_receta_form(forms.Form):
    titulo = forms.CharField()

class busca_categoria_form(forms.Form):
    nombre = forms.CharField()

##formulario de recetas modificado

class RecetaForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(queryset=Categoría.objects.all(), widget=forms.Select, label='Categoría')

    class Meta:
        model = Recetas
        fields = ["titulo", "subtitulo", "ingredientes", "pasos", "tiempo_de_coccion", "categoria", "imagen"]