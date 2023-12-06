from django.db import models
from cliente.models import Cliente
from quarto.models import Quarto

# Create your models here.
class Reserva(models.Model):
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_checkin = models.DateField()
    data_checkout = models.DateField()

    class Meta:
        verbose_name = 'reserva'
        verbose_name_plural = 'reservas'
        ordering =['id']

    def str(self):
        return f"Reserva para {self.cliente} - Quarto: {self.quarto}, de {self.data_checkin} a {self.data_checkout}"