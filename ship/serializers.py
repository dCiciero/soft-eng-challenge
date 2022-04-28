from rest_framework import serializers
from ship.models import Ship

class ShipSerializer(serializers.ModelSerializer):
    crew_member = serializers.StringRelatedField(read_only=True, many=True)
    class Meta:
        model = Ship
        fields = ['id', 'name', 'crew_member']