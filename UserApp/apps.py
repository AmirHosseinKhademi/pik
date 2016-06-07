from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class UserAppConfig(AppConfig):
    name = 'UserApp'
    verbose_name = (_("مدیریت کاربران"))