from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model

from shop.models import Product

User = get_user_model()

class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments',on_delete=models.CASCADE)

    post = models.ForeignKey(Product, related_name='comments',on_delete=models.CASCADE)

    body = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)


    

class Like(models.Model):
    user = models.ForeignKey(User, related_name='Likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Product, related_name='Likes', on_delete=models.CASCADE)

