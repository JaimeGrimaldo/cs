from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from django.http import Http404
from django.shortcuts import get_object_or_404

# Create your views here.
#importamos modelos
from Example1.models import Example

#importaciones de serializer
from Example1.serializer import ExampleSerializer

class ExampleList(APIView):
    def get(self, request, format=None):
        print("ESTRAMOS A GET")
        queryset = Example.objects.all()
        serializer = ExampleSerializer(queryset, many = True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print("ENTRO A POST OSI OSI")
        serializer = ExampleSerializer(data = request.data)
        print("PASO EL SERIALIZER")
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)