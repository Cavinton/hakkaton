from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=30, verbose_name='Категория товара')

    def __str__(self):
        return self.title



class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=60, verbose_name='Название' )
    image = models.ImageField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    in_stock = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    