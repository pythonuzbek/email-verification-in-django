from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager, AbstractUser
from django.db.models import CharField, EmailField, BooleanField, DateTimeField


class User(AbstractBaseUser, PermissionsMixin):
    first_name = CharField('first name', max_length=150, blank=True)
    last_name = CharField('last name', max_length=150, blank=True)
    email = EmailField('email address', unique=True)
    is_staff = BooleanField(
        'staff status',
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )
    is_active = BooleanField(
        'active',
        default=True,
        help_text=(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        )
    )
    date_joined = DateTimeField('date joined', auto_now_add=True)
    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['']
