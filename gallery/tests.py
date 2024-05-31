from django.test import TestCase
from django.urls import reverse
from .models import Category, Image
from django.core.files.uploadedfile import SimpleUploadedFile
import datetime

# Create your tests here.

class GalleryViewTest(TestCase):

    def setUp(self):
        Category.objects.create(name='Test Category 1')
        Category.objects.create(name='Test Category 2')

    def test_view_status_code(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)

    def test_view_context_data(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(len(response.context['categories']), 2)
        self.assertEqual(response.context['categories'][0].name, 'Test Category 1')
        self.assertEqual(response.context['categories'][1].name, 'Test Category 2')


class ImageViewTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.image = Image.objects.create(
            title='Test Image',
            image=SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg'),
            created_date=datetime.date.today(),
            age_limit=0
        )
        self.image.categories.add(self.category)

    def test_view_status_code(self):
        response = self.client.get(reverse('image_detail', args=[self.image.id]))
        self.assertEqual(response.status_code, 200)

    def test_view_context_data(self):
        response = self.client.get(reverse('image_detail', args=[self.image.id]))
        self.assertEqual(response.context['image'].title, 'Test Image')
