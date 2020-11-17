from django.shortcuts import render

def home(request):
    return render(request, 'bois/home.html', {'title': 'Home'})

def barfcompetitie(request):
    return render(request, 'bois/barfcompetitie.html', {'title': 'Barfcompetitie'})

def quotes(request):
    return render(request, 'bois/quotes.html', {'title': 'Quotes'})