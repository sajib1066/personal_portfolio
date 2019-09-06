from django.shortcuts import render
from portfolio.models import Portfolio

def home_page(request):
    return render(request, 'home.html')

def about_page(request):
    return render(request, 'about.html')

def service_page(request):
    return render(request, 'services.html')

def contact_page(request):
    return render(request, 'contact.html')
