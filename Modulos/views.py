from django.http import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from .models import *
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CustomUserForm
from django.contrib.auth import login, authenticate
#from .filters import OrderFilter

def index2(request):
    return render(request, 'index2.html')

def login(request):
    return render(request, 'login.html')

def registrar(request):
    data= {
        'form':CustomUserForm()
    }

    if request.method == 'POST': 
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            #autenticar al usuario y rediridirlo al inicio
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            #login(request, user)
            return redirect(to='index2')
    
    return render(request, 'registration/registrar.html', data)

def logout(request):
    return render(request, 'logout')

def reset(request):
    return render(request, 'password_reset.html')

def Planes(request):
    return render(request, 'Planes.html')