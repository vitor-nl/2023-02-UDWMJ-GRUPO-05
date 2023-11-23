from django.db import models

# Create your models here.

from django.db import models

class Servicoadicional(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField('Descricao', max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        verbose_name = 'Serviço Adicional'
        verbose_name_plural = 'Serviços Adicionais'
        ordering =['id']

    def str(self):
        return self.nome

