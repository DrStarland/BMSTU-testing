from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django.http.response import JsonResponse

from ..modelsDB.Transaction import *

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ('transactionID', 'productIDs', 'productQuantities', 'approvalStatus', 'transactionDate',)
    
    def create(self, validated_data):
        #validated_data['memberID'] = validated_data.pop('current_user')
        return super().create(validated_data)