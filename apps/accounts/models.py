from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    USER_TYPE_CHOICES = (
        ('PR', 'Provider'),
        ('CL', 'Client'),
    )

    username = models.CharField(max_length=255,unique=True,)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(verbose_name='email address', blank=True, max_length=255, null=True)
    activated_date = models.DateTimeField(blank=True, null=True)
    balance = models.IntegerField(default=0)
    image = models.ImageField(default='user4.png',upload_to='images/', blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    user_type = models.CharField(max_length=50,choices=USER_TYPE_CHOICES, default='PR')

    def __str__(self):
        return self.username
