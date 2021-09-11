from rest_framework import serializers
from apps.courses.models import Course
from apps.klasses.serializers import KlassSerializer


class CourseSerializer(serializers.ModelSerializer):
    klasses = KlassSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = "__all__"