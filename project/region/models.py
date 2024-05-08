from django.db import models

# Create your models here.

class RegionCategoria(models.Model):
    """categoria de regio: urbana rural etc"""
    nombre = models.CharField(max_length=200, unique=True)
    zona = models.CharField(max_length=200, null=True, blank=True, verbose_name="zona")
    
    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = "region del curso"
        verbose_name_plural= "regiones de curso"
        