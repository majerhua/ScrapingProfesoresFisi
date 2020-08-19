from django.db import models

# Create your models here.
class Profesor(models.Model):
    nombre = models.CharField(max_length=200)
    urlGoogleScholar = models.TextField()

class Articulo(models.Model):
    nombre = models.TextField()
    citas = models.IntegerField()
    anio = models.IntegerField()
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)