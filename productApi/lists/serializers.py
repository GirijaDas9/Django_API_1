
from rest_framework import serializers
from . models import List, ListItem
from django.contrib.auth import get_user_model


class ListSerializer(serializers.HyperlinkedModelSerializer):

    user = serializers.PrimaryKeyRelatedField(
            queryset=get_user_model().objects.all())

    class Meta:
        model = List
        fields = ['id', 'name', 'description','user','created_at','updated_at']

class ListItemSerializer(serializers.HyperlinkedModelSerializer):
    parent_list = serializers.PrimaryKeyRelatedField(
            queryset=List.objects.all())

    class Meta:
        model = ListItem
        fields = ['id', 'text', 'parent_list','created_at', 'updated_at']