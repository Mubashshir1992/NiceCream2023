from django.urls import path
from . import views

urlpatterns = [
    path('warehouse/', views.warehouse, name='warehouse'),
    path('product_list/', views.product_name_list, name='product_list'),
    path('add_product_name/', views.add_product_name, name='add_product_name'),
    path('update_product_name/<product_id>/', views.update_product_name, name='update_product_name'),
    path('delete_product_name/<product_id>/', views.delete_product_name, name='delete_product_name'),
    path('warehouse_list/', views.warehouse_name_list, name='warehouse_list'),
    path('add_warehouse_name/', views.add_warehouse_name, name='add_warehouse_name'),
    path('update_warehouse_name/<warehouse_id>/', views.update_warehouse_name, name='update_warehouse_name'),
    path('delete_warehouse_name/<warehouse_id>/', views.delete_warehouse_name, name='delete_warehouse_name'),
    path('in_product_list/', views.in_product_list, name='in_product_list'),
    path('add_in_product/', views.add_in_product, name='add_in_product'),
    path('update_in_product/<product_id>/', views.update_in_product, name='update_in_product'),
    path('delete_in_product/<product_id>/', views.delete_in_product, name='delete_in_product'),
    path('out_product_list/', views.out_product_list, name='out_product_list'),
    path('add_out_product/', views.add_out_product, name='add_out_product'),
    path('update_out_product/<product_id>/', views.update_out_product, name='update_out_product'),
    path('delete_out_product/<product_id>/', views.delete_out_product, name='delete_out_product'),
    path('out_productb_list/', views.out_productb_list, name='out_productb_list'),
    path('add_out_productb/', views.add_out_productb, name='add_out_productb'),
    path('update_out_productb/<product_id>/', views.update_out_productb, name='update_out_productb'),
    path('delete_out_productb/<product_id>/', views.delete_out_productb, name='delete_out_productb'),
    path('in_document_list/', views.in_document_list, name='in_document_list'),
    path('add_in_document/', views.add_in_document, name='add_in_document'),
    path('update_in_document/<document_id>/', views.update_in_document, name='update_in_document'),
    path('delete_in_document/<document_id>/', views.delete_in_document, name='delete_in_document'),
    path('in_document_products/<document_id>/', views.in_document_products, name='in_document_products'),
    path('out_document_list/', views.out_document_list, name='out_document_list'),
    path('add_out_document/', views.add_out_document, name='add_out_document'),
    path('update_out_document/<document_id>/', views.update_out_document, name='update_out_document'),
    path('delete_out_document/<document_id>/', views.delete_out_document, name='delete_out_document'),
    path('out_document_products/<document_id>/', views.out_document_products, name='out_document_products'),
    path('out_documentclient_list/', views.out_documentclient_list, name='out_documentclient_list'),
    path('add_out_documentclient/', views.add_out_documentclient, name='add_out_documentclient'),
    path('update_out_documentclient/<document_id>/', views.update_out_documentclient, name='update_out_documentclient'),
    path('delete_out_documentclient/<document_id>/', views.delete_out_documentclient, name='delete_out_documentclient'),
    path('out_documentclient_products/<document_id>/', views.out_documentclient_products, name='out_documentclient_products'),
    path('profit_list/', views.profit_list, name='profit_list'),
    
]