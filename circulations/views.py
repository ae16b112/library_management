from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Circulations
from books.models import Books
from members.models import Members

# Create your views here.
@api_view(['POST'])
def checkout(request):
    book_id=request.data.get("book_id")
    member_id = request.data.get("member_id")
    
    try:
        book=Books.objects.get(pk=book_id)
        member= Members.objects.get(pk=member_id)
    except (Books.DoesNotExist, Members.DoesNotExist):
        return Response({"error":"Book or Member not found"}, status=400)
    
    if book.available_copies<0:
        return Response({"error": "Book not available for checkout"}, status=400)
    #create checkout event
    Circulations.objects.create(book=book, member=member)
    
    #update available copies
    book.available_copies -=1
    book.save()
    
    return Response({"message": "Book checkout successfull"}, status=200)

@api_view(['POST'])
def book_return(request):
    book_id=request.data.get("book_id")
    member_id = request.data.get("member_id")
    
    try:
        circulations = Circulations.objects.filter(book_id=book_id, member_id=member_id, is_returned=False).order_by("-checkout_timestamp")
        if not circulations.exists():
            return Response({"error":"Book not found or not checkoed out"}, status=400)
        
    except Circulations.DoesNotExist:
        return Response({"error":"Book not found or not checkoed out"}, status=400)
    
    #create return event
    circulation=circulations.first()
    circulation.is_returned=True
    circulation.save()
    
    #update available copies
    circulation.book.available_copies +=1
    circulation.book.save()
    
    return Response({"message": "Book returned Successfully"}, status=200)