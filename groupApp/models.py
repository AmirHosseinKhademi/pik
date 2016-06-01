from django.db import models


class Group(models.Model):
    title = models.CharField(max_length=255)
    # admin = models.ForeignKey(Users)
    creation_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def set_admin(self, user):



class UserGroup(models.Model):
    group = models.ForeignKey(Group)
    # member = models.ManyToManyField(User)
    join_datetime = models.DateTimeField(auto_now_add=True)
