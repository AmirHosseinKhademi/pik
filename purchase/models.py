from django.db import models

# Create your models here.


class Purchase (models.Model):
    title = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    # group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    group_id = models.IntegerField(null=False)
    status = models.BooleanField(default=False)
