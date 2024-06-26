from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
      
    def __str__(self) -> str:
        return self.nombre

class Estudiante (models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.nombre

class Profesor (models.Model):
    nombre = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.nombre


class ClaseCategoria(models.Model):
    nombre = models.PositiveIntegerField(unique=True)
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True, blank=True)
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True, blank=True)
    estudiante = models.ManyToManyField(Estudiante)

    def __str__(self):
        return f"{self.nombre}, {self.curso}, {self.profesor}, {self.estudiante}"
    
    class Meta:
        verbose_name= "categoria de clase"
        verbose_name_plural = "categorias de clases"
    