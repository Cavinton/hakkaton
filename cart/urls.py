# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order/success/', views.order_success, name='order_success'),
]