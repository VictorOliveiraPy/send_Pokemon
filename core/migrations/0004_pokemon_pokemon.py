# Generated by Django 3.1.7 on 2021-03-01 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210301_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='pokemon',
            field=models.IntegerField(choices=[(20, 'Pikachu'), (19, 'Rattata')], null=True),
        ),
    ]