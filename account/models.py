from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra):
        if not email:
            raise ValueError('Email поле обязательное')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra)
        user.set_password(password)
        user.save()
        return user
    
    def create_user(self, email, password, **extra):
        user = self._create_user(email, password, **extra)
        user.create_activation_code()
        user.save()
        return user
    def create_superuser(self, email, password, **extra):
        extra.setdefault('is_active', True)
        extra.setdefault('is_staff', True)
        extra.setdefault('is_superuser',True)
        user = self._create_user(email, password, **extra)
        return user
    
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True) 
    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=10, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def create_activation_code(self):
        code = get_random_string(length=10, allowed_chars='0123456789')
        self.activation_code = code
        

