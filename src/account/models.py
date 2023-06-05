from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from account.managers import AccountManager
from app.models import ShopCard, Shop

class Account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=35, unique=True)
    photo = models.ImageField(upload_to="static/user_photo", blank=True)
    shop_card = models.ForeignKey(to="app.ShopCard", on_delete=models.CASCADE, blank=True,null=True)
    index_shop = models.ForeignKey(Shop, on_delete=models.CASCADE, blank=True,null=True)


    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. " "Unselect this instead of deleting accounts."
        ),
    )

    objects = AccountManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def save(self, *args, **kwargs):

        self.full_clean()

        return super().save(*args, **kwargs)