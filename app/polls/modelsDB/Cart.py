from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.db import models

from .Member import *

from django.contrib.auth.models import User


class Cart(models.Model):
    cartID = models.IntegerField(primary_key=True)
    #memberID = models.ForeignKey(Member, on_delete=CASCADE)

    memberID = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
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