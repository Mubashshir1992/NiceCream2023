from django.urls import path
from . import views

urlpatterns = [
    path('warehouse/', views.warehouse, name='warehouse'),
    path('product_list/', views.product_name_list, name='product_list'),
    path('add_product_name/', views.add_product_name, name='add_product_name'),
    path('update_product_name/<product_id>/', views.update_product_name, name='update_product_name'),
    path('delete_product_name/<product_id>/', views.delete_product_name, name='delete_product_name'),
    path('in_product_list/', views.in_product_list, name='in_product_list'),
    path('add_in_product/', views.add_in_product, name='add_in_product'),
    path('update_in_product/<product_id>/', views.update_in_product, name='update_in_product'),
    path('delete_in_product/<product_id>/', views.delete_in_product, name='delete_in_product'),
    path('creditors/', views.creditors, name='creditors'),
    
]