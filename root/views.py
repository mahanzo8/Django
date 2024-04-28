from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'root/index.html')

def contact(request):
    return render(request,'root/contact.html')

def about(request):
    return render(request,'root/about.html')

def support(request):
    return render(request,'root/support.html')

def profile(request):
    return render(request,'root/profile.html')
# Create your views here.
