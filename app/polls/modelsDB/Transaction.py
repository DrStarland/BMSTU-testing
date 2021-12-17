from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

from .Member import * 


class Transaction(models.Model):
    transactionID = models.IntegerField(primary_key=True)
    memberID = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
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