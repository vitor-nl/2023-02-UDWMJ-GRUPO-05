from django.db import models

from categoriaquarto.models import Categoriaquarto

class Quarto(models.Model):
    numero = models.CharField('numero', max_length=10)
    categoriaquarto = models.ForeignKey(Categoriaquarto, on_delete=models.CASCADE)
    disponivel = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Quarto'
        verbose_name_plural = 'Quartos'
        ordering =['id']

    def str(self):
        return f"{self.numero} - {self.categoria}"

# Create your models here.
