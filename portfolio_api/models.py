from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Project(models.Model):
  name = models.CharField(max_length=100)
  img = models.CharField(max_length=1000)
  liveLink = models.CharField(max_length=1000)
  githubLink = models.CharField(max_length=1000)
  techs = models.JSONField()