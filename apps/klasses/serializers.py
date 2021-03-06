from rest_framework import serializers
from apps.klasses.models import Klass
from apps.students.serializers import StudentSerializer


class KlassSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many = True, read_only = True)
    
    class Meta:
        model = Klass
        fields = "__all__"

class KlassDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klass
        fields = "__all__"