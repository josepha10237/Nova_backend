from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

# Force Django à servir les fichiers médias même en production (essentiel pour tes PDF)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)