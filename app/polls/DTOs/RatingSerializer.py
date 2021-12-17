from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django.http.response import JsonResponse

from ..modelsDB.Rating import *

class RatingSerializer(serializers.HyperlinkedModelSerializer):
    memberID = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    #memberID = Member.objects.all().get(memberID = 1)
    class Meta:
        model = Rating
        fields = ('ratingID', 'memberID', 'productID', 'value')

    # def create(self, validated_data):
    #     #validated_data['memberID'] = validated_data.pop('current_user')
    #     return super().create(validated_data)