from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny # <--- Added missing import

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes

# --- FIXED TYPO: Changed Flavorj to Flavor ---
from .models import Coffee, Feeding, Flavor 
from .serializers import CoffeeSerializer, FeedingSerializer, FlavorSerializer

class CoffeeListCreate(generics.ListCreateAPIView):
    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer

class CoffeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        # --- Using the corrected Flavor model here ---
        flavors_not_associated = Flavor.objects.exclude(id__in=instance.flavors.all())
        flavors_serializer = FlavorSerializer(flavors_not_associated, many=True)
        return Response({
            'coffee': serializer.data,
            'flavors_not_associated': flavors_serializer.data
        })

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

class FlavorListCreate(generics.ListCreateAPIView):
    queryset = Flavor.objects.all()
    serializer_class = FlavorSerializer

class FlavorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flavor.objects.all()
    serializer_class = FlavorSerializer
    lookup_field = 'id'

class CoffeeFlavorAssociate(APIView):
    def get(self, request, coffee_id):
        coffee = Coffee.objects.get(id=coffee_id)
        serializer = FlavorSerializer(coffee.flavors.all(), many=True)
        return Response(serializer.data)

    def post(self, request, coffee_id):
        coffee = Coffee.objects.get(id=coffee_id)
        flavor_id = request.data.get('flavor_id')
        coffee.flavors.add(flavor_id)
        return Response({'message': f'Flavor {flavor_id} added to Coffee {coffee_id}'}, status=status.HTTP_201_CREATED)

class CoffeeFlavorRemove(APIView):
    def delete(self, request, coffee_id, flavor_id):
        coffee = Coffee.objects.get(id=coffee_id)
        coffee.flavors.remove(flavor_id)
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    
    if not username or not password:
        return Response({'error': 'Please provide username and password'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, email=email, password=password)
    token = Token.objects.create(user=user)
    
    return Response({'token': token.key, 'username': user.username}, status=status.HTTP_201_CREATED)