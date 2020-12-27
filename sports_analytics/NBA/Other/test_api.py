#   Created by: Ishaq Yousef Haj Hasan
#   Created date: 24-12-2020
#   Last Modified: 24-12-2020
#
#   In this file I am defining functions thar run calls to the API
#   I will refer to this file when populating the database
#
#

DEBUG = True

def log_console(s):
    if DEBUG:
        print(s)

# nba-api endpoints
from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import CommonPlayerInfo, TeamInfoCommon, TeamGameLog, PlayerGameLog


import requests
import json
import time
import csv
import os

season_types = ['Regular Season', 'Playoffs']

# read json object from file
def read_json_from_file(filename):
    file = open(filename, 'r')
    obj = json.loads(file.read())
    file.close()
    return obj

# clear the file and write content into it
def clean_and_write_file(filename, content):
    # open and clear file
    fileio = open(filename, 'w')
    fileio.seek(0)
    fileio.truncate()
    # write list to file
    fileio.write(content)
    # close
    fileio.close()


# get all the teams with all the combined attributes
def get_all_teams(start=0, end=None):
    result_teams = []

    # get all teams from NBA-API
    nba_api_teams = teams.get_teams()

    if(end == None):
        end = len(nba_api_teams)

    counter = start

    # for every team from nba-api
    for idx in range(start, end):
        nba_api_team = nba_api_teams[idx]
        log_console('Processing\t' + nba_api_team['full_name'] + '\t' + str(idx) + '/' + str(len(nba_api_teams)))

        # create nba_api_id attribute
        nba_api_team['nba_api_id'] = nba_api_team['id']

        common_info = TeamInfoCommon(league_id='00', team_id=nba_api_team['id'])
        common_info = common_info.get_dict()
        common_info = common_info['resultSets']
        common_info = filter(lambda R: R['name'] == 'TeamInfoCommon', common_info)
        common_info = list(common_info)

        # list should be of size one after filtering
        if len(common_info) > 0:
            common_info = common_info[0]
            common_info_kv_mapping = {}
            attributes = common_info['headers']
            data = common_info['rowSet'][0]

            for idx in range(len(attributes)):
                common_info_kv_mapping[attributes[idx]] = data[idx]

            nba_api_team['confernce'] = common_info_kv_mapping['TEAM_CONFERENCE']
            nba_api_team['division'] = common_info_kv_mapping['TEAM_DIVISION']
            nba_api_team['min_year'] = common_info_kv_mapping['MIN_YEAR']
            nba_api_team['max_year'] = common_info_kv_mapping['MAX_YEAR']

        else:
            # no result returned
            nba_api_team['conference'] = ''
            nba_api_team['division'] = ''
            nba_api_team['min_year'] = ''
            nba_api_team['max_year'] = ''

        # store team in result list
        result_teams.append(nba_api_team)
        counter += 1
        time.sleep(.8)

    return result_teams

def get_all_players(start=0, end=None):
    result_players = []

    # get all players from nba_api
    nba_api_players = players.get_players()

    if (end == None):
        end = len(nba_api_players)

    # unnecessary just used for the log_console message
    counter = start

    for idx in range(start, end):
        nba_api_player = nba_api_players[idx]

        log_console('Processing\t' + nba_api_player['full_name'] + '\t' + str(idx) + '/' + str(len(nba_api_players)))

        # create nba_api_id attribute
        nba_api_player['nba_api_id'] = nba_api_player['id']

        # get common player info object in usable dictionary format
        try:
            common_info = CommonPlayerInfo(player_id=nba_api_player['id'])
            common_info = common_info.get_dict()
            common_info = common_info['resultSets']
            common_info = filter(lambda R: R['name'] == 'CommonPlayerInfo', common_info)
            common_info = list(common_info)
        except:
            common_info = []

        # list should be of size 1 after filtering
        if len(common_info) > 0:
            common_info = common_info[0]
            common_info_kv_mapping = {}
            attributes = common_info['headers']
            data = common_info['rowSet'][0]

            for idx in range(len(attributes)):
                common_info_kv_mapping[attributes[idx]] = data[idx]

            nba_api_player['birth_date'] = common_info_kv_mapping['BIRTHDATE']
            nba_api_player['school'] = common_info_kv_mapping['SCHOOL']
            nba_api_player['country'] = common_info_kv_mapping['COUNTRY']
            nba_api_player['height'] = common_info_kv_mapping['HEIGHT']
            nba_api_player['weight'] = common_info_kv_mapping['WEIGHT']
            nba_api_player['season_exp'] = common_info_kv_mapping['SEASON_EXP']
            nba_api_player['jersey_number'] = common_info_kv_mapping['JERSEY']
            nba_api_player['position'] = common_info_kv_mapping['POSITION']
            nba_api_player['date_from'] = common_info_kv_mapping['FROM_YEAR']
            nba_api_player['date_to'] = common_info_kv_mapping['TO_YEAR']
            nba_api_player['is_d_league'] = True if common_info_kv_mapping['DLEAGUE_FLAG'] == 'Y' else False
            nba_api_player['is_nba'] = True if common_info_kv_mapping['NBA_FLAG'] == 'Y' else False
            nba_api_player['has_played_games'] = True if common_info_kv_mapping['GAMES_PLAYED_FLAG'] == 'Y' else False
            nba_api_player['draft_year'] = common_info_kv_mapping['DRAFT_YEAR']
            nba_api_player['draft_round'] = common_info_kv_mapping['DRAFT_ROUND']
            nba_api_player['draft_number'] = common_info_kv_mapping['DRAFT_NUMBER']
            nba_api_player['nba_api_team_id'] = common_info_kv_mapping['TEAM_ID']

        else:
            # Set empty values
            nba_api_player['birth_date'] = None
            nba_api_player['school'] = ''
            nba_api_player['country'] = ''
            nba_api_player['height'] = ''
            nba_api_player['weight'] = ''
            nba_api_player['season_exp'] = ''
            nba_api_player['jersey_number'] = ''
            nba_api_player['position'] = ''
            nba_api_player['date_from'] = None
            nba_api_player['date_to'] = None
            nba_api_player['is_d_league'] = False
            nba_api_player['is_nba'] = False
            nba_api_player['has_played_games'] = False
            nba_api_player['draft_year'] = ''
            nba_api_player['draft_round'] = ''
            nba_api_player['draft_number'] = ''
            nba_api_player['nba_api_team_id'] = None

        result_players.append(nba_api_player)
        log_console('\t' + 'Players/' + str(counter) + '_' + str(nba_api_player['full_name']) + '.json')
        clean_and_write_file('Players/' + str(counter) + '_' + str(nba_api_player['full_name']) + '.json', json.dumps(nba_api_player, indent=4))
        counter += 1
        time.sleep(.8)

    return result_players

