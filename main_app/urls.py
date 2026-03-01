from django.urls import path
from .views import (
    CoffeeListCreate, 
    CoffeeDetail, 
    FeedingListCreate, 
    FeedingDetail,
    FlavorListCreate,
    FlavorDetail,
    # 1. Update imports for Many-to-Many views
    CoffeeFlavorAssociate,
    CoffeeFlavorRemove 
)

urlpatterns = [
    # Coffee routes
    path('coffees/', CoffeeListCreate.as_view(), name='coffee-list-create'),
    path('coffees/<int:pk>/', CoffeeDetail.as_view(), name='coffee-detail'),
    
    # Feeding routes
    path('coffees/<int:coffee_id>/feedings/', FeedingListCreate.as_view(), name='feeding-list-create'),
    path('coffees/<int:coffee_id>/feedings/<int:id>/', FeedingDetail.as_view(), name='feeding-detail'),
    
    # Flavor routes (CRUD for the Flavor resource itself)
    path('flavors/', FlavorListCreate.as_view(), name='flavor-list-create'),
    path('flavors/<int:id>/', FlavorDetail.as_view(), name='flavor-detail'),
    
    # 2. Add Nested Routes for Many-to-Many Relationship
    # List flavors on a coffee / Add a flavor to a coffee
    path('coffees/<int:coffee_id>/flavors/', CoffeeFlavorAssociate.as_view(), name='coffee-flavor-associate'),
    # Remove a flavor from a coffee
    path('coffees/<int:coffee_id>/flavors/<int:flavor_id>/', CoffeeFlavorRemove.as_view(), name='coffee-flavor-remove'),
]