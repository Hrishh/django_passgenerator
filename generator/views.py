from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request,'generator/home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('Uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPRSTUVWXYZ'))
    if request.GET.get('Number'):
        characters.extend(list('1234567890'))
    if request.GET.get('Special Characters'):
        characters.extend(list('%^&*$#@(){}[]\|?/<>'))


    thepassword = ''
    length=int(request.GET.get('length'))
    for x in range(length):
        thepassword+= random.choice(characters)
    if request.GET.get('return'):
        return render(request, 'generator/home.html')
    return render(request,'generator/password.html' , {'password': thepassword})


