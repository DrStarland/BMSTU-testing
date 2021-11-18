from .models import ProductType, Product, Member, Rating, Comment, Transaction, Cart
from rest_framework import permissions, viewsets
from django.contrib.auth.models import User
from .serializers import *
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly, IsCurrentUserOrReadOnly
from .schema import ProductSchema
#from rest_framework.schemas.openapi import AutoSchema
from .myapi import AutismSchema as AutoSchema

from django.shortcuts import get_object_or_404

from drf_yasg import openapi


# бесполезные декораторы, которые не помогают
# from rest_framework.decorators import api_view
# from drf_yasg.utils import swagger_auto_schema
# from django.utils.decorators import method_decorator
from rest_framework.decorators import action


'''
Django ViewSet actions:
list -- GET - список
retrieve -- GET - одну запись
create -- POST
update -- PUT
partial_update -- PATCH - обновление частичное (1 поле, например)
destroy -- DELETE
'''


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
        if self.request.method not in permissions.SAFE_METHODS:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]

    def get_serializer_class(self):
        return self.serializer_class


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
        if self.action in ('list', 'retrieve', 'create', 'partial_update'):
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
        if self.action in ('retrieve', 'create', 'partial_update'):
            return [permissions.IsAuthenticated(), IsOwnerOrReadOnly()]
        else:
            return [permissions.IsAuthenticated(), permissions.IsAdminUser()]

    def get_serializer_class(self):
        '''
        Функция определения сериалайзера.
        '''
        return self.serializer_class
