from django.db import models

COLOR = (
    ('Blanco', 'Blanco'),
    ('Azul', 'Azul'),
    ('Rojo', 'Rojo'),
    ('Negro', 'Negro'),
    ('Gris', 'Gris'),
    ('Naranja', 'Naranja'),
)

class Empresa(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre

class Vehiculo(models.Model):
    nombre = models.CharField(max_length=200)
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    color = models.CharField(max_length=200, choices=COLOR)
    placa = models.CharField(max_length=200)
    fecha_registro = models.DateField(auto_now_add=True)
    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="vehiculo_list")
    
    def __str__(self):
        return self.nombre

