from django.db import models

class Material(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField()
    sostenibilidad = models.CharField(max_length=255, null=True, blank=True)
    urlImagen = models.TextField(null=True, blank=True)

class Ingrediente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField()
    función = models.TextField()
    preocupaciones = models.TextField()
    propiedades_dermatologicas = models.TextField()
    toxicidad = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    urlImagen = models.TextField(null=True, blank=True)