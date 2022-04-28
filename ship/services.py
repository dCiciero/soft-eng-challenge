from  .models import Ship
from rest_framework import status
from rest_framework.response import Response

from django.conf import settings

def get_queryset(id=None):
    if not id:
        return Ship.objects.all()
    try:
        return Ship.objects.get(id=id)
    except Exception as e:
        return Response({'error_message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

def check_capacity():
    capacity = int(settings.SHIP_LIMIT) # getattr(settings, 'SHIP_LIMIT', None) # 
    if capacity:
        return capacity
    return Response({"Error":"No record found"}, status=status.HTTP_404_NOT_FOUND)
    
    