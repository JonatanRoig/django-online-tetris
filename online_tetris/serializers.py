from . import models

from rest_framework import serializers


class SesionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Sesion
        fields = (
            'slug', 
            'nombre', 
            'created', 
            'last_updated', 
            'puntos', 
            'velocidad', 
            'ip', 
        )


class CastigoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Castigo
        fields = (
            'slug', 
            'created', 
        )


