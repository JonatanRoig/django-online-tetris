from django.contrib import admin
from django import forms
from .models import Sesion, Castigo

class SesionAdminForm(forms.ModelForm):

    class Meta:
        model = Sesion
        fields = '__all__'


class SesionAdmin(admin.ModelAdmin):
    form = SesionAdminForm
    list_display = ['nombre', 'slug', 'created', 'last_updated', 'puntos', 'velocidad', 'ip']
    readonly_fields = ['nombre', 'slug', 'created', 'last_updated', 'puntos', 'velocidad', 'ip']

admin.site.register(Sesion, SesionAdmin)


class CastigoAdminForm(forms.ModelForm):

    class Meta:
        model = Castigo
        fields = '__all__'


class CastigoAdmin(admin.ModelAdmin):
    form = CastigoAdminForm
    list_display = ['slug', 'created']
    readonly_fields = ['slug', 'created']

admin.site.register(Castigo, CastigoAdmin)


