from rest_framework import permissions, viewsets
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from ..serializers import *
from ..permissions import IsCurrentUserOrReadOnly
from ..myapi import AutismSchema as AutoSchema


class UserAPIView(viewsets.ModelViewSet):
    '''
    Участники (пользователи), зарегистрированные на сайте.
    Поля: ID, логин, пароль.
    (опционально - другие персональные данные)
    '''
    schema = AutoSchema(
        tags=['Участники'],
    )

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        '''
        Функция определения сериалайзера.
        '''
        if self.action == 'update':
            return UserUpdateSerializer
        return UserSerializer

    def get_permissions(self):
        '''
        Функция проверки разрешений на применяемые к списку участников запросы.
        '''
        if self.action in ('update', 'partial_update', 'destroy'):
            return [permissions.IsAuthenticated(), IsCurrentUserOrReadOnly()]
        elif self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
    
    #@action(detail=True, methods=['get']) # - добавляется в список методов отдельно, не то
    # используется для одиночного get 
    def get_object(self):
        '''
        Функция, используемая в качестве (одиночного -- retrieve) GET запроса.
        '''
        obj = get_object_or_404(User.objects.filter(id=self.kwargs["pk"]))
        self.check_object_permissions(self.request, obj)
        return obj

    # используется для множественного get 
    def get_queryset(self):
        '''
        Функция, используемая в качестве (множественного -- list) GET запроса.
        '''
        user = self.request.user
        if user.is_superuser:
            return User.objects.all()
        return User.objects.filter(username=user.username)

