from django.db import models
from UserApp.models import CustomizedUser
from purchaseApp.models import Portion
from django.utils.translation import ugettext_lazy as _

class AccountingModel(models.Model):
    amount = models.PositiveIntegerField(verbose_name='مقدار')
    user = models.ForeignKey(CustomizedUser, on_delete=models.CASCADE, verbose_name='کاربر')
    portion = models.ForeignKey(Portion, blank=True,default=0, null=True, verbose_name='سهم')
    action = models.IntegerField(verbose_name='فعالیت')
    date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')
    class Meta:
        verbose_name = (_("مدیریت تراکنش‌ها"))
        verbose_name_plural = (_("مدیریت تراکنش‌ها"))
    # 0 = Pardakhte Pik
    # 1 = Sharzhe Hesab
    # 2 = Darkhaste Tasviye
    # 3 = Anjame Tasviye

