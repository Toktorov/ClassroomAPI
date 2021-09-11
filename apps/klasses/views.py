from rest_framework import viewsets
from apps.klasses.models import Klass
from apps.klasses.serializers import KlassSerializer

# Create your views here.
class KlassAPIViewSet(viewsets.ModelViewSet):
    queryset = Klass.objects.all()
    serializer_class = KlassSerializer
