from django.shortcuts import render


def portfolio_page(request):
    return render(request, 'portfolio/portfolio.html')
