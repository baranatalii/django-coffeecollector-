from rest_framework import generics
from .models import Coffee, Feeding
from .serializers import CoffeeSerializer, FeedingSerializer

class CoffeeListCreate(generics.ListCreateAPIView):
    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer

class CoffeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer

class FeedingListCreate(generics.ListCreateAPIView):
    serializer_class = FeedingSerializer

    def get_queryset(self):
        coffee_id = self.kwargs['coffee_id']
        return Feeding.objects.filter(coffee_id=coffee_id)

    def perform_create(self, serializer):
        coffee_id = self.kwargs['coffee_id']
        coffee = Coffee.objects.get(id=coffee_id)
        serializer.save(coffee=coffee)

class FeedingDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FeedingSerializer
    lookup_field = 'id'

    def get_queryset(self):
        coffee_id = self.kwargs['coffee_id']
        return Feeding.objects.filter(coffee_id=coffee_id)