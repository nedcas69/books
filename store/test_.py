import json
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from store.models import Book
from store.serializers import BookSerializer
from rest_framework import status
from django.contrib.auth.models import User


class BookSerializerTestCase(TestCase):
    def setUp(self):
        self.book_1 = Book.objects.create(name='test book 1', price=24, author_name='Author 1')
        self.book_2 = Book.objects.create(name='test book 2', price=26, author_name='Author 2')
        self.book_3 = Book.objects.create(name='test book 3', price=26, author_name='Author 3')

    def test_ok(self):
        
        data = BookSerializer([self.book_1, self.book_2, self.book_3], many=True).data
        expected_data = [
            {
                'id': self.book_1.id,
                'name': 'test book 1',
                'price': '24.00',
                'author_name': 'Author 1'
            },
            {
                'id': self.book_2.id,
                'name': 'test book 2',
                'price': '26.00',
                'author_name': 'Author 2'
            },
            {
                'id': self.book_3.id,
                'name': 'test book 3',
                'price': '26.00',
                'author_name': 'Author 3'
            },
            
        ]
        self.assertEqual(expected_data, data)


class BooksApiTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_username')
        self.book_1 = Book.objects.create(name='test book 1', price=24, author_name='Author 1')
        self.book_2 = Book.objects.create(name='test book 2', price=26, author_name='Author 2')
        self.book_3 = Book.objects.create(name='test book 3', price=26, author_name='Author 3')

    def test_get(self):    
        url = reverse('book-list')
        print(url)
        response = self.client.get(url)
        serializer_data = BookSerializer([self.book_1, self.book_2, self.book_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
        print(response.data)

    def test_get_search(self):    
        url = reverse('book-list')
        response = self.client.get(url, data={'search': 'Author 1'})
        serializer_data = BookSerializer([self.book_1], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
        

    def test_create(self):    
        self.assertEqual(3, Book.objects.all().count())
        url = reverse('book-list')
        data =  {
                "name": "One Piece Red",
                "author_name": "Oda Eiichiro",
                "price": 1500
            }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.post(url, data = json_data, content_type = "application/json")
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(4, Book.objects.all().count())
    
    def test_update(self):    
        url = reverse('book-detail', args=(self.book_1.id,))
        data =  {
                "name": self.book_1.name,
                "author_name": self.book_1.author_name,
                "price": 500
            }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.put(url, data = json_data, content_type = "application/json")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.book_1.refresh_from_db()
        self.assertEqual(500, self.book_1.price)

    def test_delete(self):    
        self.assertEqual(3, Book.objects.all().count())
        url = reverse('book-detail', args=(self.book_1.id,))
        data =  {
                "name": self.book_1.name,
                "author_name": self.book_1.author_name,
                "price": self.book_1.price
            }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.delete(url, data = json_data, content_type = "application/json")
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(2, Book.objects.all().count())    
        

        