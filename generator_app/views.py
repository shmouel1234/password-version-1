from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request, 'generator_app/home.html' )

def about(request):
    return render(request, 'generator_app/about.html')

def password(request):
    myPassword=''
    characters= list('abcdefghijklmnopqrstuvwxyz')
    length =int(request.GET.get('length'))
    if request.GET.get('uppercase'):
          characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get('numbers'):
          characters.extend(list("0123456789"))
    if request.GET.get('specials'):
          characters.extend(list("~!@#$%^&*()_+{}[]:<>?"))
    for x in range(length):
          myPassword += random.choice(characters)
    return render(request, 'generator_app/password.html', {"password":myPassword})
    
    
