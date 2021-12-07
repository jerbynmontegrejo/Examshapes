from rest_framework import serializers
from .models import Shapes


class ShapesSerializers(serializers.ModelSerializer):
    area = serializers.SerializerMethodField('_get_area')
    perimeter = serializers.SerializerMethodField('_get_perimeter')

    def _get_area(self, shapes_object):
        side = getattr(shapes_object, "side")
        shapes_choice = getattr(shapes_object, 'shapes_choice')

        if shapes_choice == 'triangle':
            area = (1.73 * side * side) / 4
            return area
        else:
            area = side * side
            return area

    def _get_perimeter(self, shapes_object):
        side = getattr(shapes_object, "side")
        shapes_choice = getattr(shapes_object, 'shapes_choice')

        if shapes_choice == 'triangle':
            perimeter = side * 3
            return perimeter
        else:
            perimeter = side * 4
            return perimeter

    class Meta:
        model = Shapes
        fields = '__all__'
