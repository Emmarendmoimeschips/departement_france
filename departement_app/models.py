from django.db import models

class Departement(models.Model):
    numero = models.IntegerField()
    nom = models.CharField(max_length=100)
