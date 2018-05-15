from django.db import models

# Create your models here.
class User(models.Model):
   serialNum = models.CharField(max_length=30, primary_key=True)
   userName = models.CharField(max_length=30, null=False)
   userID = models.CharField(max_length=30, null=False, unique=True)
   email = models.CharField(max_length=30, null=False, unique=True)
   userPW = models.CharField(max_length=30, null=False)
   phonenumber = models.CharField(max_length=11, null=False, unique=True)

