from rest_framework import serializers
from api.models import Entity

class Serializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = '__all__'