from rest_framework import viewsets
from . import models
from . import serializer


class MyShapesViewset(viewsets.ModelViewSet):
    queryset = models.MyShapes.objects.all()
    serializer_class = serializer.MyShapesSerializer

