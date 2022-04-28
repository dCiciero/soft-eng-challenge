from django.db import models
from mothership.models import Mothership


# class SystemControl(models.Model):
#     name = models.CharField(max_length=100)
#     ship_max = models.PositiveSmallIntegerField()
#     crew_to_add = models.PositiveSmallIntegerField(default=3)
    
#     def __str__(self) -> str:
#         return f"{self.name}"


class Ship(models.Model):
    name = models.CharField(max_length=120)
    mship = models.ForeignKey(Mothership, on_delete=models.CASCADE, related_name='ships')

    def __str__(self) -> str:
        return f"{self.pk}: {self.name}"
    
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)