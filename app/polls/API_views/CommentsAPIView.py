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

class CommentsAPIView(viewsets.ModelViewSet):
    '''
    Комментарии, оставленные участниками на сайте к определенным товарам.
    Поля: IDкомментария, IDавтора, IDтовара, текст, дата.
    '''
    schema = AutoSchema(
        tags=['Комментарии'],
    )
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        '''
        Функция проверки разрешений на применяемые к комментариям запросы.
        '''
        if self.action in ('list', 'retrieve'):
            return [permissions.AllowAny()]
        elif self.action == 'create':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAuthenticated(), permissions.IsAdminUser()]

    def get_serializer_class(self):
        '''
        Функция определения сериалайзера.
        '''
        return self.serializer_class