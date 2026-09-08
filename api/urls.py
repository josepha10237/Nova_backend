from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EpreuveViewSet,verify_admin_password

router = DefaultRouter()
router.register(r'epreuves', EpreuveViewSet, basename='epreuve')

urlpatterns = [
    path('', include(router.urls)),
    path('verify-admin/', verify_admin_password, name='verify-admin'),
]