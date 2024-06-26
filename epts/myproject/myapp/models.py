# myapp/models.py

from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    position = models.CharField(max_length= 100, blank=True, null = True)
    preferred_foot = models.CharField(max_length= 100 ,blank=True, null = True)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    acceleration = models.FloatField()
    sprint_speed = models.FloatField()
    agility = models.FloatField()
    stamina = models.FloatField()
    aggression = models.FloatField()
    total = models.FloatField()

    def __str__(self):
        return self.name
   
class SelectedPlayer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name