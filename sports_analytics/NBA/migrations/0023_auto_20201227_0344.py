# Generated by Django 2.2 on 2020-12-27 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NBA', '0022_auto_20201226_2215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playergame',
            name='ast',
        ),
        migrations.RemoveField(
            model_name='playergame',
            name='blk',
        ),
        migrations.RemoveField(
            model_name='playergame',
            name='dreb',
        ),
        migrations.RemoveField(
            model_name='playergame',
            name='fg3_pct',
        ),
        migrations.RemoveField(
            model_name='playergame',
            name='fg3a',
        ),
        migrations.RemoveField(
            model_name='playergame',
            name='fg3m',
        ),
        migrations.RemoveField(
            model_name='playergame',
            name='fg_pct',
        ),
        migrations.RemoveField(
            model_name='playergame',
            name='fga',
        ),
        migrations.RemoveField(
            model_name='playergame',
            name='fgm',
        ),
        migrations.RemoveField(
            model_name='playergame',
            name='ft_pct',
        ),
        migrations.RemoveField(
            model_name='playergame',
            name='fta',
        ),
        migrations.RemoveField(
            model_name='playergame',
            name='ftm',
        ),
        migrations.RemoveField(
            model_name='playergame',
            name='minutes',
        ),
        migrations.RemoveField(
            model_name='playergame',
            name='oreb',
        ),
        migrations.RemoveField(
            model_name='playergame',
            name='pf',
        ),
        migrations.RemoveField(
            model_name='playergame',
            name='plus_minus',
        ),
        migrations.RemoveField(
            model_name='playergame',
            name='pts',
        ),
        migrations.RemoveField(
            model_name='playergame',
            name='reb',
        ),
        migrations.RemoveField(
            model_name='playergame',
            name='stl',
        ),
        migrations.RemoveField(
            model_name='playergame',
            name='tov',
        ),
        migrations.RemoveField(
            model_name='playergame',
            name='video_available',
        ),
        migrations.AddField(
            model_name='playergame',
            name='AST',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='playergame',
            name='BLK',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='playergame',
            name='DREB',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='playergame',
            name='FG3A',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='playergame',
            name='FG3M',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='playergame',
            name='FG3_PCT',
            field=models.DecimalField(decimal_places=3, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='playergame',
            name='FGA',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='playergame',
            name='FGM',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='playergame',
            name='FG_PCT',
            field=models.DecimalField(decimal_places=3, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='playergame',
            name='FTA',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='playergame',
            name='FTM',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='playergame',
            name='FT_PCT',
            field=models.DecimalField(decimal_places=3, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='playergame',
            name='MIN',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='playergame',
            name='OREB',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='playergame',
            name='PF',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='playergame',
            name='PLUS_MINUS',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='playergame',
            name='PTS',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='playergame',
            name='REB',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='playergame',
            name='STL',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='playergame',
            name='TOV',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='playergame',
            name='VIDEO_AVAILABLE',
            field=models.BooleanField(null=True),
        ),
    ]
