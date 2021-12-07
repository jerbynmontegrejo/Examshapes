from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import ShapesSerializers
from .models import models as models


# Create your views here.

class ShapesAPI(generics.GenericAPIView):
    serializer_class = ShapesSerializers


    # queryset = models.Shapes.objects.all().select_related('account')

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        shapes = serializer.save()
        return Response({
            "shapes": ShapesSerializers(shapes, context=self.get_serializer_context()).data,
        })


