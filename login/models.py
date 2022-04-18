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



#def extraInitForMyModel(sender, **kwargs): 
    #user = kwargs['instance']
    #password = user.password
    #encodedStr = password.encode()
    #user.password = hashlib.md5(encodedStr).hexdigest()

#post_init.connect(extraInitForMyModel, sender=User)   


    
    

