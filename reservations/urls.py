

from django.urls.conf import path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()

urlpatterns = [
    path('reserve', views.reserve, name="reserve"),
    path('fulfillment', views.fulfillment, name="fulfillment")
]

urlpatterns += router.urls

