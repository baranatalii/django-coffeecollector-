from django.urls import path
from .views import (
    CoffeeListCreate, 
    CoffeeDetail, 
    FeedingListCreate, 
    FeedingDetail,
    FlavorListCreate,
    FlavorDetail,
    CoffeeFlavorAssociate,
    CoffeeFlavorRemove,
    register_user, # 1. Import the registration view
)

urlpatterns = [
    # Coffee routes
    path('coffees/', CoffeeListCreate.as_view(), name='coffee-list-create'),
    path('coffees/<int:pk>/', CoffeeDetail.as_view(), name='coffee-detail'),
    
    # Feeding routes
    path('coffees/<int:coffee_id>/feedings/', FeedingListCreate.as_view(), name='feeding-list-create'),
    path('coffees/<int:coffee_id>/feedings/<int:id>/', FeedingDetail.as_view(), name='feeding-detail'),
    
    # Flavor routes
    path('flavors/', FlavorListCreate.as_view(), name='flavor-list-create'),
    path('flavors/<int:id>/', FlavorDetail.as_view(), name='flavor-detail'),
    
    # Many-to-Many Routes
    path('coffees/<int:coffee_id>/flavors/', CoffeeFlavorAssociate.as_view(), name='coffee-flavor-associate'),
    path('coffees/<int:coffee_id>/flavors/<int:flavor_id>/', CoffeeFlavorRemove.as_view(), name='coffee-flavor-remove'),
    
    # 2. Add the Auth Route
    path('register/', register_user, name='register-user'),
]