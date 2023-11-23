from django.db import models

# Create your models here.

class Categoriaquarto(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    
    class Meta:
        verbose_name = 'Categoria quarto'
        verbose_name_plural = 'Categorias de quartos'
        ordering =['id']

    def __str__(self):
        return self.name