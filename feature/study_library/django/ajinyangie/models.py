from django.db import models

# Create your models here.
class dog_types(models.Model):
   name = models.CharField(max_length=50)
   group = models.CharField(max_length=200, null=True)
   height = models.CharField(max_length=200, null=True)
   weight = models.CharField(max_length=200, null=True)
   life_span = models.CharField(max_length=200, null=True)
