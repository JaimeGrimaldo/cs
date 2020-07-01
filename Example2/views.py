from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from django.http import Http404
from django.shortcuts import get_object_or_404

# Create your views here.
#importamos modelos
from Example2.models import Example2

#importaciones de serializer
from Example2.serializer import Example2Serializer

class Example2List(APIView):
    def get(self, request, format=None):
        print("entramos a get de example2")
        queryset = Example2.objects.all()
        serializer = Example2Serializer(queryset, many = True)
        return Response(serializer.data)
        
    def post(self, request, format=None):
        print("ENTRO A POST OSI OSI")
        serializer = Example2Serializer(data = request.data)
        print("PASO EL SERIALIZER")
        if serializer.is_valid:
            serializer.save()
            datas = serializer.data
            return Response(datas)