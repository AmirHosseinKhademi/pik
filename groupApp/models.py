from django.db import models

from UserApp.models import CustomizedUser
from django.utils.translation import ugettext_lazy as _


class Group(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان گروه')
    admin = models.ForeignKey(CustomizedUser, related_name='group_admin', verbose_name='مدیر گروه ')
    member = models.ManyToManyField(CustomizedUser, blank=True, related_name='group_member', verbose_name='اعضای گروه')
    creation_datetime = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد گروه')

    def __str__(self):
        return self.title

    def set_admin(self, user_id):
        self.admin = user_id
        self.save()

    class Meta:
        verbose_name = (_("مدیریت گروه‌ها"))
        verbose_name_plural = (_("مدیریت گروه‌ها"))

# class UserGroup(models.Model):
#     group = models.ForeignKey(Group)
#     member = models.ManyToManyField(CustomizedUser)
#     join_datetime = models.DateTimeField(auto_now_add=True)
