# Generated by Django 2.2 on 2020-12-22 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NBA', '0002_auto_20201222_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='nbaFranchise',
            field=models.BooleanField(),
        ),
    ]
