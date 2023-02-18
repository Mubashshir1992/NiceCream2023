from django.contrib import admin

from .models import Product, Brand, Warehouse, InProduct
# Register your models here.



admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Warehouse)
admin.site.register(InProduct)