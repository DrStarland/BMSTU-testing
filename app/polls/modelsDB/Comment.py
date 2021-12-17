from django.conf import settings
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User


from .Member import *
from .Product import *

class Comment(models.Model):
    commentID = models.IntegerField(primary_key=True)
    memberID = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    #memberID = models.ForeignKey(Member, on_delete=CASCADE)
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