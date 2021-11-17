from rest_framework import serializers
from django.contrib.auth.models import User

from .models import ProductType, Product, Member, Rating, Comment, Transaction, Cart

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    typeName = serializers.CharField(source='product_types.typeName', read_only=True)
    class Meta:
        model = ProductType
        fields = ('typeName', 'description')

class ProductSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(required=False)
    class Meta:
        model = Product
        fields = ('productName', 'description', 'stock', 'price', 'img')

    def create(self, validated_data):
        product = super().create(validated_data)
        return product

    def update(self, instance, validated_data):
        super().update(instance, validated_data)
        return instance

# class MemberSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Member
#         fields = ('url', 'username', 'fullname', 'email', 'phone', 'address')

class RatingSerializer(serializers.HyperlinkedModelSerializer):
    #current_user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Rating
        fields = ('productID', 'value')

    def create(self, validated_data):
        #validated_data['memberID'] = validated_data.pop('current_user')
        return super().create(validated_data)

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('memberID', 'message', 'commentDate',)

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
