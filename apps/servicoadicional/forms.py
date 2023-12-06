from django import forms
from .models import Servicoadicional

class ServicoadicionalForm(forms.ModelForm):

    class Meta:
        model = Servicoadicional
        exclude = ()