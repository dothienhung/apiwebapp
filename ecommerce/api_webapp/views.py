from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import  Response
# Create your views here.

class TestingAPI(APIView):
    
    def get(self ,request, format =None):
        
        an_apiview =[
            
        ]
        
        return Response({'apiview': "Hello!",'an_apiview' :an_apiview})


