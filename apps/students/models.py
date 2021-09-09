from django.db import models
from apps.users.models import User
from apps.klasses.models import Klass


class Student(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='students'
    )
    last_name = models.CharField(
        max_length=255,
        blank=True, null=True
    )
    first_name = models.CharField(
        max_length=255,
        blank=True, null=True
    )
    klass = models.ForeignKey(
        Klass,
        on_delete=models.SET_NULL,
        related_name='students',
        null=True, blank=True,
    )
    mother_first_name = models.CharField(
        max_length=255,
        blank=True, null=True
    )
    mother_last_name = models.CharField(
        max_length=255,
        blank=True, null=True
    )
    father_first_name = models.CharField(
        max_length=255,
        blank=True, null=True
    )
    father_last_name = models.CharField(
        max_length=255,
        blank=True, null=True
    )


