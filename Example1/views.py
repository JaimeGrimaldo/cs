from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics

from django.http import Http404
from django.shortcuts import get_object_or_404

#exportacion de serializer y modelos 
from Example1.models import Example1
from Example1.serializer import ExampleSerializers



class ExampleLista(APIView):
    def get(self,request,format=None):
        queryset = Example1.objects.all()
        serializer = ExampleSerializers(queryset,many = True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = ExampleSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)

class ExampleDetail(APIView):
    def get_object(self, id):
        try:
            return Example1.objects.get(pk = id)
        except Example1.DoesNotExist:
            return 404
    
    def get(self,request, id ,format=None):
        exmaple1 =  self.get_object(id)
        if exmaple1 == 404:
            return Response("NO HAY DATOS")
        else:
            serializer = ExampleSerializers(exmaple1)
            return Response(serializer.data)
        
    def put(self,request, id , format = None):
        editar = self.get_object(id)
        if editar == 404:
            return Response("DATOS NO ENCONTRADOS")
        else:
            serializer = ExampleSerializers(editar, data = request.data)
            if serializer.is_valid():
                serializer.save()
                data = serializer.data
                return Response(data)
            else:
                return Response(serializer.error)