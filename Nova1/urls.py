from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')), # ou le nom de ton app d'API
]

# 👇 C'est cette ligne qui permet à Django de renvoyer les PDF stockés dans media/
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    # Même si DEBUG = False sur Railway, forcer le routage des médias pour un petit projet évite une configuration S3 lourde
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)