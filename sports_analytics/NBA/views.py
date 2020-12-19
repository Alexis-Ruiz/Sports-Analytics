from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

import NBA.populate_database

# Create your views here.

def index(request):
    return render(request, 'NBA/index.html', {})

def update_players(request):
    NBA.populate_database.get_all_players()
    return HttpResponseRedirect(reverse('index'))

def update_teams(request):
    NBA.populate_database.get_all_teams()
    return HttpResponseRedirect(reverse('index'))