from rest_framework import viewsets
from .models import Epreuve
from .serializers import EpreuveSerializer
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view
from rest_framework.response import Response


class EpreuveViewSet(viewsets.ModelViewSet):
    queryset = Epreuve.objects.all().order_by('-date_ajout')
    serializer_class = EpreuveSerializer


@api_view(['POST'])
def verify_admin_password(request):
        password_saisi = request.data.get('password', '')

        # Ton mot de passe haché enregistré en base ou dans settings
        # (Exemple avec un hash stocké)
        hash_attendu = "pbkdf2_sha256$1500000$PGigzNxzXFxHEsUknac2mT$3kIER9XYBbC/aMWgLmBHFVTMvA3e8fEJtecmVMeVzgg="

        if check_password(password_saisi, hash_attendu):
            return Response({"success": True})
        return Response({"success": False}, status=403)