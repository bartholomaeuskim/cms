from django.db import models

# Create your models here.
class Stock_Manager(models.Manager):
    def stock_count(self):
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("""
            SELECT view_code.model, count(*)
            FROM view_code
            INNER JOIN view_vehicle
            ON view_vehicle.code = view_code.code
            WHERE view_vehicle.kaida_reg_date is null
            GROUP BY view_code.model""")
        result_list = []
        for row in cursor.fetchall():
            p = self.model(model=row[0])
            p.num_responses = row[1]
            result_list.append(p)
        return result_list

class Vehicle(models.Model):
    vin = models.CharField(max_length=17)
    code = models.CharField(max_length=16)
    color_code = models.CharField(max_length=4)
    option = models.CharField(max_length=255, null=True)
    seats = models.CharField(max_length=4, null=True)
    cif = models.IntegerField()
    produced_month = models.CharField(max_length=6)
    departure_date = models.DateField(null=True)
    arrival_date = models.DateField(null=True)
    kaida_reg_date = models.DateField(null=True)
    sagai_reg_date = models.DateField(null=True)

class Code(models.Model):
    code = models.CharField(max_length=16)
    brand = models.CharField(max_length=10)
    model = models.CharField(max_length=255)
    trim = models.CharField(max_length=255, blank=True)
    engine = models.CharField(max_length=20)
    transmission = models.CharField(max_length=10)
    stop_and_start = models.BooleanField(default=True)
    objects = Stock_Manager()

class Color(models.Model):
    model = models.CharField(max_length=255)
    color_code = models.CharField(max_length=4)
    color = models.CharField(max_length=30)
    roof_color = models.CharField(max_length=30)
