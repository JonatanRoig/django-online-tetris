from . import models
from . import serializers
from rest_framework import viewsets, permissions


class SesionViewSet(viewsets.ModelViewSet):
    """ViewSet for the Sesion class"""

    queryset = models.Sesion.objects.all()
    serializer_class = serializers.SesionSerializer
    permission_classes = [permissions.IsAuthenticated]


class CastigoViewSet(viewsets.ModelViewSet):
    """ViewSet for the Castigo class"""

    queryset = models.Castigo.objects.all()
    serializer_class = serializers.CastigoSerializer
    permission_classes = [permissions.IsAuthenticated]


