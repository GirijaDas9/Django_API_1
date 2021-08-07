from django.shortcuts import render

from .models import List,ListItem
from .serializers import ListSerializer,ListItemSerializer
from rest_framework import viewsets



class ListViewset(viewsets.ModelViewSet):

    queryset=List.objects.all()
    serializer_class = ListSerializer

class ListItemViewSet(viewsets.ModelViewSet):
    queryset = ListItem.objects.all()
    serializer_class = ListItemSerializer