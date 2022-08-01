from django import views
from django.contrib import admin
from django.urls import URLPattern, path, include

from .views import home, orders

urlpatterns = [
    path("", home, name="home"),
    path("order/", orders, name="order_url")
]
