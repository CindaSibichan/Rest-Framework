from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.utils.translation import gettext as _
from.models import PersonUser

# class UserAdmin(BaseUserAdmin):
#     ordering = ['email']  
#     list_display = ['email', 'is_active', 'is_admin']
#     readonly_fields = ('date_joined',)
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         (_('Permissions'), {'fields': ('is_active', 'is_admin')}),
#         (_('Important dates'), {'fields': ('date_joined',)}), 
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2'),
#         }),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)

admin.site.register(PersonUser)
