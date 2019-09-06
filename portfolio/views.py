from django.shortcuts import render
from .models import Category, Portfolio


def portfolio_page(request):
    return render(request, 'portfolio/portfolio.html')

def portfolio_details(request, portfolio_id):
    item = Portfolio.objects.get(id=portfolio_id)
    context = {
        'item': item
    }
    return render(request, 'portfolio/portfolio-details.html', context)
