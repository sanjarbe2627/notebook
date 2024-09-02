from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")

        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save()
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(PermissionsMixin, AbstractBaseUser):
    """ User Model """
    email = models.EmailField(help_text=_("User email field"), max_length=255, unique=True)
    first_name = models.CharField(help_text=_('User name'), max_length=30, null=True, blank=True)
    last_name = models.CharField(help_text=_('User lastname'), max_length=30, null=True, blank=True)
    avatar = models.ImageField(upload_to="users", null=True, blank=True)

    instagram = models.URLField(null=True, blank=True, help_text=_("User instagram link"))
    twitter = models.URLField(null=True, blank=True, help_text=_("User twitter link"))
    facebook = models.URLField(null=True, blank=True, help_text=_("User facebook link"))

    is_verified = models.BooleanField(default=False, null=False, blank=False)
    is_active = models.BooleanField(_("is_active"), default=True)
    is_staff = models.BooleanField(_("is_staff"), default=False)
    date_joined = models.DateTimeField(_("Date Register"), auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return "#%s - %s - %s" % (self.pk, self.email, self.first_name)

    class Meta:
        verbose_name_plural = "Users"
        ordering = ['-date_joined']
