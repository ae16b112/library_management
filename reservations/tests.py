from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from books.models import Books
from members.models import Members
from .models import Reservations

# Create your tests here.
class ReservationsAPITest(APITestCase):
    def setUp(self):
        self.book=Books.objects.create(book_name="Test Book", total_copies=1, available_copies=0)
        self.member=Members.objects.create(member_name="Test User")
        return super().setUp()
    
    def test_reserve_book(self):
        url = reverse('reserve')
        data={'book_id':self.book.book_id, 'member_id': self.member.member_id}
        response=self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_reserve_book(self):
        url = reverse('reserve')
        data={'book_id':self.book.book_id, 'member_id': self.member.member_id}
        response=self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.book.available_copies +=1
        self.book.save()
        url = reverse('fulfillment')
        data={'book_id':self.book.book_id, 'member_id': self.member.member_id}
        response=self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    
        