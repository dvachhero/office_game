from django.shortcuts import render
from django.contrib.auth.decorators import login_required
@login_required
def game_menu(request):
    return render(request, 'gamemenu.html')