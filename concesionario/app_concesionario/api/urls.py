from django.urls import path
from app_concesionario.api.views import EmpresaAV, VehiculoAV
from app_concesionario.api.views import EmpresaDetailAV, VehiculoDetailAV



urlpatterns = [
    path('empresa/', EmpresaAV.as_view(), name='empresa-list'),  
    path('empresa/<int:pk>/', EmpresaDetailAV.as_view(), name='empresa-detail'),
    path('vehiculo/', VehiculoAV.as_view(), name='vehiculo-list'),  
    path('vehiculo/<int:pk>/', VehiculoDetailAV.as_view(), name='vehiculo-detail'),
    
    #path('vista_vehiculos/', vista_vehiculos, name='vista-vehiculos'),
    #path('empresas/', views.empresa_menu, name='empresa_menu'),
    #path('vehiculos/', views.vehiculo_menu, name='vehiculo_menu'),
    #path('vehiculos/nuevo/', views.crear_vehiculo, name='crear_vehiculo'),
    #path('vehiculos/editar/<int:vehiculo_id>/', views.actualizar_vehiculo, name='actualizar_vehiculo'),
    #path('vehiculos/eliminar/<int:vehiculo_id>/', views.eliminar_vehiculo, name='eliminar_vehiculo'),
]

