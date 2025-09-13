from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    staff = models.BooleanField(default=False)
    student = models.BooleanField(default=False)
    academic_level = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return self.username
 
