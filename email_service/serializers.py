from rest_framework import serializers
from .models import Sentemails
from .utils import get_time_ago

class SentemailsSerializer(serializers.ModelSerializer):
    time_ago = serializers.SerializerMethodField()

    class Meta:
        model = Sentemails
        fields = ['id', 'subject', 'recipient_email', 'date_created', 'date_updated', 'time_ago']

    def get_time_ago(self, obj):
        timestamp = obj.date_created
        return get_time_ago(timestamp)
