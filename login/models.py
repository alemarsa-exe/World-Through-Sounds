from django.utils import timezone
from django.db import models
import hashlib
from django.db.models.signals import post_init


class User(models.Model):
    userId = models.IntegerField(primary_key=True)
    role = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=500)

    
        
    def changeUsername(self, username):
        self.username = username

    def getPassword(self):
        return self.password
        
    def getUsername(self):
        return self.username

class LevelPlayedScore(models.Model):
    userId = models.IntegerField()
    level = models.IntegerField()
    score = models.IntegerField()
    lives = models.IntegerField()
    duration = models.IntegerField()
    date = models.DateTimeField(auto_now_add = True)

class TopUserScores(models.Model):
    userId = models.IntegerField(primary_key=True)
    scoreLevel1 = models.IntegerField()
    scoreLevel2 = models.IntegerField()
    scoreLevel3 = models.IntegerField()
    scoreLevel4 = models.IntegerField()






    
    

