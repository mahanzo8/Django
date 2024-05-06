from django.urls import path
from .views import services,service_details,quote
app_name = 'services'

urlpatterns = [
    path('',services,name='services'),
    path('service-details/',service_details,name='service-detailes'),
    path('get-a-quote/',quote,name='quote')
]

