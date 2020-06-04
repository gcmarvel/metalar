from django.urls import path
from .views import HomePageView, PortfolioView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('portfolio/<int:service>', PortfolioView.as_view(), name='portfolio'),
]
