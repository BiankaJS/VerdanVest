from django.db import models
from django.conf import settings

class Ticket(models.Model):
  id = models.AutoField(primary_key=True)
  folio = models.TextField(null=True,blank=True)
  usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.TextField()
    email = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return f"{self.nombre} - {self.email}"