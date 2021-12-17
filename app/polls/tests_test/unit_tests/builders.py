from ...models import ProductType, Product
from django.contrib.auth.models import User

class UserBuilder:
    def __init__(self, username):
        self.user = User.objects.create(username=username)

    def with_email(self, email):
        self.user.email = email
        return self

    def with_password(self, password):
        self.user.password = password
        return self

    def build(self):
        return self.user


class ProductTypeBuilder:
    def __init__(self, typeID, typeName, description):
        self.producttype = ProductType.objects.create(typeID=typeID, typeName=typeName, description=description)

    def build(self):
        return self.producttype

class ProductBuilder:
    def __init__(self, productID, productType, productName, description='', stock=5, price=0):
        self.product = Product.objects.create(productID=productID, productName=productName, productType=productType, description=description, stock=stock, price=price)

    def with_price(self, price):
        self.product.price = price
        return self

    def build(self):
        return self.product

def datetime_stub():
    return '2018-10-16'