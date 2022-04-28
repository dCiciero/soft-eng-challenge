from rest_framework import serializers

from .models import Mothership

class MothershipSerializer(serializers.ModelSerializer):
    ships = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Mothership
        fields = ['name', 'ships']
    