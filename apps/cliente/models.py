from django.db import models

# Create your models here.

class Cliente(models.Model):
    primeiro_nome = models.CharField('Nome', max_length=50)
    ultimo_nome = models.CharField('Sobrenome', max_length=100) 
    endereço = models.CharField('Endereco', max_length=200)
    numero_telefone = models.CharField('Telefone celular', max_length=20)
    email = models.EmailField('E-mail',null=False, blank=False)
    escolha_genero = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )
    genero = models.CharField('Genero', max_length=1, choices=escolha_genero)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering =['id']

    def str(self):
        return self.primeiro_nome