from django.db import models

class Mothership(models.Model):
    name = models.CharField(max_length=120)
    
    def __str__(self) -> str:
        return self.name
    
    def get_ships(self):
        return self.objects.all()
    
    def save(self, *args, **kwargs):
        return super().save()
        
    
