

from django.urls.conf import path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()

urlpatterns = [
    path('checkout', views.checkout, name="checkout"),
    path('book_return', views.book_return, name="book_return")
]

urlpatterns += router.urls

