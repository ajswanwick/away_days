# Generated by Django 4.2.17 on 2025-01-06 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_alter_premierleagueteam_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='premierleagueteam',
            name='team',
            field=models.CharField(choices=[('ARS', 'Arsenal'), ('AST', 'Aston Villa'), ('BOU', 'Bournemouth'), ('BRE', 'Brentford'), ('BRI', 'Brighton'), ('CHE', 'Chelsea'), ('CRY', 'Crystal Palace'), ('EVE', 'Everton'), ('FUL', 'Fulham'), ('IPS', 'Ipswich'), ('LIC', 'Leicester City'), ('LIV', 'Liverpool'), ('MCI', 'Manchester City'), ('MNU', 'Manchester United'), ('NEW', 'Newcastle'), ('NFR', 'Nottingham Forest'), ('SOU', 'Southampton'), ('TOT', 'Tottenham Hotspur'), ('WHU', 'West Ham'), ('WLV', 'Wolverhampton Wanderers')], max_length=20, unique=True),
        ),
    ]
