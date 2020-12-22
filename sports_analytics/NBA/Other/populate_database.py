import psycopg2
import json
import datetime

try:
    conn = psycopg2.connect(dbname='NBA', user='postgres', host='localhost', password='')
except:
    print('cannot connect to DB')
    exit(1)

cur = conn.cursor()

LEAGUESEARCHSQL = """  SELECT id, name
	                 FROM public."NBA_league"
	                 WHERE name = %s;
                  """

LEAGUEINSERTSQL = """ INSERT INTO public."NBA_league"(name) VALUES (%s);
          """

CONFERENCESEARCHSQL = """SELECT id, "confName", "divName", league_id
	                     FROM public."NBA_conference" CONF
	                     WHERE "confName" = %s and "divName" = %s and "league_id" = %s;
                      """

CONFERENCEINSERTSQL = """ INSERT INTO public."NBA_conference"(
    "confName", "divName", league_id)
	VALUES (%s, %s, %s);
"""

TEAMSEARCHSQL = """SELECT id, nickname, city, "allStar", "fullName", logo, "nbaFranchise", "shortName", "teamID", conference_id
	FROM public."NBA_team"
	WHERE "teamID" = %s;
"""

TEAMINSERTSQL = """INSERT INTO public."NBA_team"(
	nickname, city, "allStar", "fullName", logo, "nbaFranchise", "shortName", "teamID", conference_id)
	VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
"""

PLAYERSEARCHSQL = """ SELECT id, affiliation, "collegeName", country, "dateOfBirth", "firstName", "heightInMeters", "lastName", "playerId", "startNba", team_id, "weightInKilograms", "yearsPro"
	FROM public."NBA_player" 
	WHERE "playerId" = %s;
"""

PLAYERINSERTSQL = """INSERT INTO public."NBA_player"(
	affiliation, "collegeName", country, "dateOfBirth", "firstName", "heightInMeters", "lastName", "playerId", "startNba", team_id, "weightInKilograms", "yearsPro")
	VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
	"""

PLAYERLEAGUESEARCHSQL = """SELECT id, jersey, active, pos, league_id, player_id
	FROM public."NBA_playerleague"
	WHERE league_id = %s and player_id = %s
"""

PLAYERLEAGUEINSERTSQL = """INSERT INTO public."NBA_playerleague"(
	jersey, active, pos, league_id, player_id)
	VALUES (%s, %s, %s, %s, %s);
	"""


def add_leagues():

    filename = 'league_info.txt'
    league_info = open(filename, 'r')
    league_json = json.loads(league_info.read())
    league_info.close()
    leagues = (league_json['api'])['leagues']

    for league in leagues:
        cur.execute(LEAGUESEARCHSQL, (league,))
        result = cur.fetchall()
        if len(result) == 0:
            cur.execute(LEAGUEINSERTSQL, (league,))
        else:
            print('League: ' + league + ' already exists')

    conn.commit()

def add_conferences():
    filename = 'team_info.txt'
    league_info = open(filename, 'r')
    league_json = json.loads(league_info.read())
    league_info.close()

    for league in league_json:
        cur.execute(LEAGUESEARCHSQL, (league,))
        leagueobj = cur.fetchall()[0]

        teams = league_json[league]['api']['teams']

        for team in teams:
            conference = team['leagues'][league]

            cur.execute(CONFERENCESEARCHSQL, (conference['confName'], conference['divName'], leagueobj[0],))
            res = cur.fetchall()

            if len(res) == 0:
                cur.execute(CONFERENCEINSERTSQL, (conference['confName'], conference['divName'], leagueobj[0],))
                conn.commit()
            else:
                print('Conference: ' + conference['confName'] + ', Division: ' + conference['divName'] + ', League: ' + str(leagueobj[0]) + ' already exists')


