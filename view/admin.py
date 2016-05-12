from django.contrib import admin
from view.models import Vehicle, Code, Color

# Register your models here.
class CodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'brand', 'model', 'trim', 'engine', 'transmission', 'stop_and_start')

admin.site.register(Vehicle)
admin.site.register(Code, CodeAdmin)
admin.site.register(Color)
