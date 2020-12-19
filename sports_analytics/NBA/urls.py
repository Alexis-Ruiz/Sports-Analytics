from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),


    # URLs that populate the database
    path('update/players', views.update_players),
    path('update/teams', views.update_teams),
]