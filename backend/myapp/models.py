from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext as _
from django.contrib.auth.models import UserManager


# Create your models here.


class PersonUserManager(UserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.pop('email', None)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(email, password, **extra_fields)
class PersonUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, blank=True, null=True)
    otp = models.CharField(max_length=6, blank=True, null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = PersonUserManager()

    def __str__(self):
        return self.email
    
    @classmethod
    def create(cls, email, password=None, **extra_fields):
        email = cls.normalize_email(email)
        user = cls(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
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

