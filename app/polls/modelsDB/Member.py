# from django.conf import settings
# from django.db.models.deletion import CASCADE
# from django.urls import reverse
# from django.db import models

# class Member(models.Model):
#     memberID = models.IntegerField(primary_key=True)
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     fullname = models.CharField(max_length=100)
#     address = models.CharField(max_length=150)
#     phone = models.CharField(max_length=20)

#     def __str__(self):
#         return str(self.username)

#     def get_absolute_url(self):
#         return reverse('industry-detail', args=[str(self.memberID)])

#     class Meta:
#         verbose_name = 'участник'
#         verbose_name_plural = 'участники'