from django.db import models
# models.py
from django.db import models

class OpeningHours(models.Model):
    day_of_week = models.IntegerField(choices=((0, 'Sunday'), (1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday')))
    opening_time = models.TimeField()
    closing_time = models.TimeField()

class ExceptionDay(models.Model):
    date = models.DateField(unique=True)
    is_closed = models.BooleanField(default=False)

# Create your models here.
