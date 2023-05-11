from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db.models import BooleanField, CharField, DateTimeField, EmailField, Model, IntegerField, \
    PositiveIntegerField, TextField

from shared.models import CustomUserManager, BaseDateModel


class User(AbstractBaseUser, PermissionsMixin):
    first_name = CharField('first name', max_length=150, blank=True)
    last_name = CharField('last name', max_length=150, blank=True)
    email = EmailField('email address', unique=True)
    balance = PositiveIntegerField('balance', default=0)
    is_staff = BooleanField(
        'staff status',
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )
    is_active = BooleanField(
        'active',
        default=False,
        help_text=(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        )
    )
    date_joined = DateTimeField('date joined', auto_now_add=True, editable=False)
    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

# nulled full template
# crack

# class Notification(BaseDateModel):
#     title = CharField(max_length=255)
#

class Settings(Model):
    phone = CharField(max_length=25)
    email = EmailField(max_length=125)
    about_us = CharField(max_length=512)


class Faq(Model):
    question = CharField(max_length=255)
    text = TextField()
