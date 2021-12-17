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

from drf_yasg import openapi


class TransactionsAPIView(viewsets.ModelViewSet):
    '''
    Заказы, созданные участниками.
    Поля: IDзаказа, IDучастника, IDтоваров, количества_товаров, статус, дата.
    '''
    schema = AutoSchema(
        tags=['Заказы'],
    )
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    permission_classes = [
        permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_permissions(self):
        '''
        Функция проверки разрешений на применяемые к заказам запросы.
        '''
        if self.action in ('retrieve', 'create', 'partial_update'):
            return [permissions.IsAuthenticated(), IsOwnerOrReadOnly()]
        else:
            return [permissions.IsAuthenticated(), permissions.IsAdminUser()]

    def get_serializer_class(self):
        '''
        Функция определения сериалайзера.
        '''
        return self.serializer_class