from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . serializers import SupersSerializer
from . models import Supers
from super_types.models import SuperType


# Create your views here.

@api_view(['GET','POST'])
def supers_table(request):
    
    if request.method == 'GET':
        super_type_param = request.query_params.get('type')
        sort_param = request.query_params.get('sort')
        supers = Supers.objects.all()
        if super_type_param:
            supers = supers.filter(super_type__type=super_type_param)
        if sort_param:
            supers = supers.order_by(sort_param)
        serializer = SupersSerializer(supers, many=True)
        return Response(serializer.data)

    elif request.method == 'GET':
        supers_types = Supers.objects.all()
        Custom_response = {}
        for super_type in supers_types:
            supers = Supers.objects.filter(super_type__type=super_type.type)
            serializer = SupersSerializer(supers, many=True)
            Custom_response[super_type.type] = {"Heroes": [], "Villains": []}

        return Response(Custom_response)


    elif request.method == 'POST':
        serializer = SupersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED) 


@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):
    super = get_object_or_404(Supers, pk=pk)
    if request.method == 'GET':
        serializer = SupersSerializer(super)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = SupersSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

