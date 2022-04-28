from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from crew.models import Crew
from crew.serializers import CrewSerializer
from .services import get_queryset
from ship import services as ss


crew_members = get_queryset()
@api_view(["GET", "POST"])
def list_crew(request):
    if request.method == "GET":
        if crew_members:
            serialized_crew = CrewSerializer(crew_members, many=True)
            return Response(serialized_crew.data)
        return Response({"Error":"No crew member deployed at the moment."}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "POST":
        ship = request.data['ship_assigned']
        ship_capacity = ss.check_capacity()
        if ss.get_queryset(ship).crew_member.count() >= ship_capacity:
            return Response({"Error":f"Cannot add member to ship as it has reached its capacity"}, status=status.HTTP_400_BAD_REQUEST)     
        
        serialized_record = CrewSerializer(data=request.data)
        if serialized_record.is_valid():
            serialized_record.save()
            return Response(serialized_record.data, status=status.HTTP_201_CREATED)
        return Response(serialized_record.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def crew_details(request, id):
    crew_member = get_queryset(id)
    if request.method == "GET":
        if crew_member:
            if isinstance(crew_member, Crew):
                crew_serializer = CrewSerializer(crew_member, many=False)
                return Response(crew_serializer.data)
        return Response({"Error":f"No ship with Id={id}"}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "PUT":
        
        from_ship = request.data['from_ship']
        to_ship = request.data['to_ship']
        ship_capacity = ss.check_capacity()
        if crew_member.ship_assigned.pk != from_ship:
            return Response({"Error":f"{crew_member.name} does not belong to ship {from_ship}"}, status=status.HTTP_400_BAD_REQUEST)
        elif crew_member.ship_assigned.pk == to_ship:
            return Response({"Error":f" Destination and origin cannot be the same"}, status=status.HTTP_400_BAD_REQUEST)
        if ss.get_queryset(to_ship).crew_member.count() >= ship_capacity:
            return Response({"Error":f"Cannot move {crew_member.name} to {to_ship} destination as it has reached its capacity"}, status=status.HTTP_400_BAD_REQUEST)
        
        data = {"name":crew_member.name, "ship_assigned": to_ship }
        serialized_record = CrewSerializer(crew_member, data=data)
        if serialized_record.is_valid():
            try:
                serialized_record.save()
            except Exception as e:
                Response({"Error":f"Error occured while switching {crew_member.name} to another ship"}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"Success":f"Successfully switched {crew_member.name} between ships "}, status=status.HTTP_201_CREATED)
        
        return Response({"Succes":f"Transfer done"}, status=status.HTTP_400_BAD_REQUEST)