from django.urls import path
from app_concesionario.api.views import EmpresaAV, VehiculoAV
from app_concesionario.api.views import EmpresaDetailAV, VehiculoDetailAV
from app_concesionario.views import vista_vehiculos, vista_empresas
from . import views
from .views import listar_vehiculos, listar_empresas

urlpatterns = [
    path('empresa/', EmpresaAV.as_view(), name='empresa-list'),  
    path('empresa/<int:pk>/', EmpresaDetailAV.as_view(), name='empresa-detail'),
    
    path('vehiculo/', VehiculoAV.as_view(), name='vehiculo-list'),  
    path('vehiculo/<int:pk>/', VehiculoDetailAV.as_view(), name='vehiculo-detail'),
    
    path('vista_vehiculos/', vista_vehiculos, name='vista-vehiculos'),
    path('vista_empresas/', vista_empresas, name='vista-empresas'),
    
    path('empresas/<int:id>/', views.empresa_menu, name='empresa_menu'),
    path('empresas/crear/', views.crear_empresa, name='crear_empresa'),
    path('empresas/editar/<int:empresa_id>/', views.actualizar_empresa, name='actualizar_empresa'),
    path('empresas/eliminar/<int:empresa_id>/', views.eliminar_empresa, name='eliminar_empresa'),
    
    path('vehiculos/<int:id>/', views.vehiculo_menu, name='vehiculo_menu'),
    path('vehiculos/crear/', views.crear_vehiculo, name='crear_vehiculo'),
    path('vehiculos/editar/<int:vehiculo_id>/', views.actualizar_vehiculo, name='actualizar_vehiculo'),
    path('vehiculos/eliminar/<int:vehiculo_id>/', views.eliminar_vehiculo, name='eliminar_vehiculo'),
    
    path('vehiculos/listado/', listar_vehiculos, name='listar_vehiculos'),
    path('empresas/listado/', listar_empresas, name='listar_empresas'),

]

