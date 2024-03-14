from django.shortcuts import render
from api.models import Entity
from rest_framework import viewsets
from api.serializer import Serializer

class Screen(viewsets.ModelViewSet):
    queryset = Entity.objects.all()  # Definindo o queryset
    serializer_class = Serializer

    def list(self, request, *args, **kwargs):
        last_entity = Entity.objects.last()  # Obtém o último objeto Entity
        return render(request, 'home.html', {'count': [last_entity]})
