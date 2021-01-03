from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from NBA.models import Player, Team, PlayerGame, TeamGame, PlaysFor
from django.core.paginator import Paginator

from django.conf import settings

import json

CURRENT_SEASON = 2020

# Create your views here.

def index(request):
    # player request parameters
    qd = request.GET.copy()

    player_page = (qd.pop('ppage', [1]))[0]
    player_first_name = (qd.pop('pfname', ['']))[0]
    player_last_name = (qd.pop('plname', ['']))[0]
    team_page = (qd.pop('tpage', [1]))[0]

    # filter based on search parameters if exist and page
    players = Player.objects.all()
    if (player_first_name != None and player_first_name != ''):
        players = players.filter(first_name__contains=player_first_name)
    if (player_last_name != None and player_last_name != ''):
        players = players.filter(last_name__contains=player_last_name)
    player_paginator = Paginator(players, 50)

    teams = Team.objects.all()
    team_paginator = Paginator(teams, 10)

    try:
        player_list = player_paginator.page(player_page)
    except:
        player_list = player_paginator.page(1)

    try:
        team_list = team_paginator.page(team_page)
    except:
        team_list = team_paginator.page(1)

    # reinsert search parameters for team and player filters
    qd.update({'pfname': player_first_name})
    qd.update({'plname': player_last_name})

    return render(request, 'NBA/index.html', {'player_list': player_list, 'team_list': team_list, 'qd': qd})

def player_page(request, player_id):

    context = {}

    try:
        player = Player.objects.get(pk = player_id)
    except:
        return HttpResponseRedirect(reverse('nba_index'))

    try:
        playsfor = PlaysFor.objects.get(player_nba_api_id=player.nba_api_id)
        team = Team.objects.get(nba_api_id=playsfor.team_nba_api_id)
        context['team'] = team
    except:
        pass

    playergames = PlayerGame.objects.filter(nba_api_player_id=player.nba_api_id).order_by('-game_date')
    if len(playergames) > 5:
        playergames = playergames[:5]

    context['player'] = player
    context['recent_games'] = playergames

    return render(request, 'NBA/player_page.html', context)
