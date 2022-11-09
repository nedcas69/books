from django.urls import reverse
from rest_framework.test import APITestCase


class BooksApiTestCase(APITestCase):
    def test_get(self):
        url = reverse('book-list')
        print(url)
        response = self.client.get(url)
        print(response.data)