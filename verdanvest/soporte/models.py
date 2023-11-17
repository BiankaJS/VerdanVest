from django.db import models
from django.conf import settings

class Ticket(models.Model):
  id = models.AutoField(primary_key=True)
  folio = models.TextField(null=True,blank=True)
  usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)