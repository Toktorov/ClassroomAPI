from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.courses.models import Course


class Klass(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='klasses',
    )
    klass_id = models.CharField(
        max_length=255,
        blank=True, null=True
    )

    def __str__(self):
        return f"{self.course.title} -- {self.klass_id}"


@receiver(post_save, sender=Klass)
def create_klass_id(sender, instance, created, *args, **kwargs):
    if created:
        instance.klass_id = f"{instance.course.title}-{instance.id}"
        instance.save()
