from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=30)
    score = models.FloatField()
    year = models.IntegerField(default=2000)
    genres = models.CharField(max_length=50,default='dfsdfsd')
    description = models.CharField(max_length=100)
    photo = models.ImageField(blank=True,null=True)
    url = models.CharField(max_length=100)
