from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Super_typeSerializer
from .models import SuperType

@api_view(['GET'])
def super_type_list(request):
    super_types= SuperType.objects.all()
    serializer = Super_typeSerializer(super_types, many=True)
    return Response(serializer.data)