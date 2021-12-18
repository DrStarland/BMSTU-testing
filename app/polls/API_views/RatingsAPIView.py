from rest_framework import permissions, viewsets
from django.contrib.auth.models import User
from ..serializers import *
from rest_framework import permissions
from ..permissions import IsOwnerOrReadOnly, IsCurrentUserOrReadOnly
from ..schema import ProductSchema
#from rest_framework.schemas.openapi import AutoSchema
from ..myapi import AutismSchema as AutoSchema

from django.shortcuts import get_object_or_404

from ..modelsDB.Rating import *


class RatingsAPIView(viewsets.ModelViewSet):
    '''
    Оценки, оставленные участниками на сайте к определенным товарам.
    Поля: IDоценки, IDавтора, IDтовара, значение.
    '''
    schema = AutoSchema(
        tags=['Оценки'],
    )
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    permission_classes = [
        permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_permissions(self):
        '''
        Функция проверки разрешений на применяемые к оценкам запросы.
        '''
        if self.action in ('list', 'retrieve', 'create', 'partial_update', 'destroy'):
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAuthenticated(), permissions.IsAdminUser()]

    def get_serializer_class(self):
        '''
        Функция определения сериалайзера.
        '''
        if self.action == 'update':
            return RatingUpdateSerializer
        return RatingSerializer