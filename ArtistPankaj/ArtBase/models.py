# Create your models here.
from django.db import models

# # Create your models here.

class paintings(models.Model):
    art=models.FileField(upload_to='media/')

class feedback(models.Model):
    name=models.CharField(max_length=200)
    msg=models.CharField(max_length=2000)

class book(models.Model):
    name=models.CharField(max_length=200)
    num=models.IntegerField()
    img=models.FileField(upload_to='sketch/')

class contact(models.Model):
    name=models.CharField(max_length=200)
    num=models.IntegerField()
    msg=models.FileField(max_length=3000)