from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_customer, name='register_customer'),
    path('register-product/', views.register_product, name='register_product'),
    path('recommend-products/', views.recommend_products, name='recommend_products'),
    path('checkout/', views.checkout, name='checkout'),
    path('customers/', views.list_customers, name='list_customers'),
    path('products/', views.list_products, name='list_products'),
]