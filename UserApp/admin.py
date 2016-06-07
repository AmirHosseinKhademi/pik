from django.contrib import admin
from .models import CustomizedUser
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.html import format_html
from django.contrib.admin import AdminSite
from django.contrib.auth import get_user_model

# Register your models here.
class CustomizedUserAdmin(admin.ModelAdmin):
    fields = ('name', 'email', 'password', 'balance', 'debit_card', 'is_active', 'is_staff', 'is_superuser',
              'last_login', 'groups', 'user_permissions')
    list_display = ('name', 'email', 'is_superuser', 'is_active')
    password = ReadOnlyPasswordHashField(label=("Password"))
    list_display_links = ('email','name')
    list_filter = ('is_superuser', 'is_active')
    ordering = ('name', )
    preserve_filters = False
    search_fields = ['name', 'email']
    class Meta:
        verbose_name = "My Model"
        verbose_name_plural = "My Models"
        app_label = "app"

    def save_model(self, request, obj, form, change):
        # Override this to set the password to the value in the field if it's
        # changed.
        if obj.pk:
            orig_obj = get_user_model().objects.get(pk=obj.pk)
            if obj.password != orig_obj.password:
                obj.set_password(obj.password)
        else:
            obj.set_password(obj.password)
        obj.save()

class PikAdminSite(AdminSite):
    site_header = 'Pik Administration'
    site_title = 'Pik Site Admin'

admin_site = PikAdminSite(name='PikAdminSite')

admin_site.register(CustomizedUser, CustomizedUserAdmin)