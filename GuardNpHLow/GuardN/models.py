from django.db import models

class Zone(models.Model):
  Name = models.CharField(max_length=40)
  ZoneID = models.IntegerField(default=0)
  PlantKc = models.IntegerField(default=0)
  Area = models.IntegerField(default=0)
  # AdjZone = models.
