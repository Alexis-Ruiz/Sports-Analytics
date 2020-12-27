# Generated by Django 2.2 on 2020-12-25 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NBA', '0011_playsfor'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nba_api_game_id', models.IntegerField(unique=True)),
                ('nba_api_team_id', models.IntegerField()),
                ('game_date', models.DateField()),
                ('is_win', models.BooleanField(null=True)),
                ('minutes', models.CharField(max_length=5, null=True)),
                ('fgm', models.IntegerField(null=True)),
                ('fga', models.IntegerField(null=True)),
                ('fg_pct', models.DecimalField(decimal_places=3, max_digits=4, null=True)),
                ('fg3m', models.IntegerField(null=True)),
                ('fg3a', models.IntegerField(null=True)),
                ('fg3_pct', models.DecimalField(decimal_places=3, max_digits=4, null=True)),
                ('ftm', models.IntegerField(null=True)),
                ('fta', models.IntegerField(null=True)),
                ('ft_pct', models.DecimalField(decimal_places=3, max_digits=4, null=True)),
                ('oreb', models.IntegerField(null=True)),
                ('dreb', models.IntegerField(null=True)),
                ('reb', models.IntegerField(null=True)),
                ('ast', models.IntegerField(null=True)),
                ('stl', models.IntegerField(null=True)),
                ('blk', models.IntegerField(null=True)),
                ('tov', models.IntegerField(null=True)),
                ('pf', models.IntegerField(null=True)),
                ('pts', models.IntegerField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='team',
            name='balldontlie_id',
        ),
        migrations.RemoveField(
            model_name='team',
            name='name',
        ),
        migrations.AddField(
            model_name='team',
            name='max_year',
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.AddField(
            model_name='team',
            name='min_year',
            field=models.CharField(blank=True, max_length=4),
        ),
    ]