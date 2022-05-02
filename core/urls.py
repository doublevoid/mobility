from django.urls import path
from .views import ProviderViewSet, LocationViewSet
from rest_framework import routers
router = routers.SimpleRouter()

location_coordinates = LocationViewSet.as_view({
    'get': 'get_by_coordinates',
})

router.register(r'locations', LocationViewSet)
router.register(r'providers', ProviderViewSet)
urlpatterns = [
    path('locations/<str:lat>/<str:lng>', location_coordinates)
]
urlpatterns += router.urls
