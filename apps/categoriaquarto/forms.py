from django import forms
from .models import Categoriaquarto

class CategoriaquartoForm(forms.ModelForm):

    class Meta:
        model = Categoriaquarto
        exclude = ()