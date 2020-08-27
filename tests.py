from django.test import TestCase
from .models import Item

# Create your tests here.
class TestItem(TestCase):

    def setUp(self):
        a = Item.objects.create(name='Vliegtuig')

    def test_object(self):
        a = Item.objects.get(name='Vliegtuig')
        self.assertIsInstance(a,Item)