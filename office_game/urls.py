from django.contrib import admin
from django.urls import include, path
from office_game.views import home, logout_view
from game.views import game_menu
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('office_game/admin/', admin.site.urls, name='admin'),
    path('office_game/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('office_game/logout/', logout_view, name='logout'),
    path('office_game/home/', home, name='home'),
    path('office_game/gamemenu/', game_menu, name='gamemenu'),
]
