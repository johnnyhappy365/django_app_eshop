from django.db import models

# Create your models here.
class Good(models.Model):
  good_name = models.CharField(max_length=128)
  good_price = models.FloatField()
  class Meta:
    ordering=['-good_price']