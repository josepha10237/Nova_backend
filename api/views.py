from rest_framework import viewsets
from .models import Epreuve
from .serializers import EpreuveSerializer

class EpreuveViewSet(viewsets.ModelViewSet):
    queryset = Epreuve.objects.all().order_by('-date_ajout')
    serializer_class = EpreuveSerializer