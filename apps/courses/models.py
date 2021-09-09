from django.db import models


class Course(models.Model):
    OPEN = 'O'
    CLOSE = 'C'
    ESTIMATION = 'E'
    COURSES_CHOICE = (
        (OPEN, 'Open'),
        (CLOSE, 'Close'),
        (ESTIMATION, 'Estimation')
    )
    title = models.CharField(
        max_length=255,
        blank=True, null=True
    )
    status = models.CharField(
        max_length=255,
        choices=COURSES_CHOICE,
    )
    description = models.TextField(
        blank=True, null=True
    )
    period = models.CharField(
        max_length=20,
        default=12,
        blank=True, null=True
    )

    def __str__(self):
        return f"{self.title} -- {self.status}"
