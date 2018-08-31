from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    iconAddr = models.CharField(max_length=256)
    relAddr = models.CharField(max_length=256)
    numInRow = models.IntegerField(null=True)