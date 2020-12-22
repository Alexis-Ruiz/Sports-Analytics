from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='nba_index'),
    path('player/<int:player_id>', views.player_page, name = 'player_page'),
]