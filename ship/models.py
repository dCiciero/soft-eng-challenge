from django.db import models
from mothership.models import Mothership


class Ship(models.Model):
    name = models.CharField(max_length=120)
    mship = models.ForeignKey(Mothership, on_delete=models.CASCADE, related_name='ships')


    class Meta:
        db_table='ship'
        
        
    def __str__(self) -> str:
        return f"{self.pk}: {self.name}"
    
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)