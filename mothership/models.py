from django.db import models

class Mothership(models.Model):
    name = models.CharField(max_length=120)
    
    def __str__(self) -> str:
        return self.name

    
    def save(self, *args, **kwargs):
        return super().save()
        
    
