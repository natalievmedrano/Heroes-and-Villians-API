from rest_framework import serializers
from .models import SuperType

class Super_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperType
        fields=['Heroes','Villians']