from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MemberViewSet

router = DefaultRouter()
router.register(r'books', MemberViewSet)

urlpatterns =  router.urls