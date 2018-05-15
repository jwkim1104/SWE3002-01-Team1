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

# CRM -> mysql변경시 ...
# questNum : (Value Name) questNum -> id로 변경되었습니다(기본 django default제공)
# serialNum : (Field) INTEGER -> VARCHAR(30)
# emailNeed : (Field) BIT -> VARCHAR(1), (Default) 0 -> 'F'


class Process(models.Model):
    videoNum = models.IntegerField(primary_key=True)
    multiType = models.CharField(max_length=30)
    videoType = models.CharField(max_length=30)
    popular = models.IntegerField(default=0)
    placeName = models.CharField(max_length=30)


# Process -> mysql변경시 ...


class Breed(models.Model):
    breedName = models.CharField(max_length=30, primary_key=True)
    maxWeight = models.FloatField(null=False)
    minWeight = models.FloatField(null=False)
    lifespan = models.IntegerField(null=False)
    size = models.FloatField(null=False)


# Breed -> mysql변경시 ...


class Pet(models.Model):
    petId = models.IntegerField(primary_key=True)
    serialNum = models.ForeignKey(User, on_delete=models.CASCADE)
    petName = models.CharField(max_length=30, null=False)
    breedName = models.ForeignKey(Breed, on_delete=models.CASCADE)
    age = models.IntegerField(default=0, null=False)
    gender = models.CharField(max_length=1, null=False)
    weight = models.FloatField(null=False)
    neutralization = models.CharField(max_length=1, default='F')
    neutralizationDate = models.DateField(auto_now=False, null=True)
    obesityDegree = models.IntegerField(null=False)
    activityDegree = models.IntegerField(null=False)
    allergy = models.CharField(max_length=30, null=True)
    taste = models.CharField(max_length=30, null=True)
    healthIssue = models.CharField(max_length=30, null=True)


# Pet -> mysql변경시 ...
# serialNum : (Field) INTEGER -> VARCHAR(30)
# gender : (Field) BIT -> VARCHAR(1), (Default) 0 -> 'F'


class Product(models.Model):
    productId = models.IntegerField(primary_key=True)
    nutrition = models.CharField(max_length=30, null=False)
    petId = models.ForeignKey(Pet, on_delete=models.CASCADE)
    calorie = models.FloatField(null=False)
    ingredient = models.CharField(max_length=100)
    mixportion = models.FloatField(null=False)
    price = models.FloatField(default=0.)


# Product -> mysql변경시 ...


class Order(models.Model):
    orderId = models.IntegerField(primary_key=True)
    serialNum = models.ForeignKey(User, on_delete=models.CASCADE)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    orderDate = models.DateField(auto_now=True)
    periodOption = models.CharField(max_length=1, default='F')
    period = models.CharField(max_length=30, null=True)
    quantity = models.FloatField(null=False)
    totalPrice = models.FloatField(null=False, default=0.)


# Order -> mysql변경시 ...
# serialNum : (Field) INTEGER -> VARCHAR(30)
# periodOption : (Field) BIT -> VARCHAR(1), (Default) 0 -> 'F'


class Delivery(models.Model):
    deliveryNumber = models.IntegerField(primary_key=True)
    deliveryStatus = models.CharField(max_length=30, null=False)
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE)
    expectedDeliveryDate = models.DateField(auto_now=False, null=True)


# Delivery -> mysql변경시 ...
# expectedDeliveryDate : (Default) now+3 -> 0
# orderDate(delete)
