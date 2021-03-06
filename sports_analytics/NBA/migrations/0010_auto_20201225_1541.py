# Generated by Django 2.2 on 2020-12-25 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NBA', '0009_auto_20201225_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='balldontlie_id',
        ),
        migrations.RemoveField(
            model_name='player',
            name='height_feet',
        ),
        migrations.RemoveField(
            model_name='player',
            name='height_inches',
        ),
        migrations.RemoveField(
            model_name='player',
            name='weight_pounds',
        ),
        migrations.AddField(
            model_name='player',
            name='birth_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='country',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='player',
            name='date_from',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='date_to',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='draft_number',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='player',
            name='draft_round',
            field=models.CharField(blank=True, max_length=1),
        ),
        migrations.AddField(
            model_name='player',
            name='draft_year',
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.AddField(
            model_name='player',
            name='has_played_games',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='height',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AddField(
            model_name='player',
            name='is_d_league',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='is_nba',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='jersey_number',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='player',
            name='school',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='player',
            name='season_exp',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='player',
            name='weight',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='player',
            name='nba_api_id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.CharField(blank=True, default=1, max_length=50),
            preserve_default=False,
        ),
    ]
