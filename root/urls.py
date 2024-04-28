from django.urls import path
from .views import home,contact,about,support,profile

urlpatterns = [
    path('',home),
    path('contact_us',contact),
    path('about_us',about),
    path('support',support),
    path('profile',profile)]