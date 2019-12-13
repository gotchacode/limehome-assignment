
from django.contrib import admin
from django.urls import path, include
from .views import HotelAPIView

urlpatterns = [
    path('list/', HotelAPIView.as_view(), name='hotels-search-api'),
]
