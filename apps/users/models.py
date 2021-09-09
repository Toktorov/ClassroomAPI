from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.validator import phone_validator


class User(AbstractUser):
    GENDER_CHOICES = (
        ('m', 'Men'),
        ('f', 'Female'),
        ("I don't know", 'Trans'),
    )
    username = models.CharField(max_length=255, unique=True)
    profile = models.ImageField(upload_to='profiles', blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=255)
    phone_number = models.CharField(
        max_length=255,
        validators=[phone_validator],
        blank=True, null=True
    )

    def __str__(self):
        return f"{self.username} -- {self.gender}"
