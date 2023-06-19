from django.test import TestCase
from django.urls import reverse

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    
    def setUp(cls):
        cls.menu_item = Menu.objects.create(
            title="IceCream",
            price=25,
            inventory=80
        )
        print(cls.menu_item)

    def test_getall(self):
        pass

        