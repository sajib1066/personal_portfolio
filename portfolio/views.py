from django.shortcuts import render
from .models import Category, Portfolio


def portfolio_page(request):
    portfolio = Portfolio.objects.filter(is_draft=False)
    context = {
        'portfolio': portfolio
    }
    return render(request, 'portfolio/portfolio.html', context)

def portfolio_details(request):
    return render(request, 'portfolio/portfolio-details.html')
