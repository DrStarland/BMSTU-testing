from ..models import ProductType, Product,  Rating, Comment, Transaction, Cart # !!!! переделать на импорты из файцлов
from rest_framework import permissions, viewsets
from django.contrib.auth.models import User
from ..serializers import *
from rest_framework import permissions
from ..permissions import IsOwnerOrReadOnly, IsCurrentUserOrReadOnly
from ..schema import ProductSchema
#from rest_framework.schemas.openapi import AutoSchema
from ..myapi import AutismSchema as AutoSchema

from django.shortcuts import get_object_or_404

from drf_yasg import openapi

class ProductTypeAPIView(viewsets.ModelViewSet):
    '''
    Типы товаров.
    Поля: ID, название, описание.
    '''
    schema = AutoSchema(
        tags=['Тип товара'],
    )
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

    def get_permissions(self):
        '''
        Функция проверки разрешений на применяемые к типу товаров запросы.
        '''
        if self.request.method not in permissions.SAFE_METHODS:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]