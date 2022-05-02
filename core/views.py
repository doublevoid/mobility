from rest_framework.response import Response
from rest_framework import status, viewsets
from .serializers import ProviderSerializer, LocationSerializer
from .models import Provider, Location
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class ProviderViewSet(viewsets.ModelViewSet):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        action = self.action
        if (action == 'list'):
            context['fields'] = ('name', 'email', 'phone_number', 'language', 'currency')
        elif (action == 'create'):
            context['fields'] = ('id', 'name', 'email', 'phone_number', 'language', 'currency')
        elif (action == 'update'):
            context['fields'] = ('name', 'email', 'phone_number', 'language', 'currency')
        elif (action == 'retrieve'):
            context['fields'] = ('name', 'email', 'phone_number', 'language', 'currency')
        return context

    @method_decorator(cache_page(30 * 30))
    def dispatch(self, *args, **kwargs):
        return super(ProviderViewSet, self).dispatch(*args, **kwargs)


class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        action = self.action
        if (action == 'list'):
            context['fields'] = ('id', 'name', 'price', 'provider', 'provider_detail')
        elif (action == 'get_by_coordinates'):
            context['fields'] = ('name', 'price', 'provider', 'provider_detail')
        elif (action == 'create'):
            context['fields'] = ('id', 'price', 'geojson', 'lat', 'lng', 'provider', 'name')
        elif (action == 'update'):
            context['fields'] = ('price', 'geojson', 'lat', 'lng', 'provider', 'name')
        elif (action == 'retrieve'):
            context['fields'] = ('name', 'geojson')
        return context

    def get_by_coordinates(self, request, lat, lng):
        item = Location.objects.all().filter(lat=lat, lng=lng)
        serializer = LocationSerializer(item, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    @method_decorator(cache_page(30 * 30))
    def dispatch(self, *args, lat=None, lng=None, **kwargs):
        return super(LocationViewSet, self).dispatch(*args, lat, lng, **kwargs)

# Create your views here.
