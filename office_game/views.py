from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.db.models import F
import random
from django.urls import reverse
from django.http import HttpResponseRedirect

@login_required
def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('/office_game/login')

@login_required(login_url='login')
def rules(request):
    return render(request, 'rules.html')

