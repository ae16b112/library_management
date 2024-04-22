from django.db import models

# Create your models here.
class Books (models.Model):
    book_id=models.BigAutoField(primary_key=True)
    book_name=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_copies = models.IntegerField(default=0)
    available_copies = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.book_name} __ {self.total_copies} __ {self.available_copies}"