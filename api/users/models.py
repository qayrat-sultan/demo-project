from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _

from users.managers import CustomUserManager


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)
    fullname = models.CharField(max_length=255)

    is_admin = models.BooleanField(default=False)
    stopped = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['fullname']

    class Meta:
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def __str__(self):
        return str(self.id)


class UserToken(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, default=uuid4)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="tokens")
