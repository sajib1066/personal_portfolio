from django.urls import path
from .import views


urlpatterns = [
    path('', views.portfolio_page, name='portfolio')
]
