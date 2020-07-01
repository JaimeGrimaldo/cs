from rest_framework import routers, serializers, viewsets

from Example2.models import Example2

class Example2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Example2
        fileds = ('__all__')