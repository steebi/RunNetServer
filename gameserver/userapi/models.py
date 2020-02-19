from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.core.validators import EmailValidator
from django.contrib.auth.validators import UnicodeUsernameValidator


class Player(AbstractUser):
    """
    This class extends the Abstract User class to leverage Django's default user authentication
    while allowing us to add some additional information
    """
    username_validator = UnicodeUsernameValidator()
    email_validator = EmailValidator()

    username = models.CharField(
        verbose_name=_('username'),
        max_length=150,
        unique=False,
        blank=False,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
    )
    email = models.EmailField(
        verbose_name=_('email address'),
        max_length=255,
        unique=True,
        help_text=_('Required. 255 characters or fewer.'),
        validators=[email_validator],
        error_messages={
            'unique': _("A user with that email address already exists!")
        }
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
