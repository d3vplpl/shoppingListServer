from django.contrib.auth.models import User, Group
from .models import ListElement, ShopList
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ListElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListElement
        fields = ('__all__')
        #serialized_obj = serializers.serialize('json', [ListElement, ])


class ShopListSerializer(serializers.ModelSerializer):
    list_elements = ListElementSerializer(many=True)
    class Meta:
        model = ShopList
        fields = ('shopList_name', 'list_elements')





