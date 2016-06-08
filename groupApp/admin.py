from django.contrib import admin

from UserApp.admin import admin_site
from groupApp.models import Group
from UserApp.models import CustomizedUser


class GroupAdmin(admin.ModelAdmin):

    fields = ('title', 'admin', 'member', 'creation_datetime')
    list_display = ('title', 'get_admin', 'get_members', 'creation_datetime',)
    list_display_links = ('title', )
    list_filter = ('title', 'member', 'admin' )
    ordering = ('title',)
    readonly_fields = ('creation_datetime',)
    preserve_filters = False

    filter_horizontal = ('member',)

    def get_admin(self, obj):
        return obj.admin.email

    get_admin.short_description = 'مدیر گروه'

    def get_members(self, obj):
        return "\n".join([mem.email for mem in obj.member.all()])

    get_members.short_description = 'اعضای گروه'



admin_site.register(Group, GroupAdmin)
