from django.db import models
from .managers import UserManager
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class User(AbstractBaseUser):
    class Meta:
        verbose_name = 'کاربر وبلاگ'
        verbose_name_plural = 'کاربرهای وبلاگ'
    username = models.CharField(verbose_name='نام کاربری', max_length=20, unique=True)
    first_name = models.CharField(verbose_name='نام', max_length=100, null=True, blank=True)
    last_name = models.CharField(verbose_name='نام خانوادگی', max_length=100)
    email = models.EmailField(verbose_name='پست الکتریکی', unique=True, null=True, blank=True)
    # phone = PhoneField(verbose_name='تلفن همراه', blank=True,
    #                    help_text='Contact Phone Number!', unique=True)
    phone = models.PositiveBigIntegerField(unique=True, verbose_name='تلفن همراه')
    image = models.ImageField(verbose_name='تصویر', upload_to='img/users/%Y/%m/', null=True, blank=True)
    start_time = models.DateField(verbose_name='زمان ثبت نام', auto_now_add=True)
    login_time = models.DateField(verbose_name='زمان آخرین بازدید', auto_now=True, blank=True)
    password = models.CharField(verbose_name='کلمه عبور', max_length=300)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD ='username'
    REQUIRED_FIELDS = ['last_name', 'phone']

    def __str__(self):
        if self.first_name:
            return self.first_name + ' ' + self.last_name
        else:
            return self.last_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin