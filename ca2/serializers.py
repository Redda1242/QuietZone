from rest_framework import serializers
from .models import QuietZone


class QuietZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuietZone
        fields = ['id', 'name', 'description', 'location', 'noise_level', 'average_rating', 'tags']
