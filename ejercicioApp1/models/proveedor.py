from django.db import models

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre_empresa = models.CharField(max_length=100)
    pais_origen = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    tipo_colaboracion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_empresa

