#? Django
from django.db import models
#? Models
from src.utils.models import BasicModel

class Profile(BasicModel):
    """Profile Model. 

    Modelo de perfil tiene datos publicos como biografia y foto de perfil.
    """

    user = models.OneToOneField(
        'users.User', on_delete=models.CASCADE
    )

    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/'
    )

    biography = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return str(self.user) 
