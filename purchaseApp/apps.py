from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PurchaseConfig(AppConfig):
    name = 'purchaseApp'
    verbose_name = (_("مدیریت خریدهای کاربران"))