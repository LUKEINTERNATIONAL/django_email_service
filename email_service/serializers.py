from rest_framework import serializers
from .models import Sentemails

class SentemailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sentemails
        fields = ['subject', 'recipient_email', 'date_created', 'date_updated']