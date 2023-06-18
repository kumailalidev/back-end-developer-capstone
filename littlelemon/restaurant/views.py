from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    DestroyAPIView)
from rest_framework.viewsets import ModelViewSet

from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

def index(request):
    """Index page view"""
    return render(request, 'index.html', {})

class MenuItemView(ListCreateAPIView):
    """Create and view a menu item."""

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(RetrieveUpdateDestroyAPIView, DestroyAPIView):
    """View, update, and delete single menu item."""

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(ModelViewSet):
    """View, update and delete booking item."""

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

