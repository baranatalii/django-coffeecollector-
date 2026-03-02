# Django Coffee Collector API

## A simple RESTful API built with Django and Django Rest Framework to manage a coffee collection.

- Quick Start Checklist
- [ ] Install dependencies (pipenv install)

- [ ] Create Database (createdb catcollector)

- [ ] Run Migrations (python manage.py migrate)

- [ ] Start Server (python manage.py runserver)

- [ ] Test API (http://localhost:8000/)

## 🗺️ Project Learning Plan

We are building a modern full-stack API named CoffeeCollector.

High-Level Topics:

- Django Setup, URLs, and Views

- Data Models, Serializers, and Migrations

- Class-based Views (CRUD)

- One-to-Many & Many-to-Many Relationships

## URL Patterns =

[

- Admin
  path('admin/', admin.site.urls),
- Root Redirect
  path('', include('main_app.urls')),
- Built-in DRF Auth (for browser UI)
  path('api-auth/', include('rest_framework.urls')),
  ]

## main_app.urls

urlpatterns = [ # Authentication
path('register/', register_user, name='register-user'),
path('api-token-auth/', obtain_auth_token, name='api-token-auth'), # For Postman

    # Coffee Routes
    path('coffees/', CoffeeListCreate.as_view(), name='coffee-list-create'),
    path('coffees/<int:pk>/', CoffeeDetail.as_view(), name='coffee-detail'),

    # Feeding Routes
    path('coffees/<int:coffee_id>/feedings/', FeedingListCreate.as_view(), name='feeding-list-create'),
    path('coffees/<int:coffee_id>/feedings/<int:id>/', FeedingDetail.as_view(), name='feeding-detail'),

    # Flavor Routes
    path('flavors/', FlavorListCreate.as_view(), name='flavor-list-create'),
    path('flavors/<int:id>/', FlavorDetail.as_view(), name='flavor-detail'),

    # Many-to-Many Routes
    path('coffees/<int:coffee_id>/flavors/', CoffeeFlavorAssociate.as_view(), name='coffee-flavor-associate'),
    path('coffees/<int:coffee_id>/flavors/<int:flavor_id>/', CoffeeFlavorRemove.as_view(), name='coffee-flavor-remove'),

]

- Authentication

🔄 Request/Response Cycle

- The API is protected using Token Authentication.

- Registration: Use /register/ to create a user account.

- Log In: Use /api-token-auth/ to exchange credentials for a token.

- Protected Routes: Include the token in the Authorization header for all requests:
- Authorization: Token <your-token-key>

## User Authentication

Method Endpoint Description Protected
POST /register/ Register a new user No
POST /api-token-auth/ Log in and get a token No

## User Authentication

POST. /register/ (Register A New User)
POST /api-token-auth/ (Login & Get A New Token)

## Coffee Routes

GET /coffees/ ( List Of Coffees)
POST /coffees/ (Create A New Coffee)
GET /coffees/<id>/ (View Coffee Details)
PUT /coffees/<id>/ ( Update A Coffee)
DELETE /coffees/<id>/ ( Delete A New Coffee)

## Flavor Routes

GET /flavors/ ( List All Flavors)
POST /flavors ( Create A New Flavor)

## Many-to-Many Routes ( Coffee-Flavor )

POST /coffees/<id>/flavors/ ( Assosicate Flavor )
DELETE /coffees/<c_id>/flavors/<f_id>/ (Remove Flavor)

CREATED BY BARANATALII
