from rest_framework.routers import DefaultRouter
from apps.klasses import views
from django.urls import path


router = DefaultRouter()
router.register('klasses', views.KlassAPIViewSet, basename='klasses')

urlpatterns = router.urls