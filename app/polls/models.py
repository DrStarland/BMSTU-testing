from django.conf import settings
from django.core.checks import messages
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField
from django.db import models

import uuid
import os

def custom_save_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('img/', filename)


class ProductType(models.Model):
    typeID = models.SmallIntegerField(primary_key=True)
    typeName = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return str(self.typeName) + ": " + str(self.description)

    def get_absolute_url(self):
        return reverse('application-detail', args=[str(self.typeID)])
    
    class Meta:
        verbose_name = 'тип'
        verbose_name_plural = 'типы'

class Product(models.Model):
    productID = models.IntegerField(primary_key=True)
    productType = models.ForeignKey(ProductType,  on_delete=CASCADE)
    productName = models.CharField(max_length=100)
    description = models.TextField()
    stock = models.IntegerField()
    price = models.IntegerField()
    imageSource = models.ImageField(upload_to=custom_save_path,
                            verbose_name='изображение', default='img/image.png')

    def __str__(self):
        return str(self.productName) + ": " + str(self.description)

    def get_absolute_url(self):
        return reverse('industry-detail', args=[str(self.productID)])
    
    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

class Member(models.Model):
    memberID = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return str(self.username)

    def get_absolute_url(self):
        return reverse('industry-detail', args=[str(self.memberID)])

    class Meta:
        verbose_name = 'участник'
        verbose_name_plural = 'участники'

class Rating(models.Model):
    raitingID = models.IntegerField(primary_key=True)
    memberID = models.ForeignKey(Member, on_delete=CASCADE)
    productID = models.ForeignKey(Product, on_delete=CASCADE)
    value = models.SmallIntegerField()

    def __str__(self):
        return "ID: " + str(self.productID) + ", rating: " + str(self.value)

    def get_absolute_url(self):
        return reverse('application-detail', args=[str(self.raitingID)])
    
    class Meta:
        verbose_name = 'оценка'
        verbose_name_plural = 'оценки'

class Comment(models.Model):
    commentID = models.IntegerField(primary_key=True)
    memberID = models.ForeignKey(Member, on_delete=CASCADE)
    productID = models.ForeignKey(Product, on_delete=CASCADE)
    message = models.TextField()
    commentDate = models.DateField()

    def __str__(self):
        return str(self.message) + str(self.commentDate)

    def get_absolute_url(self):
        return reverse('application-detail', args=[str(self.commentID)])
    
    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'

class Transaction(models.Model):
    transactionID = models.IntegerField(primary_key=True)
    memberID = models.ForeignKey(Member, on_delete=CASCADE)
    productIDs = ArrayField(models.IntegerField(), default=list())
    productQuantities = ArrayField(models.SmallIntegerField(), default=list())
    approvalStatus = models.CharField(max_length=10)
    transactionDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return "TID: " + str(self.transactionID) + ", status: " + str(self.approvalStatus)

    def get_absolute_url(self):
        return reverse('application-detail', args=[str(self.transactionID)])
    
    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

class Cart(models.Model):
    cartID = models.IntegerField(primary_key=True)
    memberID = models.ForeignKey(Member, on_delete=CASCADE)
    productIDs = ArrayField(models.IntegerField())
    productQuantities = ArrayField(models.SmallIntegerField())
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.cartID)

    def get_absolute_url(self):
        return reverse('application-detail', args=[str(self.cartID)])
    
    class Meta:
        verbose_name = 'корзина'
        verbose_name_plural = 'корзины'
