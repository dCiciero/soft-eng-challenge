from .models import Mothership
from ship.models import Ship
from . import services
from .serializers import MothershipSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
import uuid

mships = services.get_queryset()
mothership_capacity = services.check_capacity()
mothership_capacity = int(mothership_capacity)

@api_view(["GET", "POST"])
def mothership(request):
    if request.method == "GET":
        mship_serializer = MothershipSerializer(mships, many=True)
        if mship_serializer.data:
            return Response(mship_serializer.data)
        return Response({"Info":"No mothership has been deployed to battle"}, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        serialized_record = MothershipSerializer(data=request.data)
        if serialized_record.is_valid():
            print(len(mships))
            if len(mships) == services.check_capacity:
                return Response({"Error": "Mothership limit reached"}, status=status.HTTP_400_BAD_REQUEST)
            serialized_record.save()
            return Response(serialized_record.data, status=status.HTTP_201_CREATED)
        return Response(serialized_record.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def mothership_details(request, id, *args, **kwargs):
    mship = services.get_queryset(id)
    if request.method == "GET":
        if isinstance(mship, Mothership):
            mship_serializer = MothershipSerializer(mship, many=False)
            return Response(mship_serializer.data)
    
    elif request.method == "PUT":
        current_mship_load = mship.ships.count()
        ships_to_add = request.data['ships_to_add']
        if current_mship_load == mothership_capacity:
            return Response({"Error":"Mothership limit reached, cannot add more ships"})
        
        elif current_mship_load < mothership_capacity:
            if (ships_to_add + current_mship_load) > mothership_capacity:
                return Response({"Info":"The number of ships to add will exceed the capacity of the mothership."})
            
            else:
                for ship in range(ships_to_add):
                    Ship.objects.create(name=f"Ship-{str(uuid.uuid4()).replace('-','')[:8]}", mship=mship)
                return Response({"Success":f"Successfully added {ships_to_add} ships to {mship.name}"}, status=status.HTTP_201_CREATED)
        return Response({"Error":"Bad request"}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        return Response({"Error":"Delete operation is not implemented"}, status=status.HTTP_400_BAD_REQUEST)