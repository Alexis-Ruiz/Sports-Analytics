from django.db import models
# from django.core.validators import URLValidator

class Team(models.Model):
    #nba-api
    nba_api_id = models.IntegerField()
    full_name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)
    nickname = models.CharField(max_length=50)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    year_founded = models.CharField(max_length=5, blank=True)
    conference = models.CharField(max_length = 50, blank=True)
    division = models.CharField(max_length = 50, blank=True)
    min_year = models.CharField(max_length = 4, blank=True)
    max_year = models.CharField(max_length = 4, blank=True)


    def __str__(self):
        return self.full_name + ' (' + self.abbreviation + ')'

class Player(models.Model):
    # static
    nba_api_id = models.IntegerField(unique=True)
    full_name = models.CharField(max_length=50, blank=True)
    first_name = models.CharField(max_length = 50, blank=True)
    last_name = models.CharField(max_length = 50, blank=True)
    is_active = models.BooleanField()

    # common endpoints
    birth_date = models.DateTimeField(null=True)
    school = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True)
    height = models.CharField(max_length=5, blank=True)
    weight = models.CharField(max_length=5, blank=True)
    season_exp = models.CharField(max_length=2, blank=True)
    jersey_number = models.CharField(max_length=10, blank=True)
    position = models.CharField(max_length=50, blank=True)
    date_from = models.CharField(max_length=4, blank=True, null=True)
    date_to = models.CharField(max_length=4, blank=True, null=True)
    is_d_league = models.BooleanField()
    is_nba = models.BooleanField()
    has_played_games = models.BooleanField()
    draft_year = models.CharField(max_length=10, blank=True, null=True)
    draft_round = models.CharField(max_length=10, blank=True, null=True)
    draft_number = models.CharField(max_length=10, blank=True, null=True)


    def __str__(self):
        return self.full_name

# Relational Tables
class PlaysFor(models.Model):
    player_nba_api_id = models.IntegerField(unique=True)
    team_nba_api_id = models.IntegerField()

class TeamGame(models.Model):
    nba_api_game_id = models.IntegerField()
    nba_api_team_id = models.IntegerField()
    game_date = models.DateField()
    is_win = models.BooleanField(null=True)
    MIN = models.CharField(max_length=5, null=True)
    FGM = models.IntegerField(null=True)
    FGA = models.IntegerField(null=True)
    FG_PCT = models.DecimalField(max_digits=4, decimal_places=3, null=True)
    FG3M = models.IntegerField(null=True)
    FG3A = models.IntegerField(null=True)
    FG3_PCT = models.DecimalField(max_digits=4, decimal_places=3, null=True)
    FTM = models.IntegerField(null=True)
    FTA = models.IntegerField(null=True)
    FT_PCT = models.DecimalField(max_digits=4, decimal_places=3, null=True)
    OREB = models.IntegerField(null=True)
    DREB = models.IntegerField(null=True)
    REB = models.IntegerField(null=True)
    AST = models.IntegerField(null=True)
    STL = models.IntegerField(null=True)
    BLK = models.IntegerField(null=True)
    TOV = models.IntegerField(null=True)
    PF = models.IntegerField(null=True)
    PTS = models.IntegerField(null=True)

class PlayerGame(models.Model):
    nba_api_season_id = models.IntegerField()
    nba_api_player_id = models.IntegerField()
    nba_api_game_id = models.IntegerField()
    game_date = models.DateField()
    matchup = models.CharField(max_length=20, null=True)
    is_win = models.BooleanField(null=True)
    MIN = models.CharField(max_length=5, null=True)
    FGM = models.IntegerField(null=True)
    FGA = models.IntegerField(null=True)
    FG_PCT = models.DecimalField(max_digits=4, decimal_places=3, null=True)
    FG3M = models.IntegerField(null=True)
    FG3A = models.IntegerField(null=True)
    FG3_PCT = models.DecimalField(max_digits=4, decimal_places=3, null=True)
    FTM = models.IntegerField(null=True)
    FTA = models.IntegerField(null=True)
    FT_PCT = models.DecimalField(max_digits=4, decimal_places=3, null=True)
    OREB = models.IntegerField(null=True)
    DREB = models.IntegerField(null=True)
    REB = models.IntegerField(null=True)
    AST = models.IntegerField(null=True)
    STL = models.IntegerField(null=True)
    BLK = models.IntegerField(null=True)
    TOV = models.IntegerField(null=True)
    PF = models.IntegerField(null=True)
    PTS = models.IntegerField(null=True)
    PLUS_MINUS = models.IntegerField(null=True)
    VIDEO_AVAILABLE = models.BooleanField(null=True)



