from django.db import models

from UserApp.models import CustomizedUser


class Group(models.Model):
    title = models.CharField(max_length=255)
    admin = models.ForeignKey(CustomizedUser)
    creation_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def set_admin(self, user):
        self.admin = user
        self.save()

class UserGroup(models.Model):
    group = models.ForeignKey(Group)
    member = models.ManyToManyField(CustomizedUser)
    join_datetime = models.DateTimeField(auto_now_add=True)
