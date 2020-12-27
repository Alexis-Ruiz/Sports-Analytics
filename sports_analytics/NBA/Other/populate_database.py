import test_api
import psycopg2
import json
import datetime
import csv
import os

from sql_scripts import *

def read_csv_from_file(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        columns = []
        rows = []

        for row in csv_reader:
            if line_count == 0:
                columns = row
            else:
                row_dict = {}
                for idx in range(len(columns)):
                    row_dict[columns[idx]] = row[idx]
                rows.append(row_dict)
            line_count += 1

        return rows

def read_json_from_file(filename):
    file = open(filename, 'r')
    obj = json.loads(file.read())
    file.close()
    return obj

# establish connection with NBA Database
def connect_to_database():
    try:
        conn = psycopg2.connect(dbname='NBA', user='postgres', host='localhost', password='')
    except:
        print('cannot connect to DB')
        exit(1)

    return conn

# database connection with cursor
CONN = connect_to_database()
CUR = CONN.cursor()


# helper functions to add specific objects ---------------------
def add_update_specific_team(team):
    # temporary fixes
    team['conference'] = team['confernce']


    CUR.execute(TEAM_SQLS['search'] + 'WHERE nba_api_id = %s;', (team['nba_api_id'],))
    db_team = CUR.fetchall()

    if len(db_team) == 0:
        # This is a new team and must be inserted into the database
        CUR.execute(TEAM_SQLS['insert'], tuple(team[column] for column in TEAM_SQLS['columns']))
    else:
        # this team already exists and so update its values
        CUR.execute(TEAM_SQLS['update'] + 'id = ' + str(db_team[0][0]) + ';' , tuple(team[column] for column in TEAM_SQLS['columns']))

def add_update_specific_player(player):
    CUR.execute(PLAYER_SQLS['search'] + 'WHERE nba_api_id = %s;', (player['nba_api_id'], ))
    db_player = CUR.fetchall()

    if len(db_player) == 0:
        # This is a new player and must be inserted into the database
        CUR.execute(PLAYER_SQLS['insert'], tuple(player[column] for column in PLAYER_SQLS['columns']))
    else:
        # this player already exists and so update its values
        CUR.execute(PLAYER_SQLS['update'] + 'id = ' + str(db_player[0][0]) + ';' , tuple(player[column] for column in PLAYER_SQLS['columns']))

def add_update_specific_playsfor(player):
    # mapping to database column
    player['team_nba_api_id'] = player['nba_api_team_id']
    player['player_nba_api_id'] = player['nba_api_id']

    if (player['team_nba_api_id'] == None or player['team_nba_api_id'] == '' or player['team_nba_api_id'] == 0):
        return

    CUR.execute(PLAYSFOR_SQLS['search'] + 'WHERE player_nba_api_id = %s;', (player['nba_api_id'],))
    db_player = CUR.fetchall()

    if len(db_player) == 0:
        # This is a new player and must be inserted into the database
        CUR.execute(PLAYSFOR_SQLS['insert'], tuple(player[column] for column in PLAYSFOR_SQLS['columns']))
    else:
        # this player already exists and so update its values
        CUR.execute(PLAYSFOR_SQLS['update'] + 'id = ' + str(db_player[0][0]) + ';',
                    tuple(player[column] for column in PLAYSFOR_SQLS['columns']))

def add_update_specific_teamgame(teamgame):
    # mapping to database column
    for attr in teamgame:
        if teamgame[attr] == '':
            teamgame[attr] = None

    teamgame['nba_api_game_id'] = teamgame['Game_ID']
    teamgame['nba_api_team_id'] = teamgame['Team_ID']
    teamgame['game_date'] = teamgame['GAME_DATE']
    teamgame['is_win'] = True if teamgame['WL'] == 'W' else False
    teamgame['minutes'] = teamgame['MIN']
    try:
        teamgame['FG_PCT'] = round(((1.0 * int(teamgame['FGM']))/int(teamgame['FGA'])), 3)
    except:
        teamgame['FG_PCT'] = None

    try:
        teamgame['FG3_PCT'] = round(((1.0 * int(teamgame['FG3M'])) / int(teamgame['FG3A'])), 3)
    except:
        teamgame['FG3_PCT'] = None

    try:
        teamgame['FT_PCT'] = round(((1.0 * int(teamgame['FTM'])) / int(teamgame['FTA'])), 3)
    except:
        teamgame['FT_PCT'] = None

    CUR.execute(TEAMGAMES_SQLS['search'] + 'WHERE nba_api_game_id = %s AND nba_api_team_id = %s;',
                (teamgame['Game_ID'], teamgame['Team_ID']))
    db_player = CUR.fetchall()

    if len(db_player) == 0:
        # This is a new teamgame and must be inserted into the database
        CUR.execute(TEAMGAMES_SQLS['insert'], tuple(teamgame[column] for column in TEAMGAMES_SQLS['columns']))
    else:
        # this teamgame already exists and so update its values
        CUR.execute(TEAMGAMES_SQLS['update'] + 'id = ' + str(db_player[0][0]) + ';',
                    tuple(teamgame[column] for column in TEAMGAMES_SQLS['columns']))


# functions to populate all the data ---------------------------
def add_update_all_playsfor():
    for player_filename in os.listdir('Players/'):
        if player_filename.endswith('.json'):
            player = read_json_from_file('Players/' + player_filename)
            print('Players/' + player_filename)
            print('\n')
            add_update_specific_playsfor(player)
    CONN.commit()
    return 1

def add_update_all_teams():
    filename = 'teams_list.json'
    teams_info = open(filename, 'r')
    teams_list = json.loads(teams_info.read())
    teams_info.close()
    for team in teams_list:
        add_update_specific_team(team)
    CONN.commit()
    return 1

def add_update_all_players():
    for player_filename in os.listdir('Players/'):
        if player_filename.endswith('.json'):
            player = read_json_from_file('Players/' + player_filename)
            print('Players/' + player_filename)
            print('\n')
            add_update_specific_player(player)
    CONN.commit()
    return 1

def add_update_all_team_games():
    for teamgame_filename in os.listdir('TeamGames/'):
        if teamgame_filename.endswith('.csv'):
            teamgames = read_csv_from_file('TeamGames/' + teamgame_filename)
            print('Processing ' + teamgame_filename)
            for teamgame in teamgames:
                print('\tProcessing Game: ' + teamgame['Game_ID'])
                add_update_specific_teamgame(teamgame)
    CONN.commit()
    return 1


def update_all_data():
    add_update_all_teams()
    add_update_all_players()
    add_update_all_playsfor()
    return 1



