from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin


# Create your models here.
class PersonUser(AbstractUser):
    username = None
    otp = models.CharField(max_length=6, blank=True, null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_query_name="%(app_label)s_%(class)s",
        related_name="+",
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_query_name="%(app_label)s_%(class)s",
        related_name="+",
        help_text=_('Specific permissions for this user.'),
    )
    # @property
    # def is_staff(self):
    #     return self.is_admin

    # @property
    # def is_superuser(self):
    #     return self.is_admin

    # def has_perm(self, perm, obj=None):
    #     return self.is_admin

    # def has_module_perms(self, app_label):
    #     return self.is_admin
    


    
# class PersonUser(AbstractUser):
#     otp = models.CharField(max_length=6 ,null=True, blank=True)

    # groups = models.ManyToManyField(
    #     Group,
    #     related_name='personuser_set', 
    #     blank=True,
    #     help_text='The groups this user belongs to.',
    #     verbose_name='groups',
    # )
    # user_permissions = models.ManyToManyField(
    #     Permission,
    #     related_name='personuser_set', 
    #     blank=True,
    #     help_text='Specific permissions for this user.',
    #     verbose_name='user permissions',
    # )

