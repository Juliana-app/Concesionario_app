from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from app_concesionario.forms import VehiculoForm, EmpresaForm
from app_concesionario.models import Empresa
from app_concesionario.models import Vehiculo
from app_concesionario.api.serializers import EmpresaSerializer
from app_concesionario.api.serializers import VehiculoSerializer

#--------------------------------------------------------------------------------------------

# VISTAS PARA PROBAR LA API Y VERIFICAR QUE FUNCIONAN LOS MÉTODOS

# Vista para la API de Vehiculo y Empresa
class EmpresaAV(APIView):
    # Obtener todas las empresas
    def get(self, request, format=None):
        empresas = Empresa.objects.all()
        serializer = EmpresaSerializer(empresas, many=True)
        return Response(serializer.data)

    # Crear una nueva empresa
    def post(self, request, format=None):
        serializer = EmpresaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmpresaDetailAV(APIView):
    # Obtener, actualizar o eliminar una empresa específica
    def get(self, request, pk, format=None):
        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            raise NotFound("Empresa no encontrada")
        
        serializer = EmpresaSerializer(empresa)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            raise NotFound("Empresa no encontrada")

        serializer = EmpresaSerializer(empresa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            raise NotFound("Empresa no encontrada")

        empresa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class VehiculoAV(APIView):
    # Obtener todos los vehiculos
    def get(self, request, format=None):
        vehiculos = Vehiculo.objects.all()
        serializer = VehiculoSerializer(vehiculos, many=True)
        return Response(serializer.data)

    # Crear una nuevo vehiculo
    def post(self, request, format=None):
        serializer = VehiculoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VehiculoDetailAV(APIView):

    def get(self, request, pk):
        vehiculo = get_object_or_404(Vehiculo, pk=pk)
        serializer = VehiculoSerializer(vehiculo)
        return Response(serializer.data)

    def put(self, request, pk):
        vehiculo = get_object_or_404(Vehiculo, pk=pk)
        serializer = VehiculoSerializer(vehiculo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            vehiculo = Vehiculo.objects.get(pk=pk)
        except Vehiculo.DoesNotExist:
            raise NotFound("Vehiculo no encontrado")

        vehiculo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#--------------------------------------------------------------------------------------

# Vista para la página de vehículos

# Vista para el menú de vehículos
def vehiculo_menu(request, id):
    vehiculo = get_object_or_404(Vehiculo, pk=id)
    form = VehiculoForm(instance=vehiculo)
    return render(request, 'menubar/vehiculoMenu.html', {
        'vehiculo': vehiculo,
        'form': form
    })

# Vista para crear un vehículo
def crear_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vista-vehiculos')  # Redirige a la lista de vehículos
    else:
        form = VehiculoForm()
    return render(request, 'vehiculos/formulario_vehiculo.html', {'form': form})

# Vista para editar un vehículo
def actualizar_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, pk=vehiculo_id)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect('vehiculo_menu', id=vehiculo.id)  
    else:
        form = VehiculoForm(instance=vehiculo)
    return render(request, 'menubar/vehiculoMenu.html', {'vehiculo': vehiculo, 'form': form})

# Vista para eliminar un vehículo
def eliminar_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, pk=vehiculo_id)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect('vista-vehiculos')  # Redirige a la lista de vehículos
    return render(request, 'vehiculos.html', {'vehiculo': vehiculo})

# Vista para listar vehículos
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculos/listado.html', {'vehiculos': vehiculos})

#---------------------------------------------------------------------------------------

# Vista para la página de empresas

# Vista para listar empresas
def listar_empresas(request):
    empresas = Empresa.objects.all()
    return render(request, 'empresas/listado.html', {'empresas': empresas})

#Vista para editar empresas
def actualizar_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, pk=empresa_id)
    if request.method == 'POST':
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            return redirect('empresa_menu', id=empresa.id) 
    else:
        form = EmpresaForm(instance=empresa)
    return render(request, 'menubar/empresaMenu.html', {'empresa': empresa, 'form': form})


# Vista para eliminar empresas
def eliminar_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, pk=empresa_id)
    if request.method == 'POST':
        empresa.delete()
    return render(request, 'empresas.html', {'empresa': empresa})

#Vista para crear empresas
def crear_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vista-empresas') 
    else:
        form = EmpresaForm()
    return render(request, 'empresas/formulario_empresa.html', {'form': form})

#Vista para el menú de empresas
def empresa_menu(request, id):
    empresa = get_object_or_404(Empresa, pk=id)
    form = EmpresaForm(instance=empresa)
    return render(request, 'menubar/empresaMenu.html', {
        'empresa': empresa,
        'form': form
    })

#----------------------------------------------------------------------------------------