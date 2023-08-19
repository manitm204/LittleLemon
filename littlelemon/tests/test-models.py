from django.tests import TestCase
from restaurant.models import *

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(id=101, title="food_name", price=101, inventory=21)
        self.assertEqual(item, "food_name : 69")
