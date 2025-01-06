from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Review(models.Model):
    
    
    TeamsChoices = (
        ('Arsenal', 'Arsenal'),
        ('Villa', 'Aston Villa'),
        ('Bouremouth', 'Bournemouth'),
        ('Brentford', 'Brentford'),
        ('Brighton', 'Brighton'),
        ('Chelsea', 'Chelsea'),
        ('Palace', 'Crystal Palace'),
        ('Everton', 'Everton'),
        ('Fulham', 'Fulham'),  
        ('Ipswich', 'Ipswich'),
        ('Leicester', 'Leicester City'),
        ('Man City', 'Manchester City'), 
        ('Man Utd', 'Manchester United'),
        ('Newcastle', 'Newcastle'),
        ('Forst', 'Nottingham Forest'),
        ('SOuthmpton', 'Southampton'), 
        ('Spurs', 'Tottenham Hotspur'),
        ('West Ham', 'West Ham'),
        ('Wolves', 'Wolverhampton Wanderers')
    )

    ReviewChoices = (
        ('A', 'Poor'),
        ('B', 'Average'),
        ('C', 'Good'),
        ('D', 'Outstanding')
    )

    ResultChoices= (
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
    catering_rating =  models.CharField(max_length=12, default='B', choices=ReviewChoices)
    overall_rating =  models.CharField(max_length=12, default='B', choices=ReviewChoices)
    comments = models.TextField(blank=True)


    def __str__(self):
       return f"{self.team_visited} away,  reviewed by {self.user}"

