from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def portfolio(request):
    return render(request, 'portfolio.html')
def elements(request):
    return render(request, 'elements.html')
def portfolio_details(request):
    return render(request, 'portfolio_details.html')
def blog(request):
    return render(request, 'blog.html')
def singleblog(request):
    return render(request, 'singleblog.html')
def contact(request):
    return render(request, 'contact.html')