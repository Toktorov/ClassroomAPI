from rest_framework.routers import DefaultRouter
from apps.courses import views
from django.urls import path


router = DefaultRouter()
router.register('courses', views.CourseAPIViewSet, basename='courses')


urlpatterns = router.urls