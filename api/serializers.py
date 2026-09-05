from rest_framework import serializers
from .models import Epreuve

class EpreuveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Epreuve
        fields = '__all__'