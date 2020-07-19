from rest_framework import serializers
from .models import URL

class URLSerializer(serializers.ModelSerializer):
    """
    This class is serializer class. It defines which data is to convert to json and vice verse.
    """
    class Meta:
        model = URL
        fields = '__all__'