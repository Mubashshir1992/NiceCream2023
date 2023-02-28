from django.contrib import admin

from .models import Product, Brand, WarehouseName, InProduct, OutProduct, OutProductB, Warehouse
# Register your models here.



admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(WarehouseName)
admin.site.register(Warehouse)
admin.site.register(InProduct)
admin.site.register(OutProduct)
admin.site.register(OutProductB)