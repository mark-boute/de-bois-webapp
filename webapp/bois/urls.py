from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='bois-home'),
    path('barfcompetitie', views.barfcompetitie, name='bois-barfcompetitie'),
    path('quotes', views.quotes, name='bois-quotes'),
]
