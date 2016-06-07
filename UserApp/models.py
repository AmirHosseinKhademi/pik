from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None ,**extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password,*args, **extra_fields):
        return self._create_user(email, password, True,
                                True, **extra_fields)


class CustomizedUser(AbstractBaseUser, PermissionsMixin):
    objects = CustomUserManager()
    name = models.CharField(max_length=60, blank=False, verbose_name='نام و نام خانوادگی')
    balance = models.PositiveIntegerField(default=0, null=True, blank=True, verbose_name='موجودی حساب')
    debit_card = models.PositiveIntegerField(null=True, blank=True, verbose_name='شماره کارت بانکی عضو شبکه شتاب')
    email = models.EmailField(unique=True, verbose_name='آدرس ایمیل', max_length=255)
    is_staff = models.BooleanField(verbose_name='وضعیت کاربر', default=False,
                                   help_text=('آیا کاربر می‌تواند در سایت مدیریتی وارد شود یا خیر؟'))
    is_active = models.BooleanField(verbose_name='فعال', default=True,
                                    help_text=('وضعیت فعال یا غیر فعال بودن کاربر (به جای حذف حساب کاربری، این گزینه را غیر فعال کنید.)'))
    #is_superuser = models.BooleanField(('superuser status'), default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_short_name(self):
        "Returns the short name for the user."
        return self.name

    class Meta:
        verbose_name = (_("مدیریت حساب کاربری کاربران"))
        verbose_name_plural = (_("مدیریت حساب کاربری کاربران"))






