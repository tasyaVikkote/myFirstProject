from django.contrib import admin
from .models import Product, Category, Comment, Addresses

# Register your models here.
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Addresses)