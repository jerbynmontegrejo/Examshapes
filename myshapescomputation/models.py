from examshapes.models import BaseModel
from shapes.models import Shapes
from django.db import models


# from rest_framework.serializers import ValidationError
# Create your models here.
class MyShapes(BaseModel):
    length = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    side = models.IntegerField(blank=True, null=True)
    # shape = models.ForeignKey(Shapes, on_delete=models.CASCADE)



    def __str__(self):
        return f'MyShapes {self.id}'

    # objects = Shapes()
