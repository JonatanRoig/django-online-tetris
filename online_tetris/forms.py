from django import forms
from .models import Sesion, Castigo


class SesionForm(forms.ModelForm):
    class Meta:
        model = Sesion
        fields = ['nombre', 'puntos', 'velocidad', 'ip']


class CastigoForm(forms.ModelForm):
    class Meta:
        model = Castigo
        fields = ['emisor', 'receptor']


