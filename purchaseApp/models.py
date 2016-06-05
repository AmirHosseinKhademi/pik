from django.db import models
from groupApp.models import Group


class Purchase (models.Model):
    title = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
