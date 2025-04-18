from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from app_concesionario.forms import VehiculoForm
from app_concesionario.models import Empresa
from app_concesionario.models import Vehiculo
from app_concesionario.api.serializers import EmpresaSerializer
from app_concesionario.api.serializers import VehiculoSerializer


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
    

def empresa_menu(request):
    return render(request, 'menubar/empresaMenu.html')

def vehiculo_menu(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'menubar/vehiculoMenu.html', {'vehiculos': vehiculos})

# Vista para crear un vehículo
def crear_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehiculo_menu')  # Redirige a la lista de vehículos
    else:
        form = VehiculoForm()
    return render(request, 'vehiculos/formulario_vehiculo.html', {'form': form})

# Vista para actualizar un vehículo
def actualizar_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, pk=vehiculo_id)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect('vehiculo_menu')
    else:
        form = VehiculoForm(instance=vehiculo)
    return render(request, 'vehiculos/formulario_vehiculo.html', {'form': form})

# Vista para eliminar un vehículo
def eliminar_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, pk=vehiculo_id)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect('vehiculo_menu')
    return render(request, 'vehiculos/confirmar_eliminacion.html', {'vehiculo': vehiculo})
