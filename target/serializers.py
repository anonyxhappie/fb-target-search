from rest_framework import serializers
from .models import *

class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        exclude = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'