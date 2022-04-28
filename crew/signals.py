from webbrowser import get
from requests import Response
from .models import Crew
from ship.models import Ship
from ship.services import check_capacity, get_queryset
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid, os
from datetime import date

@receiver(post_save, sender=Ship)
def create_crew_on_ship_creation(sender, instance, created, **kwargs):
    max_crew = os.getenv('SHIP_CREW') # get_queryset()
    # max_crew = max_crew[0].crew_to_add
    if created:
        for i in max_crew:
            Crew.objects.create(name=f'Crew-{str(uuid.uuid4())[:8]}', ship_assigned=instance)