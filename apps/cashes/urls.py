from django.urls import path
from . import views

urlpatterns = [
    path('cash_list/', views.cash_name_list, name='cash_list'),
    path('add_cash_name/', views.add_cash_name, name='add_cash_name'),
    path('update_cash_name/<cash_id>/', views.update_cash_name, name='update_cash_name'),
    path('delete_cash_name/<cash_id>/', views.delete_cash_name, name='delete_cash_name'),
    path('in_cash_list/', views.in_cash_list, name='in_cash_list'),
    path('add_in_cash/', views.add_in_cash, name='add_in_cash'),
    path('update_in_cash/<int:id>/', views.update_in_cash, name='update_in_cash'),
    path('delete_in_cash/<int:id>/', views.delete_in_cash, name='delete_in_cash'),
    path('in_cashclient_list/', views.in_cashclient_list, name='in_cashclient_list'),
    path('add_in_cashclient/', views.add_in_cashclient, name='add_in_cashclient'),
    path('update_in_cashclient/<int:id>/', views.update_in_cashclient, name='update_in_cashclient'),
    path('delete_in_cashclient/<int:id>/', views.delete_in_cashclient, name='delete_in_cashclient'),
    path('out_cash_list/', views.out_cash_list, name='out_cash_list'),
    path('add_out_cash/', views.add_out_cash, name='add_out_cash'),
    path('update_out_cash/<int:id>/', views.update_out_cash, name='update_out_cash'),
    path('delete_out_cash/<int:id>/', views.delete_out_cash, name='delete_out_cash'),
    path('out_cashClient_list/', views.out_cashClient_list, name='out_cashClient_list'),
    path('add_out_cashClient/', views.add_out_cashClient, name='add_out_cashClient'),
    path('update_out_cashClient/<int:id>/', views.update_out_cashClient, name='update_out_cashClient'),
    path('delete_out_cashClient/<int:id>/', views.delete_out_cashClient, name='delete_out_cashClient'),
    path('expense_list/', views.expense_list, name='expense_list'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('update_expense/<int:id>/', views.update_expense, name='update_expense'),
    path('delete_expense/<int:id>/', views.delete_expense, name='delete_expense'),
]