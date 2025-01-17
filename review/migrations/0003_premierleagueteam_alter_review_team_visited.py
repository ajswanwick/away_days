# Generated by Django 4.2.17 on 2025-01-06 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_rename_atmosphere_review_atmosphere_rating_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PremierLeagueTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(choices=[('ARS', 'Arsenal'), ('AST', 'Aston Villa'), ('BOU', 'Bournemouth'), ('BRE', 'Brentford'), ('BRI', 'Brighton'), ('CHE', 'Chelsea'), ('CRY', 'Crystal Palace'), ('EVE', 'Everton'), ('FUL', 'Fulham'), ('IPS', 'Ipswich'), ('LEI', 'Leicester City'), ('LIV', 'Liverpool'), ('MCI', 'Manchester City'), ('MNU', 'Manchester United'), ('NEW', 'Newcastle'), ('NFR', 'Nottingham Forest'), ('SOU', 'Southampton'), ('TOT', 'Tottenham Hotspur'), ('WHU', 'West Ham'), ('WLV', 'Wolverhampton Wanderers')], max_length=30, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='review',
            name='team_visited',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='review.premierleagueteam'),
        ),
    ]
