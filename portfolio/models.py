from django.db import models

class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    tecnologia = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='proyectos/', blank=True, null=True)
    url_github = models.URLField(blank=True)
    url_demo = models.URLField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ['-fecha_creacion']