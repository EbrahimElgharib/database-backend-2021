from django.contrib import admin

from .models import Employees, Manager, StationEmployees,Station,Crew,Vehicles,Casualties

# Register your models here.

admin.site.register(Employees)
admin.site.register(Manager)
admin.site.register(StationEmployees)
admin.site.register(Station)
admin.site.register(Crew)
admin.site.register(Vehicles)
admin.site.register(Casualties)