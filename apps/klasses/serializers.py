from rest_framework import serializers
from apps.klasses.models import Klass


class KlassSerializer(serializers.ModelSerializer):

    class Meta:
        model = Klass
        fields = "__all__"

class KlassDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Klass
        fields = "__all__"