from django.db import models

# Create your models here.

class Articles(models.Model):
    title   = models.CharField(max_length=120)
    content = models.TextField()
    active = models.BooleanField()
