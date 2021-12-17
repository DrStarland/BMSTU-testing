from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django.http.response import JsonResponse

from ..modelsDB.Product import *

class ProductSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(required=False)
    class Meta:
        model = Product
        fields = ('productID', 'productName', 'productType', 'description', 'stock', 'price', 'img')

    # def create(self, validated_data):
    #     product = super().create(validated_data)
    #     return product

    # def update(self, instance, validated_data):
    #     product = super().update(instance, validated_data)
    #     product.save()
    #     return product