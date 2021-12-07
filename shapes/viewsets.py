from rest_framework import viewsets
from . import models
from . import serializers


class ShapesViewset(viewsets.ModelViewSet):
    queryset = models.Shapes.objects.all()
    serializer_class = serializers.ShapesSerializers

