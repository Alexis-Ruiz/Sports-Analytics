from django.db import models

# Create your models here.
class Player(models.Model):
    # from nba-api
    full_name   = models.CharField(max_length = 100)
    first_name  = models.CharField(max_length = 50)
    last_name   = models.CharField(max_length = 50)
    is_active   = models.BooleanField(default = False)

    def __str__(self):
        return self.full_name

class Team(models.Model):
    # from nba-api
    full_name       = models.CharField(max_length = 100)
    abbreviation    = models.CharField(max_length = 10)
    nickname        = models.CharField(max_length = 50)
    city            = models.CharField(max_length = 50)
    state           = models.CharField(max_length = 50)
    year_founded    = models.IntegerField()

    def __str__(self):
        return self.full_name + ' (' + self.abbreviation + ')'
