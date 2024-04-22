from django.db import models

# Create your models here.
from django.db import models
from books.models import Books
from members.models import Members
from circulations.models import Circulations
from django.core.exceptions import ValidationError
# Create your models here.
class Reservations (models.Model):
    book=models.ForeignKey(Books, on_delete=models.CASCADE, db_index=True)
    member=models.ForeignKey(Members, on_delete=models.CASCADE, db_index=True)
    fulfilled = models.BooleanField(default=False)
    timestamp=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.member.member_name}__{self.book.book_name}"
    
