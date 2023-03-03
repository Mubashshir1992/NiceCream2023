from django.contrib import admin

from .models import Product, Brand, WarehouseName, InProduct, OutProduct, OutProductB, Warehouse
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'capacity', 'brand', 'product_size', 'product_weight', 'code',]

class BrandAdmin(admin.ModelAdmin):
    model = Brand
    list_display = ['name', 'phone', 'address',]

class WarehouseAdmin(admin.ModelAdmin):
    model = Warehouse
    list_display = ['warehouse', 'date', 'product', 'comment',]

class InProductAdmin(admin.ModelAdmin):
    model = InProduct
    list_display = ['warehouse', 'in_date', 'provider', 'product', 'comment',]

class OutProductAdmin(admin.ModelAdmin):
    model = OutProduct
    list_display = ['warehouse', 'out_date', 'trader', 'product', 'comment',]

class OutProductBAdmin(admin.ModelAdmin):
    model = OutProductB
    list_display = ['warehouse', 'out_date', 'trader', 'client', 'product', 'comment',]

admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(WarehouseName)
admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(InProduct, InProductAdmin)
admin.site.register(OutProduct, OutProductAdmin)
admin.site.register(OutProductB, OutProductBAdmin)