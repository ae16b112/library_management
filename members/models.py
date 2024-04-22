from django.db import models

# Create your models here.
class Members (models.Model):
    member_id=models.BigAutoField(primary_key=True)
    member_name=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.member_name}"