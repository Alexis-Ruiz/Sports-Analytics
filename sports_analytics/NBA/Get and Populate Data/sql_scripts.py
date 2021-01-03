PLAYER_SQLS = {
    'columns': ['first_name', 'full_name', 'is_active', 'last_name', 'nba_api_id', "position", 'birth_date', 'country', 'date_from', 'date_to', 'draft_number', 'draft_round', 'draft_year', 'has_played_games', 'height', 'is_d_league', 'is_nba', 'jersey_number', 'school', 'season_exp', 'weight'],

    'search': '''SELECT id, first_name, full_name, is_active, last_name, nba_api_id, "position", birth_date, country, date_from, date_to, draft_number, draft_round, draft_year, has_played_games, height, is_d_league, is_nba, jersey_number, school, season_exp, weight
	FROM public."NBA_player"''',

    'insert': '''INSERT INTO public."NBA_player"(
	first_name, full_name, is_active, last_name, nba_api_id, "position", birth_date, country, date_from, date_to, draft_number, draft_round, draft_year, has_played_games, height, is_d_league, is_nba, jersey_number, school, season_exp, weight)
	VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);''',

    'update': '''UPDATE public."NBA_player"
	SET first_name=%s, full_name=%s, is_active=%s, last_name=%s, nba_api_id=%s, "position"=%s, birth_date=%s, country=%s, date_from=%s, date_to=%s, draft_number=%s, draft_round=%s, draft_year=%s, has_played_games=%s, height=%s, is_d_league=%s, is_nba=%s, jersey_number=%s, school=%s, season_exp=%s, weight=%s
	WHERE  ''',
}

TEAM_SQLS = {
    'columns': ['nickname', 'city', 'conference', 'abbreviation', 'division', 'full_name', 'nba_api_id', 'state', 'year_founded', 'max_year', 'min_year'],

    'search': '''SELECT id, nickname, city, conference, abbreviation, division, full_name, nba_api_id, state, year_founded, max_year, min_year
	FROM public."NBA_team"''',

    'insert': '''INSERT INTO public."NBA_team"(
	nickname, city, conference, abbreviation, division, full_name, nba_api_id, state, year_founded, max_year, min_year)
	VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);''',

    'update': '''UPDATE public."NBA_team"
	SET nickname=%s, city=%s, conference=%s, abbreviation=%s, division=%s, full_name=%s, nba_api_id=%s, state=%s, year_founded=%s, max_year=%s, min_year=%s
	WHERE  ''',
}

PLAYSFOR_SQLS = {
    'columns': ['player_nba_api_id', 'team_nba_api_id'],

    'search': '''SELECT id, player_nba_api_id, team_nba_api_id
	FROM public."NBA_playsfor"''',

    'insert': '''INSERT INTO public."NBA_playsfor"(
	player_nba_api_id, team_nba_api_id)
	VALUES (%s, %s);''',

    'update': '''UPDATE public."NBA_playsfor"
	SET player_nba_api_id=%s, team_nba_api_id=%s
	WHERE ''',
}

TEAMGAMES_SQLS = {
    'columns': ['nba_api_game_id', 'nba_api_team_id', 'game_date', 'is_win', "MIN", "FGM", "FGA", "FT_PCT", "FG3M", "FG3A", "FG3_PCT", "FTM", "FTA", "FG_PCT", "OREB", "DREB", "REB", "AST", "STL", "BLK", "TOV", "PF", "PTS"],

    'search': '''SELECT id, nba_api_game_id, nba_api_team_id, game_date, is_win, "MIN", "FGM", "FGA", "FT_PCT", "FG3M", "FG3A", "FG3_PCT", "FTM", "FTA", "FG_PCT", "OREB", "DREB", "REB", "AST", "STL", "BLK", "TOV", "PF", "PTS"
	FROM public."NBA_teamgame"''',

    'insert': '''INSERT INTO public."NBA_teamgame"(
	nba_api_game_id, nba_api_team_id, game_date, is_win, "MIN", "FGM", "FGA", "FT_PCT", "FG3M", "FG3A", "FG3_PCT", "FTM", "FTA", "FG_PCT", "OREB", "DREB", "REB", "AST", "STL", "BLK", "TOV", "PF", "PTS")
	VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);''',

    'update': '''UPDATE public."NBA_teamgame"
	SET nba_api_game_id=%s, nba_api_team_id=%s, game_date=%s, is_win=%s, "MIN"=%s, "FGM"=%s, "FGA"=%s, "FT_PCT"=%s, "FG3M"=%s, "FG3A"=%s, "FG3_PCT"=%s, "FTM"=%s, "FTA"=%s, "FG_PCT"=%s, "OREB"=%s, "DREB"=%s, "REB"=%s, "AST"=%s, "STL"=%s, "BLK"=%s, "TOV"=%s, "PF"=%s, "PTS"=%s
	WHERE ''',
}

PLAYERGAMES_SQLS = {
    'columns': ['nba_api_season_id', 'nba_api_player_id', 'nba_api_game_id', 'game_date', 'matchup', 'is_win', "AST", "BLK", "DREB", "FG3A", "FG3M", "FG3_PCT", "FGA", "FGM", "FG_PCT", "FTA", "FTM", "FT_PCT", "MIN", "OREB", "PF", "PLUS_MINUS", "PTS", "REB", "STL", "TOV", "VIDEO_AVAILABLE"],

    'search': '''SELECT id, nba_api_season_id, nba_api_player_id, nba_api_game_id, game_date, matchup, is_win, "AST", "BLK", "DREB", "FG3A", "FG3M", "FG3_PCT", "FGA", "FGM", "FG_PCT", "FTA", "FTM", "FT_PCT", "MIN", "OREB", "PF", "PLUS_MINUS", "PTS", "REB", "STL", "TOV", "VIDEO_AVAILABLE"
	FROM public."NBA_playergame" ''',

    'insert': '''INSERT INTO public."NBA_playergame"(
	nba_api_season_id, nba_api_player_id, nba_api_game_id, game_date, matchup, is_win, "AST", "BLK", "DREB", "FG3A", "FG3M", "FG3_PCT", "FGA", "FGM", "FG_PCT", "FTA", "FTM", "FT_PCT", "MIN", "OREB", "PF", "PLUS_MINUS", "PTS", "REB", "STL", "TOV", "VIDEO_AVAILABLE")
	VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);''',

    'update': '''UPDATE public."NBA_playergame"
	SET nba_api_season_id=%s, nba_api_player_id=%s, nba_api_game_id=%s, game_date=%s, matchup=%s, is_win=%s, "AST"=%s, "BLK"=%s, "DREB"=%s, "FG3A"=%s, "FG3M"=%s, "FG3_PCT"=%s, "FGA"=%s, "FGM"=%s, "FG_PCT"=%s, "FTA"=%s, "FTM"=%s, "FT_PCT"=%s, "MIN"=%s, "OREB"=%s, "PF"=%s, "PLUS_MINUS"=%s, "PTS"=%s, "REB"=%s, "STL"=%s, "TOV"=%s, "VIDEO_AVAILABLE"=%s
	WHERE ''',
}