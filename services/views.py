from django.shortcuts import render

def services(request):
    return render(request,'services/services.html')
def service_details(request):
    return render(request,'services/service-details.html')
def quote(request):
    return render(request,'services/get-a-quote.html')