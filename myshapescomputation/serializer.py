from rest_framework import serializers
from .models import MyShapes

class MyShapesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyShapes
        fields = ('id', 'length', 'width', 'side')
