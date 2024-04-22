from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Reservations
from books.models import Books
from members.models import Members
from circulations.models import Circulations

@api_view(['POST'])
def reserve(request):
    book_id=request.data.get("book_id")
    member_id = request.data.get("member_id")
    
    try:
        book=Books.objects.get(pk=book_id)
        member= Members.objects.get(pk=member_id)
    except (Books.DoesNotExist, Members.DoesNotExist):
        return Response({"error":"Book or Member not found"}, status=400)
    
    if book.available_copies>0:
        return Response({"error": "Book is available, no need to reserve"}, status=400)
    
    #create reservation
    Reservations.objects.create(book=book, member=member)
    
    return Response({"message": "Book reserved successfully"}, status=200)


@api_view(['POST'])
def fulfillment(request):
    book_id=request.data.get("book_id")
    member_id = request.data.get("member_id")
    
    try:
        reservations = Reservations.objects.filter(book_id=book_id, member_id=member_id)
        if not reservations.exists():
            return Response({"error":"Reservation not found"}, status=400)
    except Reservations.DoesNotExist:
        return Response({"error":"Reservation not found"}, status=400)
    
    #Update reservation status
    reservation=reservations.first()
    reservation.fulfilled =True
    reservation.save()
    
    # Create checkout event
    Circulations.objects.create(book=reservation.book, member=reservation.member)
    
    # Update available copies
    reservation.book.available_copies -=1
    reservation.book.save()
    
    return Response({"message": "Reservation fullfilled, book issued to member"}, status=200)
    