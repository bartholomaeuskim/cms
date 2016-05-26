from django.contrib import admin
from view.models import Vehicle, Code, Color

# Register your models here.
class CodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'brand', 'model', 'trim', 'engine', 'transmission', 'stop_and_start')

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vin', 'code', 'color_code', 'option', 'seats', 'cif', 'produced_month', 'departure_date', 'arrival_date', 'kaida_reg_date', 'sagai_reg_date')

admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Code, CodeAdmin)
admin.site.register(Color)
