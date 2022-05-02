from django.urls import path
from .views import ProviderViewSet, LocationViewSet
from rest_framework import routers
router = routers.SimpleRouter()

router.register(r'locations', LocationViewSet)
router.register(r'providers', ProviderViewSet)
urlpatterns = router.urls
