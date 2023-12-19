from django.contrib import admin
from django.urls import include, path
from office_game.views import home, logout_view, rules
from game.views import game_menu
from django.contrib.auth import views as auth_views
from game.views import game, user_results, resultinfo, game_training, result_info_training, game_kmb, resultinfo_kmb, user_results_kmb
from tutorial.views import kmb_view, kmbsubmenu_view, content_view

urlpatterns = [
    path('office_game/admin/', admin.site.urls, name='admin'),
    path('office_game/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('office_game/logout/', logout_view, name='logout'),
    path('office_game/home/', home, name='home'),
    path('office_game/gamemenu/', game_menu, name='gamemenu'),
    path('office_game/game/', game, name='game'),
    path('office_game/rules/', rules, name='rules'),
    path('office_game/resultinfo/', resultinfo, name='resultinfo'),
    path('office_game/user_results/', user_results, name='user_results'),
    path('office_game/kmb/', kmb_view, name='kmb'),
    path('office_game/kmbsubmenu/<int:button_id>/', kmbsubmenu_view, name='kmbsubmenu'),
    path('office_game/content/<int:submenu_id>/', content_view, name='content'),
    path('office_game/gamemenu/', game_menu, name='gamemenu'),
    path('office_game/gametraining/', game_training, name='gametraining'),
    path('office_game/resultinfotraining/', result_info_training, name='resultinfotraining'),
    path('office_game/gamekmb/', game_kmb, name='game_kmb'),
    path('office_game/resultinfokmb/', resultinfo_kmb, name='resultinfo_kmb'),
    path('office_game/user_results_kmb/', user_results_kmb, name='user_results_kmb')
]
