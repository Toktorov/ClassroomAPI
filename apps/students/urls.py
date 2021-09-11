from rest_framework.routers import DefaultRouter
from apps.students import views
from django.urls import path

router = DefaultRouter()
router.register('students', views.StudentAPIViewSet, basename='students')

urlpatterns = router.urls