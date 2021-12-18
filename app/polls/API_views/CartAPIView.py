from rest_framework import permissions, viewsets
from ..serializers import *
from rest_framework import permissions
from ..permissions import IsOwnerOrReadOnly
from ..schema import ProductSchema
#from rest_framework.schemas.openapi import AutoSchema
from ..myapi import AutismSchema as AutoSchema

from django.shortcuts import get_object_or_404

from drf_yasg import openapi

from ..modelsDB.Cart import *

class CartsAPIView(viewsets.ModelViewSet):
    '''
    Корзина, принадлежащая участнику и позволяющая хранить товары из каталога для совершения заказа.
    Поля: IDкорзина, IDучастника, IDтоваров, количества_товаров, количество_видов_товаров.
    '''
    schema = AutoSchema(
        tags=['Корзины'],
    )
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    permission_classes = [
        permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_permissions(self):
        '''
        Функция проверки разрешений на применяемые к корзине запросы.
        '''
        if self.action in ('list', 'retrieve', 'create', 'partial_update', 'destroy'):
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAuthenticated(), permissions.IsAdminUser()]

    def get_serializer_class(self):
        '''
        Функция определения сериалайзера.
        '''
        return self.serializer_class