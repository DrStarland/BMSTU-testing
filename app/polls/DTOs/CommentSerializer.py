from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django.http.response import JsonResponse

from ..modelsDB.Comment import *

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    memberID = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = ('productID', 'memberID', 'message', 'commentDate')

    def create(self, validated_data):
        #validated_data['memberID'] = validated_data.pop('current_user')
        return super().create(validated_data)