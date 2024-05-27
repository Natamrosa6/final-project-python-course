from django.db import models
from ProyectoControlPrecios import create_supermarket

# Create your models here.
class CreateSupermarket(models.Model):
    name = models.CharField(max_length=500)
    location = models.TextField()

    supermarket = create_supermarket(name, location)