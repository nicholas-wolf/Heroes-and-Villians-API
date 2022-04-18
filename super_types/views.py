from django.shortcuts import get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperTypeSerializer
from . models import SuperType

# Create your views here.

@api_view(['GET'])
def super_type_table(request):
    review = get_list_or_404(SuperType)
    
    if request.method == 'GET':
        review = SuperType.objects.filter()
        serializer = SuperTypeSerializer(review, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

