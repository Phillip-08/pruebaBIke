from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from .models import *
from django.shortcuts import render
#from .filters import OrderFilter

def index2(request):
    return render(request, 'index2.html')

def login(request):
    return render(request, 'login.html')

def registro(request):
    return render(request, 'registro.html')

def logout(request):
    return render(request, 'logout')