from django.db import models
from groupApp.models import Group
from UserApp.models import CustomizedUser
from django.utils import timezone


class PurchaseManager(models.Manager):
    def create_purchase(self, title, price, group):
        purchase = self.create(title=title, price=price, group=group)
        return purchase


class Purchase (models.Model):
    objects = PurchaseManager()
    title = models.CharField(max_length=20)
    price = models.PositiveIntegerField(default=0)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)


class PortionManager(models.Manager):
    def create_portion(self, user, purchase, amount):
        portion = self.create(user=user, purchase=purchase, amount=amount)
        return portion


class Portion (models.Model):
    objects = PortionManager()
    user = models.ForeignKey(CustomizedUser, on_delete=models.CASCADE)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
