from rest_framework import serializers
from .models import Provider
from .models import Location
from collections import OrderedDict
from .utils.dynamic_field_serializer import DynamicFieldSerializer


class ProviderSerializer(DynamicFieldSerializer):
    class Meta:
        model = Provider
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response


class LocationSerializer(DynamicFieldSerializer):
    provider_detail = ProviderSerializer(source='provider', context={'fields': ['name']})

    class Meta:
        model = Location
        fields = ('__all__')
