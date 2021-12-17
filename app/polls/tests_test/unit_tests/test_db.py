from django import test
from django.test import TestCase
from ...models import Cart, Comment, Product, ProductType, Rating, Transaction
#from polls.repositories.repository import *
from .builders import *
#from ...business_logic.objects.ProductType import *

class ProductTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.test_type_1 = ProductTypeBuilder(1, "risovanie", "eMpTyDescription").build()
        #cls.test_bl_type = ProductType_bl(typeID=1, typeName="risovanie", description="eMpTyDescription")
        cls.test_product_1 = ProductBuilder(1, cls.test_type_1, 'kistochka', "klassnaya kistochka", 1).with_price(15).build()
        cls.test_product_2 = ProductBuilder(2, cls.test_type_1, 'kraska', "yarkaya kraska", 1).with_price(10).build()
        ##cls.bl_product = Product_bl(productID=1, productType=cls.test_bl_type, productName='kistochka', description="klassnaya kistochka")

    def test_getProductByID(self):
        test_product = Product.objects.get(productID=1)
        self.assertEqual(test_product.productID, 1)
        print("ok?")
        pass

    def test_getNotExistingProduct(self):
        throw_exception = False
        try:
            Product.objects.get(productID=3)
        except Product.DoesNotExist:
            throw_exception = True

        self.assertTrue(throw_exception)

    def test_updateProduct(self):
        new_name = "karandash"
        Product.objects.filter(productID=2).update(productName = new_name)
        self.test_product_2.refresh_from_db()
        self.assertEqual(self.test_product_2.productName, new_name)


class ProductTypeTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.test_type_1 = ProductTypeBuilder(1, "risovanie", "eMpTyDescription").build() 
        
    def test_getProductTypeByID(self):
        test_type = ProductType.objects.get(typeID=1)
        self.assertEqual(test_type.typeID, 1)
        print("ok?")
        pass

    def test_getNotExistingProductType(self):
        throw_exception = False
        try:
            ProductType.objects.get(typeID=3)
        except ProductType.DoesNotExist:
            throw_exception = True

        self.assertTrue(throw_exception)

    def test_updateProductType(self):
        new_name = "lepka"
        ProductType.objects.filter(typeID=1).update(typeName = new_name)
        self.test_type_1.refresh_from_db()
        self.assertEqual(self.test_type_1.typeName, new_name)

class RatingTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.test_type_1 = ProductTypeBuilder(1, "risovanie", "eMpTyDescription").build() 
        cls.test_product_1 = ProductBuilder(1, cls.test_type_1, 'kistochka', "klassnaya kistochka", 1).with_price(15).build()
        cls.test_type_member = UserBuilder('usa').with_password('password').build() 
        cls.test_rating_1 = Rating.objects.create(ratingID=1, memberID=cls.test_type_member, productID=cls.test_product_1, value=5)

    def test_getRatingByID(self):
        test_rating = Rating.objects.get(ratingID=1)
        self.assertEqual(test_rating.ratingID, 1)
        print("ok?")
        pass

    def test_getNotExistingRating(self):
        throw_exception = False
        try:
            Rating.objects.get(ratingID=5)
        except Rating.DoesNotExist:
            throw_exception = True

        self.assertTrue(throw_exception)

    def test_updateRating(self):
        new_value = 2
        Rating.objects.filter(ratingID=1).update(value = new_value)
        self.test_rating_1.refresh_from_db()
        self.assertEqual(self.test_rating_1.value, new_value)

class TransactionTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.test_type_member = UserBuilder('usa').with_password('password').build()
        cls.test_transaction_1 = Transaction.objects.create(transactionID=1, memberID=cls.test_type_member, productIDs=[1, 2], productQuantities=[1, 1], approvalStatus="Accepted")

    def test_getTransactionByID(self):
        test_transaction = Transaction.objects.get(transactionID=1)
        self.assertEqual(test_transaction.transactionID, 1)
        print("ok?")
        pass

    def test_getNotExistingTransaction(self):
        throw_exception = False
        try:
            Transaction.objects.get(transactionID=5)
        except Transaction.DoesNotExist:
            throw_exception = True

        self.assertTrue(throw_exception)

    def test_updateTransaction(self):
        new_productIDs = [1, 1]
        Transaction.objects.filter(transactionID=1).update(productIDs = new_productIDs)
        self.test_transaction_1.refresh_from_db()
        self.assertEqual(self.test_transaction_1.productIDs, new_productIDs)

class CartTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.test_type_member = UserBuilder('usa').with_password('password').build()
        cls.test_cart_1 = Cart.objects.create(cartID=1, memberID=cls.test_type_member, productIDs=[1, 2], productQuantities=[1, 1], quantity=2)

    def test_getCartByID(self):
        test_cart = Cart.objects.get(cartID=1)
        self.assertEqual(test_cart.cartID, 1)
        print("ok?")
        pass

    def test_getNotExistingCart(self):
        throw_exception = False
        try:
            Cart.objects.get(cartID=5)
        except Cart.DoesNotExist:
            throw_exception = True

        self.assertTrue(throw_exception)

    def test_updateCart(self):
        new_productIDs = [1, 1]
        Cart.objects.filter(cartID=1).update(productIDs = new_productIDs)
        self.test_cart_1.refresh_from_db()
        self.assertEqual(self.test_cart_1.productIDs, new_productIDs)

# class MemberTest(TestCase):
#     @classmethod
#     def setUpTestData(cls) -> None:
#         cls.test_type_member = UserBuilder('usa').with_password('password').build() 

#     def test_getMemberByID(self):
#         test_member = User.objects.get(memberID=1)
#         self.assertEqual(test_member.memberID, 1)
#         print("ok?")
#         pass

#     def test_getNotExistingMember(self):
#         throw_exception = False
#         try:
#             Member.objects.get(memberID=5)
#         except Member.DoesNotExist:
#             throw_exception = True

#         self.assertTrue(throw_exception)

#     def test_updateMember(self):
#         new_username = "vasya3000"
#         Member.objects.filter(memberID=1).update(username = new_username)
#         self.test_type_member.refresh_from_db()
#         self.assertEqual(self.test_type_member.username, new_username)

class CommentTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.test_type_1 = ProductTypeBuilder(1, "risovanie", "eMpTyDescription").build() 
        cls.test_product_1 = ProductBuilder(1, cls.test_type_1, 'kistochka', "klassnaya kistochka", 1).with_price(15).build()
        cls.test_type_member_1 = UserBuilder('usa').with_password('password').build()
        cls.test_type_comment = Comment.objects.create(commentID=1, memberID=cls.test_type_member_1, productID=cls.test_product_1, message="super", commentDate="2021-12-24")

    def test_getCommentByID(self):
        test_comment = Comment.objects.get(commentID=1)
        self.assertEqual(test_comment.commentID, 1)
        print("ok?")
        pass

    def test_getNotExistingComment(self):
        throw_exception = False
        try:
            Comment.objects.get(commentID=5)
        except Comment.DoesNotExist:
            throw_exception = True

        self.assertTrue(throw_exception)

    def test_updateComment(self):
        new_message = "ogo, kakoi tovar!"
        Comment.objects.filter(commentID=1).update(message = new_message)
        self.test_type_comment.refresh_from_db()
        self.assertEqual(self.test_type_comment.message, new_message)



# from django.test import TestCase

# from django.test.client import RequestFactory
# from rest_framework import permissions
# #from catalog.models import City, Industry, Company, JobVacancy, Application
# #from catalog.views import ApplicationsAPIView, CompaniesAPIView

# from ...models import *
# from ..unit_tests.builders import MemberBuilder, ProductBuilder, ProductTypeBuilder
# from django.contrib.auth.models import User

# class CreateRatingTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.member = MemberBuilder(1, "1234", "1234", "a@a.ru", "AAA", "a street", "+79090909090").build() 
#         cls.type = ProductTypeBuilder(1, "risovanie", "eMpTyDescription").build() 
#         cls.product = ProductBuilder(1, cls.type, 'kistochka', "klassnaya kistochka", 1).with_price(15).build()
#         cls.user = User.objects.create(username='1234', password='1234')

#     def test_createRating(self):
#         self.client.force_login(self.user)

#         rating_data = {
#             'productID' : 1,
#             'value' : 10
#         }
#         print("ya test creating and prekrasno")
#         response = self.client.post('/api/v1/Ratings/', data=rating_data)
#         self.assertEqual(response.status_code, 201)