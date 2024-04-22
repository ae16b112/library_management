from django.db import models

# Create your models here.
from django.db import models
from books.models import Books
from members.models import Members

# Create your models here.
class Circulations (models.Model):
    book=models.ForeignKey(Books, on_delete=models.CASCADE, db_index=True)
    member=models.ForeignKey(Members, on_delete=models.CASCADE, db_index=True)
    is_returned = models.BooleanField(default=False)
    checkout_timestamp=models.DateTimeField(auto_now_add=True)
    return_timeout=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.member.member_name}__{self.book.book_name}"