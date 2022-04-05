from django.db import models
import json


class User(models.Model):
    userId = models.IntegerField(primary_key=True)
    role = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
