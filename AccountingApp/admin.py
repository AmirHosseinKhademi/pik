from django.contrib import admin
from UserApp.admin import admin_site
from .models import AccountingModel
# Register your models here.

class AccountingAdmin(admin.ModelAdmin):
    fields = ('amount', 'user', 'action', 'portion')
    list_display = ('user_name', 'amount', 'action', 'portion', 'date')
    list_display_links = ('user_name', )
    list_filter = ('user', )
    ordering = ('user', )
    preserve_filters = False

    def user_name(self, obj):
        return obj.user.email

    user_name.short_description = 'ایمیل کاربر'

    def get_portion(self, obj):
        if obj.portion:
            return obj.portion.purchase.title
        else:
            return None

    get_portion.short_description = 'نام خرید مربوط به سهم'

admin_site.register(AccountingModel, AccountingAdmin)