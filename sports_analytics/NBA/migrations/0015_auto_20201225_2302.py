# Generated by Django 2.2 on 2020-12-25 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NBA', '0014_auto_20201225_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='jersey_number',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
