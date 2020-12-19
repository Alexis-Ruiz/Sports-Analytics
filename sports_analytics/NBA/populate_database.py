import json  # to process json objects
import os
import django

from NBA.models import Player, Team

# nba-api libraries
from nba_api.stats.static import players
from nba_api.stats.static import teams

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sporting_analytics.settings")
django.setup()

def get_all_teams():
    # call request to get team data
    Teams = teams.get_teams()

    # write data to file
    for team in Teams:
        try:
            oldteam = Team.objects.get(id = team['id'])
        except Team.DoesNotExist:
            newTeam = Team(full_name = team['full_name'],
                           abbreviation = team['abbreviation'],
                           nickname = team['nickname'],
                           city = team['city'],
                           state = team['state'],
                           year_founded = team['year_founded'])
            newTeam.id = team['id']
            newTeam.save()
            continue

        oldteam.full_name = team['full_name'],
        oldteam.abbreviation = team['abbreviation'],
        oldteam.nickname = team['nickname'],
        oldteam.city = team['city'],
        oldteam.state = team['state'],
        oldteam.year_founded = team['year_founded']
        oldteam.save()

# create file of player and store his prev num_years stats
def get_all_players():

    Players = players.get_players()

    for player in Players:
        try:
            oldplayer = Player.objects.get(id = player['id'])
        except Player.DoesNotExist:
            # player isn't in DB
            newPlayer = Player(full_name = player['full_name'],
                               first_name = player['first_name'],
                               last_name = player['last_name'],
                               is_active = player['is_active'])
            newPlayer.id = player['id']
            newPlayer.save()
            continue

        oldplayer.full_name = player['full_name']
        oldplayer.first_name = player['first_name']
        oldplayer.last_name = player['last_name']
        oldplayer.is_active = player['is_active']
        oldplayer.save()