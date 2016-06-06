from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
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
    name = models.CharField(max_length=60, blank=False)
    balance = models.PositiveIntegerField(default=0, null=True, blank=True)
    debit_card = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(unique=True, verbose_name='آدرس ایمیل', max_length=255)
    is_staff = models.BooleanField(('staff status'), default=False,
                                   help_text=('Designates whether the user can log into this admin '
                                              'site.'))
    is_active = models.BooleanField(('active'), default=True,
                                    help_text=('Designates whether this user should be treated as '
                                               'active. Unselect this instead of deleting accounts.'))
    #is_superuser = models.BooleanField(('superuser status'), default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def get_short_name(self):
        "Returns the short name for the user."
        return self.name





