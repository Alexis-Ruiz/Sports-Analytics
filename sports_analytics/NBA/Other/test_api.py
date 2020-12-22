import requests
import json

filename = '/Users/ishaqyousefhajhasan/Desktop/Sports Analytics/sports_analytics/NBA/API_Headers.txt'
api_info = open(filename, 'r')
headers = json.loads(api_info.read())
api_info.close()

def file_stats():
    filename = 'team_info.txt'
    league_info = open(filename, 'r')
    league_json = json.loads(league_info.read())
    league_info.close()

    print('Number of Leagues:\t' + str(len(league_json.keys())))

    total_teams = 0

    for league in league_json:
        teams = league_json[league]['api']['teams']
        num_teams = len(teams)
        print('Number of teams in ' + league + ':\t' + str(num_teams))
        total_teams += num_teams

    print('The Total Number of teams across all leagues are:\t' + str(total_teams))


def get_leagues():
    url = "https://api-nba-v1.p.rapidapi.com/leagues/"

    league_filename = 'league_info.txt'
    league_file = open(league_filename, 'w')
    league_file.seek(0)
    league_file.truncate()

    response = requests.request("GET", url, headers=headers)

    league_file.write(json.dumps(response.json()))
    league_file.close()

    print(response.text)
    print(type(response.text))

def get_teams():
    url = "https://api-nba-v1.p.rapidapi.com/teams/league/"

    filename = 'league_info.txt'
    league_info = open(filename, 'r')
    league_json = json.loads(league_info.read())
    league_info.close()

    leagues = (league_json['api'])['leagues']

    league_team = {}

    for league in leagues:
        print('Processing League:\t' + league + '...')
        response = requests.request("GET", url + league, headers=headers)
        league_team[league] =  response.json()

    team_filename = 'team_info.txt'
    team_file = open(team_filename, 'w')
    team_file.seek(0)
    team_file.truncate()
    team_file.write(json.dumps(league_team, indent=4))
    team_file.close()

def get_players(league):
    url = 'https://api-nba-v1.p.rapidapi.com/players/teamId/'

    filename = 'team_info.txt'
    league_info = open(filename, 'r')
    league_json = json.loads(league_info.read())
    league_info.close()

    teams = league_json[league]['api']['teams']

    team_players = {}

    player_filename = league + '_player_info.txt'
    player_file = open(player_filename, 'w')
    player_file.seek(0)
    player_file.truncate()

    for team in teams:
        teamId = team['teamId']
        response = requests.request("GET", url + teamId, headers=headers)
        team_players[teamId] = response.json()


    player_file.write(json.dumps(team_players, indent=4))
    player_file.close()

def get_players_from_leagues(leagues):
    for league in leagues:
        get_players(league)

def get_player_for_team(league, team_id):
    player_filename = league + '_player_info.txt'
    player_info = open(player_filename, 'r')
    players_json = json.loads(player_info.read())
    player_info.close()

    url = 'https://api-nba-v1.p.rapidapi.com/players/teamId/'
    response = requests.request("GET", url + team_id, headers=headers)

    if team_id in players_json.keys():
        print('Team ID %s already exists', team_id)

    players_json[team_id] = response.json()

    player_filename = league + '_player_info.txt'
    player_file = open(player_filename, 'w')
    player_file.seek(0)
    player_file.truncate()
    player_file.write(json.dumps(players_json, indent=4))
    player_file.close()
    
def get_missing_players(league, teamIds):
    for teamId in teamIds:
        get_player_for_team(str(teamId))





