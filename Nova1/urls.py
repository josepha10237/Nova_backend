from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

# Petite fonction pour afficher un message à la racine de l'API
def api_home(request):
    return HttpResponse("✅ Le backend Django de Nova fonctionne parfaitement ! Les services API sont disponibles sous /api/.")

urlpatterns = [
    path('', api_home), # 👈 Gère la page d'accueil de Railway
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

# Routage des fichiers médias
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)