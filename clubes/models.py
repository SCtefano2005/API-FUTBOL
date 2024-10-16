from django.db import models

class Departamento(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre

class Club(models.Model):
    nombre = models.CharField(max_length=300)
    estadio = models.CharField(max_length=300)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name='clubes')
    fecha_fundacion = models.IntegerField()
    
    def __str__(self):
        return self.nombre
    
