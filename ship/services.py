from  .models import SystemControl, Ship
from rest_framework import status
from rest_framework.response import Response

from django.db.models import Count

def get_queryset(id=None):
    if not id:
        return Ship.objects.all()
    try:
        return Ship.objects.get(id=id)
    except Exception as e:
        return Response({'error_message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

def check_capacity():
    capacity = SystemControl.objects.values('ship_max').first()
    if capacity:
        return capacity['ship_max']
    return Response({"Error":"No record found"}, status=status.HTTP_404_NOT_FOUND)
    
    