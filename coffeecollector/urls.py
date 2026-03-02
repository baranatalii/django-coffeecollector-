from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('', lambda request: redirect('coffees/', permanent=False)),
    path('', include('main_app.urls')),
   
    path('api-auth/', include('rest_framework.urls')),
]