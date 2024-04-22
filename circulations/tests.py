from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from books.models import Books
from members.models import Members
from .models import Circulations

# Create your tests here.
class CirculationsAPITest(APITestCase):
    def setUp(self):
        self.book=Books.objects.create(book_name="Test Book", total_copies=8, available_copies=2)
        self.member=Members.objects.create(member_name="Test User")
        return super().setUp()
    
    def test_checkout_book(self):
        url = reverse('checkout')
        data={'book_id':self.book.book_id, 'member_id': self.member.member_id}
        response=self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_return_book(self):
        url = reverse('checkout')
        data={'book_id':self.book.book_id, 'member_id': self.member.member_id}
        response=self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        url=reverse('book_return')
        data={'book_id':self.book.book_id, 'member_id': self.member.member_id}
        response=self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)