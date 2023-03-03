from django.urls import path
from . import views

urlpatterns = [
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register_user'),
    path('providers/', views.providers, name='providers'),
    path('clients/', views.clients, name='clients'),
    path('act_sverka/', views.act_sverka, name='act_sverka'),
    path('act_sverka_client/', views.act_sverka_client, name='act_sverka_client'),
    path('my_act_sverka/', views.my_act_sverka, name='my_act_sverka'),
]