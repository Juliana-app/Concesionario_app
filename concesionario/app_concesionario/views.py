from django.shortcuts import render, redirect, get_object_or_404
from .forms import VehiculoForm, EmpresaForm
from .models import Vehiculo, Empresa

def vista_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    marcas = Vehiculo.objects.values_list('marca', flat=True).distinct()
    empresas = Empresa.objects.all()

    # Capturamos los valores enviados por GET para los filtros
    nombre = request.GET.get('nombre', '')
    marca = request.GET.get('marca', '')
    modelo = request.GET.get('modelo', '')
    color = request.GET.get('color', '')
    placa = request.GET.get('placa', '')
    fecha_registro = request.GET.get('fecha_registro', '')
    empresa_id = request.GET.get('empresa', '')

    # Aplicamos los filtros si hay valores
    if nombre:
        vehiculos = vehiculos.filter(nombre__icontains=nombre)
    if marca:
        vehiculos = vehiculos.filter(marca__icontains=marca)
    if modelo:
        vehiculos = vehiculos.filter(modelo__icontains=modelo)
    if color:
        vehiculos = vehiculos.filter(color__icontains=color)
    if placa:
        vehiculos = vehiculos.filter(placa__icontains=placa)
    if fecha_registro:
        vehiculos = vehiculos.filter(fecha_registro=fecha_registro)
    if empresa_id:
        vehiculos = vehiculos.filter(id_empresa__id=empresa_id)

    # Diccionario de formularios para los modales de edición
    formularios = {v.id: VehiculoForm(instance=v) for v in vehiculos}

    # Pasamos también los valores actuales de los filtros para que los inputs los mantengan
    return render(request, 'vehiculos.html', {
        'vehiculos': vehiculos,
        'marcas': marcas,
        'empresas': empresas,
        'formularios': formularios,
        'filtros': {
            'nombre': nombre,
            'marca': marca,
            'modelo': modelo,
            'color': color,
            'placa': placa,
            'fecha_registro': fecha_registro,
            'empresa': empresa_id
        }
    })

def vista_empresas(request):
    empresas = Empresa.objects.all()

    # Capturamos los valores enviados por GET para los filtros
    nombre = request.GET.get('nombre', '')
    direccion = request.GET.get('direccion', '')
    telefono = request.GET.get('telefono', '')
    email = request.GET.get('email', '')

    # Aplicamos los filtros si hay valores
    if nombre:
        empresas = empresas.filter(nombre__icontains=nombre)
    if direccion:
        empresas = empresas.filter(direccion__icontains=direccion)
    if telefono:
        empresas = empresas.filter(telefono__icontains=telefono)
    if email:
        empresas = empresas.filter(email__icontains=email)

    # Diccionario de formularios para los modales de edición
    formularios = {v.id: EmpresaForm(instance=v) for v in empresas}

    return render(request, 'empresas.html', {
        'empresas': empresas,
        'formularios': formularios,
        'filtros': {
            'nombre': nombre,
            'direccion': direccion,
            'telefono': telefono,
            'email': email
        }
    })

