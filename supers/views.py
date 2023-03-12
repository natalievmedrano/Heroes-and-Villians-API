from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

from rest_framework.response import Response
from .serializers import SuperSerializer
from .models import Super
from rest_framework import status

@api_view(['GET','POST'])
def supers_list(request):
    if request.method == 'GET':
        super_type = request.query_params.get('type')
        
        supers = Super.objects.all()

        if super_type: 
           supers= supers.filter(super_type__type= super_type)

        serializer = SuperSerializer(supers, many= True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer= SuperSerializer(data= request.data)
        if serializer.is_valid() == True:
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
   

@api_view(['GET','PUT','DELETE'])
def supers_detail(request,pk):
  
    super= get_object_or_404(Super, pk=pk)
    if request.method == 'GET': 
     serializer = SuperSerializer(super)
     return Response(serializer.data)
    elif request.method == 'PUT':
     serializer = SuperSerializer(super, data=request.data)
     serializer.is_valid(raise_exception=True)
     serializer.save()
     return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
