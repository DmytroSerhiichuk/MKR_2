from django.test import TestCase
from django.urls import reverse
from .models import Category, Image

# Create your tests here.

class GalleryViewTest(TestCase):

    def setUp(self):
        Category.objects.create(name='Test Category 1')
        Category.objects.create(name='Test Category 2')

    def test_view_context_data(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(len(response.context['categories']), 2)
        self.assertEqual(response.context['categories'][0].name, 'Test Category 1')
        self.assertEqual(response.context['categories'][1].name, 'Test Category 2')
