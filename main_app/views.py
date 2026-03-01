from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics 
from .models import Coffee 
from .serializers import CoffeeSerializer 


class Home(APIView):
    def get(self, request):
        content = {'message': 'Welcome to the Coffee Collector API!'}
        return Response(content)

