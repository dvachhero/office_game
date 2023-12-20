from django.shortcuts import render

def admin_menu(request):
    return render(request, 'admin_menu.html')