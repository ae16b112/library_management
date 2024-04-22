from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MemberSerializer
from .models import Members
# Create your views here.

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer