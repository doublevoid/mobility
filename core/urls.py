from django.urls import path
from .views import ProviderViewSet, LocationViewSet

provider_list = ProviderViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

provider_detail = ProviderViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

location_list = LocationViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

location_coordinates = LocationViewSet.as_view({
    'get': 'get_by_coordinates',
})

location_detail = LocationViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})
urlpatterns = [
    path('providers/', provider_list),
    path('providers/<int:id>', provider_detail),
    path('locations/', location_list),
    path('locations/<int:id>', location_detail),
    path('locations/<str:lat>/<str:lng>', location_coordinates)
]
