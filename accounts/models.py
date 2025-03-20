from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)

    groups = models.ManyToManyField(
        Group,
        related_name="customuser_set",  # Prevents conflict with auth.User
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions_set",  # Prevents conflict with auth.User
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone']

    def __str__(self):
        return self.email
