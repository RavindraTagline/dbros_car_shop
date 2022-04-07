from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_field):
        if not email:
            raise ValueError("Users must have an Email Address.")
        if not password:
            raise ValueError("Password is not provided.")
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            **extra_field,)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_field):
        extra_field.setdefault('is_staff', True)
        extra_field.setdefault('is_active', True)
        extra_field.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_field)

    def create_superuser(self, email, password, **extra_field):
        extra_field.setdefault('is_staff', True)
        extra_field.setdefault('is_active', True)
        extra_field.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_field)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        max_length=255, unique=True, verbose_name='username')

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    object = UserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = 'Users'
