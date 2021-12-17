from django.conf import settings
from django.core.checks import messages
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField
from django.db import models

import uuid
import os

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