# Generated by Django 2.2.10 on 2020-02-22 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_clue'),
    ]

    operations = [
        migrations.AddField(
            model_name='clue',
            name='solutions',
            field=models.TextField(default='UNSOLVED'),
        ),
    ]
