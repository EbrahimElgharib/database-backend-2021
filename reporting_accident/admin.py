from django.contrib import admin

# Register your models here.


from .models import Reporter, Accident, Hospital
admin.site.register(Reporter)
admin.site.register(Accident)
admin.site.register(Hospital)