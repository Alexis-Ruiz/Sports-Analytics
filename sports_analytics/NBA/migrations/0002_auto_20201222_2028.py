# Generated by Django 2.2 on 2020-12-22 20:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NBA', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='player',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='player',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='player',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='player',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='team',
            name='abbreviation',
        ),
        migrations.RemoveField(
            model_name='team',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='team',
            name='state',
        ),
        migrations.RemoveField(
            model_name='team',
            name='year_founded',
        ),
        migrations.AddField(
            model_name='player',
            name='affiliation',
            field=models.CharField(blank=True, max_length=201),
        ),
        migrations.AddField(
            model_name='player',
            name='collegeName',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='player',
            name='country',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='player',
            name='dateOfBirth',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='firstName',
            field=models.CharField(default='NULL', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='heighInMeters',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='lastName',
            field=models.CharField(default='NULL', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='playerId',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='startNba',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player_team', to='NBA.Team'),
        ),
        migrations.AddField(
            model_name='player',
            name='weightInKilograms',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='yearsPro',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='allStar',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='fullName',
            field=models.CharField(default='NULL', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='logo',
            field=models.TextField(blank=True, validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AddField(
            model_name='team',
            name='nbaFranchise',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='shortName',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='team',
            name='teamID',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='team',
            name='city',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='team',
            name='nickname',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.CreateModel(
            name='PlayerLeague',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jersey', models.CharField(max_length=2)),
                ('active', models.BooleanField()),
                ('pos', models.CharField(max_length=10)),
                ('league', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='playerinfo_league', to='NBA.League')),
                ('player', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='playerinfo_player', to='NBA.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confName', models.CharField(max_length=50)),
                ('divName', models.CharField(blank=True, max_length=50)),
                ('league', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='conference_league', to='NBA.League')),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='conference',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_conference', to='NBA.Conference'),
        ),
    ]
