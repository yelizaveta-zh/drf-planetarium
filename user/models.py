from django.contrib.auth.models import AbstractUser, UserManager
#from django.db import models


class User(AbstractUser):
    pass

#class User(AbstractUser):
#    username = None
#    email = models.EmailField(unique=True)

#    objects = UserManager()

#    USERNAME_FIELD = "email"
#    REQUIRED_FIELDS = []

#    def __str__(self):
#        return self.email
