from django.contrib import admin

from UserApp.admin import admin_site
from groupApp.models import Group


class GroupAdmin(admin.ModelAdmin):

    fields = ('title', 'admin', 'member', 'creation_datetime',)
    ordering = ('creation_datetime',)
    readonly_fields = ('creation_datetime',)

    # def get_admin(self, obj):


admin_site.register(Group, GroupAdmin)
