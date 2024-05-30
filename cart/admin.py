# myapp/admin.py

from django.contrib import admin
from .models import Cart, CartItem, Order, OrderItem

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')  # Убедитесь, что это кортеж или список
    inlines = [CartItemInline]
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'total_price')
    inlines = [OrderItemInline]

admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)