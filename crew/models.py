# from django.db import models
# from ship.models import Ship

# class Crew(models.Model):
#     name = models.CharField(max_length=120)
#     ship_assigned = models.ForeignKey(Ship, on_delete=models.CASCADE, related_name='crew')
    
#     def __str__(self) -> str:
#         return f"{self.name} of {self.ship_assigned.name}"