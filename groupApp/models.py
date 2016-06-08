from django.db import models

from UserApp.models import CustomizedUser


class Group(models.Model):
    title = models.CharField(max_length=255)
    admin = models.ForeignKey(CustomizedUser, related_name='group_admin')
    member = models.ManyToManyField(CustomizedUser, blank=True, related_name='group_member')
    creation_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def set_admin(self, user_id):
        self.admin = user_id
        self.save()


# class UserGroup(models.Model):
#     group = models.ForeignKey(Group)
#     member = models.ManyToManyField(CustomizedUser)
#     join_datetime = models.DateTimeField(auto_now_add=True)
