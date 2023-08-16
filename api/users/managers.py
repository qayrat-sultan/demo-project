from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username=None, fullname=None, password=None):
        if not username:
            raise ValueError('The User username must be set.')

        user = self.model(
            username=username,
            fullname=fullname
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username=None, fullname=None, password=None):
        user = self.create_user(
            username=username,
            fullname=fullname,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
