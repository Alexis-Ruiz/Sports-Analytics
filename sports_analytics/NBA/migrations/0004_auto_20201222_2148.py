# Generated by Django 2.2 on 2020-12-22 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NBA', '0003_auto_20201222_2125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='heighInMeters',
        ),
        migrations.AddField(
            model_name='player',
            name='heightInMeters',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='weightInKilograms',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
