from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
import random

# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})
    return render(request, 'login.html')

@login_required
def home(request):
    return render(request, "home.html")

def generate(request):
    
    activity = random.choice(Activity.objects.all())
    food = random.choice(Food.objects.all())
    drink = random.choice(Drink.objects.all())

    context = {
        "activity" : activity,
        "food" : food,
        "drink" : drink,
    }
    return render(request, "generate.html", context)
