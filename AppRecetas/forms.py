from django import forms

class busca_receta_form(forms.Form):
    titulo = forms.CharField()

class busca_categoria_form(forms.Form):
    nombre = forms.CharField()

