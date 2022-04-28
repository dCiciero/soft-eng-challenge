from rest_framework import serializers
from crew.models import Crew

class CrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crew
        fields = ['id', 'name', 'ship_assigned']