from django.db import models
from django.core.validators import URLValidator

class League(models.Model):
    name = models.CharField(max_length = 50)

class Conference(models.Model):
    confName = models.CharField(max_length=50)
    divName = models.CharField(max_length=50, blank=True)

    # relational fields
    league = models.ForeignKey(League, on_delete = models.SET_NULL, null = True, related_name = 'conference_league')

class Team(models.Model):
    city = models.CharField(max_length=50, blank=True)
    fullName = models.CharField(max_length = 100)
    teamID = models.IntegerField()
    nickname = models.CharField(max_length = 50, blank=True)
    logo = models.TextField(validators=[URLValidator()], blank=True)
    shortName = models.CharField(max_length = 10, blank=True)
    allStar = models.BooleanField()
    nbaFranchise  = models.BooleanField()

    # relational fields
    conference =  models.ForeignKey(Conference, on_delete = models.SET_NULL, null = True, related_name = 'team_conference')

    def __str__(self):
        return self.full_name + ' (' + self.abbreviation + ')'


class Player(models.Model):
    firstName  = models.CharField(max_length = 50)
    lastName   = models.CharField(max_length = 50)
    yearsPro = models.IntegerField()
    collegeName = models.CharField(max_length = 100, blank = True)
    country = models.CharField(max_length = 100, blank = True)
    playerId = models.IntegerField()
    dateOfBirth = models.DateTimeField(null=True)
    affiliation = models.CharField(max_length = 201, blank = True)
    startNba = models.IntegerField()
    heightInMeters = models.DecimalField(max_digits = 3, decimal_places = 2, null = True)
    weightInKilograms = models.DecimalField(max_digits = 5, decimal_places = 2, null = True)

    #relational fields
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null = True, related_name='player_team')

    def __str__(self):
        return self.full_name

class PlayerLeague(models.Model):
    jersey = models.CharField(max_length = 2)
    active = models.BooleanField()
    pos = models.CharField(max_length = 10)

    # relational fields
    player = models.ForeignKey(Player, on_delete=models.SET_NULL, null = True, related_name='playerinfo_player')
    league = models.ForeignKey(League, on_delete=models.SET_NULL, null = True, related_name='playerinfo_league')