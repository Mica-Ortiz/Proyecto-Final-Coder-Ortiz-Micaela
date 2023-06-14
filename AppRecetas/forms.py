from django import forms

class receta_formulario(forms.Form):
    titulo = forms.CharField()
    ingredientes = forms.CharField()
    pasos = forms.CharField()
    tiempo_de_coccion = forms.IntegerField()

class categoria_formulario(forms.Form):
    nombre = forms.CharField()

class usuario_formulario(forms.Form):
    usuario = forms.CharField()
    contraseña = forms.CharField()
    email = forms.EmailField()

class busca_receta_form(forms.Form):
    titulo = forms.CharField()

class busca_categoria_form(forms.Form):
    nombre = forms.CharField()

class busca_usuario_form(forms.Form):
    usuario = forms.CharField()