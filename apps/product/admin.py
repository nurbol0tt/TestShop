from django.contrib import admin

from apps.product.models import Product, Category, Tag

# Register your models here.
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Product)
