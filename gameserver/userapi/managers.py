from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class PlayerUserManager(BaseUserManager):
    """
    Game User Model Manager to ensure that the email is the unique identifier of each player
    rather than the username.
    """
    def create_user(self, username, email, password, **kwargs):
        """
        Create and save a player for the given username, email and password
        """
        if not email:
            raise ValueError('Email field is mandatory!')
        if not username:
            raise ValueError('Username field is mandatory!')
        if not password:
            raise ValueError('Password field is mandatory!')

        player = self.Model(
            email=self.normalize_email(email),
            username=username,
        )
        player.set_password(password)
        player.save(using=self._db)
        return player

    def create_superuser(self, username, email, password, **kwargs):
        """
        Create and save a super user for the given username, email and password
        """
        if not email:
            raise ValueError('Email field is mandatory!')
        if not username:
            raise ValueError('Username field is mandatory!')
        if not password:
            raise ValueError('Password field is mandatory!')
        player = self.Model(
            email=self.normalize_email(email),
            username=username,
            password=password
        )
        player.is_superuser = True
        player.save()
        return player

