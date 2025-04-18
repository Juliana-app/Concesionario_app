from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('portal/', include('app_concesionario.api.urls')),  # Incluir las URLs de la API
]