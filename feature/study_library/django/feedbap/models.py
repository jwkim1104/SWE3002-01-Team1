from django.db import models

# Create your models here.


class User(models.Model):
   serialNum = models.CharField(max_length=30, primary_key=True)
   userName = models.CharField(max_length=30, null=False)
   userID = models.CharField(max_length=30, null=False, unique=True)
   email = models.CharField(max_length=30, null=False, unique=True)
   userPW = models.CharField(max_length=30, null=False)
   phonenumber = models.CharField(max_length=11, null=False, unique=True)


# User -> mysql변경시 ...
# serialNum : (Field) INTEGER -> VARCHAR(30)


class CRM(models.Model):
    serialNum = models.ForeignKey(User, on_delete=models.CASCADE)
    questDate = models.DateTimeField(auto_now=True)
    questType = models.CharField(max_length=30, null=False)
    questTypeFreq = models.IntegerField(null=True)
    emailNeed = models.CharField(max_length=1, default='F')

# User -> mysql변경시 ...
# questNum : (Value Name) questNum -> id로 변경되었습니다(기본 django default제공)
# serialNum : (Field) INTEGER -> VARCHAR(30)
# emailNeed : (Field) BIT -> VARCHAR(1), (Default) 0 -> 'F'


class Process(models.Model):
    videoNum = models.IntegerField(primary_key=True)
    multiType = models.CharField(max_length=30)
    videoType = models.CharField(max_length=30)
    popular = models.IntegerField(default=0)
    placeName = models.CharField(max_length=30)


class Breed(models.Model):
    breedName = models.CharField(max_length=30, primary_key=True)
    maxWeight = models.FloatField(null=False)
    minWeight = models.FloatField(null=False)
    lifespan = models.IntegerField(null=False)
    size = models.FloatField(null=False)



# class Pet(models.Model):
#     petId = models.IntegerField(primary_key=True)
#     serialNum = models.ForeignKey(User, on_delete=models.CASCADE)
#     petName = models.CharField(max_length=30, null=False)
#     breedName = models.CharField(max_length=30)