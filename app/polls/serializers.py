from rest_framework import serializers
from django.contrib.auth.models import User

from .models import ProductType, Product, Member, Rating, Comment, Transaction, Cart
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django.http.response import JsonResponse



# def products_list(request):
#     if request.method == 'GET':
#         products = Product.objects.all()
        
#         title = request.query_params.get('title', None)
#         if title is not None:
#             products = products.filter(title__icontains=title)
        
#         products_serializer = ProductSerializer(products, many=True)
#         return JsonResponse(products_serializer.data, safe=False)
#         # 'safe=False' for objects serialization
 
#     elif request.method == 'POST':
#         tutorial_data = JSONParser().parse(request)
#         tutorial_serializer = ProductSerializer(data=tutorial_data)
#         if tutorial_serializer.is_valid():
#             tutorial_serializer.save()
#             return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
#         return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         count = Product.objects.all().delete()
#         return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
# @api_view(['GET', 'PUT', 'DELETE'])
# def tutorial_detail(request, pk):
#     try: 
#         tutorial = Tutorial.objects.get(pk=pk) 
#     except Tutorial.DoesNotExist: 
#         return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
#     if request.method == 'GET': 
#         tutorial_serializer = TutorialSerializer(tutorial) 
#         return JsonResponse(tutorial_serializer.data) 
 
#     elif request.method == 'PUT': 
#         tutorial_data = JSONParser().parse(request) 
#         tutorial_serializer = TutorialSerializer(tutorial, data=tutorial_data) 
#         if tutorial_serializer.is_valid(): 
#             tutorial_serializer.save() 
#             return JsonResponse(tutorial_serializer.data) 
#         return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
#     elif request.method == 'DELETE': 
#         tutorial.delete() 
#         return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
   # typeName = serializers.CharField(source='producttype.typeName', read_only=True)
    class Meta:
        model = ProductType
        fields = ('typeName', 'description')

class ProductSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(required=False)
    class Meta:
        model = Product
        fields = ('productName', 'description', 'stock', 'price', 'img')

    # def create(self, validated_data):
    #     product = super().create(validated_data)
    #     return product

    # def update(self, instance, validated_data):
    #     product = super().update(instance, validated_data)
    #     product.save()
    #     return product

class RatingSerializer(serializers.HyperlinkedModelSerializer):
    #current_user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Rating
        fields = ('memberID', 'productID', 'value')

    def create(self, validated_data):
        #validated_data['memberID'] = validated_data.pop('current_user')
        return super().create(validated_data)

class RatingUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('value',)

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('memberID', 'productID', 'message', 'commentDate',)

    def create(self, validated_data):
        #validated_data['memberID'] = validated_data.pop('current_user')
        return super().create(validated_data)

class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('message',)

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ('transactionID', 'approvalStatus', 'transactionDate',)
    
    def create(self, validated_data):
        #validated_data['memberID'] = validated_data.pop('current_user')
        return super().create(validated_data)

class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ('cartID', 'productIDs', 'productQuantities',)
    
    def create(self, validated_data):
        #validated_data['memberID'] = validated_data.pop('current_user')
        return super().create(validated_data)


class UserBasicSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(UserBasicSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password',)


class UserUpdateSerializer(UserBasicSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('password',)
