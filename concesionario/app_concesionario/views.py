from django.shortcuts import render, redirect, get_object_or_404
from .forms import VehiculoForm, EmpresaForm
from .models import Vehiculo, Empresa

def vista_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    marcas = Vehiculo.objects.values_list('marca', flat=True).distinct()
    empresas = Empresa.objects.all()

    formularios = {v.id: VehiculoForm(instance=v) for v in vehiculos}

    return render(request, 'vehiculos.html', {
        'vehiculos': vehiculos,
        'marcas': marcas,
        'empresas': empresas,
        'formularios': formularios
    })

def vista_empresas(request):

    empresas = Empresa.objects.all()

    formularios = {v.id: EmpresaForm(instance=v) for v in empresas}

    return render(request, 'empresas.html', {
        'empresas': empresas,
        'formularios': formularios
    })