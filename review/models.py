from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Review(models.Model):
    
    TeamsChoices = (
        ('Arsenal', 'Arsenal'),
        ('Aston Villa', 'Aston Villa'),
        ('Barnsley', 'Barnsley'),
        ('Birmingham City', 'Birmingham City'),
        ('Blackburn Rovers', 'Blackburn Rovers'),
        ('Blackpool', 'Blackpool'),
        ('Bolton Wanderers', 'Bolton Wanderers'),
        ('Bournemouth', 'Bournemouth'),
        ('Brentford', 'Brentford'),
        ('Brighton & Hove Albion', 'Brighton & Hove Albion'),
        ('Bristol City', 'Bristol City'),
        ('Burnley', 'Burnley'),
        ('Burton Albion', 'Burton Albion'),
        ('Cambridge United', 'Cambridge United'),
        ('Cardiff City', 'Cardiff City'),
        ('Carlisle United', 'Carlisle United'),
        ('Charlton Athletic', 'Charlton Athletic'),
        ('Chelsea', 'Chelsea'),
        ('Cheltenham Town', 'Cheltenham Town'),
        ('Coventry City', 'Coventry City'),
        ('Crystal Palace', 'Crystal Palace'),
        ('Derby County', 'Derby County'),
        ('Exeter City', 'Exeter City'),
        ('Everton', 'Everton'),
        ('Fleetwood Town', 'Fleetwood Town'),
        ('Fulham', 'Fulham'),
        ('Huddersfield Town', 'Huddersfield Town'),
        ('Hull City', 'Hull City'),
        ('Ipswich Town', 'Ipswich Town'),
        ('Leeds United', 'Leeds United'),
        ('Leicester City', 'Leicester City'),
        ('Leyton Orient', 'Leyton Orient'),
        ('Lincoln City', 'Lincoln City'),
        ('Liverpool', 'Liverpool'),
        ('Luton Town', 'Luton Town'),
        ('Manchester City', 'Manchester City'),
        ('Manchester United', 'Manchester United'),
        ('Middlesbrough', 'Middlesbrough'),
        ('Millwall', 'Millwall'),
        ('Newcastle United', 'Newcastle United'),
        ('Northampton Town', 'Northampton Town'),
        ('Norwich City', 'Norwich City'),
        ('Nottingham Forest', 'Nottingham Forest'),
        ('Oxford United', 'Oxford United'),
        ('Peterborough United', 'Peterborough United'),
        ('Plymouth Argyle', 'Plymouth Argyle'),
        ('Port Vale', 'Port Vale'),
        ('Portsmouth', 'Portsmouth'),
        ('Preston North End', 'Preston North End'),
        ('Queens Park Rangers', 'Queens Park Rangers'),
        ('Reading', 'Reading'),
        ('Rotherham United', 'Rotherham United'),
        ('Sheffield United', 'Sheffield United'),
        ('Sheffield Wednesday', 'Sheffield Wednesday'),
        ('Shrewsbury Town', 'Shrewsbury Town'),
        ('Southampton', 'Southampton'),
        ('Stevenage', 'Stevenage'),
        ('Stoke City', 'Stoke City'),
        ('Sunderland', 'Sunderland'),
        ('Swansea City', 'Swansea City'),
        ('Tottenham Hotspur', 'Tottenham Hotspur'),
        ('Watford', 'Watford'),
        ('West Bromwich Albion', 'West Bromwich Albion'),
        ('West Ham United', 'West Ham United'),
        ('Wigan Athletic', 'Wigan Athletic'),
        ('Wolverhampton Wanderers', 'Wolverhampton Wanderers'),
    )

    ReviewChoices = (
        ('A', 'Poor'),
        ('B', 'Average'),
        ('C', 'Good'),
        ('D', 'Outstanding')
    )

    ResultChoices = (
        ('A', 'Win'),
        ('B', 'Draw'),
        ('C', 'Lose'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review')
    team_visited = models.CharField(max_length=30, default='ARS', choices=TeamsChoices)
    visit_date = models.DateField()
    final_score = models.CharField(max_length=10,)
    result = models.CharField(max_length=4, default='A', choices=ResultChoices)
    location_rating = models.CharField(max_length=12, default='B', choices=ReviewChoices)
    atmosphere_rating = models.CharField(max_length=12, default='B', choices=ReviewChoices)
    facilities_rating = models.CharField(max_length=12, default='B', choices=ReviewChoices)
    catering_rating = models.CharField(max_length=12, default='B', choices=ReviewChoices)
    overall_rating = models.CharField(max_length=12, default='B', choices=ReviewChoices)
    comments = models.TextField(blank=True)


    def __str__(self):
       return f"{self.team_visited} away,  reviewed by {self.user}"

