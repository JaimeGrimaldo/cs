from rest_framework import routers, serializers, viewsets

from Example1.models import Example

class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fileds = ('__all__')