# myapp/models.py

from django.db import models
from django.conf import settings
from shop.models import Product


class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Изменено на settings.AUTH_USER_MODEL
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f'Cart of {self.user.username}'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def str(self):
        return f'{self.product.name} ({self.quantity})'

    def get_total_price(self):
        return self.quantity * self.product.price

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Изменено на settings.AUTH_USER_MODEL
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def str(self):
        return f'Order #{self.id} by {self.user.username}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def str(self):
        return f'{self.product.name} ({self.quantity})'

    def get_total_price(self):
        return self.quantity * self.product.price