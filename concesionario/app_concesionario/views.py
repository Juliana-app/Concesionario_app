from django.shortcuts import render, redirect, get_object_or_404
from .forms import VehiculoForm
from .models import Vehiculo, Empresa

def vista_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    marcas = Vehiculo.objects.values_list('marca', flat=True).distinct()
    empresas = Empresa.objects.all()  # Obtener todas las empresas
    return render(request, 'vehiculos.html', {
        'vehiculos': vehiculos,
        'marcas': marcas,
        'empresas': empresas  # Pasar las empresas al contexto
    })
    
