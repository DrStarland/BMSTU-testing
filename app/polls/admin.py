from django.contrib import admin
from .models import ProductType, Product, Rating, Comment, Transaction, Cart

admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(Rating)
admin.site.register(Comment)
admin.site.register(Transaction)
admin.site.register(Cart)
