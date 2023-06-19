from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    
    def setUp(self):
        '''Setting up test data'''

        # Creating user object
        self.user = get_user_model().objects.create(
            username='jimmydoe',
            email='jimmydoe@email.com',
            password='jimmy123A',
        )

        # Authenticating user
        self.client.force_login(self.user)

        # Creating menu items
        self.menu_items = Menu.objects.bulk_create(
            [
                Menu(title='Greek Salad', price=5, inventory=30),
                Menu(title='Bruschetta', price=6.50, inventory=25),
                Menu(title='Pasta Carbonara', price=6.50, inventory=20),
                Menu(title='Lemon Dessert', price=4.50, inventory=15),
                Menu(title='Burger', price=75, inventory=10),
            ]
        )

    def test_getall(self):
        '''Test: Get all the menu items.'''
        response = self.client.get(reverse('menu'))
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

        