from django.conf import settings
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.db import models

from .Member import *
from .Product import *

from django.contrib.auth.models import User

class Rating(models.Model):
    ratingID = models.IntegerField(primary_key=True)
   # memberID = models.ForeignKey(Member, on_delete=CASCADE)
    memberID = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    productID = models.ForeignKey(Product, on_delete=CASCADE)
    value = models.SmallIntegerField()

    def __str__(self):
        return "ID: " + str(self.productID) + ", rating: " + str(self.value)

    def get_absolute_url(self):
        return reverse('application-detail', args=[str(self.raitingID)])
    
    class Meta:
        verbose_name = 'оценка'
        verbose_name_plural = 'оценки'