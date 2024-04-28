from django.urls import path
from .views import home,contact,about

urlpatterns = [
    path('',home),
    path('contact_us',contact),
    path('about_us',about)]