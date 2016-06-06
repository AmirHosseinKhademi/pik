from django.db import models
from groupApp.models import Group
from UserApp.models import CustomizedUser


class Purchase (models.Model):
    title = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)


class Portion (models.Model):
    user = models.ForeignKey(CustomizedUser, on_delete=models.CASCADE)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
