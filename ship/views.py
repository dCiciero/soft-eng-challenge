from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Ship
from ship.serializers import ShipSerializer
from .services import check_capacity, get_queryset
from crew.models import Crew
import uuid
from django.conf import settings


ship_capacity = check_capacity()
ships = get_queryset()
@api_view(["GET", "POST"])
def list_ship(request):
    if request.method == "GET":
        if ships:
            serialized_crew = ShipSerializer(ships, many=True)
            return Response(serialized_crew.data)
        return Response({"Errror":"There are no ships to display."}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "POST":
        print(request.data)
        serialized_record = ShipSerializer(data=request.data)
        if serialized_record.is_valid():
            serialized_record.save()
            return Response(serialized_record.data, status=status.HTTP_201_CREATED)
        return Response(serialized_record.errors, status=status.HTTP_400_BAD_REQUEST)
 
@api_view(["GET", "PUT", "DELETE"])
def ship_details(request, id, *args, **kwargs):
    ship = get_queryset(id)
    if request.method == "GET":
        if ship:
            if isinstance(ship, Ship):
                mship_serializer = ShipSerializer(ship, many=False)
                return Response(mship_serializer.data)
        return Response({"Error":f"No ship with Id={id}"}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "PUT":
        current_crew_load = ship.crew_member.count()
        crew_to_add = request.data['crew_name']
        if current_crew_load == ship_capacity:
            return Response({"Error":"Ship limit reached, cannot add more crew member"})
        
        elif current_crew_load < ship_capacity:
            try:
                Crew.objects.create(name=f"{crew_to_add}", ship_assigned=ship)
                return Response({"Success":f"Successfully added {crew_to_add} ships to {ship.name}"}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"Error":f"Cannot create crew member. {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"Error":"Bad request"}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        ship.delete()
        
        return Response({"Info":"Ship deleted with its crew members"}, status=status.HTTP_204_NO_CONTENT) 