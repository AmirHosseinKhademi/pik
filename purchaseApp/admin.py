from django.contrib import admin
from UserApp.admin import admin_site
from .models import Purchase, Portion
# Register your models here.

class PurchaseAdmin(admin.ModelAdmin):
    fields = ('title', 'price', 'group', 'status', 'created_at', 'updated_at')
    list_display = ('title', 'price', 'get_group', 'status', 'created_at', 'updated_at')
    list_display_links = ('get_group','title' )
    list_filter = ('title','group' )
    ordering = ('title', )
    preserve_filters = False

    def get_group(self, obj):
        return obj.group.title

    get_group.short_description = 'گروه'


class PortionAdmin(admin.ModelAdmin):
    fields = ('user', 'purchase', 'amount', 'status', 'created_at', 'updated_at')
    list_display = ('user_name', 'get_purchase', 'amount', 'status', 'created_at', 'updated_at')
    list_display_links = ('user_name', 'get_purchase' )
    list_filter = ('user','purchase', 'status' )
    ordering = ('user', )
    preserve_filters = False

    def user_name(self, obj):
        return obj.user.email

    user_name.short_description = 'ایمیل کاربر'

    def get_purchase(self, obj):
        return obj.purchase.title

    get_purchase.short_description = 'عنوان خرید'


admin_site.register(Purchase, PurchaseAdmin)
admin_site.register(Portion, PortionAdmin)