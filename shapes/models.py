from examshapes.models import BaseModel
from account.models import Account
from django.db import models


# from rest_framework.serializers import ValidationError
# Create your models here.
class Shapes(BaseModel):
    name = models.CharField(max_length=256)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    shape_choices = (
        ('square', 'Square'),
        ('triangle', 'Triangle')
    )
    shapes_choice = models.CharField(max_length=30, blank=True, null=True, choices=shape_choices)
    side = models.IntegerField(blank=True, null=True)

    print(shapes_choice)

    def __str__(self):
        return f'Shape {self.id} - {self.username}'

    # objects = Shapes()
