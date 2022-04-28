from django.db import models


class SystemControl(models.Model):
    name = models.CharField(max_length=100)
    mship_max = models.PositiveSmallIntegerField()
    new_ship_to_add = models.PositiveSmallIntegerField(default=3)
    
    def __str__(self) -> str:
        return f"{self.name}"

class Mothership(models.Model):
    name = models.CharField(max_length=120)
    
    def __str__(self) -> str:
        return self.name
    
    def get_ships(self):
        return self.objects.all()
    
    def save(self, *args, **kwargs):
        return super().save()
        
    
