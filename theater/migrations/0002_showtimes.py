# Generated by Django 5.2 on 2025-04-14 10:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
        ('theater', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Showtimes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_time', models.DateTimeField()),
                ('screen_number', models.CharField(blank=True, null=True)),
                ('movie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.movie')),
                ('theater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theater.theaters')),
            ],
        ),
    ]
