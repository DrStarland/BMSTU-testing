from django.conf import settings
from django.core.checks import messages
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField
from django.db import models

import uuid
import os

from .ProductType import *

def custom_save_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('img/', filename)

    # licnum = models.CharField(
    #     max_length=15, unique=True, validators=[validate_licnum])
  

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