from .models import ProductType, Product, Member, Rating, Comment, Transaction, Cart
from rest_framework import permissions, viewsets
from django.contrib.auth.models import User
from .serializers import (ProductTypeSerializer, ProductSerializer,
                         RatingSerializer, CommentSerializer, # MemberSerializer, 
                        CommentUpdateSerializer, TransactionSerializer, CartSerializer, 
                        UserBasicSerializer, UserSerializer, UserUpdateSerializer)
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly, IsCurrentUserOrReadOnly
from .schema import ProductSchema

class HomeAPIView(viewsets.ModelViewSet):
    schema = ProductSchema()
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        list_products = self.queryset
        # query = self.request.query_params.get('sortBy')
        # if (query is not None):
        #     if (query == 'favs'):
        #         list_webmarketes = list_products.most_favs()
        #     elif (query == 'comments'):
        #         list_webmarketes = list_products.most_comments()
        #     else:
        #         list_webmarketes = list_products.alph()

        query = self.request.query_params.get('favourite')
        user = self.request.user
        if (query is not None and user is not None):
            list_products = list_products.in_bookmarks(self.request.user)
        return list_products

    def get_permissions(self):
        if self.request.method not in permissions.SAFE_METHODS:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]

    def get_serializer_class(self):
        return self.serializer_class

class CommentAPIView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'update':
            return CommentUpdateSerializer
        return CommentSerializer

class UserAPIView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == 'update':
            return UserUpdateSerializer
        return UserSerializer

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return [permissions.IsAuthenticated(), IsCurrentUserOrReadOnly()]
        elif self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

class ProductTypeAPIView(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

    def get_permissions(self):
        if self.request.method not in permissions.SAFE_METHODS:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]
        
################# Дописать для остального.


        
















# class ProductTypesAPIView(viewsets.ModelViewSet):
#     queryset = ProductType.objects.all()
#     serializer_class = ProductTypeSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# class ProductsAPIView(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# # class MembersAPIView(viewsets.ModelViewSet):
# #     queryset = Member.objects.all()
# #     serializer_class = MemberSerializer
# #     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# class RatingsAPIView(viewsets.ModelViewSet):
#     queryset = Rating.objects.all()
#     serializer_class = RatingSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# class CommentsAPIView(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# class TransactionsAPIView(viewsets.ModelViewSet):
#     queryset = Transaction.objects.all()
#     serializer_class = TransactionSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# class CartsAPIView(viewsets.ModelViewSet):
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
