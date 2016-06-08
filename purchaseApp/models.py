from django.db import models
from groupApp.models import Group
from UserApp.models import CustomizedUser
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class PurchaseManager(models.Manager):
    def create_purchase(self, title, price, group):
        purchase = self.create(title=title, price=price, group=group)
        return purchase


class Purchase (models.Model):
    objects = PurchaseManager()
    title = models.CharField(max_length=20, verbose_name='عنوان خرید')
    price = models.PositiveIntegerField(default=0, verbose_name='قیمت')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='گروه')
    status = models.BooleanField(default=False, verbose_name='وضعیت پرداخت اعضا')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='زمان ایجاد')
    updated_at = models.DateTimeField(default=timezone.now, verbose_name='زمان به روزرسانی')
    class Meta:
        verbose_name = (_("مدیریت خرید کاربران"))
        verbose_name_plural = (_("مدیریت خرید کاربران"))

    def __str__(self):
        return self.title

class PortionManager(models.Manager):
    def create_portion(self, user, purchase, amount):
        portion = self.create(user=user, purchase=purchase, amount=amount)
        return portion


class Portion (models.Model):
    objects = PortionManager()
    user = models.ForeignKey(CustomizedUser, on_delete=models.CASCADE, verbose_name='کاربر')
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, verbose_name='خرید')
    amount = models.PositiveIntegerField(default=0, verbose_name='سهم کاربر')
    status = models.BooleanField(default=False, verbose_name='وضعیت پرداخت')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='زمان ایجاد')
    updated_at = models.DateTimeField(default=timezone.now, verbose_name='زمان به روزرسانی')
    def __str__(self):
        return self.purchase.title

    class Meta:
        verbose_name = (_("مدیریت سهم خرید کاربران"))
        verbose_name_plural = (_("مدیریت سهم خرید کاربران"))
