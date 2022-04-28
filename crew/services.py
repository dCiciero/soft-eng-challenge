from  .models import Crew
from rest_framework import status
from rest_framework.response import Response

from django.db.models import Count

def get_queryset(id=None):
    if not id:
        return Crew.objects.all()
    try:
        return Crew.objects.get(id=id)
    except Exception as e:
        return Response({'error_message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    