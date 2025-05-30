from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from drfapp.serializers import StudentSerializer
from drfapp.models import Students 

class TesView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Students.objects.all()
        serializer = StudentSerializer(qs, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

##From scratch 
