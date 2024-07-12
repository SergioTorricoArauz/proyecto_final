from django.contrib.auth.models import User
from django.db import models


class Camion(models.Model):
    nombre = models.CharField(max_length=10)
    chofer = models.IntegerField()