def get_season_games_for_team(team_id, season):
    log_console('Processing Season:\t' + str(season) + '\tTeam:\t' + str(team_id))
    for seasontype in season_types:
        res = TeamGameLog(season=season, team_id=team_id, season_type_all_star=seasontype)
        res = res.get_dict()
        res = res['resultSets']
        res = res[0]
        columns = res['headers']
        games = res['rowSet']

        if len(games) == 0:
            continue

        with open('TeamGames/' + str(season) + '_' + str(team_id) + '_' + seasontype + '.csv', 'w', newline='') as file:
            log_console('\tWriting CSV file - ' + seasontype)
            writer = csv.writer(file)
            writer.writerow(columns)
            for game in games:
                writer.writerow(game)

            file.close()
        time.sleep(.8)

def get_season_games_for_player(player_id, season):
    log_console('Processing Season:\t' + str(season) + '\tPlayer:\t' + str(player_id))
    for seasontype in season_types:
        res = PlayerGameLog(season=season, player_id=player_id, season_type_all_star=seasontype)
        res = res.get_dict()
        res = res['resultSets']
        res = res[0]
        columns = res['headers']
        games = res['rowSet']

        if len(games) == 0:
            continue

        with open('PlayerGames/' + str(season) + '_' + str(player_id) + '_' + seasontype + '.csv', 'w', newline='') as file:
            log_console('\tWriting CSV file - ' + seasontype)
            writer = csv.writer(file)
            writer.writerow(columns)
            for game in games:
                writer.writerow(game)

            file.close()
        time.sleep(.8)

# in each CSV file store all the games for a team in a season
# will cover season from 1975 onwards by default
def store_team_games_in_csv(season_start=1975, season_end=2021):
    nba_api_teams = read_json_from_file('teams_list.json')
    for season in range(season_start, season_end):
        for team in nba_api_teams:
            get_season = player['min_year'] != None
            get_season = get_season and player['max_year'] != None
            get_season = get_season and player['min_year'] != ''
            get_season = get_season and player['max_year'] != ''
            get_season = get_season and int(player['min_year']) <= season
            get_season = get_season and season <= int(player['max_year'])
            if (get_season):
                log_console('Processing Team:\t' + team['full_name'])
                get_season_games_for_team(team['id'], season)

# in each CSV file store all the games for a player in a season
# will cover season from 1975 onwards by default
def store_player_games_in_csv(season_start=1975, season_end=2021):
    nba_api_players = []
    for player_filename in os.listdir('Players/'):
        if player_filename.endswith('.json'):
            nba_api_players.append(read_json_from_file('Players/' + player_filename))

    for season in range(season_end, season_start-1, -1):
        for player in nba_api_players:
            get_season = player['date_from'] != None
            get_season = get_season and player['date_to'] != None
            get_season = get_season and player['date_from'] != ''
            get_season = get_season and player['date_to'] != ''
            get_season = get_season and player['date_from'] <= season
            get_season = get_season and season <= player['date_to']
            if (get_season):
                log_console('Processing Player:\t' + player['full_name'])
                get_season_games_for_player(player['id'], season)


# store all te teams as json in teams_list.json
def store_teams_in_json():
    teams = get_all_teams()
    clean_and_write_file('teams_list.json', json.dumps(teams, indent=4))

# store all the players as json in players_list.json
def store_players_in_json():
    players = get_all_players()
    clean_and_write_file('players_list.json', json.dumps(players, indent=4))




