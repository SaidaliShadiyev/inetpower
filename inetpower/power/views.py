from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def base(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def privacy(request):
    return render(request, 'privacy.html')

def terms(request):
    return render(request, 'terms.html')



