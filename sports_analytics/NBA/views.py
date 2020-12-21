from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from NBA.models import Player, Team
from django.core.paginator import Paginator

import NBA.populate_database

# Create your views here.

def index(request):
    # player request parameters
    player_page = request.GET.get('ppage', 1)
    player_first_name = request.GET.get('pfname', None)
    player_last_name = request.GET.get('plname', None)
    player_is_active = request.GET.get('pisactive', None)

    # filter based on search parameters if exist and page
    players = Player.objects.all()
    if (player_first_name != None and player_first_name != ''):
        players = players.filter(first_name__contains=player_first_name)
    if (player_last_name != None and player_last_name != ''):
        players = players.filter(first_name__contains=player_last_name)
    if (player_is_active != None and player_is_active != ''):
        players = players.filter(first_name__contains=player_is_active)
    player_paginator = Paginator(players, 50)

    teams = Team.objects.all()
    team_paginator = Paginator(teams, 10)
    team_page = request.GET.get('tpage', 1)

    try:
        player_list = player_paginator.page(player_page)
    except PageNotAnInteger:
        player_list = player_paginator.page(1)
    except EmptyPage:
        player_list = player_paginator.page(paginator.num_pages)

    try:
        team_list = team_paginator.page(team_page)
    except PageNotAnInteger:
        team_list = team_paginator.page(1)
    except EmptyPage:
        team_list = team_paginator.page(paginator.num_pages)

    return render(request, 'NBA/index.html', {'player_list': player_list, 'team_list': team_list})

def player_page(request, player_id):
    try:
        player = Player.objects.get(pk = player_id)
    except:
        return HttpResponseRedirect(reverse('nba_index'))

    return render(request, 'NBA/player_page.html', {'player': player})

def update_players(request):
    NBA.populate_database.get_all_players()
    return HttpResponseRedirect(reverse('nba_index'))

def update_teams(request):
    NBA.populate_database.get_all_teams()
    return HttpResponseRedirect(reverse('nba_index'))