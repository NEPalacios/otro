from django import forms


class ProductoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    cantidad = forms.IntegerField()

class ProductoBusqueda(forms.Form):
    nombre = forms.CharField(max_length=50)