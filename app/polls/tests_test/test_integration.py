from django.test import TestCase

from django.test.client import RequestFactory
from rest_framework import permissions
#from catalog.models import City, Industry, Company, JobVacancy, Application
#from catalog.views import ApplicationsAPIView, CompaniesAPIView

from ..models import *
from .unit_tests.builders import UserBuilder, ProductBuilder, ProductTypeBuilder
from django.contrib.auth.models import User

from ..views import *

class CreateRatingTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.member = UserBuilder('usa').with_password('password').build() 
        cls.type = ProductTypeBuilder(1, "risovanie", "eMpTyDescription").build() 
        cls.product = ProductBuilder(1, cls.type, 'kistochka', "klassnaya kistochka", 1).with_price(15).build()
        cls.user = User.objects.create(username='1234', password='1234')
        cls.rating = Rating.objects.create(ratingID=2, productID=cls.product, value=10)

    def test_createRating(self):
        self.client.force_login(self.user)

        rating_data = {
            "ratingID" : 1,
            'productID' : "http://127.0.0.1:8000/api/v1/Products/1/",
            'value' : 10
        }
        print("ya test creating and prekrasno")
        response = self.client.post('/api/v1/Ratings/', data=rating_data)
        self.assertEqual(response.status_code, 201)

    def test_patchRating(self):
        self.client.force_login(self.user)

        rating_data = {
            'value' : 5
        }

        response = self.client.patch('/api/v1/Ratings/2/', content_type='application/json', data=rating_data)
        self.assertEqual(response.status_code, 200)

class PermissionTest(TestCase):
    def test_authenticated_permission(self):
        authenticated_user = UserBuilder('usa').with_password('password').build() 
        factory = RequestFactory()
        permission = permissions.IsAuthenticatedOrReadOnly()

        request = factory.post('/api/v1/Ratings/')
        request.user = authenticated_user

        has_permission = permission.has_permission(request, RatingsAPIView)
        self.assertTrue(has_permission)

    def test_no_admin_permission(self):
        admin_user = UserBuilder('admin').with_password('password').build() 
        factory = RequestFactory()
        permission = permissions.IsAdminUser()

        request = factory.post('/api/v1/Transactions/')
        request.user = admin_user
        
        has_permission = not permission.has_permission(request, TransactionsAPIView)
        self.assertTrue(has_permission)


    def test_admin_permission(self):
        admin_user = User.objects.create(email='admin', password='password', is_staff=True)
        
        factory = RequestFactory()
        permission = permissions.IsAdminUser()

        request = factory.post('/api/v1/ProductTypes/')
        request.user = admin_user
        
        has_permission = permission.has_permission(request, ProductTypeAPIView)
        self.assertTrue(has_permission)

class RegistrationTest(TestCase):
    def test_registration_success(self):
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
        self.assertTrue(user_created)
        self.assertEqual(created_user.username, user_data['username'])


