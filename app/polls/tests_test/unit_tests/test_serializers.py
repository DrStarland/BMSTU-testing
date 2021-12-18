from django.test import TestCase
from unittest.mock import MagicMock
from django.contrib.auth.models import User
from ...serializers import *
from ...models import Cart, Comment, Product, ProductType, Rating, Transaction
from .builders import *



class ProductSerializerTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.test_type_1 = ProductTypeBuilder(1, typeName="risovanie", description="eMpTy").build()

        cls.test_product_1 = ProductBuilder(productID=1, productName='kistochka',
                                                    productType=cls.test_type_1).build()
        cls.test_product_2 = ProductBuilder(productID=2, productName='kraska', productType=cls.test_type_1).build()


        cls.test_product_serializer = ProductSerializer(cls.test_product_1, context={'request': MagicMock()})

    def test_included_fields(self):
        data = self.test_product_serializer.data
        self.assertEqual(set(data.keys()), {'productID', 'productName', 'productType', 'stock', 'price', 'description'})
        print(data.keys())
        print("&_&")

    def test_product_field_content(self):
        data = self.test_product_serializer.data
        self.assertEqual(data['productName'], 'kistochka')

    def test_update_name_field(self):
        self.test_product_serializer.update(self.test_product_1, {'productName': 'kistochka_new'})
        self.test_product_1.refresh_from_db()
        self.assertEqual(self.test_product_1.productName, 'kistochka_new')


class ProductTypeSerializerTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.test_type_1 = ProductTypeBuilder(1, typeName="risovanie", description="eMpTy").build()

        cls.test_productType_serializer = ProductTypeSerializer(cls.test_type_1, context={'request': MagicMock()})

    def test_included_fields(self):
        data = self.test_productType_serializer.data
        self.assertEqual(set(data.keys()), {'typeID', 'typeName', 'description'})
        print(data.keys())

    def test_product_field_content(self):
        data = self.test_productType_serializer.data
        self.assertEqual(data['typeName'], "risovanie")

    def test_update_name_field(self):
        self.test_productType_serializer.update(self.test_type_1, {'description': 'Все товары'})
        self.test_type_1.refresh_from_db()
        self.assertEqual(self.test_type_1.description, 'Все товары')


class ProductTypeSerializerTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.test_type_1 = ProductType.objects.create(typeID=1, typeName="risovanie", description="eMpTy")

        cls.test_productType_serializer = ProductTypeSerializer(cls.test_type_1, context={'request': MagicMock()})

    def test_included_fields(self):
        data = self.test_productType_serializer.data
        self.assertEqual(set(data.keys()), {'typeID', 'typeName', 'description'})
        print(data.keys())

    def test_product_field_content(self):
        data = self.test_productType_serializer.data
        self.assertEqual(data['typeName'], "risovanie")

    def test_update_name_field(self):
        self.test_productType_serializer.update(self.test_type_1, {'description': 'Все товары'})
        self.test_type_1.refresh_from_db()
        self.assertEqual(self.test_type_1.description, 'Все товары')

        
class CartSerializerTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        #cls.test_member = UserBuilder(
        #    memberID=1, username="1234", password="1234", email="a@a.ru", fullname="AAA", address="a street", phone="+79090909090").build()

        cls.test_member = UserBuilder('usa').with_password('password').build()

        cls.test_cart = Cart.objects.create(
            cartID=1, memberID=cls.test_member, productIDs=[1, 2], productQuantities=[1, 1], quantity=2)

        cls.test_cart_serializer = CartSerializer(cls.test_cart, context={'request': MagicMock()})

    def test_included_fields(self):
        data = self.test_cart_serializer.data
        self.assertEqual(set(data.keys()), {'cartID', 'memberID', 'productIDs', 'productQuantities', 'quantity'})
        print(data.keys())

    def test_cart_field_content(self):
        data = self.test_cart_serializer.data
        self.assertEqual(data['cartID'], 1)

    def test_update_quantities_field(self):
        self.test_cart_serializer.update(self.test_cart, {'productQuantities': [2, 5]})
        self.test_cart.refresh_from_db()
        self.assertEqual(self.test_cart.productQuantities, [2, 5])


class CommentSerializerTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.test_type_1 = ProductType.objects.create(typeID=1, typeName="risovanie", description="eMpTy")
        cls.test_product_1 = Product.objects.create(productID=1, productName='kistochka',
                                                    productType=cls.test_type_1, stock = 1, price=1)

        cls.test_member = UserBuilder('usa').with_password('password').build()

        cls.test_comment = Comment.objects.create(
            commentID=1, memberID=cls.test_member, productID=cls.test_product_1, message="great", commentDate=datetime_stub()) 

        cls.test_comment_serializer = CommentSerializer(cls.test_comment, context={'request': MagicMock()})

    def test_included_fields(self):
        data = self.test_comment_serializer.data
        self.assertEqual(set(data.keys()), {'productID', 'memberID', 'message', 'commentDate'})
        print(data.keys())

    def test_comment_field_content(self):
        data = self.test_comment_serializer.data
        self.assertEqual(data['message'], "great")

    def test_update_message_field(self):
        self.test_comment_serializer.update(self.test_comment, {'message': "Не очень"})
        self.test_comment.refresh_from_db()
        self.assertEqual(self.test_comment.message, "Не очень")



class RatingSerializerTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.test_type_1 = ProductType.objects.create(typeID=1, typeName="risovanie", description="eMpTy")
        cls.test_product_1 = ProductBuilder(productID=1, productName='kistochka',
                                                    productType=cls.test_type_1, description='Большая').build()
        cls.test_member = UserBuilder('usa').with_password('password').build()

        cls.test_rating = Rating.objects.create(
            ratingID=1, memberID=cls.test_member, productID=cls.test_product_1, value=7)

        cls.test_rating_serializer = RatingSerializer(cls.test_rating, context={'request': MagicMock()})

    def test_included_fields(self):
        data = self.test_rating_serializer.data
        self.assertEqual(set(data.keys()), {'ratingID', 'memberID', 'productID', 'value'})
        print(data.keys())

    def test_rating_field_content(self):
        data = self.test_rating_serializer.data
        self.assertEqual(data['value'], 7)

    def test_update_message_field(self):
        self.test_rating_serializer.update(self.test_rating, {'value': 8})
        self.test_rating.refresh_from_db()
        self.assertEqual(self.test_rating.value, 8)




class TransactionSerializerTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.test_member = UserBuilder('usa').with_password('password').build()

        cls.test_transaction = Transaction(transactionID=1, memberID = cls.test_member, productIDs = [1, 2],
                productQuantities=[1, 1], approvalStatus='accepted', transactionDate = datetime_stub())

        cls.test_transaction_serializer = TransactionSerializer(cls.test_transaction, context={'request': MagicMock()})

    def test_included_fields(self):
        data = self.test_transaction_serializer.data
        print(data.keys())
        self.assertEqual(set(data.keys()), {'transactionID', 'productIDs', 'productQuantities',
                'approvalStatus', 'transactionDate'})

    def test_transaction_field_content(self):
        data = self.test_transaction_serializer.data
        self.assertEqual(data['transactionID'], 1)

    def test_update_message_field(self):
        self.test_transaction_serializer.update(self.test_transaction, {'approvalStatus' : 'denied'})
        self.test_transaction.refresh_from_db()
        self.assertEqual(self.test_transaction.approvalStatus, 'denied')

    