def add_teams():
    filename = 'team_info.txt'
    league_info = open(filename, 'r')
    league_json = json.loads(league_info.read())
    league_info.close()

    for league in league_json:
        cur.execute(LEAGUESEARCHSQL, (league,))
        leagueobj = cur.fetchall()[0]

        teams = league_json[league]['api']['teams']

        for team in teams:
            conference = team['leagues'][league]

            cur.execute(CONFERENCESEARCHSQL, (conference['confName'], conference['divName'], leagueobj[0],))
            conferenceobj = cur.fetchall()[0]

            cur.execute(TEAMSEARCHSQL, (team['teamId'], ))
            res = cur.fetchall()

            if len(res) == 0:
                if team['allStar'] == '':
                    team['allStar'] = 0
                cur.execute(TEAMINSERTSQL, (team['nickname'], team['city'], team['allStar'],
                                            team['fullName'], team['logo'], team['nbaFranchise'],
                                            team['shortName'], team['teamId'], conferenceobj[0],))
                conn.commit()
            else:
                print('Team: ' + team['fullName'] + 'with teamId: ' + team['teamId'] + 'already exists')


def add_players(league):
    filename = league + '_player_info.txt'
    team_info = open(filename, 'r')
    team_json = json.loads(team_info.read())
    team_info.close()
    
    for teamId in team_json:
        players = team_json[teamId]['api']['players']

        cur.execute(TEAMSEARCHSQL, (teamId,))
        teamobj = cur.fetchone()[0]

        for player in players:
            cur.execute(PLAYERSEARCHSQL, (player['playerId'], ))
            res = cur.fetchall()

            if len(res) == 0:
                if  player['dateOfBirth'] == '':
                    player['dateOfBirth'] = None
                if  player['heightInMeters'] == '':
                    player['heightInMeters'] = None
                if  player['weightInKilograms'] == '':
                    player['weightInKilograms'] = None
                cur.execute(PLAYERINSERTSQL, (player['affiliation'], player['collegeName'], player['country'],
                                              player['dateOfBirth'], player['firstName'], player['heightInMeters'],
                                              player['lastName'], player['playerId'], player['startNba'], teamobj[0],
                                              player['weightInKilograms'], player['yearsPro']))
                conn.commit()
            else:
                print('Player: ' + player['firstName'] + ' ' + player['lastName'] + ' already exists')


def add_playerleagues(league):
    filename = league + '_player_info.txt'
    team_info = open(filename, 'r')
    team_json = json.loads(team_info.read())
    team_info.close()

    cur.execute(LEAGUESEARCHSQL, (league,))

    for teamId in team_json:
        players = team_json[teamId]['api']['players']

        cur.execute(TEAMSEARCHSQL, (teamId,))
        # teamobj = cur.fetchone()[0]

        for player in players:
            cur.execute(PLAYERSEARCHSQL, (player['playerId'], ))
            res = cur.fetchall()

            if (len(res) > 0):
                playerobj = res[0]

                playerleagues = player['leagues']

                for league2 in playerleagues:
                    playerleague = playerleagues[league2]
                    cur.execute(LEAGUESEARCHSQL, (league2,))
                    leagueobj = cur.fetchall()[0]

                    cur.execute(PLAYERLEAGUESEARCHSQL, (leagueobj[0], playerobj[0]))
                    res = cur.fetchall()

                    if len(res) == 0:
                        if playerleague['active'] == '':
                            playerleague['active'] = False

                        cur.execute(PLAYERLEAGUEINSERTSQL,
                                    (playerleague['jersey'], playerleague['active'], playerleague['pos'],
                                     leagueobj[0], playerobj[0]))
                        conn.commit()
                    else:
                        print('League: ' + league + " with player " + player['firstName'] + ' ' + player[
                            'lastName'] + 'already has his info filled')


leagues = ["africa", "orlando", "sacramento", "standard", "utah", "vegas"]

def init():
    add_leagues()
    add_conferences()
    add_teams()
    
    for league in leagues:
        add_players(league)
        add_playerleagues(league)
    
    

cur.close()
conn.close()