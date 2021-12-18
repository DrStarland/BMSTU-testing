from django.test import TestCase
from django.contrib.auth.models import User
from polls.tests_test.unit_tests.builders import UserBuilder, ProductBuilder, ProductTypeBuilder
from polls.models import *


class EndToEndTest1(TestCase):
    @classmethod
    def setUpTestData(cls):

        cls.type = ProductTypeBuilder(1, "risovanie", "eMpTyDescription").build() 
        cls.product = ProductBuilder(1, cls.type, 'kistochka', "klassnaya kistochka", 1).with_price(15).build()

        cls.passed = 0

    def __get(self, model_class):
         return model_class.objects.all().first()

    def get_user(self):
         return self.__get(User)

    def get_product(self):
         return self.__get(Product)

    def test_get_product_and_set_rating(self):
        for _ in range(100):
            user_data = {
                'username': 'username',
                'password': 'password',
            }

            response = self.client.post('/api/v1/Members/', content_type='application/json', data=user_data)
            try:
                created_user = User.objects.get(username=user_data['username'])
                user_created = True
            except User.DoesNotExist:
                created_user = {'username': None}
                user_created = False

            self.assertEqual(response.status_code, 201)

            self.assertEqual(self.get_user().username, 'username')

            self.client.force_login(self.get_user())

            response = self.client.get('/api/v1/Products/')
            self.assertEqual(response.status_code, 200)

            response = self.client.get('/api/v1/Products/?price=15')
            self.assertEqual(response.status_code, 200)

            response = self.client.get('/api/v1/Products/1/')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(self.get_product().productName, 'kistochka')

            rating_data = {
            "ratingID" : 1,
            'productID' : "http://127.0.0.1:8000/api/v1/Products/1/",
            'value' : 10
            }

            response = self.client.post('/api/v1/Ratings/', data=rating_data)
            self.assertEqual(response.status_code, 201)

            response = self.client.delete(f"/api/v1/Ratings/{rating_data['ratingID']}/")
            self.assertEqual(response.status_code, 204)

            User.objects.all().delete()

            self.passed += 1

    def tearDown(self):
        print('E2E w/ rating passed: %d' % self.passed)


class EndToEndTest2(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.type = ProductTypeBuilder(1, "risovanie", "eMpTyDescription").build() 
        cls.product = ProductBuilder(1, cls.type, 'kistochka', "klassnaya kistochka", 10).with_price(15).build()

        cls.passed = 0

    def __get(self, model_class):
         return model_class.objects.all().first()

    def get_user(self):
         return self.__get(User)

    def get_product(self):
         return self.__get(Product)

    def test_get_product_to_cart(self):
        for _ in range(100):
            user_data = {
                'username': 'username',
                'password': 'password',
            }

            response = self.client.post('/api/v1/Members/', content_type='application/json', data=user_data)
            try:
                created_user = User.objects.get(username=user_data['username'])
                user_created = True
            except User.DoesNotExist:
                created_user = {'username': None}
                user_created = False

            self.assertEqual(response.status_code, 201)

            self.assertEqual(self.get_user().username, 'username')

            self.client.force_login(self.get_user())

            response = self.client.get('/api/v1/Products/')
            self.assertEqual(response.status_code, 200)

            response = self.client.get('/api/v1/Products/1/')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(self.get_product().productName, 'kistochka')

            cart = {
            "cartID": 1,
            "productIDs": [1],
            "productQuantities": [1],
            "quantity": 1
            }

            response = self.client.post('/api/v1/Carts/', content_type='application/json',  data=cart)
            self.assertEqual(response.status_code, 201)


            product_dec = {
            'stock' : 9
            }
            response = self.client.patch('/api/v1/Products/1/', content_type='application/json', data=product_dec)   
            self.assertEqual(response.status_code, 200)



            # delete
            response = self.client.delete(f"/api/v1/Carts/{cart['cartID']}/")
            self.assertEqual(response.status_code, 204)
            

            User.objects.all().delete()

            self.passed += 1

    def tearDown(self):
        print('E2E w/ cart passed: %d' % self.passed)
    
