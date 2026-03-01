from django.urls import path
from .views import CoffeeListCreate, CoffeeDetail, FeedingListCreate, FeedingDetail

urlpatterns = [
    path('coffees/', CoffeeListCreate.as_view(), name='coffee-list-create'),
    path('coffees/<int:pk>/', CoffeeDetail.as_view(), name='coffee-detail'),
    path('coffees/<int:coffee_id>/feedings/', FeedingListCreate.as_view(), name='feeding-list-create'),
    path('coffees/<int:coffee_id>/feedings/<int:id>/', FeedingDetail.as_view(), name='feeding-detail'),
]