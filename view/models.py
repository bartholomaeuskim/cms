from django.db import models

# Create your models here.
class Vehicle(models.Model):
    vin = models.CharField(max_length=17)
    code = models.CharField(max_length=16)
    color_code = models.CharField(max_length=4)
    option = models.CharField(max_length=255, blank=True)
    seats = models.CharField(max_length=4, blank=True)
    cif = models.IntegerField()
    produced_month = models.CharField(max_length=6)
    departure_date = models.DateField(blank=True)
    arrival_date = models.DateField(blank=True)
    kaida_reg_date = models.DateField(blank=True)
    sagai_reg_date = models.DateField(blank=True)

class Code(models.Model):
    code = models.CharField(max_length=16)
    brand = models.CharField(max_length=10)
    model = models.CharField(max_length=255)
    trim = models.CharField(max_length=255, blank=True)
    engine = models.CharField(max_length=20)
    transmission = models.CharField(max_length=10)
    stop_and_start = models.BooleanField(default=True)

class Color(models.Model):
    model = models.CharField(max_length=255)
    color_code = models.CharField(max_length=4)
    color = models.CharField(max_length=30)
    roof_color = models.CharField(max_length=30)
