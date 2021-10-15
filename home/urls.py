from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("home/contact", views.contact, name="contact"),
]
