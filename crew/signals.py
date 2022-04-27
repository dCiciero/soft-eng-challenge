# from requests import Response
# from .models import Crew_Member
# from ship.models import Ship, SystemControl
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# import uuid
# from datetime import date

# @receiver(post_save, sender=Ship)
# def create_crew_on_ship_creation(sender, instance, created, **kwargs):
#     if created:
#         for i in range(3):
#             Crew_Member.objects.create(name=f'Crew-{str(uuid.uuid4())[:8]}', ship_assigned=instance)