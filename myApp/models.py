from django.db import models

# Create your models here.
class userMeasurements(models.Model):
  firstSize = models.FloatField(verbose_name='Длина')
  secondSize = models.FloatField(verbose_name='Ширина')
  square = models.FloatField()
  perimeter = models.FloatField()