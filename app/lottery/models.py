from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Lottery(models.Model):
    name = models.CharField(max_length=100)
    plate_number = CharField(max_length=20)
    date = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=50)
    lottery_number = models.CharField(max_length=50, db_index=True)