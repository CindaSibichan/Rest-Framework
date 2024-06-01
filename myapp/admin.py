from django.contrib import admin
from .models import PersonUser
from django.contrib.auth.admin import UserAdmin


# Register your models here.
admin.site.register(PersonUser,UserAdmin)

