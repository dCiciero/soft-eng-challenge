from django.forms import ValidationError
from .models import Ship
from mothership import services
from mothership.models import Mothership
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from rest_framework.response import Response
from rest_framework import status
import uuid

@receiver(post_save, sender=Mothership)
def create_ship_on_mothership_creation(sender, created, instance,*args, **kwargs):
    
    if created:
        max_ship_to_add = services.get_queryset()
        max_ship_to_add = max_ship_to_add[0].new_ship_to_add
        try:
            for i in max_ship_to_add:
                Ship.objects.create(name=f"Ship-{str(uuid.uuid4()).replace('-','')[:8]}", mship=instance)
        except:
            return Response({"Error" : "Cannot add ships to mothership"}, status=status.HTTP_400_BAD_REQUEST)
            # raise ValidationError("Error saving ship")
            