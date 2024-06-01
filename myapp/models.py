from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class PersonUser(AbstractUser):
    otp = models.CharField(max_length=6 ,null=True, blank=True)

    groups = models.ManyToManyField(
        Group,
        related_name='personuser_set', 
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='personuser_set', 
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

