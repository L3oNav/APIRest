"""User Model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Models
from src.utils.models import BasicModel

class User(BasicModel, AbstractUser):
    """User model.

    Extiende de django abstract User, 
    cambiando username a email y a se añade nuevos campos.
    """

    email = models.EmailField(
            "Email address",
            unique=True,
            error_messages={
                "unique":"Un usuario ya existe con ese correo."
            }
    
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_client = models.BooleanField(
        'client status',
        default=True,
        help_text=('help easily distinguish users and perform queries', 'Clients are the main type user.')
    )
    is_verified = models.BooleanField('verified', default=False, help_text=(
        'set to true when the user have verified its email address'))

    def __str__(self):
        return self.username

    def get_short_name(self):
        """return first name"""
        return self.username
