from django.http import request
from ..models import ProductType, Product, Rating, Comment, Transaction, Cart # !!!! переделать на импорты из файцлов
from rest_framework import permissions, viewsets
from django.contrib.auth.models import User
from ..serializers import *
from rest_framework import permissions
from ..permissions import IsOwnerOrReadOnly, IsCurrentUserOrReadOnly
from ..schema import ProductSchema
#from rest_framework.schemas.openapi import AutoSchema
from ..myapi import AutismSchema as AutoSchema

from django.shortcuts import get_object_or_404



class ProductAPIView(viewsets.ModelViewSet):
    '''
    Товары, хранящиеся в каталоге.
    Поля: ID, тип, название, описание, количество в наличии, цена, изображение (опционально).
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    schema = AutoSchema(
        tags=['Товары'],
    )

    def get_queryset(self):
        '''
        Функция для получения списка товаров. (а также несколько заложенных на будущее фильтров)
        '''
        list_products = self.queryset
        query = self.request.query_params.get('favourite')
        user = self.request.user
        if (query is not None and user is not None):
            list_products = list_products.in_bookmarks(self.request.user)
        return list_products

    def get_permissions(self):
        '''
        Функция проверки разрешений на применяемые к каталогу товаров запросы.
        '''
        # if self.request.method not in permissions.SAFE_METHODS:
        #     return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]

    def get_serializer_class(self):
        return self.serializer_class