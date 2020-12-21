from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='nba_index'),
    path('player/<int:player_id>', views.player_page, name = 'player_page'),


    # URLs that populate the database
    path('update/players', views.update_players),
    path('update/teams', views.update_teams),
]