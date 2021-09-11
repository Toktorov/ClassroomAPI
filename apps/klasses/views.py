from rest_framework import viewsets
from apps.klasses.models import Klass
from apps.klasses.serializers import KlassSerializer, KlassDetailSerializer

# Create your views here.
class KlassAPIViewSet(viewsets.ModelViewSet):
    queryset = Klass.objects.all()
    serializer_class = KlassSerializer

    def get_serializer_class(self):
        if self.action in ['retrieve']:
            return KlassDetailSerializer
        return self.serializer_class
