from django import forms
from app_concesionario.models import Vehiculo, Empresa

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['nombre', 'marca', 'modelo', 'color', 'placa', 'id_empresa']

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nombre', 'direccion', 'telefono', 'email']