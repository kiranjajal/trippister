from django.db import models
import json

# Create your models here.
class overview(models.Model):
    content = models.CharField(max_length=150)
    def __str__(self):
        return self.content

class itinerary(models.Model):
    content1=models.CharField(max_length=200)
    def __str__(self):
        return self.content1

class location(models.Model):
    content2=models.CharField(max_length=150)
    def __str__(self):
        return self.content2

class reviews(models.Model):
    content3=models.CharField(max_length=150)
    def __str__(self):
        return self.content3
