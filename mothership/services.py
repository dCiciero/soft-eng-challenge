from rest_framework.response import Response
from rest_framework import status
from  .models import Mothership
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.conf import settings

def get_queryset(id=None):
    if not id:
        return Mothership.objects.all()
    try:
        return Mothership.objects.get(id=id)
    except Exception as e:
        return Response({'error_message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

def check_capacity():
    capacity = int(settings.MOTHERSHIP_LIMIT) # getattr(settings, 'MOTHERSHIP_LIMIT', None)#
    if capacity:
        return capacity
    return Response({"Error":"No record found"}, status=status.HTTP_404_NOT_FOUND)