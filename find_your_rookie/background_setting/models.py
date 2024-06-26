from django.db import models


class offensive(models.Model):
    Rating = models.FloatField()
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    position1 = models.CharField(max_length = 20)
    Apps = models.CharField(max_length = 20)
    Mins = models.FloatField()
    Goals = models.FloatField()
    Assists = models.FloatField()
    SpG = models.FloatField()
    KeyP = models.FloatField()
    Drb = models.FloatField()
    Fouled = models.FloatField()
    Off = models.FloatField()
    Disp = models.FloatField()
    UnsTch = models.FloatField()
    
    def __str__(self):
        return f"{self.name}({self.age}/{self.position1})"
    
class defensive(models.Model):
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    position1 = models.CharField(max_length = 20)
    position2 = models.CharField(max_length = 20)
    Apps = models.CharField(max_length = 20)
    Mins = models.FloatField()
    Tackles = models.FloatField()
    Inter = models.FloatField()
    Fouls = models.FloatField()
    Offsides = models.FloatField()
    Clear = models.FloatField()
    Drb = models.FloatField()
    Blocks = models.FloatField()
    OwnG = models.FloatField()
    Rating = models.FloatField()
    def __str__(self):
        return f"{self.name}({self.age}/{self.position1},{self.position2})"

class passing(models.Model):
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    position1 = models.CharField(max_length = 20)
    position2 = models.CharField(max_length = 20)
    Apps = models.CharField(max_length = 20)
    Mins = models.FloatField()
    Assists = models.FloatField()
    KeyP = models.FloatField()
    AvgP = models.FloatField()
    PSpercent = models.FloatField()
    Crosses = models.FloatField()
    LongB = models.FloatField()
    ThrB = models.FloatField()
    Rating = models.FloatField()
    def __str__(self):
        return f"{self.name}({self.age}/{self.position1},{self.position2})"
    
# class Option(models.Model):
#     number = models.ExpressionList
    
# Create your models here.
