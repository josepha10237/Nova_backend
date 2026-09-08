from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Remplace 'api' par le nom exact de ton app si c'est 'nova'
]