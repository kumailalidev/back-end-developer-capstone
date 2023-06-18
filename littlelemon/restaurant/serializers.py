from rest_framework import serializers

from django.contrib.auth.models import User

from .models import Menu, Booking

class UserSerializer(serializers.ModelSerializer):
    """Serializer for user"""

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class MenuSerializer(serializers.ModelSerializer):
    """Serializer for menu item object."""

    class Meta:
        model = Menu
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    """Serializer for booking object"""

    class Meta:
        model = Booking
        fields = '__all__'