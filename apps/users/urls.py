from rest_framework.routers import DefaultRouter
from apps.users import views
from django.urls import path


router = DefaultRouter()
router.register('users', views.UserAPIViewSet, basename='users')


urlpatterns = router.urls
