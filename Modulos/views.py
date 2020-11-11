from django.shortcuts import render
from django.utils import timezone

# Create your views here.

def principal(request):
    return render(request, 'Modulos/index2.html',{})