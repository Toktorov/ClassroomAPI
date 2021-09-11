from rest_framework import viewsets
from apps.courses.models import Course
from apps.courses.serializers import CourseSerializer

# Create your views here.
class CourseAPIViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
