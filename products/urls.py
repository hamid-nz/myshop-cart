# products/urls.py
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('base/', views.index),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
]