# Generated by Django 4.2 on 2023-05-23 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='favoriteExpert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expertId', models.IntegerField()),
                ('userId', models.IntegerField()),
            ],
        ),
    ]
